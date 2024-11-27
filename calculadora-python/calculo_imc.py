
altura = float(input('Qual é sua altura em cm? ')) / 100  # convertendo para metros
peso = float(input('Qual é seu peso em kg? '))

IMC = peso / (altura ** 2)

print(f'Seu IMC calculado é {IMC:.2f}')

if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Magreza.')
elif 18.5 <= IMC < 24.9:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Normal.')
elif 25 <= IMC < 29.9:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Sobrepeso.')
else:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Obesidade.')


