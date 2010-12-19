# Ini File Game.py yg berisi function setiap tingkat game kuis

# mengimport module operand
from operator import *

# Mengimport module/library random
import random

# Mode Game Mudah
def modeMudah(data):

    # Jumlah Soal 
    jmlSoal = 0

    # Skor Sekarang
    currentSkor = 0

    # No Soal
    intSoal = 0

    for jmlSoal in range(1,11):

        # Mencetak no soal 
        currentSoal = 1
        intSoal += currentSoal

        # Angka Random
        angka1 = random.randint(1,25)
        angka2 = random.randint(1,25)
        
        # Soal Mudah ( penjumlahan )
        soal = add(angka1, angka2)
        print('{}. Hasil Dari {} + {} ??'.format(intSoal, angka1, angka2))

        # print(soal)
        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban yg Benar
                jwbnBenar = 10

                currentSkor += jwbnBenar
                print('\n---Jawaban Anda Benar ----')
                print('Skor Saya: {}\n'.format(currentSkor))
            
            elif int(answer) != soal:
                # Memberikan Koreksi Jwbn Yg benar
                print('\n---- Jawaban Anda Salah ---- ')
                print('Jawaban Yang Benar : {}\n'.format(soal))
        
        except Exception as err:
            err = '\nJawaban Tidak Dikenali!\n'
            print(err)

    # Kategori Nilai Akhir
    kategoriNilai(currentSkor, data)


# Mode Game Sedang
def modeSedang(data):
    jmlSoal = 0
    currentSkor = 0
    intSoal = 0

    # Nyawa / Kesempatan Player Salah Menjawab
    life = 3

    print('Anda Mempunyai : 3 Nyawa , Jika Salah Menjawab Nyawa Anda Berkurang!!\n')

    for jmlSoal in range(1,21):
        # Mencetak no soal 
        currentSoal = 1
        intSoal += currentSoal

        # Angka Random
        angka1 = random.randint(1,50)
        angka2 = random.randint(1,50)

        # operasi matematika
        listMtk = random.randint(1,2)
        
        if listMtk == 1:
            soal = add(angka1, angka2)
            print('{}. Hasil Dari {} + {} ??'.format(intSoal, angka1, angka2))

        elif listMtk == 2:
            soal = sub(angka1, angka2)
            print('{}. Hasil Dari {} - {} ??'.format(intSoal, angka1, angka2))

         # Jawaban User
        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban yg Benar
                jwbnBenar = 5

                currentSkor += jwbnBenar
                print('\n---Jawaban Anda Benar ---')
                print('Skor Saya : {}\n'.format(currentSkor))
            
            elif int(answer) != soal:
                # Skor Jawaban Yg Salah 
                # Dikurangi
                jwbnSalah = 3
                currentSkor -= jwbnSalah

                # Nyawa Akan Berkurang Jika Salah Menjawab Pertanyaan
                life -= 1

                print('\n---- Jawaban Anda Salah ----')
                print('Jawaban Yang Benar : {}'.format(soal))
                print('Skor Saya : {}'.format(currentSkor))
                print('Nyawa Anda : {} life\n'.format(life))

                # Permainan Berakhir Jika Nyawa / Kesempatan Salah Menjawab Sudah Habis
                if life == 0:
                    print('Game Over , Anda Sudah Salah 3x Menjawab!!\n')
                    break
            
        except Exception as err:
            err = '\nJawaban Tidak Dikenali!\n'
            print(err)

    # Kategori Nilai Akhir
    kategoriNilai(currentSkor, data)


