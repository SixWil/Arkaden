import keyboard
from random import randint as rand
import time
import threading
import PySimpleGUI as sg

spel = True
bonus = False
mask = [5,5,5,5]
poäng = 0
counter = 9
hastighet = 1


# spelplanen som kallas varje 'tick'
yta = [
    '#',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','[_]','#',
    '#',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ',' # ','#',
    ]
# pop up ruta
window = sg.Window('', layout=[
[sg.Text(f'poäng: {round(poäng)}',key='-poäng-')],
[sg.Text(f'hastighet: {round((1-hastighet))}',key='-hastighet-'),],
[sg.Text(f'''
{yta[0+(12*0)]}{yta[1+(12*0)]}{yta[2+(12*0)]}{yta[3+(12*0)]}{yta[4+(12*0)]}{yta[5+(12*0)]}{yta[6+(12*0)]}{yta[7+(12*0)]}{yta[8+(12*0)]}{yta[9+(12*0)]}{yta[10+(12*0)]}{yta[11+(12*0)]}
{yta[12+(12*0)]}{yta[1+(12*1)]}{yta[2+(12*1)]}{yta[3+(12*1)]}{yta[4+(12*1)]}{yta[5+(12*1)]}{yta[6+(12*1)]}{yta[7+(12*1)]}{yta[8+(12*1)]}{yta[9+(12*1)]}{yta[10+(12*1)]}{yta[11+(12*1)]}
{yta[12+(12*1)]}{yta[1+(12*2)]}{yta[2+(12*2)]}{yta[3+(12*2)]}{yta[4+(12*2)]}{yta[5+(12*2)]}{yta[6+(12*2)]}{yta[7+(12*2)]}{yta[8+(12*2)]}{yta[9+(12*2)]}{yta[10+(12*2)]}{yta[11+(12*2)]}
{yta[12+(12*2)]}{yta[1+(12*3)]}{yta[2+(12*3)]}{yta[3+(12*3)]}{yta[4+(12*3)]}{yta[5+(12*3)]}{yta[6+(12*3)]}{yta[7+(12*3)]}{yta[8+(12*3)]}{yta[9+(12*3)]}{yta[10+(12*3)]}{yta[11+(12*3)]}
{yta[12+(12*3)]}{yta[1+(12*4)]}{yta[2+(12*4)]}{yta[3+(12*4)]}{yta[4+(12*4)]}{yta[5+(12*4)]}{yta[6+(12*4)]}{yta[7+(12*4)]}{yta[8+(12*4)]}{yta[9+(12*4)]}{yta[10+(12*4)]}{yta[11+(12*4)]}
{yta[12+(12*4)]}{yta[1+(12*5)]}{yta[2+(12*5)]}{yta[3+(12*5)]}{yta[4+(12*5)]}{yta[5+(12*5)]}{yta[6+(12*5)]}{yta[7+(12*5)]}{yta[8+(12*5)]}{yta[9+(12*5)]}{yta[10+(12*5)]}{yta[11+(12*5)]}
{yta[12+(12*5)]}{yta[1+(12*6)]}{yta[2+(12*6)]}{yta[3+(12*6)]}{yta[4+(12*6)]}{yta[5+(12*6)]}{yta[6+(12*6)]}{yta[7+(12*6)]}{yta[8+(12*6)]}{yta[9+(12*6)]}{yta[10+(12*6)]}{yta[11+(12*6)]}
{yta[12+(12*6)]}{yta[1+(12*7)]}{yta[2+(12*7)]}{yta[3+(12*7)]}{yta[4+(12*7)]}{yta[5+(12*7)]}{yta[6+(12*7)]}{yta[7+(12*7)]}{yta[8+(12*7)]}{yta[9+(12*7)]}{yta[10+(12*7)]}{yta[11+(12*7)]}
{yta[12+(12*7)]}{yta[1+(12*8)]}{yta[2+(12*8)]}{yta[3+(12*8)]}{yta[4+(12*8)]}{yta[5+(12*8)]}{yta[6+(12*8)]}{yta[7+(12*8)]}{yta[8+(12*8)]}{yta[9+(12*8)]}{yta[10+(12*8)]}{yta[11+(12*8)]}
{yta[12+(12*8)]}{yta[1+(12*9)]}{yta[2+(12*9)]}{yta[3+(12*9)]}{yta[4+(12*9)]}{yta[5+(12*9)]}{yta[6+(12*9)]}{yta[7+(12*9)]}{yta[8+(12*9)]}{yta[9+(12*9)]}{yta[10+(12*9)]}{yta[11+(12*9)]}
{yta[12+(12*9)]}{yta[1+(12*10)]}{yta[2+(12*10)]}{yta[3+(12*10)]}{yta[4+(12*10)]}{yta[5+(12*10)]}{yta[6+(12*10)]}{yta[7+(12*10)]}{yta[8+(12*10)]}{yta[10+(12*10)]}{yta[10+(12*10)]}{yta[11+(12*10)]}
{yta[12+(12*10)]}{yta[1+(12*11)]}{yta[2+(12*11)]}{yta[3+(12*11)]}{yta[4+(12*11)]}{yta[5+(12*11)]}{yta[6+(12*11)]}{yta[7+(12*11)]}{yta[8+(12*11)]}{yta[9+(12*11)]}{yta[10+(12*11)]}{yta[11+(12*11)]}
''', font='arial 20', key='-banan-')],
])
window.Read(1000)


