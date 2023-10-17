total_belanja=float(input("Masukkan total belanja = "))
if total_belanja > 100000 :
    diskon=(5*total_belanja)/100
    total=total_belanja - diskon
    print("Total belanja = ", total_belanja)
    print("Diskon adalah ", diskon)
    print("Total bayar = ", total)  
else :
    print("Dapat hadiah piring cantik")
    
