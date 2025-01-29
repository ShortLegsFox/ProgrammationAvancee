import random

cpt = 0

mem_cpt = 0
memoizable_stored = {}


def store_memoizable(v, x, operator):
    global memoizable_stored
    global mem_cpt

    calc = calculation(v, x, operator)
    expression = f'{v}{operator}{x}'

    if expression in memoizable_stored.keys():
        mem_cpt += 1
        return memoizable_stored[expression]
    else:
        memoizable_stored[expression] = calc
        return calc


def calculation(v, x, operator):
    if operator == '+':
        return v+x
    elif operator == '-':
        return v-x
    elif operator == '/':
        return v // x
    elif operator == '*':
        return v * x
    return 0


def trouveExpr(v, valeurs):
    global cpt
    global memoizable_stored
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

                op = store_memoizable(v, x, operateurs[0])
                (t, ch) = trouveExpr(op, valeurs2)
                if t: return (t, ch + " - " + str(x))

                if (v >= x):
                    op = store_memoizable(v, x, operateurs[1])
                    (t, ch) = trouveExpr(op, valeurs2)
                    if t: return (t, str(x) + " + (" + ch + ") ")

                if (v <= x):
                    op = store_memoizable(x, v, operateurs[1])
                    (t, ch) = trouveExpr(op, valeurs2)
                    if t: return (t, str(x) + " + (" + ch + ") ")

                if (v >= x) and v % x == 0:
                    op = store_memoizable(v, x, operateurs[3])
                    (t, ch) = trouveExpr(op, valeurs2)
                    if t: return (t, "(" + ch + ") * " + str(x))

                if (v <= x) and x % v == 0:
                    op = store_memoizable(x, v, operateurs[3])
                    (t, ch) = trouveExpr(op, valeurs2)
                    if t: return (t, str(x) + " / (" + ch + ") ")

                op = store_memoizable(v, x, operateurs[2])
                (t, ch) = trouveExpr(op, valeurs2)
                if t: return (t, "(" + ch + ") / " + str(x))

            return (False, "")


NBNOMBRES = 6
nombres = []
operateurs = ['+', '-', '*', '/']
operandes = list(range(1, 11)) + list(range(1, 11)) + [25, 50, 75, 100]

for i in range(NBNOMBRES):
    nombres.append(operandes[random.randint(0, len(operandes) - 1)])
cible = random.randint(100, 999)

res = trouveExpr(cible, nombres)
print(cible, nombres, res, cpt)
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

print(f'Total memoizable calculation {round((mem_cpt / cpt) * 100)} % (total {mem_cpt})')
