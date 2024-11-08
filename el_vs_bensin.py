# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:46:20 2024
____


Oppgave

Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene 
ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og 
for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets 
skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader 
er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
Lykke til!

Mvh.
Finn
____



@author: Daniel Dale Laabak
"""

"""
Variabler for utregning
"""

km = 10000 #kilometer pr. år 
fe = 5000 #forsikringspris elbil
fb = 7500 #forsikringspris bensinbil
tfa = 8.38 #trafikkforsikringsavgift daglig
tfa_ar = tfa * 365 #trafikkforsikringsavgift årlig (365 dager i et år)
eb_kWh_km = 0.2 #elbil antall kWh pr. km
sp = 2 #elbil strømpris pr kWh
eb_kWh_kost_ar = km*eb_kWh_km*sp #strømkostnad basert på antall kilometer pr år
bpkm = 1 #bensinpris pr. km
bpkm_kost_ar = km * bpkm #bensinkostnad baset på antall kilometer pr år
be = 0.1 #bomkost elbil pr. kilometer
be_kost = be * km #bomkost elbil basert på antall kilometer pr år
bb = 0.3 #bomkost bensinbil pr. kilometer
bb_kost = bb * km #bomkost bensinbil basert på antall kilometer pr år


sumelbil = fe + tfa_ar + eb_kWh_kost_ar + be_kost #summerer kostnader knyttet til el-bil
sumbensinbil = fb + tfa_ar + bpkm_kost_ar + bb_kost #summerer kostnader knyttet til bensinbil
differanse = sumbensinbil - sumelbil #regner ut differansen mellom el- og bensinbil

"""
Lager variabel for å vise hva som er billigst til slutt
"""
if sumelbil > sumbensinbil:
    billigst = "Bensinbil"
elif sumbensinbil > sumelbil:
    billigst = "Elbil"
elif sumbensinbil == sumelbil:
    billigst = "Lik kostnad"



print("Sammenlikning av årlige kostnader ved elbil sammenliknet med bensinbil.")
print("_______________________________________________________________________")
print("Forsikring:")
print("Elbil            |    Bensinbil")
print(f"kr.{fe:.2f},-     |    kr. {fb:.2f},-")
print(f"\nTrafikkforsikringsavgift: kr. {tfa_ar:.2f},- (lik for begge)")
print("_______________________________________________________________________")
print(f"Kostnad basert på kjørelengde, {km} km/år:")
print("\nElbil                 |   Bensinbil")
print(f"strøm: kr.{eb_kWh_kost_ar:.2f},-   |   bensin: kr. {bpkm_kost_ar:.2f},-")
print(f"bom: kr.{be_kost:.2f},-     |   bom: kr. {bb_kost:.2f},-")
print("_______________________________________________________________________")
print(f"Sum elbil: kr. {sumelbil:.2f},-     |   Sum bensinbil: kr. {sumbensinbil:.2f},-")
print("_______________________________________________________________________")
print(f"\n-------> Billigst: {billigst} ! <--------")
