import PySimpleGUI as sg
from time import sleep
import random
import threading

# variabler

värde = random.randint(1,9)
poäng = 0
timer = 10
wait = 1
spel = False

# timer

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
        
# thread för timer så den kan köra oavsett av spelarens input

tt = threading.Thread(target=timerer)

# skärmen

window = sg.Window('', layout=[
    [sg.Text(f'poäng: {poäng}', key='-poäng-')],
    [sg.Text(f'värde: {värde}', key='-värde-')],
    [sg.Text(f'timer: {timer}', key='-timer-')],
    [sg.Button(1),sg.Button(2),sg.Button(3)],
    [sg.Button(4),sg.Button(5),sg.Button(6)],
    [sg.Button(7),sg.Button(8),sg.Button(9)],
])


# event blir värdet av knappen tryckt
event, value = window.read()
#starta timern
tt.start()
# avläs om event är samma som värde, om så ge poäng av tid, annars dra av poäng av tid.
while True:
    # så länge det finns tid kvar på klockan.
    if timer > 0:
        # om knappen tryckt är rätt
        if int(event) == värde:
            poäng += timer
            timer = 11
            wait -= 0.1
            window['-poäng-'].update(f'poäng: {poäng}')
            värde = random.randint(1,9)
            window['-värde-'].update(f'värde: {värde}')
        # om knappen tryckt är fel
        else:
            poäng -= timer
            timer = 11
            wait -= 0.1
            window['-poäng-'].update(f'poäng: {poäng}')
            värde = random.randint(1,9)
            window['-värde-'].update(f'värde: {värde}')
    # kolla vilken knapp är tryckt
    event, value = window.read()