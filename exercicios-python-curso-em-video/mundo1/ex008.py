medida = float(input('Digite um valor em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'Você digitou {medida} metro(s)')
print(f'Esse valor convertido em centímetros é {cm:.0f}cm e em milímetros é {mm:.0f}mm')
print(f'Em decímetro é {dm:.0f} em decâmetro é {dam:.0f} em hectômetro é {hm} e em quilômetro é {km}')
