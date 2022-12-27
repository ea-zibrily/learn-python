#Menghitung rata-rata dari 3 bilangan bulat sembarang
#by ea-zibrily

enterName = input("Masukkan nama anda: ")
enterNumber1 = int(input("Masukkan bilangan bulat pertama: "))
enterNumber2 = int(input("Masukkan bilangan bulat kedua: "))
enterNumber3 = int(input("Masukkan bilangan bulat ketiga: "))
averageNumber = float((enterNumber1 + enterNumber2 + enterNumber3) / 3)

print("Rata-rata dari %d, %d, dan %d adalah %.2f" %(enterNumber1, enterNumber2, enterNumber3, averageNumber))