# Code pour afficher dans un temrinal un questionnaire interactif
# Escape Game DATABASE


from termcolor import colored
import os
import sys
import time
from progress.bar import Bar
from progress.bar import FillingCirclesBar
from progress.spinner import LineSpinner, MoonSpinner
import secrets
import string
import random
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN) # Ctrl + c
signal.signal(signal.SIGTSTP, signal.SIG_IGN) # Ctrl + z
signal.signal(signal.SIGQUIT, signal.SIG_IGN) # Ctrl + \
os.system("stty eof 0x7") # Ctrl-D (binder le buzzer (0x7) sur EOF donc impossible à provoquer manuellement)

# alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

def searching_file_code(file_code_size, iteration):
    x = 1
    while x in range (1, iteration):
        file_code_1 = ''.join(random.choice(alphabet) for i in range(file_code_size))
        file_code_2 = ''.join(random.choice(alphabet) for i in range(file_code_size))
        os.system('clear')
        print("Searching for anomalies in database: processing FILE ' "+file_code_1+"-"+file_code_2+" '")
        time.sleep(0.4)
        x = x + 1 

def anomaly():
    os.system('clear')
    print("----------------------------")
    print("!!!   Anomalies FOUND!   !!!")
    print("----------------------------")
    print("")
    time.sleep(1)

def finding_file_code(file_code_anomaly):
    print("- FILE ' "+file_code_anomaly+" ' seems to be compromised!")
    time.sleep(0.25)
    print("")


def plot_text(text):
        text_to_plot = text
        for char in text_to_plot:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

def plot_text_speed(text):
        text_to_plot = text
        for char in text_to_plot:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)

def processing(text):
        for x in range (0,2):  
            b = text + "." * x
            print (b, end="\r")
            time.sleep(1)                        


time.sleep(1)
os.system('clear')

print("                              .*#&&&&&&&&&&%(,                                   ") 
print("                        /%&&&&&&/           .*&&&&&&&&&(                         ")
print("                   *%&&&&&%.    (&&,   %%     %&#      %&/                       ")
print("                .&&%       &&(         &&    /&#        %&&&&&%.                 ")
print("              .&&*  *&.,/%  &&,  /&#.%&&.    ,&&       .(&&&   #&&/              ")
print("              .*     &(##( /&#(///&&#,     /.       /&&#.  (&&*   #&%            ")
print("            (&&@@@&&     .&&&.  ///&&     .&&     .&&,        %&#   %&#          ")
print("          %@@ %@@&/(@@, &&/ #&&/..#&&&&&&&&&&,                       *&&         ")
print("         &@@,@&  ,@%/@@*/, /#* *&&/   .%(*  &&                        %&,        ")
print("          (@/#@@@@&,&@ ,@,(#% (&(*#(%  ,*.,(%&&#    .&%              .&&%        ")
print("            #@@&%&@&,   &%//#.//  (#(.%&&#*    &&%,&&*  #&#*.    ,/%&&*&&,       ")
print("            // .#.( /,#% ,(, ,%/((, &&*  (#&@@& ..(&#      ,/(###&&    &&,       ")
print("            .. &% # #&@  /#(, &(/&. /   (%*&(& #%. #&(         ,%&(   %&%        ")
print("              %%/#  &(&/   /( /( ##*%#% *& %&#%&&  ..&&&.         #&&&#          ")
print("              .@&/./.&%* @&*.,,%@& %&&*   (&&&/%  #((.%&%%%&&&&%#/               ")
print("                ,,.& *,.@*&&, %@,&&/*/(%&&&%/*,*/#&&&%,                          ")
print("                      .#@%(@&%@&,@&*%#.     .,,,,.                               ")
print("                      #(&(@&&%&@@/                                               ")
print("                     ,&*/&.   *           ____ ___ ___ _____ _____ ____          ")
print("                     & *( &              | __ )_ _/ _ \_   _| ____/ ___|         ")
print("                      */,/               |  _ \| | | | || | |  _|| |             ")   
print("                                         | |_) | | |_| || | | |__| |___          ")
print("                                         |____/___\___/ |_| |_____\____|         ")

time.sleep(10)
os.system('clear')

cmd = "figlet B I O T E C - O S"

