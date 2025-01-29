import math

def test1(n):
    bas, haut = 1, n
    nmbre_essais = 0
    while bas < haut:
        nmbre_essais += 1
        print(print(f"Test à {bas} et {haut} assiettes..."))
        milieu = (bas + haut) // 2
        if tester_repas(milieu):  
            bas = milieu + 1  
        else:
            haut = milieu  
    return bas, nmbre_essais

# def test2(n, k):
#     pas = max(1, n // k)  # Ajustement du pas pour ne pas dépasser k essais
#     dernier_sain = 0
#     nmbre_essais = 0
    
#     for i in range(pas, n + 1, pas):

#         if nmbre_essais >= k:  # Stopper si on atteint k essais
#             break
#         nmbre_essais += 1
#         if not tester_repas(i):  
#             break
#         dernier_sain = i
    
#     debut, fin = dernier_sain + 1, min(i, n)  # Limite supérieure ajustée
    
#     while debut <= fin and nmbre_essais < k:
#         milieu = (debut + fin) // 2
#         nmbre_essais += 1
#         if tester_repas(milieu):
#             dernier_sain = milieu
#             debut = milieu + 1
#         else:
#             fin = milieu - 1
    
#     return dernier_sain + 1, min(nmbre_essais, k) 

def test2(n, k):
    pas = n // k
    nmbre_essais = 0
    dernier_sain = 0
    assiette_tester = []
    
    for i in range(pas, n + 1, pas):
        print(f"Test à {i} assiettes...")
        nmbre_essais += 1
        assiette_tester.append(i)
        if not tester_repas(i): 
            break
        dernier_sain = i  
    
    for j in range(dernier_sain + 1, i):
        nmbre_essais += 1
        assiette_tester.append(j)
        print(f"Test précis à {j} assiettes...")
        if not tester_repas(j):
            return j, nmbre_essais, assiette_tester
    
    return n + 1, nmbre_essais, assiette_tester


def test2(n, k):
    pas = max(1, n // (2 * k - 1))  
    seuil = pas
    nbr_essaies = 0

    print(f"\n--- Début du test2 avec n={n}, k={k} ---")

    # **1ère phase : Recherche par pas**
    while seuil <= n and tester_repas(seuil):
        print(f"Test {nbr_essaies+1}: {seuil} assiettes -> OK")
        seuil += pas
        nbr_essaies += 1
        if nbr_essaies >= k:  # Vérification pour ne pas dépasser k
            print(f"Arrêt forcé après {nbr_essaies} essais (max {k})")
            return seuil, nbr_essaies

    print(f"Début de la recherche dichotomique entre {max(seuil - pas, 1)} et {min(seuil, n)}")

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

    print(f"Seuil final estimé à {gauche} assiettes après {nbr_essaies} essais.")
    return gauche, nbr_essaies


def test3(n):
    pas = int(math.sqrt(n))
    dernier_sain = 0
    nmbre_essais = 0
    print(f"Début de la recherche, pas = {pas}")
    
    for i in range(pas, n + 1, pas):
        print(f"Test à {i} assiettes...")
        nmbre_essais += 1
        if not tester_repas(i):  
            print(f"Étudiant mort à {i} assiettes")
            break
        dernier_sain = i
    
    print(f"Recherche linéaire entre {dernier_sain + 1} et {i}")
    
    for j in range(dernier_sain + 1, i):
        nmbre_essais += 1
        print(f"Test précis à {j} assiettes...")
        if not tester_repas(j):
            print(f"Seuil mortel trouvé à {j} assiettes")
            return j, nmbre_essais
    
    return j + 1, nmbre_essais


def tester_repas(x):
    MORT = 50  
    return x < MORT 

n = 100

# k = 50
# print(test1(n))
k = 6
print(test2(n, k))
# k = 2
# print(test3(n))


