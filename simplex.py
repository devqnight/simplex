# Methode du simplexe: programme

def disp_tab(simp):
    iter_line = 1
    iter_x = 1
    for i in simp:
        if 'l' in i:
            print("L", str(iter_line), " : ", end="")
            for j in simp[i]:
                print(str(j), "x_", str(iter_x), " ", end="")
                iter_x += 1
            print("")
            iter_line += 1
            iter_x = 1


def disp_simplexe_tab(simp):
    print()
    for i in simp['base']:
        print(" ", i, " ", end="")
    print(" | ", end="")
    for i in simp['free']:
        print(" ", i, " ", end="")
    print(" |  d  |  ligne")
    for i in range(len(simp['base'])+len(simp['free'])+len(" |  d  |  ligne")-3):
        print("---", end="")


def get_input_raw(nb_l):
    raw = [
        "e1 + 4x + 5y = 40",
        "e2 + 2x + 5y = 30",
        "z_max = 600x + 1000y"
    ]
    '''for i in range(nb_l+1):
        if i != nb_l:
            raw_line = input(f"Entrez L{i+1} : ")
        else:
            raw_line = input("Entrez z_max : ")
        raw.append(raw_line)
    print(raw)'''
    return raw


def convert_raw(final, raw, base):
    base_data = base.strip('}{').split(',')
    for i in base_data:
        final['base'].append(i)
    for i in raw:
        if 'z_max' not in i:
            raw_data = i.split(' = ')
            raw_d = raw_data[1]
            raw_calc = raw_data[0].split(' + ')
        else:
            raw_data = i.split(' = ')
            raw_d = raw_data[1].split(' + ')
            raw_calc = raw_data[0]
        print(raw_calc, " = ", raw_d)


def input_simp():
    simp = {'base': [], 'free': [], 'base_coef': [], 'free_coef': [], 'd': [], 'z_max': []}
    nb_line = 2 #int(input("Entrez le nombre de ligne : "))
    base = "{e1,e2}" #input("Entrez la base ( forme : {b1,b2} : ")
    simp_raw = get_input_raw(nb_line)
    convert_raw(simp, simp_raw, base)
    return simp


def simplexe():
    simplexe_var = input_simp()
    disp_simplexe_tab(simplexe_var)


