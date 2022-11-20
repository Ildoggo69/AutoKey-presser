
# importiamo le librerie necessarie

from pyautogui import *
import keyboard
import time
import pyautogui

counter = 0                                                                        # variabile per il primo ciclo

key = str(input("Mettere (solo) la lettera da premere->: "))                       # hotkey da premere
stopkey = str(input("Mettere (solo) la lettera per stoppare il programma->: "))    # hotkey per stoppare

#Primo ciclo
while counter == 0:
    
    start = int(input("metti cifra sopra lo zero per iniziare il programma->: "))  # valore per iniziare il programma
    

    if start == start>0:                                                           # condizione per avviare il secondo ciclo

        time.sleep(2)                                                              # piccolo delay prima del ciclo
        
        while start>0:                                                             # ciclo infinito
            
            pyautogui.press(key)                                                   # premuta del tasto, precedentemente dichiarato
            
            if keyboard.is_pressed(stopkey):                                       # condizione per il blocco del ciclo
                break                                                              # usando break usciamo dal ciclo while
        counter = counter + 1                                                      # uscita dal primo ciclo

    else:
        print("Cifra invalida, reinserire numero")


time.sleep(0.03)

print("\nChiusura app in: ")                                                       #countdown per la chiusra dello script

for tempo in range(1, 4):
    print(tempo)
    time.sleep(1)

print("Chiuso")





       
