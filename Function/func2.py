# Buatlah program untuk mengonversi Celcius, Fahrenheit, Reamur, dan Kelvin
# by ea-zibrily

# Make Function
def CelciusConverter(x):

    fahrenheitConv = 9/5 * x + 32
    reamurConv = 4/5 * x
    kelvinConv = x + 273.15

    print(f"Celcius ke Fahrenheit: {fahrenheitConv}")
    print(f"Celcius ke Reamur: {reamurConv}" )
    print(f"Celcius ke Kelvin: {kelvinConv}" )

    return fahrenheitConv, reamurConv, kelvinConv


def FahrenheitConverter(x):

    celciusConv = 5/9 * (x - 32)
    reamurConv = 4/9 * (x - 32)
    kelvinConv = 5/9 * (x - 32) + 273.15

    print(f"Fahrenheit ke Celcius: {celciusConv}")
    print(f"Fahrenheit ke Reamur: {reamurConv}")
    print(f"Fahrenheit ke Kelvin: {kelvinConv}")

    return celciusConv, reamurConv, kelvinConv


def ReamurConverter(x):

    celciusConv = 5/4 * x
    fahrenheitConv = 9/4 * x + 32
    kelvinConv = 5/4 * x + 273.15

    print(f"Reamur ke Celcius: {celciusConv}")
    print(f"Reamur ke Fahrenheit: {fahrenheitConv}")
    print(f"Reamur ke Kelvin: {kelvinConv}")
    
    return celciusConv, fahrenheitConv, kelvinConv


def KelvinConverter(x):

    celciusConv = x - 273, 15
    fahrenheitConv = 9/5 * (x - 273.15) + 32
    reamurConv = 4/5 * (x - 273.15)

    print(f"Kelvin ke Celcius: {celciusConv}")
    print(f"Kelvin ke Fahrenheit: {fahrenheitConv}")
    print(f"Kelvin ke Reamur: {reamurConv}")

    return celciusConv, fahrenheitConv, reamurConv


# Main Program
print("Program Konversi Suhu")
print("---------------------------")

print("Berikut adalah daftar konversi yang tersedia: ")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Reamur")
print("4. Kelvin")

selectionInput = int(input("\nSilahkan pilih konversi yang diinginkan: "))
print("---------------------------")

inputNumber = float(input("Masukkan angka yang akan dikonversi: "))

match selectionInput:
    case 1:
        CelciusConverter(inputNumber)
    case 2:
        FahrenheitConverter(inputNumber)
    case 3:
        ReamurConverter(inputNumber)
    case 4:
        KelvinConverter(inputNumber)
    case _:
        print("Pilihan tidak tersedia!")
