import pandas as pd
import math
import json

Ana = 17
Jose = 15
Juan = 10
#Partidos jugados
Pj = (Ana + Jose + Juan)/2
#21
#Menor cantidad de partidos posibles

b = math.floor(Pj/2)
#10

# Como el jugador Juan tiene 10 partidos jugados quiere decir que perdió todo los partidos y empezó de segundas



#Simulación partidos
df = pd.DataFrame.from_dict(
    [
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Juan','Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Ana', 'Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Juan','Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Ana', 'Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Juan','Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Ana', 'Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Juan','Vencedor':'Jose'},
    {'Jugador1':'Jose', 'Jugador2':'Ana', 'Vencedor':'Juan'},
    {'Jugador1':'Ana', 'Jugador2':'Juan', 'Vencedor':'Ana'},
    {'Jugador1':'Ana', 'Jugador2':'Jose', 'Vencedor':'Ana'}
   ])

result = df.to_json(orient="split")
parsed = json.loads(result)
a = json.dumps(parsed, indent=4) 
#print(a)

f = open("C:\\Users\\nicolas.corchuelo\\OneDrive\\Professional Path\\Data Engineering\\git\\test\\juego.JSON", "x")
f.write(a)
f.close()

Ana ='Gano 12 partidos'
Jose ='Ganó 8 partidos'
Juan ='Ganó 0 partidos'