# Menghitung rumus fungsi f(x)
# by ea-zibrily

def f(x):
    y = 2 * x**3 +2 * x + 15 / x
    return y

#Main Program
print("Menghitung Fungsi f(x)")
print("---------------------------")
enterNumber = int(input("Masukkan nilai x: "))
hasil = float(enterNumber)
print("Nilai f(%d) adalah %.2f" % (enterNumber, hasil))
