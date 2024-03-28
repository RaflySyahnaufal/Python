def fibo (i) :
    if i < 2 :
        return i
    else:
        return fibo(i-1) + fibo(i-2)
    
jml_bilangan = 10

for i in range(jml_bilangan):
    print(fibo(i),end="")