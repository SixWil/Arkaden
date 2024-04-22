import keyboard
from random import randint as rand

spel = True
bonus = False
mask = [5,5,5,5]

yta = [
    '0','1','2','3','4','5','6','7','8','9',
    '1',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '2',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '3',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '4',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '5',' ',' ',' ','*',' ',' ',' ',' ',' ',
    '6',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '7',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '8',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    '9',' ',' ',' ',' ',' ',' ',' ',' ',' ',
    ]

def placering(x,y):
    global mask
    if yta[x+(y*10)] == 'O':
        global spel
        spel = False
        print('FAIL')
        
    else:

        if yta[x+(y*10)] == '*':
            mask += [x]
            mask += [y]
            yta[rand(1,9)+(rand(1,9)*10)] = '*'
            

        yta[mask[-2] + mask[-1]*10] = 'O'
        yta[mask[0] + mask[1]*10] = ' '
        mask.pop(0)
        mask.pop(0)
    
        for i in range(33):
            print()
        for i in range(10):
            print(yta[10*(i):10*(i+1)])

placering(5,5)

x = 5

y = 5

key = keyboard.read_key()

while spel == True:
    if keyboard.read_key() in ['w','s','d','a']:

        # yta[x+((y+bonus)*10)] = ' '
        # yta[x+((y-bonus)*10)] = ' '
        # yta[x+bonus+(y*10)] = ' '
        # yta[x-bonus+(y*10)] = ' '

        key = keyboard.read_key()
        if key == 'w' and y > 0:
            
            y -= 1
        if key == 's' and y < 9:
            
            y += 1
        if key == 'a' and x > 0:
            
            x -= 1
        if key == 'd' and x < 9:
            
            x += 1

        mask += [x,y]
        
        print(mask)
        placering(x,y)