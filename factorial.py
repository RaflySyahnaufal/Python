def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Input bilangan untuk dihitung faktorialnya
num = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))

# Cek apakah input bilangan negatif atau non-natural
if num < 0:
    print("Maaf, faktorial hanya untuk bilangan non-negatif")
else:
    result = factorial(num)
    print(f"Faktorial dari {num} adalah {result}")