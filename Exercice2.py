import copy


TROU = '0'
dim = 0

# Print du board
def afficheJeu(jeu):
    for l in jeu:
        print(" ".join(l))
    print()

# Initialisation du jeu
def initTaquin(nf):
    with open(nf, "r") as f:
        lignes = f.readlines()
    jeu, ref = [], []
    global dim
    dim = len(lignes) // 2
    for l in lignes[:dim]:
        jeu.append(l.split())
    for l in lignes[dim:]:
        ref.append(l.split())
    return jeu, ref

# Chercher la position d'une valeur dans le jeu
def chercher(val, ref):
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def valJeu(jeu, ref): # Somme des distances entre le jeu et la référence
    sommedist = 0
    for i in range(len(jeu)):
        for j in range(len(jeu[i])):
            if jeu[i][j] != ref[i][j]:
                y, x = chercher(jeu[i][j], ref)
                sommedist += abs(y - i) + abs(x - j)
    return sommedist

# Recupérer les mouvements possibles à partir du trou
def coups_possibles(jeu):
    moves = []
    mt, nt = chercher(TROU, jeu)

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)

    directions = [left, right, up, down]
    for x, y in directions:
        next_mt, next_nt = mt + x, nt + y # On se déplace dans les directions possibles

        if 0 <= next_mt < dim and 0 <= next_nt < dim: # Si la case est dans le jeu (pour éviter de sortir du board)
            next_step = copy.deepcopy(jeu)
            next_step[mt][nt], next_step[next_mt][next_nt] = next_step[next_mt][next_nt], next_step[mt][nt]
            moves.append(next_step) # Donc mouvement possible, on l'ajoute dans la liste

    return moves

# Rechercher le plus court chemin
def jouer(jeu, ref):
    heuristic = valJeu(jeu, ref) # Initialisation de l'heuristique
    nbEssais = 0
    path = []
    open_set = [(heuristic, nbEssais, jeu, path)]

    while open_set:
        open_set.sort()
        _, coups, current, path = open_set.pop(0) # On prend le premier élément de la liste triée

        if current == ref:
            return path

        for move in coups_possibles(current):
            new_path = path + [move]
            open_set.append((valJeu(move, ref) + coups + 1, coups + 1, move, new_path))
            print(valJeu(move, ref))

    return []

def main():
    nbEssais = 0
    jeu, ref = initTaquin("taquin_data/taquin4.txt")

    print("Jeu initial:")
    afficheJeu(jeu)

    solution = jouer(jeu, ref)

    for step in solution:
        nbEssais += 1
        print("Etape", nbEssais)
        afficheJeu(step)

    print("Total coups :", nbEssais)


main()