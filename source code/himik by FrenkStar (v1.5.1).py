import pyautogui
import time
import pygame
import tkinter

timer=1
clicki = 1
outhimX = 1427
outhimY = 848
pos4000X = 997
pos4000Y = 514
poshimX = 1000
poshimY = 584
waterX = 500
waterY = 500
razrab=0
pyautogui.FAILSAFE=True
window = 0

def Close():
    window.destroy()

def proverkawindowshim():
    global window
    window = tkinter.Tk()
    window.overrideredirect(True)
    window.attributes('-alpha', 0.3, "-topmost", True)
    window.title('Проверка расположения')
    window.geometry('751x452+1170+590')
    window.resizable(width=False, height=False)
    button = tkinter.Button(window, text='закрыть окно', command=Close, bd=600)
    button.pack()
    window.mainloop()

def proverkawindows4000():
    global window
    window = tkinter.Tk()
    window.overrideredirect(True)
    window.attributes('-alpha',0.3,"-topmost", True)
    window.title('Проверка расположения')
    window.geometry('619x668+0+25')
    window.resizable(width=False, height=False)
    button = tkinter.Button(window,text='закрыть окно',command=Close,bd=600)
    button.pack()
    window.mainloop()

def bikardin():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц бикардина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(1426,714) # координаты кислорода
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=1343,y=778) # сахар
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1534, y=785) # углерод
        pyautogui.click(clicks=4)
        time.sleep(timer)
        pyautogui.moveTo(x = outhimX, y= outhimY) # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y) # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174) # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97) # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x= poshimX, y = poshimY) # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def dermalin():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц дермалина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(1426, 714)  # координаты кислорода
        pyautogui.mouseDown()
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.mouseUp()
        pyautogui.moveTo(x=1534, y=785)  # углерод
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1231, y=806)  # фосфор
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def diloven():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц диловена): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1203, y=688)  # азот
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.mouseUp()
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def hironalin():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц хироналина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1222, y=675)  # азот
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1546, y=742)  # радий
        pyautogui.click(clicks=3)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def kosmo():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц космоциллина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1534, y=785)  # углерод
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1343,y=778) # сахар
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.moveTo(1426,714) # координаты кислорода
        pyautogui.mouseDown()
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def deksplus():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц дексалина плюс): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1540, y=679)  # железо
        pyautogui.click(clicks=2)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=1534, y=785)  # углерод
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.moveTo(1426,714) # координаты кислорода
        pyautogui.mouseDown()
        pyautogui.click(clicks=2)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def triko():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 90 единиц трикордразина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1343,y=778) # сахар
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.mouseUp()
        pyautogui.moveTo(x=1534, y=785)  # углерод
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(1426,714) # координаты кислорода
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1222, y=675)  # азот
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def tabletki():
    kaki = 0
    print('наведитесь на то место куда вы будете кидать таблетки у вас 5 секунд')
    time.sleep(5)
    pygame.mixer.init()
    pygame.mixer.music.load("trink.mp3")
    pygame.mixer.music.play()
    posrasX, posrasY = pyautogui.position()
    calc = int(input('введите число таблеток: '))
    povt = int(input('выберите число повторений цикла'))
    zasek = 0
    while True:
        if (zasek==povt):
            illusion()
        else:
            while (zasek != povt):
                pyautogui.moveTo(x=309, y=628)  # 9 раз колва таблеток
                pyautogui.mouseDown()
                pyautogui.click(clicks=calc)
                pyautogui.moveTo(x=606, y=624)  # 1 раз создает нажимает
                pyautogui.mouseDown()
                pyautogui.click(clicks=1)
                time.sleep(timer)
                pyautogui.moveTo(x=612, y=106)  # 1 раз извлекает препарат
                pyautogui.mouseDown()
                pyautogui.click(clicks=1)
                time.sleep(0.1)
                pyautogui.press('z')
                time.sleep(0.1)
                pyautogui.press('x')
                while (kaki != calc):
                    pyautogui.moveTo(x=474, y=450)  # нажимать чтоб вытаскивать кол-во равно 1
                    pyautogui.mouseDown()
                    pyautogui.click(clicks=1)
                    time.sleep(0.1)
                    pyautogui.moveTo(x=posrasX, y=posrasY)  # кидаем на раздатку
                    pyautogui.hotkey('ctrl', 'q')
                    kaki = kaki + 1
                pyautogui.press('x')
                pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
                pyautogui.click(clicks=clicki)
                zasek=zasek+1
                kaki = 0


