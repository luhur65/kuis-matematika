# this file is contain a function for every mode game in the file main.py

# import module operand
from operator import *

# import module random
import random

# Easy Game Mode
def modeEasy(data):

    # Count Total Quiz default value is 0
    countQuiz = 0

    # Current Skor default value is 0
    currentSkor = 0

    # Number Quiz
    numberQuiz = 0

    for countQuiz in range(1,11):

        # Mencetak no Quiz 
        currentQuiz = 1
        numberQuiz += currentQuiz

        # Number Random to make a quiz 
        randomNo1 = random.randint(1,25)
        randomNo2 = random.randint(1,25)
        
        # Quiz Mudah ( penjumlahan )
        Quiz = add(randomNo1, randomNo2)
        print('{}. What The Result From {} + {} ??'.format(numberQuiz, randomNo1, randomNo2))

        # print(Quiz)
        answer = input('Answer : ')

        try:
            if int(answer) == Quiz:
                # the skor if the answer is true
                scoreForRightAnswer = 10

                currentSkor += scoreForRightAnswer
                print('\n--- Well Done , Your Answer is Correct ----')
                print('My Score: {}\n'.format(currentSkor))
            
            elif int(answer) != Quiz:
                # Memberikan Koreksi Jwbn Yg benar
                print('\n---- Unfortunetly , Your Answer is Wrong ---- ')
                print('The Right Answer is : {}\n'.format(Quiz))
        
        except Exception as err:
            err = '\nYour Answer Can\'t be Accepted!\n'
            print(err)

    # category to know how great smart you ??
    gradeForFinish(currentSkor, data)


# Medium Mode game
def modeMedium(data):
    countQuiz = 0
    currentSkor = 0
    numberQuiz = 0

    # Life to player
    life = 3

    print('You Only have 3 life , if you wrong to answer your life will lost -1 !!\n')

    for countQuiz in range(1,21):
        # print no Quiz 
        currentQuiz = 1
        numberQuiz += currentQuiz

        # No. Random
        randomNo1 = random.randint(1,50)
        randomNo2 = random.randint(1,50)

        # operasi matematika
        shuffleQuiz = random.randint(1,2)
        
        if shuffleQuiz == 1:
            Quiz = add(randomNo1, randomNo2)
            print('{}. What The Result From {} + {} ??'.format(numberQuiz, randomNo1, randomNo2))

        elif shuffleQuiz == 2:
            Quiz = sub(randomNo1, randomNo2)
            print('{}. What The Result From {} - {} ??'.format(numberQuiz, randomNo1, randomNo2))

         # Jawaban User
        answer = input('Answer : ')

        try:
            if int(answer) == Quiz:
                # score to right answer
                scoreForRightAnswer = 5

                currentSkor += scoreForRightAnswer
                print('\n--- Well Done , Your Answer is Correct ---')
                print('My Score : {}\n'.format(currentSkor))
            
            elif int(answer) != Quiz:
                # score to worng answer
                # will be substract 3
                substractScore = 3
                currentSkor -= substractScore

                # you life will be lost -1 if you are wrong to answer
                life -= 1

                print('\n---- Unfortunetly , Your Answer is Wrong ----')
                print('The Right Answer is : {}'.format(Quiz))
                print('My Score : {}'.format(currentSkor))
                print('Nyawa Anda : {} life\n'.format(life))

                # game over if all your life is lost
                if life == 0:
                    print('Game Over , You have been 3 times wrong to answer the quiz !!\n')
                    break
            
        except Exception as err:
            err = '\nYour Answer Can\'t be Accepted!\n'
            print(err)

    # Kategori Nilai Akhir
    gradeForFinish(currentSkor, data)


# hard Game
def modeHard(data):
    countQuiz = 0
    currentSkor = 0
    numberQuiz = 0

    life = 3

    print('You Only have 3 life , if you wrong to answer your life will lost -1 !!\n')

    for countQuiz in range(1,26):
        currentQuiz = 1
        numberQuiz += currentQuiz

        randomNo1 = random.randint(1,100)
        randomNo2 = random.randint(1,100)

        randomNo3 = random.randint(1,50)
        randomNo4 = random.randint(1, 25)
        
        shuffleQuiz = random.randint(1,4)

        if shuffleQuiz == 1:
            Quiz = (sub(randomNo1, randomNo3)) * add(randomNo4, randomNo2)
            print('{}. What The Result From ( {} - {} ) *  {} + {} '.format(numberQuiz, randomNo1, randomNo3, randomNo4, randomNo2))

        elif shuffleQuiz == 2:
            Quiz = sub(randomNo1, randomNo2)
            print('{}. What The Result From {} - {} ??'.format(numberQuiz, randomNo1, randomNo2))

        elif shuffleQuiz == 3:
            Quiz = mul(randomNo1, randomNo2)
            print('{}. What The Result From {} * {} ??'.format(numberQuiz, randomNo1, randomNo2))

        elif shuffleQuiz == 4:
            Quiz = mul(randomNo4, randomNo1) - ( add(randomNo2, randomNo3) )
            print('{}. What The Result From  {} * {}  - ( {} + {} )'.format(numberQuiz, randomNo4, randomNo1, randomNo2, randomNo3))

        answer = input('Answer: ')

        try:
            if int(answer) == Quiz:
                scoreForRightAnswer = 4

                currentSkor += scoreForRightAnswer
                print('\nMy Score: {}'.format(currentSkor))
                print('--- Well Done , Your Answer is Correct ----\n')
            
            elif int(answer) != Quiz:
                substractScore = 3
                currentSkor -= substractScore

                # life will be lost
                life -= 1

                print('\n---- Unfortunetly , Your Answer is Wrong ----')
                print('The Right Answer is : {}'.format(Quiz))
                print('My Score: {}'.format(currentSkor))
                print('Nyawa Anda : {} life\n'.format(life))

                # game over
                if life == 0:
                    print('Game Over , Anda Sudah Salah 3x Menjawab!!\n')
                    break
            
        except Exception as err:
            err = '\nYour Answer Can\'t be Accepted!\n'
            print(err)
    
    gradeForFinish(currentSkor,data)


