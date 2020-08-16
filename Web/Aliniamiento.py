#abrimos el archivo de texto	
f = open ('FastaSeqCL.txt','r')
#variables iniciales
contador=0
CadenaA=[]
CadenaB=[]
Cadena1=[]
Cadena2=[]
#limpieza del texto
for i in f:
	if ">"in i:
		contador=contador +1
	else:
		if contador==1:
			
			i=" ".join(i)
			i=i.split()
			CadenaA.append(i)
		else:
			i=" ".join(i)
			i=i.split()
			CadenaB.append(i)

for x in range(len(CadenaA)):
	for y in range(len(CadenaA[x])):
		Cadena1.append(CadenaA[x][y])

for x in range(len(CadenaB)):
	for y in range(len(CadenaB[x])):
		Cadena2.append(CadenaB[x][y])

print("Cadena 1: \n", Cadena1)
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Cadena 2: \n", Cadena2)
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("\nLa cadena 1 tiene ",len(Cadena1),"elementos \n")
print("C:",Cadena1.count("C") , "\tG:",Cadena1.count("G"))
print("A:",Cadena1.count("A") , "\tT:",Cadena1.count("T"))

print("\nLa cadena 2 tiene ",len(Cadena2),"elementos\n")
print("C:",Cadena2.count("C") , "\tG:",Cadena2.count("G"))
print("A:",Cadena2.count("A") , "\tT:",Cadena2.count("T"))

#programa de puntuacion
puntuacion=[]

for z in range(len(Cadena1)-len(Cadena2)+1):
	puntos=0
	for x in range(len(Cadena2)):
		for y in range(len(Cadena1)):
			if x==y:
				if Cadena1[y+z]==Cadena2[x]:
					puntos=puntos+1
				else:
					puntos=puntos-1
	puntuacion.append(puntos)
#Resultados
print("\nLas puntuaciones fueron:",puntuacion)
print("\nLa puntucion maxima es:",max(puntuacion))
ubicacion=puntuacion.index(max(puntuacion))
print("\nLa puntuacion Maxima se ubica a partir del elemento:",ubicacion+1)


