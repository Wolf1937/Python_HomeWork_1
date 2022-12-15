# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите X: "))
y = int(input("Введите Y: "))
z = int(input("Введите Z: "))

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide
if result == True:
    print("Истина")
else:
    print("Ложь")
