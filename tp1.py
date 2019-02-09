#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import gcd
from random import randint,choice
from numpy import mean,abs,sqrt
from time import sleep
import operator

mots = """homme
mari
femme
jour
mer
temps
main
chose
vie
yeux
grand
petit
neuf
deux
trois
son
que
qui
dans
elle
le
pour
pas
que
vous
par
sur
plus
mon
lui
nous
comme
mais
avec
tout
balcon
bien
sans
tu
ou
leur
deux
moi
quand
celui
notre
meme
votre
tout
rien
encore
aussi
quelque
dont
tout
peu
sous
alors
ton
autre
heure
salle
grand
bruite""".split('\n')

def cesar(texte, clef):
	rep = ''
	for i in range(len(texte)):
		if i%5==0:
			rep += ' '
		index = ( ord(texte[i])+clef ) %26 +ord('a')
		rep += chr(index)
	return rep

def pgcd(tab):
	res = gcd(tab[0],tab[1])
	if res == 1:
		return 1
	for i in range(2,len(tab)):
		res = gcd(res,tab[i])

	return res

def exo1():
	texte = """vcfgrwqwoizcuwgtowbsobhgoizcuwgsghqseisqsghoixcif
	rviwxcifrstshsqcaasbhsghqseisjcigbsgojsndogeishobhrsg
	ofhwgobgjcigbsrsjsndogjcigacbhfsfibxcifcijfwsfgobgojcwf
	zsgwbgwubsgrsjcgdfctsggwcbgdofzshcweiszsghhcbashwsf""".replace('\n','')

	for i in range(1,26):
		print(cesar(texte,i),i) #rep 19

def affine(texte,a,b):
	rep = ''
	for i in range(len(texte)):
		if i%5==0:
			rep += ' '
		index = ( (ord(texte[i])-ord('a')-b)*a  ) %26 +ord('a')
		rep += chr(int(index))
	return rep

def exo2():
	texte ="""ntjmpumgxpqtstgqpgtxpnchumtputgfsftgthnngxnchumwx
ootrtumhpyctgktjqtjchfooxujqhgztumxpotjxotfoqtohr
xumhzutwftgtopfmntjmpuatmfmshodpfrxpjjtqtghbxuj""".replace('\n','')
	for i in range(1,26):
		if gcd(26,i)==1:
			for j in range(0,26):
				test = affine(texte,i,j) #9 7
				print(test)
				print(i,j)
				input()

def vigenere(texte,cle):
    texte=texte.upper().replace(' ','')
    cle=cle.upper().replace(' ','')
    if mode_=="d":
        #il faut inverser
        #print()
        clef=''
        for i in range(len(cle)):
            clef+=chr(ord("A")+(26-ord("A")-ord(cle[i]))%26)
        cle=clef
        #print(cle)
    res=''
    for i in range(len(texte)):
        res+=chr(ord("A")+(ord(cle[i%len(cle)])+ord(texte[i])-2*ord("A"))%26)
    #print("entree: ",texte)
    #print("sortie: ",res)
    return res

def exo3():
	texte = """zbpuevpuqsdlzgllksousvpasfpddggaqwptdgptzweemqzrdjtddefek
eferdprrcyndgluaowcnbptzzzrbvpssfpashpncotemhaeqrferdlrlw
wertlussfikgoeuswotfdgqsyasrlnrzppdhtticfrciwurhcezrpmhtp
uwiyenamrdbzyzwelzucamrptzqseqcfgdrfrhrpatsepzgfnaffisbpv
dblisrplzgnemswaqoxpdseehbeeksdptdttqsdddgxurwnidbdddplncsd""".replace('\n','')




	table = dict()
	for i in range(0,len(texte)):
		by = texte[i:i+2]
		spaces = []
		for j in range(i+1,len(texte)):
			if by == texte[j:j+2]:
				spaces.append(j-(i))
		if len(spaces)>1:
			#print(spaces)
			rep = pgcd(spaces)
			if rep !=1:
				try:
					table[rep]+=1
				except Exception:
					table[rep]=1
	#print(table)#changer 4

	maxi = 0
	longueur = ''
	for item in table.keys():
		if table[item] >maxi:
			longueur = item
			maxi = table[item]
	longueur = int(longueur)
	print(longueur)

	blocs = [texte[i::longueur] for i in range(longueur)]
	blocsnew = []

	maxi = 0
	while  True:
		kc = []
		blocs = [texte[i::longueur] for i in range(longueur)]
		blocsnew = []
		for i in range(longueur):
			clef = randint(0,25)
			kc.append(clef)
			blocsnew.append(cesar(blocs[i],clef))
		respuesta = ''
		for i in range(len(blocs[0])):
			for j in range(longueur):
				try:
					respuesta += blocsnew[j][i]
				except Exception:
					pass
		respuesta = respuesta.replace('\n','').replace(' ','')
		compte = 0
		for cl in mots:
			if cl in respuesta:
				compte+=1
		
		if compte>maxi:
			maxi = compte
			print(respuesta,'\n',kc , compte)
			input()
	"""
	for i in range(len(texte)):
		if i % 4==0:
			print(chr((ord(texte[i])-ord('z'))%26+ord('a')),end='')
		elif i % 4==1:
			print(chr((ord(texte[i])-ord('o'))%26+ord('a')),end='')
		elif i % 4==2:
			print(chr((ord(texte[i])-ord('l'))%26+ord('a')),end='')
		elif i % 4==3:
			print(chr((ord(texte[i])-ord('a'))%26+ord('a')),end='')
			#print('')
		#print(texte[i],end='')"""


