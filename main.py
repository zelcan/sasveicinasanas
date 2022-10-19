#Autors: Tavs vārds, uzvārds 
#Datums: dd-mm-yyyy
#Programma, kas sasveicinās ar lietotāju



# mainīgajā vards saglabā lietotāja ievadīto vārdu 

#ar if ... else... sazarojumu izvadi dzimumam attiecīgu uzrunu: Sveiks (vīriešiem), Sveika (sievietēm)

# Izvada rezultātu konsolē (Output)
#Saglabā lietotāja ievadīto informāciju mainīgajā
print("Čau! Es esmu programma, kas ar Tevi sasveicināsies :) \n")

print("*********************************")

vards=input("Lūdzu ievadi savu vārdu un nospied ENTER")

# Izprintē no vārda otro burtu
print(vards[2])

#ar if ... else... sazarojumu izvadi dzimumam attiecīgu uzrunu: Sveiks (vīriešiem), Sveika (sievietēm)
if vards[0] == "A" :
  print("Tu esi alfabēta augšgalā")
elif vards[0] == "Z":
  print("Tu esi alfabēta apakšā")
else: 
  print("Tu esi kaut kur pa vidu")