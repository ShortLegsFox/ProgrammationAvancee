import random

cpt = 0

mem_cpt = 0
mem_cpt_new = 0
memoizable_stored = {}
memoizable_stored_new = {}




def store_memoizable_new(target, values):
    global memoizable_stored_new
    global mem_cpt_new

    key = (target, tuple(sorted(values)))
    if key in memoizable_stored_new.keys():
        mem_cpt_new += 1
    else:
        memoizable_stored_new[key] = trouveExpr(target, values)

    return memoizable_stored_new[key]


def trouveExpr(v, valeurs):
    global cpt
    global memoizable_stored_new
    cpt += 1

    if len(valeurs) == 1:
        if (v == valeurs[0]):
            return (True, str(v))
        else:
            return (False, "")

    else:
        if v in valeurs:
            return (True, str(v))

        else:
            for x in valeurs:
                valeurs2 = valeurs[:]
                valeurs2.remove(x)

                (t, ch) = store_memoizable_new(v+x, valeurs2)
                if t: return (t, ch + " - " + str(x))

                if (v >= x):
                    (t, ch) = store_memoizable_new(v-x, valeurs2)
                    if t: return (t, str(x) + " + (" + ch + ") ")

                if (v <= x):
                    (t, ch) = store_memoizable_new(x-v, valeurs2)
                    if t: return (t, str(x) + " + (" + ch + ") ")

                if (v >= x) and v % x == 0:
                    (t, ch) = store_memoizable_new(v//x, valeurs2)
                    if t: return (t, "(" + ch + ") * " + str(x))

                if (v <= x) and x % v == 0:
                    (t, ch) = store_memoizable_new(x//v, valeurs2)
                    if t: return (t, str(x) + " / (" + ch + ") ")

                (t, ch) = store_memoizable_new(v*x, valeurs2)
                if t: return (t, "(" + ch + ") / " + str(x))

            return (False, "")


NBNOMBRES = 6
nombres = []
operateurs = ['+', '-', '*', '/']
operandes = list(range(1, 11)) + list(range(1, 11)) + [25, 50, 75, 100]

for i in range(NBNOMBRES):
    nombres.append(operandes[random.randint(0, len(operandes) - 1)])
cible = random.randint(100, 999)

cible = 799
nombres = [4, 8, 5, 6, 6, 2]

res = trouveExpr(cible, nombres)
print(cible, nombres, res, cpt)
print(mem_cpt_new)
if (res[0] == False):
    for i in range(cible):
        print("écart", i)
        res = trouveExpr(cible + i, nombres)
        if (res[0] == True):
            print(cible, cible + i, nombres, res, cpt)
            break
        res = trouveExpr(cible - i, nombres)
        if (res[0] == True):
            print(cible, cible - i, nombres, res, cpt)
            break

print(f'Total memoizable calculation {round((mem_cpt_new / cpt) * 100)} % (total {mem_cpt_new})')
print(f'Total calculation optimized {cpt-mem_cpt_new}')