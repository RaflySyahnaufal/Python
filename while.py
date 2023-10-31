tahun=0
saldo_awal=float(input("Masukkan saldo awal = "))
saldo_target=float(input("Masukkan saldo yang diinginkan = "))

while saldo_awal < saldo_target:
    saldo_awal= saldo_awal + (saldo_awal*0.1)
    tahun=tahun+1
    
print(f"Saldo awal : {saldo_awal}")    
print(f"Harus menunggu {tahun} tahun untuk mencapai saldo {saldo_target}")