# Mode Game Sulit
def modeSulit(data):
    jmlSoal = 0
    currentSkor = 0
    intSoal = 0

    # Nyawa / Kesempatan Player Salah Menjawab
    life = 3

    print('Anda Mempunyai : 3 Nyawa , Jika Salah Menjawab Nyawa Anda Berkurang!!\n')

    for jmlSoal in range(1,26):
        # Mencetak no soal 
        currentSoal = 1
        intSoal += currentSoal

        # Angka Random Utama untuk Penjumlahan, Pengurangan, Perkalian
        angka1 = random.randint(1,100)
        angka2 = random.randint(1,100)

        # Angka Random Tambahan untuk Operasi Campuran
        angka3 = random.randint(1,50)
        angka4 = random.randint(1,25)

        # Operasi Matematika untuk menentukan soal operasi mana yg keluar
        listMtk = random.randint(1,4)

        if listMtk == 1:
            soal = (sub(angka1, angka3)) * add(angka4, angka2)
            print('{}. Hasil Dari ( {} - {} ) *  {} + {} '.format(intSoal, angka1, angka3, angka4, angka2))

        elif listMtk == 2:
            soal = sub(angka1, angka2)
            print('{}. Hasil Dari {} - {} ??'.format(intSoal, angka1, angka2))

        elif listMtk == 3:
            soal = mul(angka1, angka2)
            print('{}. Hasil Dari {} * {} ??'.format(intSoal, angka1, angka2))

        elif listMtk == 4:
            # Soal Operasi Matematika Campuran
            soal = mul(angka4, angka1) - ( add(angka2, angka3) )
            print('{}. Hasil Dari  {} * {}  - ( {} + {} )'.format(intSoal, angka4, angka1, angka2, angka3))

        # jawaban user
        # print(soal)
        answer = input('Answer: ')

        try:
            if int(answer) == soal:
            # Skor Jawaban yg Benar
                jwbnBenar = 4

                currentSkor += jwbnBenar
                print('\nSkor Saya: {}'.format(currentSkor))
                print('---Jawaban Anda Benar ----\n')
            
            elif int(answer) != soal:
                # Skor Jawaban Yg Salah 
                # Dikurangi
                jwbnSalah = 3
                currentSkor -= jwbnSalah

                # Nyawa Akan Berkurang Jika Salah Menjawab Pertanyaan
                life -= 1

                print('\n---- Jawaban Anda Salah ----')
                print('Jawaban Yang Benar : {}'.format(soal))
                print('Skor Saya: {}'.format(currentSkor))
                print('Nyawa Anda : {} life\n'.format(life))

                # Permainan Berakhir Jika Nyawa / Kesempatan Salah Menjawab Sudah Habis
                if life == 0:
                    print('Game Over , Anda Sudah Salah 3x Menjawab!!\n')
                    break
            
        except Exception as err:
            err = '\nJawaban Tidak Dikenali!\n'
            print(err)
    
    # Kategori Nilai Akhir
    kategoriNilai(currentSkor,data)


