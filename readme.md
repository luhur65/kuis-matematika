# System Alur Program Game Kuis Matematika

""" 
Alur Program :

1.  user Memilih Tingkat Kesulitan Kuis 
    { Mudah, Sedang, Sulit }

2.  Jumlah Soal Disetiap Tingkat Permainan:
    {
        10 Soal ==> tingkat Mudah
        20 Soal ==> tingkat Sedang
        25 Soal ==> tingkat Sulit
    }

2.  kemudian `user` Menjawab Soal Yg Diberikan `Comp` Secara Acak 
    Menurut Tingkat Kesulitan Kuis

3.  Jika `User` Menjawab Benar Maka `User` mendapatkan point jawaban benar sesuai tingkat permainan , 
    {
        
        Mudah ==> Skor Benar = +10
                  Skor Salah = 0
        
        Sedang ==> Skor Benar = +5
                   Skor Salah = -3
        
        Sulit ==> Skor Benar = +4
                  Skor Salah = -3
    }

4.  Jika User Berhasil Menjawab Semua Soal,
    Game Berakhir . 
    user akan mendapatkan skor akhir
    dimana akan dikategorikan menurut total skor yg user peroleh selama bermain
    Contoh :

    Point Total user = 90
    Maka kategori nilai 90 adalah A

"""
