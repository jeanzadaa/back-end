1)
import math

angulo_graus = 45
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Ângulo: {angulo_graus}°")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")

2)
cateto_oposto = 3
cateto_adjacente = 5

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"Hipotenusa: {hipotenusa:.2f}m")

3)
numero = float(input("Digite um número: "))
porcao_real = numero - int(numero)
print(f"Porção real: {porcao_real:.4f}")

4)
#Bibliotecas são conjuntos de códigos prontos que outras pessoas desenvolveram para resolver problemas específicos. Elas servem para:

#-Reutilizar código sem precisar reinventar a roda
#-Economizar tempo usando funções já testadas
#-Adicionar funcionalidades extras ao Python (como trabalhar com emojis, gráficos, dados, etc.

import emoji

texto = input("Digite um texto com emojis (ex: :heart: :smile: ): ")
texto_com_emoji = emoji.emojize(texto)
print(f"Texto convertido: {texto_com_emoji}")

from emoji import emojize

texto2 = "Estou aprendendo Python :rocket:"
print(emojize(texto2))
