#Name: Eugen Maier
#Klasse: ETS2021
#Datum: 05.11.2021

import math

jahr = 1999

if (jahr % 4==0) and (jahr % 100 != 0) or (jahr % 400 ==0 ):

    print( "Das Jahr",jahr,"ist ein Schaltjahr")
else:
    print( "Das Jahr",jahr,"ist kein Schaltjahr")
        