def exo4():
	texte = """gmyxzoocxziancxktanmyolupjrztgxwshctzluibuic
yzwxyqtvqxzukibkotuxkagbknmimmzzyajvjzampqyz
loinoiqknaumbknknvkaiakgwtnilvvzvqydmvjcximr
vzkilxzqtomrgqmdjrzyazvzmmyjgkoaknkuiaivknvvy""".replace('\n','')
	icfr = 0.0746
	ics = dict()
	for longueur in range(1,7): #en esperant que la clef ne soit pas plus longue
		blocs = [texte[i::longueur] for i in range(longueur)]
		ic = []
		for bloc in blocs : 
			score = 0
			for lettre in range(ord('a'),ord('z')+1):
				lettre = chr(lettre) 
				tmp = bloc.count(lettre)
				score += tmp*(tmp-1)

			ic.append(score/(len(bloc)*(len(bloc)-1)) )
		
		
		ics[longueur] = abs(mean(ic)-icfr)

	longueur = min(ics.items(), key=operator.itemgetter(1))[0]


	blocs = [texte[i::longueur] for i in range(longueur)]
	blocsnew = []

	maxi = 0
	while  True:
		kc = []
		blocs = [texte[i::longueur] for i in range(longueur)]
		blocsnew = []
		for i in range(longueur):
			clef = randint(0,25)
			kc.append(clef)
			blocsnew.append(cesar(blocs[i],clef))
		respuesta = ''
		for i in range(len(blocs[0])):
			for j in range(longueur):
				try:
					respuesta += blocsnew[j][i]
				except Exception:
					pass
		respuesta = respuesta.replace('\n','').replace(' ','')
		compte = 0
		for cl in mots:
			if cl in respuesta:
				compte+=1
		
		if compte>maxi:
			maxi = compte
			print(respuesta,'\n',kc , compte)
			input()

def facteurs(n):
	tab = []
	for i in range(2,int(sqrt(n))):
		if n%i ==0:
			tab.append(i)
			tab.append(n//i)
	return tab

def exo5():
	texte = """lelnracsrunanatuvllerrmcnjeeaeseiaetanctsagsgeemftqdnne
ntraraueneciliianeredofaesntdneenignpcdaishdcaoaeenede""".replace('\n','')

	icfr = 0.0746
	ics = dict()
	for longueur in range(1,15): #en esperant que la clef ne soit pas plus longue
		blocs = [texte[i::longueur] for i in range(longueur)]
		ic = []
		for bloc in blocs : 
			score = 0
			for lettre in range(ord('a'),ord('z')+1):
				lettre = chr(lettre) 
				tmp = bloc.count(lettre)
				score += tmp*(tmp-1)

			ic.append(score/(len(bloc)*(len(bloc)-1)) )
		
		
		ics[longueur] = abs(mean(ic)-icfr)

	longueur = min(ics.items(), key=operator.itemgetter(1))[0]
	#longueur = 11
	print(longueur)


	blocs = [texte[i::longueur] for i in range(longueur)]
	print(''.join(blocs))


def exo6():
	texte='''ahcaaieqreeiecadapniieliuouuxiusnlbocoretcllia
uintsefesetdletvseeeedeauennsuuivntshnenlttvtl
ydsrtonsasrutonndiicneijttestjliiaeesaoleddrev
lriaimxrpserulnaereautvorqhidoeelutssglaneeslh'''.replace('\n','')
	#texte = 'BUNNAEDRMERDEQENMIAETONX'
	icfr = 0.0746
	ics = dict()
	for longueur in range(1,9): #en esperant que la clef ne soit pas plus longue
		blocs = [texte[i::longueur] for i in range(longueur)]
		ic = []
		for bloc in blocs : 
			score = 0
			for lettre in range(ord('a'),ord('z')+1):
				lettre = chr(lettre) 
				tmp = bloc.count(lettre)
				score += tmp*(tmp-1)

			ic.append(score/(len(bloc)*(len(bloc)-1)) )
		
		
		ics[longueur] = abs(mean(ic)-icfr)

	longueur = min(ics.items(), key=operator.itemgetter(1))[0]
	longueur = 8
	#print(longueur)

	maxi = 0
	blocs = [texte[(i)*int(len(texte)/longueur):(i+1)*int(len(texte)/longueur)] for i in range(longueur)]
	print(blocs)
	while True:
		blocsnew = []
		kc = []
		while True:
			indice = randint(0,len(blocs)-1)
			bloc = blocs[indice]
			
			if bloc not in blocsnew:
				blocsnew.append(bloc)
				kc.append(indice)

			if len(blocsnew) == len(blocs):
				break
		
		#on evalue le nombre de mots connus
		
		#refusion
		respuesta = ''
		for i in range(len(blocs[0])):
			for j in range(len(blocs)):
				respuesta += blocsnew[j][i]


		compte = 0
		for cl in mots:
			if cl in respuesta:
				compte+=1
		
		if compte>maxi:
			maxi = compte
			print(respuesta,kc , compte)
			input()




#exo1()
#exo2()
#exo5()
exo6()