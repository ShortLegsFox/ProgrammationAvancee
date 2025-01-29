import math

def test1(n):
    bas, haut = 1, n
    nmbre_essais = 0
    nbr_morts = 0 
    while bas < haut:
        nmbre_essais += 1
        print(print(f"Test à {bas} et {haut} assiettes..."))
        milieu = (bas + haut) // 2
        if tester_repas(milieu):  
            bas = milieu + 1  
        else:
            nbr_morts += 1
            haut = milieu
    return bas, nmbre_essais, nbr_morts




def test2(n, k):
    pas = max(1, n // (2 * k - 1))  
    seuil = pas
    nbr_essaies = 0
    nbr_morts = 0
    print(f"\n--- Début du test2 avec n={n}, k={k} ---")

    # **1ère phase : Recherche par pas**
    while seuil <= n and tester_repas(seuil):
        print(f"Test {nbr_essaies+1}: {seuil} assiettes -> OK")
        seuil += pas
        nbr_essaies += 1

    print(f"Début de la recherche dichotomique entre {max(seuil - pas, 1)} et {min(seuil, n)}")
    
    nbr_morts += 1
    
    gauche, droite = max(seuil - pas, 1), min(seuil, n)
    while gauche < droite and nbr_essaies < k:
        milieu = (gauche + droite) // 2
        nbr_essaies += 1
        print(f"Test {nbr_essaies}: {milieu} assiettes...")

        if tester_repas(milieu):
            print(f"{milieu} assiettes -> OK, on monte...")
            gauche = milieu + 1
        else:
            print(f"{milieu} assiettes -> Échec, on descend...")
            droite = milieu
            nbr_morts += 1

    return gauche, nbr_essaies, nbr_morts


def test3(n):
    pas = int(math.sqrt(n))
    dernier_sain = 0
    nmbre_essais = 0
    nbr_mort = 0
    print(f"Début de la recherche, pas = {pas}")
    
    for i in range(pas, n + 1, pas):
        print(f"Test à {i} assiettes...")
        nmbre_essais += 1
        if not tester_repas(i):  
            print(f"Étudiant mort à {i} assiettes")
            nbr_mort += 1
            break
        dernier_sain = i
    
    print(f"Recherche linéaire entre {dernier_sain + 1} et {i}")
    
    for j in range(dernier_sain + 1, i):
        nmbre_essais += 1
        print(f"Test précis à {j} assiettes...")
        if not tester_repas(j):
            nbr_mort += 1
            print(f"Seuil mortel trouvé à {j} assiettes")
            return j, nmbre_essais, nbr_mort
    
    return j + 1, nmbre_essais, nbr_mort


def tester_repas(x):
    MORT = 64
    return x < MORT 

n = 100


# k = 110 
# print(test1(n))
# k = 5 
# print(test2(n, k))
k = 2
print(test3(n))


