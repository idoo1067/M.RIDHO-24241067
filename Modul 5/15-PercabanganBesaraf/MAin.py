#percabangan bersaraf / Nested IF

# kekulator 
# +,-,x,/,mod,//,pangkat(exponen)
print(20*"=")
print('kekulator sederhana')
print(20*"=")

angka_1 = float(input('masukan bilangan 1 = '))
operator = input('operatar (+,-,/,x,%,//,**)=')
angaka_2 = float(input('masukan bilangan 2 = '))

#Percabangan bersarang (Elif strateme)
if operator == '+':
    hasil = angka_1 + angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '-':
    hasil = angka_1 - angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == 'x':
    hasil = angka_1 * angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '/':
    hasil = angka_1 / angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '%':
    hasil = angka_1 % angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '//':
    hasil = angka_1 // angaka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '**':
    hasil = angka_1 ** angaka_2
    print(f'hasilnya adalah = {hasil}')
else:
    print('operasi{operatar} tidak ditemukan!')
print('terimakasi')