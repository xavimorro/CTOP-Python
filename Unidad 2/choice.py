from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# my_list = [x for x in range(20)] Lo mismo que arriba pero abreviado
print("Primer premio", sample(my_list, 1))
print("Segundo premio", sample(my_list, 1))
print("Tercer premio", sample(my_list, 1))