def fakultet(tall):
    resultat = 1
    for i in range(1, tall):
        resultat *= i + 1
    return resultat

print(fakultet(24))