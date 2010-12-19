# import file game.py
import Game

# Data Mode Awal Game
modeGame = 0

print('  Welcome To Game Kuis Matematika  '.center(80,'-'))
print(' By : Dharma Bakti Situmorang '.center(80))

# Data Nama Pemain
print('\nSiapa Nama Kamu??')
playerName = input() # atau kamu bisa langsung mengisikan namamu disini dengan menggantikan input() dangan nama mu

while modeGame != 9:

    print('\n')
    print(' Selamat Bermain !! '.center(80, '-'))
    print('-'.center(80, '-'))
    print('Silakan Pilih Tingkat Kesulitan Permainan ??')

    # Membuat List Mode Game
    print('(1) Mudah')
    print('(2) Sedang')
    print('(3) Sulit \n')

    print('[6] Game Mode Advanced')
    print('[7] Ganti Nama Pemain')
    print('[9] Keluar')

    try:
        # user memilih 
        modeGame = int(input('\nPilihan Anda :'))

    except ValueError:
        print('Masukkan Angka Saja!!')
        print('Pilih Hanya Kategori Diatas Saja\n')
    
    if modeGame == 1:
        # User Meminta Mode Mudah
        print('\nAnda Memilih Tingkat Mudah, Jawab Semua Soal')
        Game.modeMudah(playerName)

    elif modeGame == 2:
        # User Meminta Mode Sedang
        print('\nAnda Memilih Tingkat Sedang/Normal, Jawab Semua Soal')
        Game.modeSedang(playerName)

    elif modeGame == 3:
        # User Meminta Mode Sulit
        print('\nAnda Memilih Tingkat Sulit, Jawab Semua Soal')
        Game.modeSulit(playerName)

    elif modeGame == 6:
        # user ingin bermain game mode campuran / advanced
        print('\nDi Game Mode Yang Satu Ini Anda Ditantang Untuk Memdapatkan nilai sebanyak-banyaknya!!')
        Game.advancedMode(playerName)

    elif modeGame == 7:
        # user ingin mengubah namanya 
        print('Siapa Nama Kamu Sekarang ??')
        playerName = input()

print('Good Bye!!!')
