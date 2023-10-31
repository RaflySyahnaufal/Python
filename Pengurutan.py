for i in range(10) :
    bil=int(input(f"Masukkan bilangan ke- {i+1} :"))
    if(i==0):
        besar=bil
        kecil=bil
    else:
        if(bil>besar):
            besar=bil
        if(bil<kecil):
            kecil=bil
print(besar)
print(kecil)