def water():
    global waterX
    global waterY
    print('наведитесь на то место откуда брать воду у вас 5 секунд')
    time.sleep(5)
    pygame.mixer.init()
    pygame.mixer.music.load("trink.mp3")
    pygame.mixer.music.play()
    waterX, waterY = pyautogui.position()
    nasal()

def sinap():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 30 единиц синаптизина): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=waterX, y=waterY)  # вода
        pyautogui.click(clicks=2)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        pyautogui.moveTo(x=1221, y=745)  # литий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1321, y=777) # сахар
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def LSD():
    math = 0
    repeat = int(input('введите число повторений (одно повторение даёт 30 единиц ЛСД): '))
    if (repeat==0):
        illusion()
    while (math != repeat):
        pyautogui.moveTo(x=1203, y=688)  # азот
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1444, y=679)  # водород
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        math = math + 1
        if (math == repeat):
            illusion()

def paks():
    math = 0
    repeat = 1
    while (math != repeat):
        pyautogui.moveTo(x=1203, y=688)  # азот
        pyautogui.mouseDown()
        pyautogui.click(clicks=1)
        pyautogui.mouseUp()
        time.sleep(timer)
        pyautogui.moveTo(x=1356, y=718)  # калий
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1444, y=679)  # водород
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=1547, y=711)  # кремний
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
        pyautogui.click(clicks=clicki)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
        pyautogui.click(clicks=1)
        time.sleep(timer)
        pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
        pyautogui.click(clicks=clicki)
        time.sleep(timer)

        math = math + 1
        if (math == repeat):
            math = 0
            repeat = 1
            while (math != repeat):
                pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
                pyautogui.click(clicks=1)
                time.sleep(timer)
                pyautogui.moveTo(x=waterX, y=waterY)  # вода
                pyautogui.click(clicks=2)
                pyautogui.mouseUp()
                time.sleep(timer)
                pyautogui.moveTo(x=poshimX, y=poshimY)  # позиция раздатчика
                pyautogui.click(clicks=clicki)
                time.sleep(timer)
                pyautogui.moveTo(x=1221, y=745)  # литий
                pyautogui.click(clicks=1)
                time.sleep(timer)
                pyautogui.moveTo(x=1321, y=777)  # сахар
                pyautogui.mouseDown()
                pyautogui.click(clicks=1)
                time.sleep(timer)
                pyautogui.moveTo(x=outhimX, y=outhimY)  # извлеч из раздатчика
                pyautogui.click(clicks=1)
                time.sleep(timer)
                pyautogui.moveTo(x=pos4000X, y=pos4000Y)  # расположение 4000
                pyautogui.click(clicks=clicki)
                time.sleep(timer)
                pyautogui.moveTo(x=567, y=174)  # слить все у одного ресурса
                time.sleep(timer)
                math = math + 1
        if (math == repeat):
            pyautogui.moveTo(x=571, y=511)  # слить все у двух ресурса
            pyautogui.click(clicks=2)
            time.sleep(timer)
            pyautogui.moveTo(x=560, y=97)  # извлеч из 4000
            pyautogui.click(clicks=1)
            time.sleep(timer)
            pyautogui.moveTo(x=waterX, y=waterY)  # вода
            pyautogui.click(clicks=6)
            time.sleep(timer)
            pyautogui.mouseUp()
            time.sleep(timer)
            illusion()





