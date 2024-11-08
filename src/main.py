
KM_PER_AAR = 12000
FORSIKRING_ELBIL = 5000
FORSIKRING_BENSINBIL = 7500
TRAFIKKFORSIKRINGSAVGIFT = 8.38 * 365

ELBIL_KWH_PER_KM = 0.2
ELBIL_STRØMPRIS = 2.00
ELBIL_BOMAVGIFT_PER_KM = 0.1

BENSINBIL_KOSTNAD_PER_KM = 1.0
BENSINBIL_BOMAVGIFT_PER_KM = 0.3


def årlige_totalkostnader(bil):
    if bil == 'elbil':
        return KM_PER_AAR * ELBIL_KWH_PER_KM * ELBIL_STRØMPRIS + KM_PER_AAR * ELBIL_BOMAVGIFT_PER_KM + TRAFIKKFORSIKRINGSAVGIFT + FORSIKRING_ELBIL
    elif bil == "bensinbil":
        return KM_PER_AAR * BENSINBIL_KOSTNAD_PER_KM + KM_PER_AAR * BENSINBIL_BOMAVGIFT_PER_KM + TRAFIKKFORSIKRINGSAVGIFT + FORSIKRING_BENSINBIL
    else:
        return "Ugyldig biltype"
def årlig_kostnadsdifferanse(elbil_kostnad, bensinbil_kostnad):
    if bensinbil_kostnad > elbil_kostnad:
         differanse = bensinbil_kostnad - elbil_kostnad
         return f'Bensinbil er {differanse:.2f} kr dyrere enn elbil'
    else:
        differanse = elbil_kostnad - bensinbil_kostnad
        return f'Elbil er {differanse:.2f} kr dyrere enn bensinbil'

    return 5
elbil_kostnad = årlige_totalkostnader('elbil')
bensinbil_kostnad = årlige_totalkostnader('bensinbil')

kostnadsdifferanse = årlig_kostnadsdifferanse(elbil_kostnad, bensinbil_kostnad)


print(f'De årlige totalkostnadene for en elbil er {elbil_kostnad:.2f} kr om man kjører {KM_PER_AAR} kilometer')
print(f'De årlige totalkostnadene for en bensinbil er {bensinbil_kostnad:.2f} kr om man kjører {KM_PER_AAR} kilometer')
print(f'{kostnadsdifferanse} per år')