print("")
os.system(cmd)
print("")
plot_text_speed("[Starting... SYSTEM DIAGNOSTIC protocol]\n[//DEVICE: mem_slot 32K slot 1-2]\n[//DEVICE: mem_slot 32K slot 2-2]\n[//DEVICE: floppy_disk 700K slot 1-1]\n\n[//ALT: mem 43-65rvvvv err 00x01003432]\n[//ALT: mem 43-98rvvvv err 00x01002556]\n\n[//STATE: cpu x0x1-77786x fan_temp 41]\n[//STATE: cpu x2x5-65286x fan_temp 28]\n[//STATE: cpu x2x2-57231x fan_temp 33]\n\n[cmd load biotec.kernel]\n[cmd run biotec.systemd-logind]\n[cmd run biotec.profile]\n")
time.sleep(2)
os.system('clear')
plot_text_speed("COPYRIGHT 1979 BIOTEC(R)\nLOADER V1.5\nEXEC VERSION 78.90\n64K RAM SYSTEM\n698751 BYTES FREE\nNO SUPERVISOR ID FOUND\n")
plot_text_speed("(C) Biomedical Technology Institute | ALL RIGHTS RESERVED\n\n")
print("")
time.sleep(5)

#with LineSpinner('Initializing BIOTEC INSTITUTE Software...    ') as spinner:
#    for i in range(50):
#        time.sleep(0.1)
#        spinner.next()
for x in range (0,20):  
    b = "Initializing BIOTEC INST. SOFTWARE" + "." * x
    print (b, end="\r")
    time.sleep(0.3)


time.sleep(2)
os.system('clear')

plot_text_speed("******* YOU HAVE (1) UNREAD MESSAGE(S) FROM BIOTEC SUPERVISOR *******\n\n\n\nFrom: 'macrodata.officer@biotec.org' To: 'macrodata.department@biotec.org'\nObject: 'internal problem'\n--------------------------\n\n")
plot_text("Nice to see you Macrodata Operator.\n\nWe need your skills to identify some dissident employees from BIOTEC Sector C.\n\nYou have direct access to the BIOTEC database to recover missing information.\n\nTo continue your recruitment process and get the code of the safe, please fill in the form correctly.\n\n(If you encounter any difficulty, please consult your supervisor).\n\nRegards,\nMacro Data Chief Officer.")
print("")
print("")
print("")
input("Press [ENTER] Key to continue...")
os.system('clear')

plot_text("STARTING Biotec(C) [RESEARCH PROGRAM v3.2] IN [10] Sec.")
time.sleep(10)

searching_file_code(4,30)
anomaly()         
finding_file_code("$0FE-$210")
finding_file_code("0/65-&05#")
finding_file_code("M%P3-*O6$")
finding_file_code("$1R9-#56A")
finding_file_code("#6ET-$223")

print("")
print("")
input("Press [ENTER] Key to continue...")
os.system('clear')
time.sleep(1)


print("")
print("")
print(colored("---------------------------------------------------------------", "green"))
print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R)  FILE: $0FE-$210     -", "green"))
print(colored("---------------------------------------------------------------", "green"))
print(colored("- FIRSTNAME       :", "green"),"S??n?ey       ", colored(" (X)", "green"))
print(colored("- LASTNAME        :", "yellow"),"_____________ ", colored(" ( )", "red"))
print(colored("- AGE             :", "green"),"31            ", colored(" (X)", "green"))
print(colored("- CITY OF BIRTH   :", "green"),"Me??h?s       ", colored(" (X)", "green"))
print(colored("- ZIP CODE        :", "green"),"TN 6??72      ", colored(" (X)", "green"))
print(colored("- BIOTEC dis. ID  :", "green"),"31?8?1-?63    ", colored(" (X)", "green"))
print(colored("- OLD JOB         :", "green"),"E?g?n???      ", colored(" (X)", "green"))
print(colored("- BLOOD GROUP     :", "green"),"AB-           ", colored(" (X)", "green"))
print(colored("---------------------------------------------------------------", "green"))
print("")
print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
print("")

time.sleep(1)

#print("LOADING BIOMEDICAL DATA...")