def advancedMode(pemain):
    # usr life  == 3
    life = 3
    # Total Skor
    score= 0
    # no Quiz
    noQuiz = 0

    for i in range(1,500):

        noQuiz += 1

        # angka random buat Quiz kuis
        randomNo1 = random.randint(1, 20)
        randomNo2 = random.randint(21, 40)
        randomNo3 = random.randint(41, 60)
        randomNo4 = random.randint(61, 100)

        shuffleQuiz = random.randint(1, 5)

        # shuffleQuiz
        if shuffleQuiz == 1:
            Quiz = add(randomNo1, randomNo2)
            print('{}. What The Result From {} + {} ??'.format(noQuiz, randomNo1, randomNo2))
        elif shuffleQuiz == 2:
            Quiz = sub(randomNo1, randomNo2)
            print('{}. What The Result From {} - {} ??'.format(noQuiz, randomNo1, randomNo2))
        elif shuffleQuiz == 3:
            Quiz = mul(randomNo3, randomNo4)
            print('{}. What The Result From {} * {} ??'.format(noQuiz, randomNo3, randomNo4))
        elif shuffleQuiz == 4:
            Quiz = randomNo4 * ( randomNo3 + randomNo1 - randomNo2) * randomNo4
            print('{}. What The Result From {} * ( {} + {} - {} ) * {} ??'.format(noQuiz, randomNo4, randomNo3, randomNo1, randomNo2, randomNo4))

        # user answer
        try:
            print(Quiz)
            answer = int(input('Your Answer is :\t'))

            # if user answer is true
            if answer == Quiz:
                score += 10

                print('\n---Your Answer is True !---')
                print('Your Score = {}'.format(score))
                print('Your Life = {} Life \n'.format(life))

                # if user reach score 500 
                if noQuiz == 500:
                    print('\n-----Congratulation For You!----')
                    print('--------------------------------')
                    print('You Have Finished , The Mission With Total Score => {}'.format(score))
                    break

            # if wrong
            elif answer != Quiz:
                score -= 5
                life -= 1

                print('\n---Wrong Answer!---')
                print('The Right Answer is = {}'.format(Quiz))
                print('Your Life = {} Life\n'.format(life))

                # check user life
                if life == 0:
                    print('Game Over!, Your Life is 0!')
                    print('Score that you have = {} Point\n'.format(skor))
                    break

        except Exception as err:
            print(err)
    

def gradeForFinish(totalScore, playerName):
    # List Ucapan 
    # kategori > 80
    goodCategory = [
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
    enoughCategory = [
        'Oke Lumayan Untuk Kamu',
        'Jangan Langsung Berbangga Diri yah Ini Belum Seberapa',
        'Aku Yakin Kamu bisa lebih baik dari ini',
        'Dapet Nilai B , itu bagus loh',
        'Sedikit Lagi Mencapai Keberhasilan',
        'Tetap Semangat Yah !!',
        'Terus Belajar & raih Kategori A'
    ]
    # kategori < 45
    badCategory = [
        'Yah , Semangat Terus Deh Buat Kamu',
        'Ayo Kamu Pasti Bisa',
        'Mungkin Kamu Masih Belum terbiasa ya !!',
        'Jangan Mengganggap Diri Kamu Bodoh',
        'Jangan Berkecil Hati Dengan Apa Yg Kamu Dapatkan Sekarang',
        'Tetap Belajar Dan Ubah Kelemahan Menjadi Kelebihanmu',
        'Jangan Patah Semangat Ya'
    ]

    # Pengacakan pesan kategori
    goodQuotes = random.choice(goodCategory)
    enoughQuotes = random.choice(enoughCategory)
    badQuotes = random.choice(badCategory)

    # Total Jumlah Skor yg Diperoleh , 
    # Kategory Tingkat Kemampuan dalam Mengerjakan Quiz
    if totalScore <= 45:
        print('Your Final Score is :', totalScore, ' ( Category : C )')
        print('Quotes To You : \n', badQuotes, playerName)
       
    elif totalScore >= 50 and totalScore <= 75:
        print('Your Final Score is :', totalScore, ' ( Category : B )')
        print('Quotes To You : \n', enoughQuotes, playerName)
       
    elif totalScore >= 80:
        print('Your Final Score is :', totalScore, ' ( Category : A )')
        print('Quotes To You : \n', goodQuotes, playerName)
       

