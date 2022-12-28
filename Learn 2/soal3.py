# Swap Number Program
# by ea-zibrily

isSwap = False

# Make Function
def swapNumber(number1, number2, number3, number4):
    global isSwap
    number1, number2, number3, number4 = number2, number4, number1, number3
    isSwap = True
    return number1, number2, number3, number4


def checkNumber(x):
    if (type(x) is int):
        return 1
    else:
        return 0

def printNumber(x):
    if (isSwap):
        print("Setelah ditukar: ")
    else:
        print("Sebelum ditukar: ")
    print("%d, %d, %d, %d" % (x[0], x[1], x[2], x[3]))

# Main Program
print("Swap Number Program")
print("---------------------------")

enterName = input("Masukkan nama anda: ")
enterNumber = []

for i in range(4):
    enterNumber.append(int(input("Masukkan bilangan bulat ke-%d: " % (i + 1))))
    checkNumber(enterNumber[i])

printNumber(enterNumber)

swapResult = swapNumber(enterNumber[0], enterNumber[1], enterNumber[2], enterNumber[3])

printNumber(swapResult)
