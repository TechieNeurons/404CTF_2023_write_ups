from z3 import *

def solve_password():
    # Création des variables pour chaque caractère du mot de passe
    password = [BitVec(f'password_{i}', 8) for i in range(48)]

    solver = Solver()

    # Ajout des contraintes sur les caractères du mot de passe
    for i in range(48):
        solver.add(password[i] >= 32, password[i] <= 126)  # Les caractères doivent être imprimables ASCII

    cody = 518

    solver.add(password[36] + cody * password[37] + password[38] == 25556)
    solver.add(password[3] + cody * password[4] + password[5] == 19862)
    solver.add(password[21] + cody * password[22] + password[23] == 39570)
    solver.add(password[0] + password[1] + cody * password[2] == 35329)
    solver.add(password[6] + password[7] + cody * password[8] == 67347)
    solver.add(password[3] + password[4] + cody * password[5] == 100914)
    solver.add(password[3] + cody * password[4] + password[5] == 49274)    
    solver.add(password[6] + cody * password[7] + password[8] == 61221)
    solver.add(password[36] + password[37] + cody * password[38] == 64773)
    solver.add(password[9] + password[10] + cody * password[11] == 49360)
    solver.add(password[9] + cody * password[10] + password[11] == 18857)
    solver.add(password[9] + cody * password[10] + password[11] == 46721)    
    solver.add(password[15] + password[16] + cody * password[17] == 58164)
    solver.add(password[15] + password[16] + cody * password[17] == 144852)
    solver.add(password[12] + password[13] + cody * password[14] == 147438)
    solver.add(password[12] + password[13] + cody * password[14] == 59202)
    solver.add(password[45] + cody * password[46] + password[47] == 39501)
    solver.add(password[12] + cody * password[13] + password[14] == 25080)
    solver.add(password[15] + cody * password[16] + password[17] == 27661)
    solver.add(password[18] + password[19] + cody * password[20] == 135810)
    solver.add(password[18] + cody * password[19] + password[20] == 128064)    
    solver.add(password[15] + cody * password[16] + password[17] == 68683)    
    solver.add(password[12] + cody * password[13] + password[14] == 62232)    
    solver.add(password[24] + cody * password[25] + password[26] == 66114)    
    solver.add(password[27] + cody * password[28] + password[29] == 25071)
    solver.add(password[6] + cody * password[7] + password[8] == 152553)    
    solver.add(password[6] + password[7] + cody * password[8] == 27099)
    solver.add(password[21] + password[22] + cody * password[23] == 54563)
    solver.add(password[45] + cody * password[46] + password[47] == 98325) 
    solver.add(password[39] + password[40] + cody * password[41] == 115125)
    solver.add(password[24] + cody * password[25] + password[26] == 26640)
    solver.add(password[21] + password[22] + cody * password[23] == 135833)
    solver.add(password[9] + password[10] + cody * password[11] == 122890)
    solver.add(password[39] + password[40] + cody * password[41] == 46239)
    solver.add(password[0] + password[1] + cody * password[2] == 87961)
    solver.add(password[27] + password[28] + cody * password[29] == 144847)
    solver.add(password[30] + password[31] + cody * password[32] == 35402)
    solver.add(password[27] + password[28] + cody * password[29] == 58159)
    solver.add(password[3] + password[4] + cody * password[5] == 40542)
    solver.add(password[0] + cody * password[1] + password[2] == 42776)    
    solver.add(password[30] + cody * password[31] + password[32] == 57633)
    solver.add(password[42] + cody * password[43] + password[44] == 26019)
    solver.add(password[18] + password[19] + cody * password[20] == 54540)
    solver.add(password[18] + cody * password[19] + password[20] == 51438)
    solver.add(password[21] + cody * password[22] + password[23] == 98394)    
    solver.add(password[24] + password[25] + cody * password[26] == 51973)
    solver.add(password[24] + password[25] + cody * password[26] == 129373)
    solver.add(password[30] + password[31] + cody * password[32] == 88034)
    solver.add(password[0] + cody * password[1] + password[2] == 17234)
    solver.add(password[30] + cody * password[31] + password[32] == 143547)    
    solver.add(password[33] + cody * password[34] + password[35] == 43078)
    solver.add(password[33] + password[34] + cody * password[35] == 42770)
    solver.add(password[33] + cody * password[34] + password[35] == 107320)    
    solver.add(password[36] + password[37] + cody * password[38] == 26073)
    solver.add(password[33] + password[34] + cody * password[35] == 17228)
    solver.add(password[39] + cody * password[40] + password[41] == 27627)
    solver.add(password[39] + cody * password[40] + password[41] == 68649)    
    solver.add(password[27] + cody * password[28] + password[29] == 62223)    
    solver.add(password[42] + cody * password[43] + password[44] == 64719)    
    solver.add(password[45] + password[46] + cody * password[47] == 29161)
    solver.add(password[42] + password[43] + cody * password[44] == 35842)
    solver.add(password[36] + cody * password[37] + password[38] == 63482)    
    solver.add(password[42] + password[43] + cody * password[44] == 89248)
    solver.add(password[45] + password[46] + cody * password[47] == 72505)

    # carmen = 0
    # for i in range(48):
    #    carmen += dumas[i] + cody * password[i]

    # solver.add()  # Exemple de contrainte, la somme doit être égale à 25556

    # Résolution du solveur
    print (solver.check())
    if solver.check() == sat:
        model = solver.model()
        password_str = ''.join([chr(model[password[i]].as_long()) for i in range(48)])
        return password_str
    else:
        return None

# Appel de la fonction pour trouver le mot de passe
password = solve_password()

if password:
    print("Mot de passe trouvé :", password)
else:
    print("Aucun mot de passe trouvé.")
