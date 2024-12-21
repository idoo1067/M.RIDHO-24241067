# TPM tugas 
member = input("apalakah member? : ")
total_belaaja = float(input("masukkan total belanja = Rp. "))

if member == 'ya' and total_belaaja > 500.000:
    diskon_persen = 20
elif member == 'ya' and total_belaaja <= 500.000:
    diskon_persen = 10
elif member == 'tigak' and total_belaaja > 500.000:
    diskon_persen = 5
elif member == 'tidak' and total_belaaja <= 500.000:
    diskon_persen = 0

diskon_Rp = total_belaaja * (diskon_persen / 100)
total_bayar = total_belaaja - diskon_Rp

print(f'total belanja: Rp. {total_belaaja:.3f}')
print(f'diskon persen: {diskon_persen}%')
print(f'diskon Rp: Rp. {diskon_Rp:.3f}')
print(f'bayar Rp: Rp. {total_bayar:.3f}')