# System
import Game

# Data Mode Awal Game
modeGame = 0

print('  Welcome To Game Kuis Matematika  '.center(80,'-'))
print(' By : Dharma Bakti Situmorang '.center(80))

# Data Nama Pemain
print('\nKita Kenalan Dulu ya , Siapa Nama Kamu??')
playerName = input('Nama Saya Adalah : ')

while modeGame != 9:

    print('\n')
    print(' Selamat Bermain !! '.center(80, '-'))
    print('-'.center(80, '-'))
    print('Silakan Pilih Tingkat Kesulitan Permainan ??')

    # Membuat List Mode Game
    print('(1) Mudah')
    print('(2) Sedang')
    print('(3) Sulit \n')

    print('[7] Ganti Nama Pemain')
    print('[9] Keluar')

    try:
        # user memilih 
        modeGame = int(input())

    except ValueError:
        print('Masukkan Angka Saja!!')
        print('Pilih Hanya Kategori Diatas Saja\n')
    
    if modeGame == 1:
        # User Meminta Mode Mudah
        Game.modeMudah(playerName)

    elif modeGame == 2:
        # User Meminta Mode Sedang
        Game.modeSedang(playerName)

    elif modeGame == 3:
        # User Meminta Mode Sulit
        Game.modeSulit(playerName)

    elif modeGame == 7:
        # Data Nama Pemain
        print('Siapa Nama Kamu Sekarang ??')
        playerName = input()

print('Good Bye!!!')
