def countdown(n):
    if n == 0:
        print(n, end='')
    else:
        print(n, end='')
        countdown(n -1)

#panggil funsgi countdown dengan parameter 10
countdown(10)

#def countdown(n) : Mendefinisikan fungsi rekrusif bernama 'countdown' dengan parameter 'n'.
#if n == 0 : ini adalah kondisi basis atau kondisi berhenti dari rekrusi, jika 'n' sama dengan 0, maka cetak 'n' dan berhenti