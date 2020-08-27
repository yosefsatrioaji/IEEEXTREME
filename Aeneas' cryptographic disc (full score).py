import math as m
panj = float(input())
ggg = {}
for i in range (26):
    abjad,sudut = input().split()
    ggg[abjad] = float(sudut)
hasil = 0
kalimat = input().replace(" ", "").upper()
only_alpha = ""
for char in kalimat:
    if ord(char) >= 65 and ord(char) <= 90:
        only_alpha += char
sudut1 = ggg[only_alpha[0]]
for i in only_alpha[1:]:
    x = ggg[i]
    x = float(x)
    hitung = 2*panj*abs(m.sin(m.radians((x-sudut1)/2)))
    sudut1 = x
    hasil = hasil + hitung
print (m.ceil(hasil+panj))