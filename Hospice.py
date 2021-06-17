#Dictionnaire
hospice ={'Matières':['Java','Analyse', 'Se', 'Anglais', 'Langage C', 'reseaux','UML'],'Note':[18,20,12,14,13,15,14]}

print(hospice)

moy = (hospice['Note'][0]+hospice['Note'][1]+hospice['Note'][2]+hospice['Note'][3]+hospice['Note'][4]+hospice['Note'][5]+hospice['Note'][6])/7

print(moy)




E0
#1
n = [1,2,3,4,5,6,7,8,9]
print(n)

#2
n[0] = n[0]+11
n[1] = n[1]+11  
n[2] = n[2] + 11
n[3] = n[3] + 11
n[4] = n[4] + 11
n[5] = n[5] + 11
n[6] = n[6] + 11
n[7] = n[7] + 11
n[8] = n[8] + 11
n[9] = n[9] + 11

#3 

n.append(22)

#4
n = n + [23, 24]

#5
n = n + ['l2':[2,4,6,8], 'l3':[1,3,5,7,9]]

#6 
help(n.remove)
n.remove(3)




#E1
d = {'nom': 'Dupon','prenom':'Jacque','age':30
     
     d['prenom']= 'Jacques'
     print(d.Keys)
     print(d.Values)
     print(d)
     print(d['prenom'], " " , d['nom'], " à " , d['age'], " ans")
     
