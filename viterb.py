
import numpy as np
import os
np.set_printoptions(threshold=np.inf)


##### couper un fichier bin

# f=open("sortie2.bin","rb")
# byte = np.fromfile(f, dtype=np.int8)
# f.close()
# g=open("meteor2.bin","wb")
# g.write(byte[len(byte)//4+175*1024:len(byte)//4+225*1024])
# g.close()



def encode_viterbi(d,G1,G2):
	#génération et initialisation de la matrice de convolution
	Gx=np.zeros((len(d),len(d)*2), dtype=int)

	#Interlacement des deux polynomes générateurs
	Gi=[]
	for i in range(len(G1)):
		Gi.append(G1[i])
		Gi.append(G2[i])

	#On remplit la matrice de convolution
	for j in range(len(d)):
		for i in range(len(Gi)):
			try:
				Gx[j,i+2*j]=Gi[i]
			except:
				pass

	#produit matriciel puis modulo 2
	p=np.dot(d,Gx)
	#m=[1-x%2 for x in p]
	m=[]
	for i in range(0,len(p),2):
		m.append(p[i]%2)
		m.append(1-p[i+1]%2)
	ms=''
	for i in range(len(m)):
		ms+=str(m[i])
	#on affiche le résultat
	return ms

def decode_viterbi(x):
	y=[]
	for i in range(0,len(x),2):
		y.append(int(x[i]))
		y.append(1-int(x[i+1]))
	ys=''
	for i in range(len(y)):
		ys+=str(y[i])

	if os.name == 'nt':
		os.system("C:\\Octave\\Octave-5.2.0\\mingw64\\bin\\octave-cli.exe viterbi_py.m {}".format(ys))
	else:
		os.system("octave viterbi_py.m {}".format(ys))
	filin = open("output.txt", "r")
	lignes = filin.readlines()
	filin2 = open("error.txt", "r")
	lignes2 = filin2.readlines()
	return lignes2[3],lignes[5]
