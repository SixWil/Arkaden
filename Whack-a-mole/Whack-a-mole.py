import PySimpleGUI as sg
from time import sleep
import random
import threading



värde = random.randint(1,9)
poäng = 0
timer = 10
wait = 1
spel = False

def timerer():
    global timer
    global spel

    while timer > 0:
        sleep(wait)
        timer -= 1
        window['-timer-'].update(f'timer: {timer}')
        window.refresh()
    else:
        spel = False
        

tt = threading.Thread(target=timerer)

window = sg.Window('', layout=[
    [sg.Text(f'poäng: {poäng}', key='-poäng-')],
    [sg.Text(f'värde: {värde}', key='-värde-')],
    [sg.Text(f'timer: {timer}', key='-timer-')],
    [sg.Button(1),sg.Button(2),sg.Button(3)],
    [sg.Button(4),sg.Button(5),sg.Button(6)],
    [sg.Button(7),sg.Button(8),sg.Button(9)],
])


event, value = window.read()
tt.start()
while True:
    
    if int(event) == värde and timer > 0:
        poäng += timer
        timer = 11
        wait -= 0.1
        window['-poäng-'].update(f'poäng: {poäng}')
        värde = random.randint(1,9)
        window['-värde-'].update(f'värde: {värde}')
        
    event, value = window.read()