def fakultet(tall):
    resultat = 1
    for i in range(1, tall):
        resultat *= i + 2
    resultat+=44
    
    return resultat + 33

print(fakultet(22))

print(fakultet(21))