# thread som kör samtidigt som kontrollerna
def placering():
    global mask
    global x
    global y
    global bred
    global höjd
    global spel
    global poäng
    global counter
    global hastighet
    global window
    global bonus
    # om du inte kraschat
    while spel == True:
        x += bred
        y += höjd
        
        mask += [x,y]

        # om du kraschar
        if yta[x+(y*12)] in [' ¤ ',' o ','#',' # ']:
            yta[mask[-2] + mask[-1]*12] = ' x '
            window.refresh()
            spel = False
        else:
            # poäng systemet
            if yta[x+(y*12)] == ' + ':
                poäng += 1 / hastighet
                # poäng = round(poäng)
                hastighet -= hastighet / 10
                bonus = True
                # mask.append(yta[(mask[0]) + (mask[1])*12])
                # mask += [x]
                # mask += [y]
                # while True:

                # rx = rand(3,10)
                # ry = rand(3,10)
                # while {yta[rx + ry*12]} == 'o'or yta[rx + ry] == 'O':
                #     rx = rand(3,10
                #     ry = rand(3,10)
                # else:
                #     yta[rx + ry*12] = '¤'
                #     break
            # poäng placerings systemet
            if yta.count(' + ') < 3:

                # if rand(1,10) == 10:
                #     yta[rand(1,10) + rand(1,10)*12] = ' + '
                #     counter = 0
                # else:
                counter += 1
                if counter == 10:
                    counter = 0
                    yta[rand(1,10) + rand(1,10)*12] = ' + '
           
            # yta[mask[-6] + mask[-5]*12] = ' ¤ '
                    
            # mask placerings systemet
            yta[mask[-4] + mask[-3]*12] = ' ¤ '
            yta[mask[-2] + mask[-1]*12] = ' o '
            if yta[mask[0] + mask[1]*12] == ' ¤ ':
                yta[mask[0] + mask[1]*12] = '[_]'
            if bonus == False:
                mask.pop(0)
                mask.pop(0)
            else:
                bonus = False
        
        # tick rate
        time.sleep(hastighet)
            
#             window['-banan-'].update(f'''{yta[0:10+2]}
# {yta[10+2:20+2+2]}
# {yta[20+2+2:30+2+2+2]}
# {yta[30+2+2+2:40+2+2+2+2]}
# {yta[40+2+2+2+2:50+2+2+2+2+2]}
# {yta[50+2+2+2+2+2:60+2+2+2+2+2+2]}
# {yta[60+2+2+2+2+2+2:70+2+2+2+2+2+2+2]}
# {yta[70+2+2+2+2+2+2+2:80+2+2+2+2+2+2+2+2]}
# {yta[80+2+2+2+2+2+2+2+2:90+2+2+2+2+2+2+2+2+2]}
# {yta[90+2+2+2+2+2+2+2+2+2:100+2+2+2+2+2+2+2+2+2+2]}
# {yta[100+2+2+2+2+2+2+2+2+2+2:110+2+2+2+2+2+2+2+2+2+2+2]}
# {yta[110+2+2+2+2+2+2+2+2+2+2+2:120+2+2+2+2+2+2+2+2+2+2+2+2]}''')
            # window.refresh()
    
