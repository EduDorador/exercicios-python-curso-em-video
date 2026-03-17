vel = float(input('Digite a velocidade do veículo: '))
if vel > 80:
    print(f'Você foi MULTADO! \nO valor de sua multa é de R$ {(vel - 80) * 7:.2f}')
print(f'Tenha um bom dia! Dirija com segurança!')
