import math
import matplotlib.pyplot as plt

# Définition des tests
def test1(n):
    bas, haut = 1, n
    nmbre_essais = 0
    while bas < haut:
        nmbre_essais += 1
        milieu = (bas + haut) // 2
        if tester_repas(milieu):  
            bas = milieu + 1  
        else:
            haut = milieu  
    return nmbre_essais

def test2(n, k):
    pas = n // k
    nmbre_essais = 0
    dernier_sain = 0
    
    for i in range(pas, n + 1, pas):
        nmbre_essais += 1
        if not tester_repas(i): 
            break
        dernier_sain = i  
    
    for j in range(dernier_sain + 1, i):
        nmbre_essais += 1
        if not tester_repas(j):
            return nmbre_essais
    
    return nmbre_essais

def test3(n):
    pas = int(math.sqrt(n))
    dernier_sain = 0
    nmbre_essais = 0
    
    for i in range(pas, n + 1, pas):
        nmbre_essais += 1
        if not tester_repas(i):  
            break
        dernier_sain = i
    
    for j in range(dernier_sain + 1, i):
        nmbre_essais += 1
        if not tester_repas(j):
            return nmbre_essais
    
    return nmbre_essais

def tester_repas(x):
    MORT = 900  
    return x < MORT 

# Génération des données
n_values = range(50, 1001, 50)
test1_results = [test1(n) for n in n_values]
test2_results = [test2(n, 5) for n in n_values]
test3_results = [test3(n) for n in n_values]

# Affichage des graphes
plt.figure(figsize=(10, 5))
plt.plot(n_values, test1_results, label="Test 1 (Dichotomie)", marker='o')
plt.xlabel("Nombre total d'assiettes (n)")
plt.ylabel("Nombre d'essais")
plt.title("Test 1 : Dichotomie")
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(n_values, test2_results, label="Test 2 (Pas constant)", marker='s', color='orange')
plt.xlabel("Nombre total d'assiettes (n)")
plt.ylabel("Nombre d'essais")
plt.title("Test 2 : Pas constant")
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(n_values, test3_results, label="Test 3 (Racine carrée)", marker='^', color='green')
plt.xlabel("Nombre total d'assiettes (n)")
plt.ylabel("Nombre d'essais")
plt.title("Test 3 : Racine carrée")
plt.grid()
plt.show()
