print("Сейчас мы будем заполнять список фруктов")
a=[]
while a.count("выйти")!=1:
    b=input("Введите фрукт из списка, чтобы выйти из заполнения введите выйти:  ")
    if b=="выйти":
        break
    else:
        a.append(b)
for i in range(len(a)):
    #Без F строк
    print(i ,"{:>10s}".format(a[i]))
