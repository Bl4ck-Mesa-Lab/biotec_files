/* 
 *  signal_sync
 *  
 *  4 niveaux.
 *  Le niveau est validé si le signal est correct pendant 1s.
 *  
 */

// Pins
#define ADC_PIN 34  // Pin de l'ESP32 où le signal est connecté
#define FREQ_LED_PIN 26
#define AMP_LED_PIN 27

// Config
#define RESTART_DELAY 300*1000 // 5min
//#define RESTART_DELAY 5*1000 // 5s (DEBUG)
#define PLAYTIME 240 // secondes
#define TIME_PER_SIG 60 // secondes

// SSD1306 display connected to I2C (SDA, SCL pins)
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


struct signal {
  float sig_amp;
  float sig_freq;
};

const unsigned int levels_nb = 4;
struct signal levels[levels_nb] = {
  // signaux precis
  /*{5.20, 142.00},
  {3.40, 207.00},
  {6.60, 56.00},
  {1.60, 112.00},*/
  // signaux par cases
  {2.00, 100.00},
  {4.00, 200.00},
  {3.00, 50.00},
  {6.00, 75.00},
};

//const int sampleRate = 20000;  // Taux d'échantillonnage en Hz (20 kHz pour un signal jusqu'à 10 kHz)
const int sampleRate = 1000;  // Taux d'échantillonnage en Hz (1000 Hz pour un signal jusqu'à 250 Hz) (taux à 500 Hz ne suffisait pas)
const int numSamples = 1024;   // Nombre d'échantillons à prendre

int samples[numSamples];
unsigned long lastSampleTime = 0;
// amplitude = ESP ; amplitude_final = Oscillo (obtenue via amp_coeff)
float amplitude = 0, amplitude_final = 0;
float amp_coeff_low = 3.03;
float amp_coeff_high = /*2.95*//*2.94*//*2.93*/2.91;
//float err_tol_amp[] = {/*0.030*//*0.032*//*0.020*/0.018, /*0.030*//*0.032*/0.026, /*0.022*/0.020, 0.036}; // signaux precis
float err_tol_amp[] = {0.080, 0.026, 0.026, 0.020}; // signaux par cases
float frequency = 0;
//float err_tol_freq = /*0.042*/0.013; // signaux precis
float err_tol_freq = 0.040; // signaux par cases
float err_tol_freq_min = 1 - err_tol_freq;
float err_tol_freq_max = 1 + err_tol_freq;

hw_timer_t * timer_playtime = NULL;

/*void ARDUINO_ISR_ATTR timer_isr() {
  //display_lose();
  Serial.println("Timer expiré");
  wait_serial_flush();
  delay(2000);
  ESP.restart();
}*/

void setup() {
  unsigned int i;

  // serial
  Serial.begin(115200);
  
  // signal pin
  analogReadResolution(12);  // Résolution ADC à 12 bits (0-4095)
  
  // OLED display
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("SSD1306 allocation failed"));
    //for(;;); // Don't proceed, loop forever
  }
  
  // Init screen
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display_boot();

  // LED pins
  pinMode(FREQ_LED_PIN, OUTPUT);
  pinMode(AMP_LED_PIN, OUTPUT);
  flash_leds(3, 250);

  delay(2000);

  // print info
  wait_serial_flush();
  Serial.println(" ");
  Serial.println("--- SIGNAL SYNC ---");/*
  Serial.print("err_tol_amp_min: ");
  Serial.print(err_tol_amp_min, 3);
  Serial.print(" err_tol_amp_max: ");
  Serial.print(err_tol_amp_max, 3);
  Serial.println(" ");*/
  Serial.println("-------------------");

  // LED pins
  flash_leds(1, 250);

  // lancement timer durée de la partie
  /*timer_playtime = timerBegin(1000000); // timer frequency 1MHz
  timerAttachInterrupt(timer_playtime, &timer_isr);
  timerAlarm(timer_playtime, PLAYTIME * 1000 * 1000, false, 0);*/
}

void loop() {
  unsigned int current_level;

  Serial.println("!!! Début du jeu !!!");
  wait_serial_flush();
  for(current_level = 0; current_level < levels_nb; current_level++) {
    clear_leds(true, true);
    block_till_valid_signal(current_level);
    display_lvl_valid(current_level);
    Serial.print("Niveau ");
    Serial.print(current_level+1);
    Serial.println(" validé !!!");
    wait_serial_flush();
    //delay(3000);
    flash_leds(3, 500);
  }

  display_win();
  Serial.print(" !!! Gagné !!! ");
  Serial.println("(restart automatique après tempo)");
  delay(RESTART_DELAY);  // Tempo de fin de jeu
  ESP.restart();
  
/*
  // ###################
  // TESTS - DEBUG
  get_signal(&amplitude, &frequency, &amplitude_final);

  display_measure();

  validate_signal(5.0, 100.0); // OK
  validate_signal(2.0, 50.0); // OK
  validate_signal(3.0, 200.0); // OK

  delay(1000);  // Pause avant la prochaine mesure
  
  // FIN TESTS - DEBUG
  // ###################
*/
}