for x in range (0,4):  
    b = "LOADING BIOMEDICAL DATA" + "." * x
    print (b, end="\r")
    time.sleep(1)

print("")    

question=""

time.sleep(3)

while question != "PEARSON":
    print("")
    question = input("(1/6) Please indicates the <LASTNAME> of File '$0FE-$210' --> ")
    if question == "PEARSON" or question == "Pearson" or question == "pearson":
        print("")
        print(colored("                             CORRECT INPUT. ","blue"))
        time.sleep(1)
        processing("PROCESSING")       
        


        time.sleep(5)
        os.system('clear')
        time.sleep(1)
        print("")
        print("")
        print(colored("---------------------------------------------------------------", "green"))
        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: 0/65-&05#    -", "green"))
        print(colored("---------------------------------------------------------------", "green"))
        print(colored("- FIRSTNAME       :", "green"),"J?r?m?         ", colored(" (X)", "green"))
        print(colored("- LASTNAME        :", "green"),"VE?A?Q???      ", colored(" (X)", "green"))
        print(colored("- AGE             :", "green"),"3?             ", colored(" (X)", "green"))
        print(colored("- CITY OF BIRTH   :", "green"),"Sr??ng-Va???   ", colored(" (X)", "green"))
        print(colored("- ZIP CODE        :", "green"),"?V 3??00       ", colored(" (X)", "green"))
        print(colored("- BIOTEC dis. ID  :", "yellow"),"______________ ", colored(" ( )", "red"))
        print(colored("- OLD JOB         :", "green"),"A??o. Engi??er ", colored(" (X)", "green"))
        print(colored("- BLOOD GROUP     :", "green"),"A+             ", colored(" (X)", "green"))
        print(colored("---------------------------------------------------------------", "green"))
        print("")
        print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
        print("")

        time.sleep(1)

        print("LOADING BIOMEDICAL DATA...")

        question=0

        time.sleep(3)

        while question != "315841451":
            print("")
            question = input("(2/6) Please indicates the <BIOTEC ID> of File '0/65-&05#' --> ")
            if question == "315841451" or question == "315841 451" or question == "315841-451":
                print("")
                print(colored("                             CORRECT INPUT. ","blue"))
                time.sleep(1)
                processing("PROCESSING")     
                

                time.sleep(5)
                os.system('clear')
                time.sleep(1)
                print("")
                print("")
                print(colored("---------------------------------------------------------------", "green"))
                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: M%P3-*O6$    -", "green"))
                print(colored("---------------------------------------------------------------", "green"))
                print(colored("- FIRSTNAME       :", "green"),"S??a?          ", colored(" (X)", "green"))
                print(colored("- LASTNAME        :", "green"),"J?H??O?        ", colored(" (X)", "green"))
                print(colored("- AGE             :", "green"),"??             ", colored(" (X)", "green"))
                print(colored("- CITY OF BIRTH   :", "yellow"),"______________ ", colored(" ( )", "red"))
                print(colored("- ZIP CODE        :", "green"),"A? 0?5?0       ", colored(" (X)", "green"))
                print(colored("- BIOTEC dis. ID  :", "green"),"72?9?5-10?     ", colored(" (X)", "green"))
                print(colored("- OLD JOB         :", "green"),"Me??a as?ist.  ", colored(" (X)", "green"))
                print(colored("- BLOOD GROUP     :", "green"),"B-             ", colored(" (X)", "green"))
                print(colored("---------------------------------------------------------------", "green"))
                print("")
                print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
                print("")

                time.sleep(1)

                print("LOADING BIOMEDICAL DATA...")

                question=0

                time.sleep(3)

                while question != "MONTGOMERY":
                    print("")
                    question = input("(3/6) Please indicates the <CITY OF BIRTH> of File 'M%P3-*O6$' --> ")
                    if question == "Montgomery" or question == "montgomery" or question == "MONTGOMERY":
                        print("")
                        print(colored("                             CORRECT INPUT. ","blue"))
                        time.sleep(1)
                        processing("PROCESSING")    
                        

                        time.sleep(5)
                        os.system('clear')
                        time.sleep(1)
                        print("")
                        print("")
                        print(colored("---------------------------------------------------------------", "green"))
                        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: $1R9-#56A    -", "green"))
                        print(colored("---------------------------------------------------------------", "green"))
                        print(colored("- FIRSTNAME       :", "green"),"??f???y        ", colored(" (X)", "green"))
                        print(colored("- LASTNAME        :", "green"),"S??T??G?       ", colored(" (X)", "green"))
                        print(colored("- AGE             :", "yellow"),"______________ ", colored(" ( )", "red"))
                        print(colored("- CITY OF BIRTH   :", "green"),"S?r?n?fi??d    ", colored(" (X)", "green"))
                        print(colored("- ZIP CODE        :", "green"),"?? ?.8862      ", colored(" (X)", "green"))
                        print(colored("- BIOTEC dis. ID  :", "green"),"??4??5-0??     ", colored(" (X)", "green"))
                        print(colored("- OLD JOB         :", "green"),"For??sic P?l.  ", colored(" (X)", "green"))
                        print(colored("- BLOOD GROUP     :", "green"),"A?+            ", colored(" (X)", "green"))
                        print(colored("---------------------------------------------------------------", "green"))
                        print("")
                        print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
                        print("")

                        time.sleep(1)

                        print("LOADING BIOMEDICAL DATA...")

                        question=0

                        time.sleep(3)

                        while question != "47":
                            print("")
                            question = input("(4/6) Please indicates the <AGE> of File '$1R9-#56A' --> ")
                            if question == "47":
                                print("")
                                print(colored("                             CORRECT INPUT. ","blue"))
                                time.sleep(1)
                                processing("PROCESSING")        
                                

                                time.sleep(5)
                                os.system('clear')
                                time.sleep(1)
                                print("")
                                print("")
                                print(colored("---------------------------------------------------------------", "green"))
                                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: #6ET-$223    -", "green"))
                                print(colored("---------------------------------------------------------------", "green"))
                                print(colored("- FIRSTNAME       :", "yellow"),"______________ ", colored(" ( )", "red"))
                                print(colored("- LASTNAME        :", "green"),"F????i?        ", colored(" (X)", "green"))
                                print(colored("- AGE             :", "green"),"??             ", colored(" (X)", "green"))
                                print(colored("- CITY OF BIRTH   :", "green"),"Vi??i??a C??y  ", colored(" (X)", "green"))
                                print(colored("- ZIP CODE        :", "green"),"?E ??4?9       ", colored(" (X)", "green"))
                                print(colored("- BIOTEC dis. ID  :", "green"),"??58?1-??3     ", colored(" (X)", "green"))
                                print(colored("- OLD JOB         :", "green"),"?le??r?c??n    ", colored(" (X)", "green"))
                                print(colored("- BLOOD GROUP     :", "green"),"?+             ", colored(" (X)", "green"))
                                print(colored("---------------------------------------------------------------", "green"))
                                print("")
                                print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
                                print("")


                                time.sleep(1)

                                print("LOADING BIOMEDICAL DATA...")

                                question=0

                                time.sleep(3)

                                while question != "James":
                                    print("")
                                    question = input("(5/6) Please indicates the <FIRSTNAME> of File '#6ET-$223' --> ")
                                    if question == "James" or question == "james" or question == "JAMES":
                                        print("")
                                        print(colored("                             CORRECT INPUT. ","blue"))
                                        time.sleep(1)
                                        processing("PROCESSING")


                                        time.sleep(5)
                                        os.system('clear')
                                        time.sleep(1)
                                        print("")
                                        print("")
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: 84$X-ER4%    -", "green"))
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print(colored("- FIRSTNAME       :", "green"),"??b??c?        ", colored(" (X)", "green"))
                                        print(colored("- LASTNAME        :", "green"),"??O??S         ", colored(" (X)", "green"))
                                        print(colored("- AGE             :", "green"),"2?             ", colored(" (X)", "green"))
                                        print(colored("- CITY OF BIRTH   :", "green"),"??v??gt??      ", colored(" (X)", "green"))
                                        print(colored("- ZIP CODE        :", "green"),"M? 78?92       ", colored(" (X)", "green"))
                                        print(colored("- BIOTEC dis. ID  :", "green"),"7???55-??8     ", colored(" (X)", "green"))
                                        print(colored("- OLD JOB         :", "yellow"),"______________ ", colored(" ( )", "red"))
                                        print(colored("- BLOOD GROUP     :", "green"),"??             ", colored(" (X)", "green"))
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print("")
                                        print(colored("[USER INFO] '?' is corrupted Data in Block Address", "white"))
                                        print("")

                                        time.sleep(1)

                                        print("LOADING BIOMEDICAL DATA...")

                                        question=0

                                        time.sleep(3)

                                        while question != "Mechanic":
                                            print("")
                                            question = input("(6/6) Please indicates the <OLD JOB> of File '84$X-ER4%' --> ")
                                            if question == "Mechanic" or question == "mechanic" or question == "garagiste" or question == "Garagiste":
                                                print("")
                                                print(colored("                             CORRECT INPUT. ","blue"))
                                                time.sleep(1)
                                                processing("PROCESSING")
                                                os.system('clear')        
                                                print("")
                                                print("")
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: 84$X-ER4%    -", "green"))
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print(colored("- FIRSTNAME       :", "green"),"Rebecca        ", colored(" (X)", "green"))
                                                print(colored("- LASTNAME        :", "green"),"FLORES         ", colored(" (X)", "green"))
                                                print(colored("- AGE             :", "green"),"23             ", colored(" (X)", "green"))
                                                print(colored("- CITY OF BIRTH   :", "green"),"Livington      ", colored(" (X)", "green"))
                                                print(colored("- ZIP CODE        :", "green"),"MT 78692       ", colored(" (X)", "green"))
                                                print(colored("- BIOTEC dis. ID  :", "green"),"724955-478     ", colored(" (X)", "green"))
                                                print(colored("- OLD JOB         :", "green"),"Mechanic       ", colored(" (X)", "green"))
                                                print(colored("- BLOOD GROUP     :", "green"),"A+             ", colored(" (X)", "green"))
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print("")
                                                time.sleep(5)


                                                print("")
                                                print("")
                                                time.sleep(2)
                                                print("-----------------------------------------------")
                                                print("Summary of Sector C BIOTEC dissident employees:")
                                                print("-----------------------------------------------")
                                                print("")
                                                plot_text_speed("** Optic & Design Department: **\n\n")
                                                plot_text_speed("- James FRANCIS      | Biotec Trust index: 42% | Risk for the Institute: YES  \n- Stanley PEARSON    | Biotec Trust index: 39% | Risk for the Institute: YES  \n\n")
                                                plot_text_speed("** Quietude and Security Operation Department: **\n\n")
                                                plot_text_speed("- Tiffany SANTIAGO   | Biotec Trust index: 43% | Risk for the Institute: YES  \n\n")
                                                plot_text_speed("** BIO-manufacturing Techniques Department: **\n\n")
                                                plot_text_speed("- Jeremy VELASQUEZ   | Biotec Trust index: 48% | Risk for the Institute: YES  \n- Rebecca FLORES     | Biotec Trust index: 41% | Risk for the Institute: YES  \n- Sarah JOHNSON      | Biotec Trust index: 45% | Risk for the Institute: YES  \n\n")
                                                print("")
                                                time.sleep(5)
                                                os.system('clear')
                                                plot_text_speed("******* YOU HAVE (1) UNREAD MESSAGE(S) FROM BIOTEC SUPERVISOR *******\n\n\n\nFrom: 'program.supervisor@biotec.org' To: 'macrodata.department@biotec.org'\nObject: 'CONGRATULATIONS!'\n--------------------------\n\n")
                                                plot_text("WELL DONE OPERATORS\n\nYou succeeded to recover biotec sensitive information about some...employees\n\n(Don't worry about them, we can now take care of these people).\n\nRegards,\nProgram Supervisor.")
                                                print("")
                                                print("")
                                                print("")
                                                print("")
                                                print("")
                                                print("")
                                                input("Press [ENTER] Key to continue...")
                                                os.system('clear')
                                                plot_text("STARTING Biotec(C) [CODE GENERATION PROGRAM v5.8] IN [5] Sec.")
                                                time.sleep(5)

                                                with Bar('Generating Code to Unlock the Safe...') as bar:
                                                    for i in range(100):
                                                        time.sleep(0.01)
                                                        bar.next()
                                                print("")                
                                                biotec_final_cmd = "figlet BIOTEC CODE"
                                                print("")
                                                code_generation_cmd = "figlet 2 . 1 . 4 . 6"

                                                print("")
                                                os.system(biotec_final_cmd)
                                                print("")
                                                os.system(code_generation_cmd)
                                                print("")
                                                print("")
                                                print("")
                                                plot_text("Task DONE.")

                                                time.sleep(3600)        





                                            else:
                                                print("")
                                                print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
                                                time.sleep(3)
                                                os.system('clear')
                                                print("")
                                                print("")
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: 84$X-ER4%    -", "green"))
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print(colored("- FIRSTNAME       :", "green"),"??b??c?        ", colored(" (X)", "green"))
                                                print(colored("- LASTNAME        :", "green"),"??O??S         ", colored(" (X)", "green"))
                                                print(colored("- AGE             :", "green"),"2?             ", colored(" (X)", "green"))
                                                print(colored("- CITY OF BIRTH   :", "green"),"??v??gt??      ", colored(" (X)", "green"))
                                                print(colored("- ZIP CODE        :", "green"),"M? 78?92       ", colored(" (X)", "green"))
                                                print(colored("- BIOTEC dis. ID  :", "green"),"7???55-??8     ", colored(" (X)", "green"))
                                                print(colored("- OLD JOB         :", "yellow"),"______________ ", colored(" ( )", "red"))
                                                print(colored("- BLOOD GROUP     :", "green"),"??             ", colored(" (X)", "green"))
                                                print(colored("---------------------------------------------------------------", "green"))
                                                print("")
                                                print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
                                                print("")
                                                print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")


                                    else:
                                        print("")
                                        print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
                                        time.sleep(3)
                                        os.system('clear')
                                        print("")
                                        print("")
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: #6ET-$223    -", "green"))
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print(colored("- FIRSTNAME       :", "yellow"),"______________ ", colored(" ( )", "red"))
                                        print(colored("- LASTNAME        :", "green"),"F????i?        ", colored(" (X)", "green"))
                                        print(colored("- AGE             :", "green"),"??             ", colored(" (X)", "green"))
                                        print(colored("- CITY OF BIRTH   :", "green"),"Vi??i??a C??y  ", colored(" (X)", "green"))
                                        print(colored("- ZIP CODE        :", "green"),"?E ??4?9       ", colored(" (X)", "green"))
                                        print(colored("- BIOTEC dis. ID  :", "green"),"??58?1-??3     ", colored(" (X)", "green"))
                                        print(colored("- OLD JOB         :", "green"),"?le??r?c??n    ", colored(" (X)", "green"))
                                        print(colored("- BLOOD GROUP     :", "green"),"?+             ", colored(" (X)", "green"))
                                        print(colored("---------------------------------------------------------------", "green"))
                                        print("")
                                        print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
                                        print("")
                                        print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")


                            else:
                                print("")
                                print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
                                time.sleep(3)
                                os.system('clear')
                                print("")
                                print("")
                                print(colored("---------------------------------------------------------------", "green"))
                                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: $1R9-#56A    -", "green"))
                                print(colored("---------------------------------------------------------------", "green"))
                                print(colored("- FIRSTNAME       :", "green"),"??f???y        ", colored(" (X)", "green"))
                                print(colored("- LASTNAME        :", "green"),"S??T??G?       ", colored(" (X)", "green"))
                                print(colored("- AGE             :", "yellow"),"______________ ", colored(" ( )", "red"))
                                print(colored("- CITY OF BIRTH   :", "green"),"S?r?n?fi??d    ", colored(" (X)", "green"))
                                print(colored("- ZIP CODE        :", "green"),"?? ?.8862      ", colored(" (X)", "green"))
                                print(colored("- BIOTEC dis. ID  :", "green"),"??4??5-0??     ", colored(" (X)", "green"))
                                print(colored("- OLD JOB         :", "green"),"For??sic P?l.  ", colored(" (X)", "green"))
                                print(colored("- BLOOD GROUP     :", "green"),"A?+            ", colored(" (X)", "green"))
                                print(colored("---------------------------------------------------------------", "green"))
                                print("")
                                print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
                                print("")
                                print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")




                    else:
                        print("")
                        print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
                        time.sleep(3)
                        os.system('clear')
                        print("")
                        print("")
                        print(colored("---------------------------------------------------------------", "green"))
                        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: M%P3-*O6$    -", "green"))
                        print(colored("---------------------------------------------------------------", "green"))
                        print(colored("- FIRSTNAME       :", "green"),"S??a?          ", colored(" (X)", "green"))
                        print(colored("- LASTNAME        :", "green"),"J?H??O?        ", colored(" (X)", "green"))
                        print(colored("- AGE             :", "green"),"??             ", colored(" (X)", "green"))
                        print(colored("- CITY OF BIRTH   :", "yellow"),"______________ ", colored(" ( )", "red"))
                        print(colored("- ZIP CODE        :", "green"),"A? 0?5?0       ", colored(" (X)", "green"))
                        print(colored("- BIOTEC dis. ID  :", "green"),"72?9?5-10?     ", colored(" (X)", "green"))
                        print(colored("- OLD JOB         :", "green"),"Me??a as?ist.  ", colored(" (X)", "green"))
                        print(colored("- BLOOD GROUP     :", "green"),"B-             ", colored(" (X)", "green"))
                        print(colored("---------------------------------------------------------------", "green"))
                        print("")
                        print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
                        print("")
                        print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")

        
            else:
                print("")
                print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
                time.sleep(3)
                os.system('clear')
                print("")
                print("")
                print(colored("---------------------------------------------------------------", "green"))
                print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R) - FILE: 0/65-&05#    -", "green"))
                print(colored("---------------------------------------------------------------", "green"))
                print(colored("- FIRSTNAME       :", "green"),"J?r?m?         ", colored(" (X)", "green"))
                print(colored("- LASTNAME        :", "green"),"VE?A?Q???      ", colored(" (X)", "green"))
                print(colored("- AGE             :", "green"),"3?             ", colored(" (X)", "green"))
                print(colored("- CITY OF BIRTH   :", "green"),"Sr??ng-Va???   ", colored(" (X)", "green"))
                print(colored("- ZIP CODE        :", "green"),"?V 3??00       ", colored(" (X)", "green"))
                print(colored("- BIOTEC dis. ID  :", "yellow"),"______________ ", colored(" ( )", "red"))
                print(colored("- OLD JOB         :", "green"),"A??o. Engi??er ", colored(" (X)", "green"))
                print(colored("- BLOOD GROUP     :", "green"),"A+             ", colored(" (X)", "green"))
                print(colored("---------------------------------------------------------------", "green"))
                print("")
                print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
                print("")
                print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")



    else:
        print("")
        print(colored("         /!\ NO MATCH IN DATABASE WITH THIS INPUT /!\ ","red"))
        time.sleep(3)
        os.system('clear')
        print("")
        print("")
        print(colored("---------------------------------------------------------------", "green"))
        print(colored("-  DATABASE ARCHIVE: BIOTEC Institute(R)  FILE: $0FE-$210     -", "green"))
        print(colored("---------------------------------------------------------------", "green"))
        print(colored("- FIRSTNAME       :", "green"),"S??n?ey       ", colored(" (X)", "green"))
        print(colored("- LASTNAME        :", "yellow"),"_____________ ", colored(" ( )", "red"))
        print(colored("- AGE             :", "green"),"31            ", colored(" (X)", "green"))
        print(colored("- CITY OF BIRTH   :", "green"),"Me??h?s       ", colored(" (X)", "green"))
        print(colored("- ZIP CODE        :", "green"),"TN 6??72      ", colored(" (X)", "green"))
        print(colored("- BIOTEC dis. ID  :", "green"),"31?8?1-?63    ", colored(" (X)", "green"))
        print(colored("- OLD JOB         :", "green"),"E?g?n???      ", colored(" (X)", "green"))
        print(colored("- BLOOD GROUP     :", "green"),"AB-           ", colored(" (X)", "green"))
        print(colored("---------------------------------------------------------------", "green"))
        print("")
        print(colored("[USER INFO] '?' is corrupted Data in Block Address'", "white"))
        print("")
        print("PLEASE FILL IN WITH EXISTING INFORMATION FROM DATABASE:")
