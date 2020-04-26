from Fuzzifikasi import Fuzzifikasi as Fuzzy
from inferensi import Inferensi as Infer
from Defuzifikasi import Defuzifkasi as Defuz


enggar=Fuzzy("Enggar")
wayan=Fuzzy("Wayan")

enggar.TPA(60)
enggar.UN(78)
enggar.Jarak(4500)

AnggotaTPA=enggar.memberTPA
AnggotaUN=enggar.memberUN
AnggotaJarak=enggar.memberJarak

print("============ Fuzifikasi ============")
print("MemberTPA = ",enggar.memberTPA)
print("MemberUN = ",enggar.memberUN)
print("MemberJarak = ",enggar.memberJarak)

print("============ Inferensi ============")
infer=Infer(AnggotaTPA,AnggotaUN,AnggotaJarak)

print("============ Defuzifikasi ============")
Defuzifikasi=Defuz(0.3,0)

