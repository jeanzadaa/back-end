# Podemos screver um resultado na quantidade de caracteres específica ao colocar o valor dentro da máscara após escrever

nome = input ('Qual é o seu nome?')
print ('prazer em conhece-lo {:20}!'.format(nome))

 #Podemos alinhar o nome dentro do número de caracteres que desejamos

 #Alinhamento para a direita 
 nome = input ('Qual é o seu nome?')
print('prazer em conhece-lo {:>20}!'.format(nome))

#Alinhamento para a esquerda
nome = input ('Qual é o seu nome?')
print ('prazer em conhece-lo {:<20}!'.format(nome))

#Alinhamento no centro
nome = input ('Qual é o seu nome?')
print ('prazer em conhece-lo {:^20}!'.format(nome))
