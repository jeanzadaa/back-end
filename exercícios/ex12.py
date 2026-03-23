largura= float (input('largura da parede'))
altura= float (input('altura da parede'))
area= largura*altura
print ('sua parede tem a dimensão de {} x {} e sua área é de {}m quadrados;'.format(largura,altura,largura*altura))
print ('para pintar essa parede, você precisa de {}L de tinta'.format(area/2))
