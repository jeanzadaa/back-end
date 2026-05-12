velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"MULTADO! Você excedeu o limite permitido de 80km/h.")
    print(f"O valor da multa é de R${multa:.2f}.")
else:
    print("Tenha um bom dia! Dirija com segurança.")
