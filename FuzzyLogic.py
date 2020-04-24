from Fuzzifikasi import Fuzzifikasi as Fuzzy
from inferensi import Inferensi as Infer
from Defuzifikasi import Defuzifkasi as Defuz

# x=0;    a=0
# b=0;    c=0
# adenum=0;    bdenum=0
# cdenum=0;    numerator=0


enggar=Fuzzy("Enggar")
wayan=Fuzzy("Wayan")
enggar.TPA(60.0)
enggar.UN(50)
enggar.Jarak(10000)

print("Inferensi")
MDefuz=Defuz(0.5,0.5)
print(MDefuz.hasil)

