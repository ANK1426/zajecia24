#H.G.88
import random #importujemy bibliotekę random
def generate_list(n, ranges, types): #ranges to krotka dwuelementowa, zawierająca (min,max). 
    #types to int lub float, automatycznie wybiera int 

    if type(n) == list: #jeśli n jest listą, generuje listę dla każdego wyrazu
        listy = {}
        for j in range(len(n)): 
            listy[f'lista_{j}'] = []
            if types == int:
                for i in range(n[j]):
                    ai = random.randint(ranges[0], ranges[1])
                    listy[f'lista_{j}'].append(ai)
            elif types == float:
                for i in range(n[j]):
                    ai = random.uniform(ranges[0], ranges[1]).__round__(3)
                    listy[f'lista_{j}'].append(ai)

    elif type(n) == int: #jeśli n jest liczbą generuje jedną listę długości n
        listy = []
        if types == int:
            for i in range(n):
                    ai = random.randint(ranges[0], ranges[1])
                    listy.append(ai)
        elif types == float:

#np. generate_list([5,3,4], [3.2,7.3], float)


def generate_tuple(lenght, n, ranges, types): #tutaj podobnie, tylko dla krotek
    #mamy jedynie dodatkowy parametr length, będący ilością elementów w każdej krotce
    
    tuples = {}
    for i in range(n):
        if types == int:
            tuples[f'tuple_{i}'] = tuple(random.randint(ranges[0], ranges[1]) for j in range(lenght))
        elif types == float:
            tuples[f'tuple_{i}'] = tuple(random.uniform(ranges[0], ranges[1]).__round__(3) for j in range(lenght))

    return tuples 
            for i in range(n):
                    ai = random.uniform(ranges[0], ranges[1]).__round__(3)
                    listy.append(ai)

    return listy

#np. generate_tuple(5, 1, [5.1, 11.3], float)
