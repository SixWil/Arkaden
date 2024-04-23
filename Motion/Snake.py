import keyboard
from random import randint as rand
import time
import threading

spel = True
bonus = False
mask = [5,5,5,5]
poäng = 0

yta = [
    ' ','0','1','2','3','4','5','6','7','8','9',' ',
    '0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','9',
    '1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','8',
    '2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7',
    '3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','6',
    '4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','5',
    '5',' ',' ',' ','*',' ',' ',' ',' ',' ',' ','4',
    '6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','3',
    '7',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','2',
    '8',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',
    '9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',
    ' ','9','8','7','6','5','4','3','2','1','0',' ',
    ]

def placering():
    global mask
    global x
    global y
    global bred
    global höjd
    global spel
    global poäng

    while spel == True:
        x += bred
        y += höjd
        
        mask += [x,y]
        if yta[x+(y*12)] in ['O','1','2','3','4','5','6','7','8','9','0']:
            spel = False
            print(f'Du fick {poäng} poäng')
            
        else:

            if yta[x+(y*12)] == '*':
                poäng += 1
                mask += [x]
                mask += [y]
                yta[rand(3,10)+(rand(3,10)*12)] = '*'
                

            yta[mask[-2] + mask[-1]*12] = 'O'
            yta[mask[0] + mask[1]*12] = ' '
            mask.pop(0)
            mask.pop(0)
    
            print('''
































''')
            # for i in range(10):
            print(f'''                {yta[0:10+2]}
                {yta[10+2:20+2+2]}
                {yta[20+2+2:30+2+2+2]}
                {yta[30+2+2+2:40+2+2+2+2]}
                {yta[40+2+2+2+2:50+2+2+2+2+2]}
                {yta[50+2+2+2+2+2:60+2+2+2+2+2+2]}
                {yta[60+2+2+2+2+2+2:70+2+2+2+2+2+2+2]}
                {yta[70+2+2+2+2+2+2+2:80+2+2+2+2+2+2+2+2]}
                {yta[80+2+2+2+2+2+2+2+2:90+2+2+2+2+2+2+2+2+2]}
                {yta[90+2+2+2+2+2+2+2+2+2:100+2+2+2+2+2+2+2+2+2+2]}
                {yta[100+2+2+2+2+2+2+2+2+2+2:110+2+2+2+2+2+2+2+2+2+2+2]}
                {yta[110+2+2+2+2+2+2+2+2+2+2+2:120+2+2+2+2+2+2+2+2+2+2+2+2]}''')
        
        time.sleep(.3)

# placering(5,5)

x = 5

y = 5

höjd = 0
bred = 0
print('''
































''')
print(f'''                    {yta[0:10+2]}
                    {yta[10+2:20+2+2]}
                    {yta[20+2+2:30+2+2+2]}
                    {yta[30+2+2+2:40+2+2+2+2]}
                    {yta[40+2+2+2+2:50+2+2+2+2+2]}
                    {yta[50+2+2+2+2+2:60+2+2+2+2+2+2]}
                    {yta[60+2+2+2+2+2+2:70+2+2+2+2+2+2+2]}
                    {yta[70+2+2+2+2+2+2+2:80+2+2+2+2+2+2+2+2]}
                    {yta[80+2+2+2+2+2+2+2+2:90+2+2+2+2+2+2+2+2+2]}
                    {yta[90+2+2+2+2+2+2+2+2+2:100+2+2+2+2+2+2+2+2+2+2]}
                    {yta[100+2+2+2+2+2+2+2+2+2+2:110+2+2+2+2+2+2+2+2+2+2+2]}
                    {yta[110+2+2+2+2+2+2+2+2+2+2+2:120+2+2+2+2+2+2+2+2+2+2+2+2]}''')

key = keyboard.read_key()

threading.Thread(target=placering).start()



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
    
    

    