void get_signal(float* amp, float* freq, float* amp_final)
{
  float amp_coeff;
  
  // 1. Échantillonnage du signal
  for (int i = 0; i < numSamples; i++) {
    samples[i] = analogRead(ADC_PIN);
    /*Serial.print("samples[i]=");
    Serial.print(samples[i]);
    Serial.println(" ");
    wait_serial_flush();*/
    delayMicroseconds(1000000 / sampleRate);  // Délai pour atteindre la fréquence d'échantillonnage
  }

  // 2. Calcul de l'amplitude
  unsigned int minVal = 4095;
  unsigned int maxVal = 0;
  for (int i = 0; i < numSamples; i++) {
    if (samples[i] < minVal) {
      minVal = samples[i];
    }
    if (samples[i] > maxVal) {
      maxVal = samples[i];
    }
  }
  *amp = (maxVal - minVal) * (3.3 / 4095.0);  // Amplitude en volts
  /*Serial.print("minVal: ");
  Serial.print(minVal);
  Serial.print(" maxVal: ");
  Serial.print(maxVal);
  Serial.print(" ");*/
  if(*amp < 1.8) {
     amp_coeff = amp_coeff_low;
  } else {
     amp_coeff = amp_coeff_high;
  }
  *amp_final = *amp * amp_coeff;

  // 3. Calcul de la fréquence (méthode de détection de zéro)
  int zeroCrossings = 0;
  for (int i = 1; i < numSamples; i++) {
    //if ((samples[i - 1] < 2048 && samples[i] >= 2048) || (samples[i - 1] > 2048 && samples[i] <= 2048)) {
    if ((samples[i - 1] < 2200 && samples[i] >= 2200) || (samples[i - 1] > 2200 && samples[i] <= 2200)) { // 2048 ne fonctionnait pas sur amplitude 1V ou moins, les échantillons allaient au plus bas à 2100 et qq
      zeroCrossings++;
    }
  }
  *freq = (zeroCrossings / 2.0) * (sampleRate / (float)numSamples);  // Fréquence en Hz
  // empirical adjustment
  *freq = *freq / 1.033;

}

bool validate_signal(float expected_amp_final, float expected_freq, unsigned int lvl)
{
  bool ret = false;
  bool amp_valid = false, freq_valid = false;
  float amp_ratio, freq_ratio;
  float err_tol_amp_lvl, err_tol_amp_min, err_tol_amp_max;
  
  get_signal(&amplitude, &frequency, &amplitude_final);
  amp_ratio = amplitude_final / expected_amp_final;
  freq_ratio = frequency / expected_freq;

  err_tol_amp_lvl = err_tol_amp[lvl];
  err_tol_amp_min = 1 - err_tol_amp_lvl;
  err_tol_amp_max = 1 + err_tol_amp_lvl;
  
  if (amp_ratio > err_tol_amp_min && amp_ratio < err_tol_amp_max) {
    amp_valid = true;
    set_amp_led();
    Serial.print("SIGNAL VALIDATED - AMPLITUDE -");
    Serial.print(" expected_amp_final: ");
    Serial.print(expected_amp_final);
    Serial.print(" amplitude_final: ");
    Serial.print(amplitude_final);
    Serial.print(" amp_ratio: ");
    Serial.print(amp_ratio);
    Serial.println(" ");
  }

  if (freq_ratio > err_tol_freq_min && freq_ratio < err_tol_freq_max) {
    freq_valid = true;
    set_freq_led();
    Serial.print("SIGNAL VALIDATED - FREQUENCY -");
    Serial.print(" expected_freq: ");
    Serial.print(expected_freq);
    Serial.print(" frequency: ");
    Serial.print(frequency);
    Serial.print(" freq_ratio: ");
    Serial.print(freq_ratio);
    Serial.println(" ");
  }

  if(!amp_valid) clear_leds(false, true);
  if(!freq_valid) clear_leds(true, false);
  
  ret = amp_valid && freq_valid;
  return ret;
}

void display_measure()
{
  // Affichage des résultats
  Serial.print("[Amplitude ESP: ");
  Serial.print(amplitude, 3);
  Serial.print(" V], ");
  Serial.print("Amplitude finale: ");
  Serial.print(amplitude_final, 3);
  Serial.print(" V, ");
  Serial.print("Fréquence: ");
  Serial.print(frequency, 2);
  Serial.println(" Hz");
}

void wait_serial_flush()
{
  delay(70);
}