def illusion():
    vibor = int(input('\n\nПРОГРАММА РАБОТАЕТ ТОЛЬКО ЕСЛИ РАЗРЕШЕНИЕ ЭКРАНА 1920X1080 (наверное)\n\n\nПриветствую химиков станции 14! Если вам надоела рутинная работа по изготовлению стандартных препаратов, то эта разработка специальна для вас! Для понимая работы программы используйте гайд\nDiscord:Frenk_Star#4769\n\n\n0. Перейти к начальному экрану\n1. Бикаридин (поставьте кол-во химикатов на 15)\n2. Дермалин (поставьте кол-во химикатов на 15)\n3. Диловен (поставьте кол-во химикатов на 30)\n4. Хироналин (поставьте кол-во химикатов на 15)\n5. Космоциллин (поставьте кол-во химикатов на 15) \n6. Дексалин плюс (поставьте кол-во химикатов на 15 и УЧТИТЕ ЧТО В МЕНЗУРКЕ ДОЛЖНО БЫТЬ 10ед ПЛАЗМЫ)  \n7. Трикордразин (поставьте кол-во химикатов на 15)\n8. Расфосовать по таблеткам\n9.Пакс (поставьте кол-во химикатов на 10 и установите источник откуда брать воду (пункт 6 в начальном экране)) \n10. Синаптизин (поставьте кол-во химикатов на 10)\n11. ЛСД (поставьте кол-во химикатов на 10) \nчто вы хотите сделать? (просто напишите цифру): '))
    if (vibor == 1):
        bikardin()
    if (vibor == 2):
        dermalin()
    if (vibor==3):
        diloven()
    if (vibor==4):
        hironalin()
    if (vibor==5):
        kosmo()
    if (vibor==6):
        deksplus()
    if (vibor==0):
        nasal()
    if (vibor==7):
        triko()
    if (vibor==8):
        tabletki()
    if (vibor==9):
        if (razrab==1):
            paks()
        else:
            print ('\n\n\nЭто вещество только для режима разработчика!')
            illusion()
    if (vibor==10):
        sinap()
    if (vibor==11):
        LSD()


def nasal():
    nasalvibor = int(input('1. Определить координаты устройств\n2. Записать координаты устройств\n3. Перейти в основной экран\n4. Изменить кол-во кликов на устройства\n5. Изменить задержку между действиями\n6. Установить источник набора воды\n7. Проверить расположение кислорода\n8. Проверить расположение окна у химмастера 4000 если оно не совпадает, то передвиньте окно химиастера4000\n9. Проверить расположение окна у раздатчика химикатов, если оно не совпадает, то передвиньте окно раздатчика химикатов\nЧтобы выбрать пункт, напишите цифру нужного вам пункта: '))
    if (nasalvibor == 1):
        print(pyautogui.position())
        nasal()
    if (nasalvibor == 2):
        global poshimY
        global poshimX
        global pos4000Y
        global pos4000X
        print ('Пожалуйста, наведите курсор на ХимМастер4000 и подождите 5 секунд')
        time.sleep(5)
        pos4000X, pos4000Y = pyautogui.position()
        pygame.mixer.init()
        pygame.mixer.music.load("trink.mp3")
        pygame.mixer.music.play()
        print('Теперь наведите курсор на раздатчик химикатов и подождите 5 секунд')
        time.sleep(5)
        pygame.mixer.music.play()
        poshimX, poshimY = pyautogui.position()
        nasal()
    if (nasalvibor == 3):
        illusion()
    if (nasalvibor==4):
        global clicki
        clicki = int(input('введите число кликов по устройству (или 1 или 2): '))
        print('Вы выбрали {} кликов по устройству'.format(clicki))
        nasal()
    if (nasalvibor==5):
        global timer
        timer = float(input('введите задержку между действиями в секундах (от 0.1 до x.x) главное чтоб оно было с точккой, тоесть 1.0, 3.2,0.2: '))
        nasal()
    if (nasalvibor==6):
        water()
    if (nasalvibor == 2006):
        global razrab
        razrab = 1
        print ('\n\n\n АКТИВИРОВАН РЕЖИМ РАЗРАБОТЧИКА!!! \n\n\n')
        nasal()
    if (nasalvibor==7):
        print ('Через 3 секунды ваш курсор должен оказаться на кнопке кислорода, если это не так подвиньте окно раздатчика химикатов')
        time.sleep(3)
        pyautogui.moveTo(1426,714)
        nasal()
    if (nasalvibor==8):
        proverkawindows4000()
        nasal()

    if (nasalvibor==9):
        proverkawindowshim()
        nasal()

nasal()