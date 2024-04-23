import keyboard
from random import randint as rand
import time

spel = True
bonus = False
mask = [5,5,5,5]

yta = [
    '0','1','2','3','4','5','6','7','8','9',
    '1',' ',' ',' ',' ',' ',' ',' ',' ','8',
    '2',' ',' ',' ',' ',' ',' ',' ',' ','7',
    '3',' ',' ',' ',' ',' ',' ',' ',' ','6',
    '4',' ',' ',' ',' ',' ',' ',' ',' ','5',
    '5',' ',' ',' ','*',' ',' ',' ',' ','4',
    '6',' ',' ',' ',' ',' ',' ',' ',' ','3',
    '7',' ',' ',' ',' ',' ',' ',' ',' ','2',
    '8',' ',' ',' ',' ',' ',' ',' ',' ','1',
    '9','8','7','6','5','4','3','2','1','0',
    ]

def placering(x,y):
    global mask
    mask += [x,y]
    if yta[x+(y*10)] in ['O','1','2','3','4','5','6','7','8','9','0']:
        global spel
        spel = False
        print('FAIL')
        
    else:

        if yta[x+(y*10)] == '*':
            mask += [x]
            mask += [y]
            yta[rand(2,8)+(rand(2,8)*10)] = '*'
            

        yta[mask[-2] + mask[-1]*10] = 'O'
        yta[mask[0] + mask[1]*10] = ' '
        mask.pop(0)
        mask.pop(0)
    
        for i in range(33):
            print()
        for i in range(10):
            print(yta[10*(i):10*(i+1)])
    
    time.sleep(.3)

placering(5,5)

x = 5

y = 5

höjd = 0
bred = 0

key = keyboard.read_key()

while spel == True:
    

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
    
    

    x += bred
    y += höjd
    placering(x,y)