#             print('''
































# ''')
#             # for i in range(10):
#             print(f'''                {yta[0:10+2]}
#                 {yta[10+2:20+2+2]}
#                 {yta[20+2+2:30+2+2+2]}
#                 {yta[30+2+2+2:40+2+2+2+2]}
#                 {yta[40+2+2+2+2:50+2+2+2+2+2]}
#                 {yta[50+2+2+2+2+2:60+2+2+2+2+2+2]}
#                 {yta[60+2+2+2+2+2+2:70+2+2+2+2+2+2+2]}
#                 {yta[70+2+2+2+2+2+2+2:80+2+2+2+2+2+2+2+2]}
#                 {yta[80+2+2+2+2+2+2+2+2:90+2+2+2+2+2+2+2+2+2]}
#                 {yta[90+2+2+2+2+2+2+2+2+2:100+2+2+2+2+2+2+2+2+2+2]}
#                 {yta[100+2+2+2+2+2+2+2+2+2+2:110+2+2+2+2+2+2+2+2+2+2+2]}
#                 {yta[110+2+2+2+2+2+2+2+2+2+2+2:120+2+2+2+2+2+2+2+2+2+2+2+2]}''')
        
#         time.sleep(hastighet)

# # placering(5,5)

x = 5

y = 5

höjd = 0
bred = 0
# print('''
































# ''')
# print(f'''                    {yta[0:10+2]}
#                     {yta[10+2:20+2+2]}
#                     {yta[20+2+2:30+2+2+2]}
#                     {yta[30+2+2+2:40+2+2+2+2]}
#                     {yta[40+2+2+2+2:50+2+2+2+2+2]}
#                     {yta[50+2+2+2+2+2:60+2+2+2+2+2+2]}
#                     {yta[60+2+2+2+2+2+2:70+2+2+2+2+2+2+2]}
#                     {yta[70+2+2+2+2+2+2+2:80+2+2+2+2+2+2+2+2]}
#                     {yta[80+2+2+2+2+2+2+2+2:90+2+2+2+2+2+2+2+2+2]}
#                     {yta[90+2+2+2+2+2+2+2+2+2:100+2+2+2+2+2+2+2+2+2+2]}
#                     {yta[100+2+2+2+2+2+2+2+2+2+2:110+2+2+2+2+2+2+2+2+2+2+2]}
#                     {yta[110+2+2+2+2+2+2+2+2+2+2+2:120+2+2+2+2+2+2+2+2+2+2+2+2]}''')

key = keyboard.read_key()

threading.Thread(target=placering).start()


