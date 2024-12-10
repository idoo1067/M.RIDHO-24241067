# percabangan
# Struktur percabangan 
"""
1. if -nya
2. punya kondisi
3. punya aksi
"""
nama= input ("masukan nama : ")

# percabangan yg inline 
if nama == " ido " : print("selamat tinggal ido")
print ("terimakasi")

# percabangan indentasi
if nama == "ido" :
    print("selamat ya")
    print("selamat kau telah berhasil untuk tidak pacaran")
print("bukan termaksud percabangan")

# percabangan 1 kondisi dan 2 aksi
# paikai kata kunci 'else'

if nama == "ido":
    print('selamat ya {ido}')
else:
    print(f'kau {nama}, telah berhasil ido')
print('aku bangga pada mu')