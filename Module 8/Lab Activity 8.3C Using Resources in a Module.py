import random

def number_randomizer(num):
    number_list = []
    for n in range(0, num):
        if len(number_list) < num:
            number_list.append(random.randint(0, 100))
    return number_list
        


print(number_randomizer(2)) 
print(number_randomizer(4))
print(number_randomizer(6))
