import urllib2

def countlettre (lettreacompter, txt):
	i = 0     #compteur
	
	for l in txt :    #lettre
		if l == lettreacompter:
			i = i+1
	return i


#novuellefcno



#main
f    = urllib2.urlopen("http://pi.com")
data = f.read()
f.close()
print ilya
print
print countlettre('a', data)
print countlettre('t', data)

#data = "tetzetjzekltj" 
#compter le nombre pour chaque lettre de l'alphabet -
#

#fonction#
#in 2 variables : txt lettre
#out txt enlever lettre

# txt =salut , lettre = t
# out salu




