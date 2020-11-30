# TUGAS BESAR - PINTU TOL OTOMATIS
# Oleh Kelompok 2:
#1.	Deedat Fatahillah           – 16720398
#2.	Muhammad Akbar Nugrahadi    – 16720194
#3.	Ratna Larisa 			    – 16720032
#4.	Shereen Aciana Silaban 		– 16720296

#KAMUS
# a : str (keberadaan mobil)
# R : int (jumlah roda)
# L : float (panjang mobil)
# s : int (saldo)

#ALGORITMA:
#Daftar tarif yang tersedia:
Tarif = [7000,11500,13000,16000,20000,3000]

a = input("Apakah ada mobil? : ")   
#Pengecekan keberadaan kendaraan:
while a != "ada":
    a= input("Apakah ada mobil? : ")

if a == "ada":
    R = int(input ("Jumlah roda : "))
    s = int(input("Masukkkan saldo Anda : "))
Sisa = 0    #Inisialisasi menghitung sisa pembayaran
count = 0   #Inisialisasi perhitungan jumlah pengguna pintu tol
def Proses (R):
    #Mengkategorikan jenis kendaraan berdasar jumlah roda
    if R == 4:
        L = float(input("Panjang mobil : "))
        if L >= 4.5 or L<7:         #Kendaraan yang ingin masuk pintu tol berjenis Sedan, Jip, Pick Up.      
            Sisa = s - Tarif[0]         #Proses,Membayar dengan saldo yang tarif Rp7500
        else:
            Sisa = s - Tarif[1]         #Proses,Membayar dengan saldo yang tarif Rp11500
    
    elif R == 6:        #Kendaraan yang ingin masuk pintu tol berjenis Truk Roda 6
        Sisa = s - Tarif[2]             
    
    elif R == 8:        #Kendaraan yang ingin masuk pintu tol berjenis Truk Roda 8
        Sisa = s - Tarif[3]

    elif R == 10:   #Kendaraan yang ingin masuk pintu tol berjenis Truk Roda 10
        Sisa = s - Tarif[4]
    
    elif R == 2:   #Kendaraan yang ingin masuk pintu tol berjenis Sepeda motor roda 2
        Sisa = s - Tarif[5]
    
    else:    
        print("Maaf, Kendaraan Anda tidak dapat melalui pintu tol kami.")
        Sisa = -s
    return Sisa
    
x = Proses(R)
if x >= 0:
    print('Pintu tol terbuka')              #Terminasi, Pintu tol terbuka
    count+=1                                #Proses, menghitung jumlah pengguna pintu tol
    print("Sisa saldo anda adalah :",x)     #Terminasi, menginfokan sisa saldo kepada user
elif x == -s:
    print("Terima kasih.")
else:
    print('Maaf, Saldo Anda tidak cukup')    #Terminasi, menginfokan saldo kepada user bahwa saldo tidak cukup
  
print("Jumlah pengguna jalan tol : ",count) #Terminasi, menginfokan jumlah pengguna pintu tol

        
