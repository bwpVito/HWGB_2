#без проверки на ошибки
import random
n = int(input("Введите колличество сгенерированных эллементов"))
c=[]
for i in range(n):
    c.append(random.randint(-100, 100))
print(c)