void block_till_valid_signal(unsigned int lvl)
{
  bool sig_valid = false;
  struct signal sig = levels[lvl];
  double duree_ecoulee, duree_restante;
  uint64_t compteur_timer;
  unsigned short int i;

  timer_signal_start(0);

  //display_lvl_exp_signal(lvl, sig);

  Serial.print("Niveau: ");
  Serial.print(lvl+1);
  Serial.print(" Amplitude demandée: ");
  Serial.print(sig.sig_amp, 3);
  Serial.print(" Fréquence demandée: ");
  Serial.print(sig.sig_freq, 3);
  Serial.println(" ");
  wait_serial_flush();
  
  while(!sig_valid) {
    duree_ecoulee = timerReadSeconds(timer_playtime);
    if (duree_ecoulee >= TIME_PER_SIG) {
      display_lose();
      delay(2000);
      ESP.restart();
    }
    display_lvl_timer(lvl, duree_ecoulee);
    delay(100);  // Pause avant la prochaine mesure
    //get_signal(&amplitude, &frequency, &amplitude_final);
    sig_valid = validate_signal(sig.sig_amp, sig.sig_freq, lvl);
    // si signal valide, confirmer qu'il reste valide apres une seconde (pour eviter d'etre trouve en scrollant)
    if (sig_valid) {
      // s'il reste 3s ou moins, il faut interrompre le timer car on doit attendre 1s puis valider le signal en 1s (et on prend 1s de marge)
      duree_ecoulee = timerReadSeconds(timer_playtime);
      duree_restante = TIME_PER_SIG - duree_ecoulee;
      if(duree_restante <= 3) {
        compteur_timer = timerRead(timer_playtime);
        timerStop(timer_playtime);
      }
      flash_leds(10, 50);
      set_freq_led();
      set_amp_led();
      sig_valid = validate_signal(sig.sig_amp, sig.sig_freq, lvl);
      if(duree_restante <= 3) {
        timer_signal_start(compteur_timer);
      }
    }
    display_measure();
  }
  Serial.println("Fin block_till_valid_signal");
  wait_serial_flush();
}

void timer_signal_start(uint64_t offset)
{
  // lancement timer signal en cours
  if(!timer_playtime) {
    timer_playtime = timerBegin(1000000); // timer frequency 1MHz
  }
  timerWrite(timer_playtime, offset);
  timerStart(timer_playtime);
}

void clear_leds(bool clear_freq, bool clear_amp)
{
  if(clear_freq) digitalWrite(FREQ_LED_PIN, LOW);
  if(clear_amp) digitalWrite(AMP_LED_PIN, LOW);
}

void set_freq_led()
{
  digitalWrite(FREQ_LED_PIN, HIGH);
}

void set_amp_led()
{
  digitalWrite(AMP_LED_PIN, HIGH);
}

void flash_leds(unsigned int flash_time, unsigned int wait_time)
{
  unsigned int i;
  for(i = 0; i < flash_time; i++) {
    set_freq_led();
    set_amp_led();
    delay(wait_time);
    clear_leds(true, true);
    delay(wait_time);
  }
}

void display_boot()
{
  display.clearDisplay();

  display.setCursor(0,0);             // Start at top-left corner

  //display.println(F("SIGNALSYNC"));
  display.println(F("PROCESSEUR"));
  display.println(F("BIOSIGNAUX"));
  display.println(F("INITIALISE"));
  /*display.println(F("----------"));
  display.println(F("Delai:4min"));*/
  display.display();  
}

void display_lvl_exp_signal(unsigned int lvl, struct signal exp_sig)
{
  
  display.clearDisplay();

  display.setCursor(0,0);             // Start at top-left corner
  display.print(F("Signal "));
  display.println(lvl+1);
  display.println(F("--------"));
  display.print(F("Amp:"));
  display.println(exp_sig.sig_amp, 2);
  display.print(F("Frq:"));
  display.println(exp_sig.sig_freq, 2);
  display.display();
}

void display_lvl_timer(unsigned int lvl, unsigned int timer)
{
  
  display.clearDisplay();

  display.setCursor(0,0);             // Start at top-left corner
  display.print(F("Signal "));
  display.println(lvl+1);
  display.println(F("--------"));
  display.println(F("Reste:"));
  display.print(TIME_PER_SIG - timer);
  display.println(F(" sec"));
  display.display();
}

void display_lvl_valid(unsigned int lvl)
{
  display.clearDisplay();

  display.setCursor(0,0);             // Start at top-left corner
  display.print(F("Signal "));
  display.println(lvl+1);
  display.println(F("--------"));
  display.println(F("-SYNCHRO-"));
  display.display();  
}

void display_win()
{
  display.clearDisplay();
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("TRAITEMENT"));
  display.println(F("BIOSIGNAUX"));
  display.println(F("TERMINE"));
  display.display();  
  delay(2000);
  
  display.clearDisplay();
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("LOGIN"));
  display.println(F("BASE DE"));
  display.println(F("DONNEES:"));
  display.println(F("milchick"));
  display.display();
}

void display_lose()
{
  display.clearDisplay();

  display.setCursor(0,0);             // Start at top-left corner

  display.println(F("SIGNAL"));
  display.println(F("DESYNCHRO-"));
  display.println(F("NISE"));
  display.display();  
}
