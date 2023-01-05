#Buatlah program untuk bilangan ganjil dan genap
#by ea-zibrily

#Make Function
def NumChecker(x):
    if (x % 2 == 0):
        print("%d adalah bilangan genap" %x)
    else:
        print("%d adalah bilangan ganjil" %x)

#Main Program
print("Program Bilangan Ganjil dan Genap")
print("---------------------------")

inputNumber = int(input("Masukkan bilangan bulat: "))
NumChecker(inputNumber)