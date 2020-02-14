# Eksekusi Program
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
        intSoal = intSoal + currentSoal

        # Angka Random
        angka1 = random.randint(1,25)
        angka2 = random.randint(1,25)
        
        # Soal Mudah ( penjumlahan )
        soal = angka1 + angka2
        # print(soal)
        print(intSoal,'.Hasil Dari : ', angka1, '+', angka2)

        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban yg Benar
                jwbnBenar = 10

                currentSkor += jwbnBenar
                print('\nSkor Saya: ', currentSkor)
                print('---Jawaban Anda Benar ----\n')
            
            elif int(answer) != soal:
                # Memberikan Koreksi Jwbn Yg benar
                print('\nJawaban Yang Benar : ', soal)
                print('---- Jawaban Anda Salah ---- \n')
        
        except Exception as err:
            err = 'Jawaban Tidak Dikenali!'
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

    print('\nAnda Mempunyai : 3 Nyawa , Jika Salah Menjawab Nyawa Anda Berkurang!!\n')

    for jmlSoal in range(1,21):
        # Mencetak no soal 
        currentSoal = 1
        intSoal = intSoal + currentSoal

        # Angka Random
        angka1 = random.randint(1,50)
        angka2 = random.randint(1,50)

        # operasi matematika
        listMtk = random.randint(1,2)
        
        if listMtk == 1:
            soal = angka1 + angka2
            print(intSoal,'.Hasil Dari: ', angka1 ,'+', angka2)

        elif listMtk == 2:
            soal = angka1 - angka2
            print(intSoal,'.Hasil Dari: ', angka1 ,'-', angka2)

         # Jawaban User
        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban yg Benar
                jwbnBenar = 5

                currentSkor += jwbnBenar
                print('\nSkor Saya: ', currentSkor)
                print('---Jawaban Anda Benar ----\n')
            
            elif int(answer) != soal:
                # Skor Jawaban Yg Salah 
                # Dikurangi
                jwbnSalah = 3
                currentSkor -= jwbnSalah

                # Nyawa Akan Berkurang Jika Salah Menjawab Pertanyaan
                life -= 1

                print('\nJawaban Yang Benar : ', soal)
                print('Nyawa Anda : ', life, 'Kesempatan')
                print('Skor Saya: ', currentSkor)
                print('---- Jawaban Anda Salah ---- \n')

                # Permainan Berakhir Jika Nyawa / Kesempatan Salah Menjawab Sudah Habis
                if life == 0:
                    print('Game Over , Anda Sudah Salah 3x Menjawab!!\n')
                    break
            
        except Exception as err:
            err = 'Jawaban Tidak Dikenali!'
            print(err)

    # Kategori Nilai Akhir
    kategoriNilai(currentSkor, data)


# Mode Game Sulit
def modeSulit(data):
    jmlSoal = 0
    currentSkor = 0
    intSoal = 0

    for jmlSoal in range(1,26):
        # Mencetak no soal 
        currentSoal = 1
        intSoal = intSoal + currentSoal

        # Angka Random Utama untuk Penjumlahan, Pengurangan, Perkalian
        angka1 = random.randint(1,100)
        angka2 = random.randint(1,100)

        # Angka Random Tambahan untuk Operasi Campuran
        angka3 = random.randint(1,50)
        angka4 = random.randint(1,25)

        # Operasi Matematika
        listMtk = random.randint(1,4)

        if listMtk == 1:
            soal = (angka1 - angka3) * angka4 + angka2
            print(intSoal,'.Hasil Dari: ', '(', angka1 ,'-', angka3, ') *', angka4, '+', angka2)

        elif listMtk == 2:
            soal = angka1 - angka2
            print(intSoal,'.Hasil Dari: ', angka1 ,'-', angka2)

        elif listMtk == 3:
            soal = angka1 * angka2
            print(intSoal,'.Hasil Dari: ', angka1 ,'*', angka2)

        elif listMtk == 4:
            # Soal Operasi Matematika Campuran
            soal = angka4 * angka1 - ( angka2 + angka3 )
            print(intSoal,'.Hasil Dari: ', angka4, '*', angka1, '- (', angka2, '+', angka3, ')')

        # jawaban user
        answer = input('Answer: ')

        try:
            if answer == soal:
            # Skor Jawaban yg Benar
                jwbnBenar = 4

                currentSkor += jwbnBenar
                print('\nSkor Saya: ', currentSkor)
                print('---Jawaban Anda Benar ----\n')
            
            elif answer != soal:
                # Skor Jawaban Yg Salah 
                # Dikurangi
                jwbnSalah = 3

                currentSkor -= jwbnSalah
                print('\nJawaban Yang Benar : ', soal)
                print('\nSkor Saya: ', currentSkor)
                print('---- Jawaban Anda Salah ---- \n')
            
        except Exception as err:
            err = 'Jawaban Tidak Dikenali!'
            print(err)
    
    # Kategori Nilai Akhir
    kategoriNilai(currentSkor,data)


def kategoriNilai(jmlSkor, pemain):
    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Soal
    if jmlSkor <= 45:
        print('Skor Anda :', jmlSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu!!', pemain)
        print('Terima Kasih Telah Bermain', pemain, '\n')
    elif jmlSkor >= 50 and jmlSkor <= 75:
        print('Skor Anda :', jmlSkor)
        print('Kategori : B ==> Bagus, Tingkatkan Lagi Supaya Sempurna', pemain)
        print('Terima Kasih Telah Bermain', pemain, '\n')
    elif jmlSkor >= 80:
        print('Skor Anda :', jmlSkor)
        print('Kategori : A ==>', pemain, 'Orang Yg Pintar, Pertahankan! ')
        print('Terima Kasih Telah Bermain', pemain, '\n')

