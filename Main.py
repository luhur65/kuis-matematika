# import file game.py
import Game

# Data Mode Awal Game
modeGame = 0

print(' Welcome To Math Quiz '.center(80,'-'))
print(' By : Dharma Bakti Situmorang '.center(80))

# Data Nama Pemain
print('\nWhat\'s your name ,boy ??')
playerName = input() # atau kamu bisa langsung mengisikan namamu disini dengan menggantikan input() dangan nama mu

while modeGame != 9:

    print('\n')
    print(' Le\'s Go Play The Quiz !! '.center(80, '-'))
    print('-'.center(80, '-'))
    print('Choose the category dificulty ??')

    # Membuat List Mode Game
    print('(1) Easy')
    print('(2) Medium')
    print('(3) Hard \n')

    print('[6] Game Mode Advanced')
    print('[7] Change Name')
    print('[9] Quit Game')

    try:
        # user memilih 
        modeGame = int(input('\nYour Choice is :'))

    except ValueError:
        print('Enter Only The Number!!')
        print('Choose Only The Category in above\n')
    
    if modeGame == 1:
        # User Meminta Mode Mudah
        print('\nYou Choose The Easy Mode')
        Game.modeEasy(playerName)

    elif modeGame == 2:
        # User Meminta Mode Sedang
        print('\nYou Choose Medium Mode')
        Game.modeMedium(playerName)

    elif modeGame == 3:
        # User Meminta Mode Sulit
        print('\nYou Choose Hard Mode')
        Game.modeHard(playerName)

    elif modeGame == 6:
        # user ingin bermain game mode campuran / advanced
        print('\nIn This Game You Will Challenge to get a lot of point that you can get!!')
        Game.advancedMode(playerName)

    elif modeGame == 7:
        # user ingin mengubah namanya 
        print('What\'s your name now , boy ??')
        playerName = input()

print('Good Bye!!!')