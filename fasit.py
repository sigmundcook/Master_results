def alfa(streng, tall):
    if tall == 0:
        return min(streng)
    else:
        return max(streng)

def ant_land(geografi):
    return len(geografi)

def sjekk(tall):
    if tall % 2 == 0:
        return "par"
    elif tall % 2 == 1:
        return "odde"
    else:
        return "des"

def fjern_dup(liste):
    ny_liste = [liste[0]]
    for tall in liste:
        if tall != ny_liste[-1]:
            ny_liste.append(tall)
    liste[:] = ny_liste
    return liste

def list_str(s):
    liste = []
    for i in range(5,len(s)-1):
        if s[i-5] == 'b' and s[i+1] == 'a':
            liste.append(s[i])
    return liste

def sjekk_to(streng):
    resultat = 1
    factors = (2, 3, 5)
    limits = (27, 12, 52)
    for i in range(3):
        if int(streng[i*2:i*2+2]) > limits[i]:
            resultat *= factors[i]
    return resultat

def finn_pris(matvarer, let_etter):
    for vare in matvarer:
        if let_etter == vare[0]:
            return vare[1]
    return 0

def oppdater_matvare(beholdning, matvare, antall):
    beholdning[matvare] += antall
    return beholdning

def oppdater_beholdning(beholdning, endringer):
    for endring in endringer:
        oppdater_matvare(beholdning, endring[0], endring[1])
    return beholdning

def vis_priser(beholdning, matvarer, tekst):
    varer = tekst.replace(',','').replace('.','').split(' ')
    liste = []
    for elem in varer:
        if elem in beholdning:
            liste.append((elem, finn_pris(matvarer, elem)))
    return liste

def tilgjengelig_vare(beholdning, vare):
    if beholdning[vare] >= 1:
        return True
    return False


def salg(matvarer, beholdning, handleliste):
    total, tup = 0, ()
    for vare in handleliste:
        if tilgjengelig_vare(beholdning, vare):
            pris = finn_pris(matvarer, vare)
            print(vare, pris)
            oppdater_matvare(beholdning, vare, -1)
            total += pris
            tup = tup + (vare,)
    print('Totalsum:', total)
    return tup

def skriv_beholdning(beholdning):
    skriveliste = []
    for nokkel in beholdning:
        skriveliste.append(nokkel +';'+str(beholdning[nokkel])+'\n')
    with open('beholdning.txt', 'w') as fil:
        fil.writelines(skriveliste)

def les_beholdning():
    beholdning = {}
    with open('beholdning.txt', 'r') as fil:
        linjer = fil.readlines()
    for linje in linjer:
        linje = linje.strip(' ').strip('\n')
        delt = linje.split(';')
        beholdning[delt[0]] = int(delt[1])
    return beholdning

from random import randint

def tilfeldig_middag(matvarer, budsjett):
    tilfeldig_middag = []
    middagsvarer = []
    for vare, pris, rett in matvarer:
        if rett == 'middag' and pris<=budsjett:
            middagsvarer.append([vare,pris])
    while middagsvarer:
        if budsjett<=0:
            return tilfeldig_middag
        valg = randint(0,len(middagsvarer)-1)
        tilfeldig_middag.append(middagsvarer[valg][0])
        budsjett -= middagsvarer[valg][1]
        del middagsvarer[valg]
        middagsvarer = tilgjengelige_varer(middagsvarer, budsjett)
    return tilfeldig_middag

def tilgjengelige_varer(varer, budsjett):
    vareliste = []
    for vare, pris in varer:
        if pris <= budsjett:
            vareliste.append([vare,pris])
    return vareliste
