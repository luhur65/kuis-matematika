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

        # Jawaban User
        answer = input('Answer : ')

        if int(answer) == soal:
            # Skor Jawaban yg Benar
            jwbnBenar = 10

            currentSkor = currentSkor + jwbnBenar
            print('\nSkor Saya: ', currentSkor)
            print('---Jawaban Anda Benar ----\n')
        
        elif int(answer) != soal:
            print('---- Jawaban Anda Salah ---- \n')
            
        else:
            print('Jawaban Tidak Dikenali!')

    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Soal
    if currentSkor <= 45:
        print('Skor Anda :', currentSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu', data)
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 50 and currentSkor <= 75:
        print('Skor Anda :', currentSkor)
        print('Kategori : B ==> Bagus, Tingkatkan Lagi Supaya Sempurna ')
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 80:
        print('Skor Anda :', currentSkor)
        print('Kategori : A ==> ', data, 'Orang Yg Pintar, Pertahankan! ')
        print('Terima Kasih Telah Bermain', data, '\n')


# Mode Game Sedang
def modeSedang(data):
    jmlSoal = 0
    currentSkor = 0
    intSoal = 0

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
            print(intSoal,'Hasil Dari: ', angka1 ,'+', angka2)

        elif listMtk == 2:
            soal = angka1 - angka2
            print(intSoal,'Hasil Dari: ', angka1 ,'-', angka2)

        # jawaban user
        print(soal)
        answer = input('Answer: ')

        if int(answer) == soal:
            # Skor Jawaban yg Benar
            jwbnBenar = 5

            currentSkor = currentSkor + jwbnBenar
            print('\nSkor Saya: ', currentSkor)
            print('---Jawaban Anda Benar ----\n')
        
        elif int(answer) != soal:
            # Skor Jawaban Yg Salah 
            # Dikurangi
            jwbnSalah = 3

            currentSkor = currentSkor - jwbnSalah
            print('\nSkor Saya: ', currentSkor)
            print('---- Jawaban Anda Salah ---- \n')
            
        else:
            print('Jawaban Tidak Dikenali!')

    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Soal
    if currentSkor <= 45:
        print('Skor Anda :', currentSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu!!', data)
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 50 and currentSkor <= 75:
        print('Skor Anda :', currentSkor)
        print('Kategori : B ==> Bagus, Tingkatkan Lagi Supaya Sempurna', data)
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 80:
        print('Skor Anda :', currentSkor)
        print('Kategori : A ==>', data, 'Orang Yg Pintar, Pertahankan!')
        print('Terima Kasih Telah Bermain', data, '\n')


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

        if int(answer) == soal:
            # Skor Jawaban yg Benar
            jwbnBenar = 4

            currentSkor = currentSkor + jwbnBenar
            print('\nSkor Saya: ', currentSkor)
            print('---Jawaban Anda Benar ----\n')
        
        elif int(answer) != soal:
            # Skor Jawaban Yg Salah 
            # Dikurangi
            jwbnSalah = 3

            currentSkor = currentSkor - jwbnSalah
            print('\nSkor Saya: ', currentSkor)
            print('---- Jawaban Anda Salah ---- \n')
            
        else:
            print('Jawaban Tidak Dikenali! \n')


    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Soal
    if currentSkor <= 45:
        print('Skor Anda :', currentSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu!!', data)
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 50 and currentSkor <= 75:
        print('Skor Anda :', currentSkor)
        print('Kategori : B ==> Bagus, Tingkatkan Lagi Supaya Sempurna', data)
        print('Terima Kasih Telah Bermain', data, '\n')
    elif currentSkor >= 80:
        print('Skor Anda :', currentSkor)
        print('Kategori : A ==>', data, 'Orang Yg Pintar, Pertahankan! ')
        print('Terima Kasih Telah Bermain', data, '\n')