# kontrollerna
while spel == True:

    window['-banan-'].update(f'''
{yta[0+(12*0)]}{yta[1+(12*0)]}{yta[2+(12*0)]}{yta[3+(12*0)]}{yta[4+(12*0)]}{yta[5+(12*0)]}{yta[6+(12*0)]}{yta[7+(12*0)]}{yta[8+(12*0)]}{yta[9+(12*0)]}{yta[10+(12*0)]}{yta[11+(12*0)]}
{yta[12+(12*0)]}{yta[1+(12*1)]}{yta[2+(12*1)]}{yta[3+(12*1)]}{yta[4+(12*1)]}{yta[5+(12*1)]}{yta[6+(12*1)]}{yta[7+(12*1)]}{yta[8+(12*1)]}{yta[9+(12*1)]}{yta[10+(12*1)]}{yta[11+(12*1)]}
{yta[12+(12*1)]}{yta[1+(12*2)]}{yta[2+(12*2)]}{yta[3+(12*2)]}{yta[4+(12*2)]}{yta[5+(12*2)]}{yta[6+(12*2)]}{yta[7+(12*2)]}{yta[8+(12*2)]}{yta[9+(12*2)]}{yta[10+(12*2)]}{yta[11+(12*2)]}
{yta[12+(12*2)]}{yta[1+(12*3)]}{yta[2+(12*3)]}{yta[3+(12*3)]}{yta[4+(12*3)]}{yta[5+(12*3)]}{yta[6+(12*3)]}{yta[7+(12*3)]}{yta[8+(12*3)]}{yta[9+(12*3)]}{yta[10+(12*3)]}{yta[11+(12*3)]}
{yta[12+(12*3)]}{yta[1+(12*4)]}{yta[2+(12*4)]}{yta[3+(12*4)]}{yta[4+(12*4)]}{yta[5+(12*4)]}{yta[6+(12*4)]}{yta[7+(12*4)]}{yta[8+(12*4)]}{yta[9+(12*4)]}{yta[10+(12*4)]}{yta[11+(12*4)]}
{yta[12+(12*4)]}{yta[1+(12*5)]}{yta[2+(12*5)]}{yta[3+(12*5)]}{yta[4+(12*5)]}{yta[5+(12*5)]}{yta[6+(12*5)]}{yta[7+(12*5)]}{yta[8+(12*5)]}{yta[9+(12*5)]}{yta[10+(12*5)]}{yta[11+(12*5)]}
{yta[12+(12*5)]}{yta[1+(12*6)]}{yta[2+(12*6)]}{yta[3+(12*6)]}{yta[4+(12*6)]}{yta[5+(12*6)]}{yta[6+(12*6)]}{yta[7+(12*6)]}{yta[8+(12*6)]}{yta[9+(12*6)]}{yta[10+(12*6)]}{yta[11+(12*6)]}
{yta[12+(12*6)]}{yta[1+(12*7)]}{yta[2+(12*7)]}{yta[3+(12*7)]}{yta[4+(12*7)]}{yta[5+(12*7)]}{yta[6+(12*7)]}{yta[7+(12*7)]}{yta[8+(12*7)]}{yta[9+(12*7)]}{yta[10+(12*7)]}{yta[11+(12*7)]}
{yta[12+(12*7)]}{yta[1+(12*8)]}{yta[2+(12*8)]}{yta[3+(12*8)]}{yta[4+(12*8)]}{yta[5+(12*8)]}{yta[6+(12*8)]}{yta[7+(12*8)]}{yta[8+(12*8)]}{yta[9+(12*8)]}{yta[10+(12*8)]}{yta[11+(12*8)]}
{yta[12+(12*8)]}{yta[1+(12*9)]}{yta[2+(12*9)]}{yta[3+(12*9)]}{yta[4+(12*9)]}{yta[5+(12*9)]}{yta[6+(12*9)]}{yta[7+(12*9)]}{yta[8+(12*9)]}{yta[9+(12*9)]}{yta[10+(12*9)]}{yta[11+(12*9)]}
{yta[12+(12*9)]}{yta[1+(12*10)]}{yta[2+(12*10)]}{yta[3+(12*10)]}{yta[4+(12*10)]}{yta[5+(12*10)]}{yta[6+(12*10)]}{yta[7+(12*10)]}{yta[8+(12*10)]}{yta[10+(12*10)]}{yta[10+(12*10)]}{yta[11+(12*10)]}
{yta[12+(12*10)]}{yta[1+(12*11)]}{yta[2+(12*11)]}{yta[3+(12*11)]}{yta[4+(12*11)]}{yta[5+(12*11)]}{yta[6+(12*11)]}{yta[7+(12*11)]}{yta[8+(12*11)]}{yta[9+(12*11)]}{yta[10+(12*11)]}{yta[11+(12*11)]}
''')
    window['-poäng-'].update(f'poäng: {round(poäng)}')
    window['-hastighet-'].update(f'hastighet: {round((1-hastighet)*100)}')
    window.refresh()
    

    if keyboard.is_pressed('w'):
        # if keyboard.read_key() in ['s','a','d']:
        #     break
        höjd = -1
        bred = 0
        
        
    if keyboard.is_pressed('s'):
        # if keyboard.read_key() in ['w','a','d']:
        #     break
        höjd = 1
        bred = 0
        

    if keyboard.is_pressed('a'):
        # if keyboard.read_key() in ['w','s','d']:
        #     break
        bred = -1
        höjd = 0
        

    if keyboard.is_pressed('d'):
        # if keyboard.read_key() in ['w','s','a']:
        #     break
        bred = 1
        höjd = 0
# om du kraschat
else:
    window['-poäng-'].update(f'Du fick {round(poäng)} poäng,')
    window['-hastighet-'].update(f'med en top hastighet på {round((1-hastighet)*100)}')
    print(f'Du fick {round(poäng)} poäng, med en top hastighet på {round((1-hastighet*100))}')
    window.read()