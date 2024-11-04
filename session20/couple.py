import random

def names(list):
    return input(list).split(',')

def create_couple(boys, girls):
    couple = []
    while boys and girls:
        boy = random.choice(boys)
        girl = random.choice(girls)
        couple.append((boy, girl))
        boys.remove(boy)
        girls.remove(girl)
    return couple
boys = names("Enter boy's names separated by commas: ")
girls = names("Enter girl's names separated by commas: ")
couples = create_couple(boys, girls)

for couple in couples:
    print(couple)