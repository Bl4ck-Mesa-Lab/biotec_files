# Test Gurilande lumineuse BIOTEC

Les tests sont à effectuer : 

- [x] Depuis un Ordinateur
- [ ] Depuis un Téléphone 

Accès à l'adresse IP :

Une fois connecté à l'AP Wi-fI : 
    - SSID `BIOTEC-Escape`
    - password : `Biotec1234!`
  
Consulter la page Web pour accéder au service :
- http://192.168.XX.63:80

## ----- UTILISATION DU START ----- 

### Comportement du START

- [x] Vérifier que le start fait un Reset avant de le lancement du décompte 
- [x] Vérifier le lancement du décompte
- [x] Chaque LED ne doit pas clignoter de plus d'1min

### Transisitions depuis le START
#### Transistion Depuis l'état START, Vérifier qu'il est possible de faire :

- [x] START --> STOP
- [x] START --> SUCCESS
- [x] START --> FAILED
- [x] START --> PAUSE
- [x] START --> RESET

## ----- UTILISATION DU STOP -----

### Comportement du STOP

- [x] Vérifier que le stop lance L'Arrêt de toutes les LEDs

### Transisitions depuis le STOP
#### Transistion Depuis l'état STOP, Vérifier qu'il est possible de faire :

- [x] STOP --> START
- [x] STOP --> SUCCESS : Il faut parfois appuyer 2x sur SUCCESS ? => je n'ai plus ce pb suite aux dev récents (interruption immédiate par le STOP lors de SUCCESS ou FAILED), à retester chez toi pour confirmer que t'es ok ;)
- [x] STOP --> FAILED : Il faut parfois 2x sur FAILED ? => idem que ligne précédente
- [x] STOP --> PAUSE
- [x] STOP --> RESET

## ----- UTILISATION DU SUCCESS ------

### Comportement du SUCESS

- [x] Vérifier que le Success lance un chenillard vert sur l'ensemble des LEDs

### Transisitions depuis le START
#### Transistion Depuis l'état START, Vérifier qu'il est possible de faire :

- [x] SUCCESS --> START
- [x] SUCCESS --> STOP
- [x] SUCCESS --> FAILED : OK mais il faut parfois 3 sequences de success avant
- [x] SUCCESS --> PAUSE
- [x] SUCCESS --> RESET : OK mais il faut parfois 3 sequences de success avant

## ----- UTILISATION DU FAILED -----

### Comportement du FAILED

- [x] Vérifier que le Failed lance un clignotement rouge d'1Hz sur l'ensemble des LEDs

### Transisitions depuis le FAILED
#### Transistion Depuis l'état FAILED, Vérifier qu'il est possible de faire :

- [x] FAILED --> START
- [x] FAILED --> STOP
- [x] FAILED --> SUCCESS
- [x] FAILED --> PAUSE
- [x] FAILED --> RESET

## ----- UTILISATION DU PAUSE -----

### Comportement du PAUSE

- [x] Vérifier que le Pause attend le fin d'un clignotement d'une LED, arrête le clignotement de celle-ci et met en pause le décompte global
- [x] Vérifier que lorsque l'état pause à été demandé, un bouton "PAUSED" en bleu vient remplacer le bouton "PAUSE" en Jaune
- [x] Vérifier que lorsque l'état pause à été demandé, un bouton "RESUME" en bleu vient remplacer le bouton "START" en bleu
- [x] Vérifier que lorsqu'on demande l'état RESUME, la LED mise sur pause reprend son clignotement depuis 0s

Remarque : lorsqu'on se trouve dans un autre etat que START, l'état pause à un effet de STOP (ce qui n'est pas problèmatique puisque faire PAUSE dans un autre état que START n'a pas vraiment d'intérêt dans notre cas).

### Transisitions depuis le PAUSE
#### Transistion Depuis l'état PAUSE, Vérifier qu'il est possible de faire :

- [X] PAUSE --> RESUME ("START")
- [X] PAUSE --> STOP
- [X] PAUSE --> SUCCESS
- [X] PAUSE --> FAILED
- [x] PAUSE --> RESET 

## ----- UTILISATION DU RESET -----

### Comportement du RESET

- [x] Vérifier que le Reset éteint toute les LED (comme le STOP) et réinitilise toutes les couleurs (comme le début du START mais sans démarrer le décompte

### Transisitions depuis le RESET
#### Transistion Depuis l'état RESET, Vérifier qu'il est possible de faire :

- [x] RESET --> START
- [x] RESET --> STOP
- [x] RESET --> SUCCESS
- [x] RESET --> FAILED
- [x] RESET --> PAUSE
