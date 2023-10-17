bil1=int(input("Masukkan bilangan 1= "))
bil2=int(input("Masukkan bilangan 2= "))
bil3=int(input("Masukkan bilangan 3= "))

if bil1>bil2 and bil2>bil3:
    print(bil1, "Adalah bilangan terbesar")
elif bil2>bil1 and bil1>bil3 :
    print(bil2, "Adalah bilangan terbesar")
else :
    print(bil3, "Adalah bilangan terbesar")