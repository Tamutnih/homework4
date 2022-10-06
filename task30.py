# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

from math import pi

fraser = str(pi)

length_of_pi = []

number_of_places = raw_input(
    "Enter the number of decimal places you want to see: ")

for number_of_places in fraser:
    length_of_pi.append(str(number_of_places))

print(" ".join(length_of_pi))
