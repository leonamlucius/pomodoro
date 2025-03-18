import time

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer

def music():

    mixer.init()

    engagedSound = mixer.Sound("beep.mp3")

    mixer.Sound.play(engagedSound)

def timer(num):

    t = num*60


    while t: 
      mins = t // 60 
      secs = t % 60
      timeformat = '{:02d}:{:02d}'.format(mins,secs)
      print(timeformat,end='\r')
      time.sleep(1)
      t -= 1


    print('Tempo encerrado!')
    music()

    yesOrNo = input('\nDeseja começar outro pomodoro? Y/N: ' )


    if yesOrNo == "Y" or yesOrNo == "y":

        selection()

    

def selection():

    custom = False

    chosen = int(input('\nDigite 1 para o modo padrão ou 2 para ou modo customizável:'))
    
    if chosen == 2:
        custom = True

    print('\n10-15-30-45')

    num = int(input('\nDigite a quantidade de minutos que deseja o Pomodoro: '))

    
    if num <= 0:
        print("\nO valor não pode ser zero!")

        selection()

    if custom == False:
        if num != 10 or num != 15 or num != 30 or num!= 45:

            print("\nO valor não suportado, escolha os valores apresentados!")

            selection()

    try: 
        timer(num)
    except Exception:
        print('ERRO! ')
    except KeyboardInterrupt:
        print('\n---Programa encerrado!---')


if __name__ == "__main__":
   
    try:
         selection()
    except ValueError :
        print("ERRO! O valor selecionado tem que ser número inteiro")
    else:
        print('\nCerto, pomodoro encerrado')
    finally:
        print('\n---Programa encerrado!---')

    

