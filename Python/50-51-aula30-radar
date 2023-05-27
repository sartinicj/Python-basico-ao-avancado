'''
CONSTANTE = "Variaveis que não serão alteradas no codigo
Muitas condições no mesmo if (ruim)
'''

veloc = 61 #velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local em que o carro está na estrada 
RADAR_RANGE = 1 #A distancia onde o radar pega

#1: Indepentende se ele passar ou não pelo radar, eu quero saber se ele ultrapassou a velocidade do radar
#2: Saaber se o carro foi multado no radar 1

'''
if veloc > 60:
    print('Carro ultrapassou o limite de velocidade do radar')
else:
    print('Carro não ultrapassou o limite de velocidade do radar')
    
if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and veloc > RADAR_1:
    print('Carro ultrapassou o limite de velocidade do radar, e foi multado')
else:
    print('Carro não ultrapassou o limite de velocidade do radar, portanto não foi multado')
    '''
    
passou_radar_1 = veloc > RADAR_1
multar_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if passou_radar_1 and multar_radar_1:
    print('Carro ultrapassou o limite de velocidade do radar, e foi multado')
else:
    print('Carro não ultrapassou o limite de velocidade do radar, portanto não foi multado')