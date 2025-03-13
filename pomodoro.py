import time


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

    yesOrNo = input('\nDeseja começar outro pomodoro? Y/N: ' )


    if yesOrNo == "Y" or yesOrNo == "y":

        selection()

    

def selection():

    print('\n10-15-30-45')

    num = int(input('\nDigite a quantidade de minutos que deseja o Pomodoro: '))

    if num <= 0:
        print("O valor não pode ser zero!")

        selection()

    try: 
        timer(num)
    except Exception:
        print('ERRO! ')


if __name__ == "__main__":
   
    try:
         selection()
    except ValueError :
        print("ERRO! O valor selecionado tem que ser número inteiro")
    else:
        print('\nCerto, pomodoro encerrado')
    finally:
        print('\n---Programa encerrado!---')

    