def advancedMode(pemain):
    # nyawa user == 3
    life = 3
    # Total Skor
    skor= 0
    # no soal
    noSoal = 0

    for i in range(1,500):

        noSoal += 1

        # angka random buat soal kuis
        angka1 = random.randint(1, 20)
        angka2 = random.randint(21, 40)
        angka3 = random.randint(41, 60)
        angka4 = random.randint(61, 100)

        # random acak buat nentuin soal yg muncul
        pilihSoal = random.randint(1, 5)

        # Membuat pilihSoal
        if pilihSoal == 1:
            soal = add(angka1, angka2)
            print('{}. Hasil Dari {} + {} ??'.format(noSoal, angka1, angka2))
        elif pilihSoal == 2:
            soal = sub(angka1, angka2)
            print('{}. Hasil Dari {} - {} ??'.format(noSoal, angka1, angka2))
        elif pilihSoal == 3:
            soal = mul(angka3, angka4)
            print('{}. Hasil Dari {} * {} ??'.format(noSoal, angka3, angka4))
        elif pilihSoal == 4:
            soal = angka4 * ( angka3 + angka1 - angka2) * angka4
            print('{}. Hasil Dari {} * ( {} + {} - {} ) * {} ??'.format(noSoal, angka4, angka3, angka1, angka2, angka4))

        # jawaban user
        try:
            print(soal)
            answer = int(input('Jawaban Anda :\t'))

            # jika jawaban benar 
            if answer == soal:
                skor += 10

                print('\n---Jawaban Benar!---')
                print('Skor Mu = {}'.format(skor))
                print('Nyawa Anda = {} Life \n'.format(life))

                # jika user bisa mencapai soal ke 500
                if noSoal == 500 and life == 3:
                    print('\n-----Congratulation For You!----')
                    print('--------------------------------')
                    print('Skor Kamu Berjumlah => {}'.format(skor))
                    break

            # jika jawaban salah
            elif answer != soal:
                skor -= 5
                life -= 1

                print('\n---Jawaban Salah!---')
                print('Jawaban Benarnya = {}'.format(soal))
                print('Nyawa Anda = {} Life\n'.format(life))

                # cek nyawa pemain
                if life == 0:
                    print('Permainan Habis!, Nyawa Anda Tidak Ada Lagi!')
                    print('Skor yg Anda Peroleh = {} Point\n'.format(skor))
                    break

        except Exception as err:
            print(err)
    

def kategoriNilai(jmlSkor, pemain):
    # List Ucapan 
    # kategori > 80
    kategoriBaik = [
        'Kamu Orang Yg Pintar, Pertahankan!',
        'Wah , Kamu Hebat Sekali !!',
        'Jawaban Kamu Diatas rata-rata',
        'Kamu Bisa Menjadi Seperti Einstein',
        'Orang Tua Mu Bangga Punya Anak Seperti Mu',
        'Rahasia Kamu Apa Sih , Jago Banget Matematikanya',
        'Aku Tak Pernah Bertemu Orang Seperti mu!!, Hebat',
        'Ajari Aku Dong!! , Kamu Pintar Sekali',
        'Gak Ada Yang Bisa Ngalahin Kamu !!'
    ]
    # kategori 50 > nilai < 75
    kategoriCukup = [
        'Oke Lumayan Untuk Kamu',
        'Jangan Langsung Berbangga Diri yah Ini Belum Seberapa',
        'Aku Yakin Kamu bisa lebih baik dari ini',
        'Dapet Nilai B , itu bagus loh',
        'Sedikit Lagi Mencapai Keberhasilan',
        'Tetap Semangat Yah !!',
        'Terus Belajar & raih Kategori A'
    ]
    # kategori < 45
    kategoriBuruk = [
        'Yah , Semangat Terus Deh Buat Kamu',
        'Ayo Kamu Pasti Bisa',
        'Mungkin Kamu Masih Belum terbiasa ya !!',
        'Jangan Mengganggap Diri Kamu Bodoh',
        'Jangan Berkecil Hati Dengan Apa Yg Kamu Dapatkan Sekarang',
        'Tetap Belajar Dan Ubah Kelemahan Menjadi Kelebihanmu',
        'Jangan Patah Semangat Ya'
    ]

    # Pengacakan pesan kategori
    pesanBaik = random.choice(kategoriBaik)
    pesanCukup = random.choice(kategoriCukup)
    pesanBuruk = random.choice(kategoriBuruk)

    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Soal
    if jmlSkor <= 45:
        print('Skor Anda :', jmlSkor, ' ( Kategori : C )')
        print('Quotes Untuk Anda : \n', pesanBuruk, pemain)
       
    elif jmlSkor >= 50 and jmlSkor <= 75:
        print('Skor Anda :', jmlSkor, ' ( Kategori : B )')
        print('Quotes Untuk Anda : \n', pesanCukup, pemain)
       
    elif jmlSkor >= 80:
        print('Skor Anda :', jmlSkor, ' ( Kategori : A )')
        print('Quotes Untuk Anda : \n', pesanBaik, pemain)
       

