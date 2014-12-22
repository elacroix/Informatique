#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_number_in_list(nb,tab):
    """
	Renvoie True si le nombre nb est dans la liste de nombres tab.
    Renvoie False sinon. 
    
    Keyword arguments:
    nb -- nombre entier
    tab -- liste de nombre entiers
    """
    i=0
    while i<len(tab) and tab[i]!=nb:
        i+=1
    return i<len(tab)
# Exemple :
#nb1,nb2,liste = 4,9,[1,2,3,5,9]
#print(is_number_in_list(nb1,liste))
#print(is_number_in_list(nb2,liste))


def what_is_max(tab):
    """ 
	Renvoie le plus grand nombre d'une liste
    
    Keyword arguments:
    tab -- liste de nombres
    """
    i=1
    maxi=tab[0]
    while i<len(tab):
        if tab[i]>maxi:
            maxi=tab[i]
        i+=1
    return maxi
# Exemple :
#liste = [1,2,3,5,9]
#print(what_is_max(liste))


def what_is_max(tab):
    """ 
    Renvoie le plus grand nombre d'une liste.
    Keyword arguments:
    tab -- liste de nombres
    """
    i=1
    maxi=tab[0]
    while i<len(tab):
        if tab[i]>maxi:
            maxi=tab[i]
        i+=1
    return maxi
# Exemple :
#liste = [1,2,3,5,9,5,3,1,5]
#print(what_is_max(liste))


def is_number_in_list_dicho(nb,tab):
    """ 
    Renvoie l'index si le nombre nb est dans la liste de nombres tab.
    Renvoie None sinon.
    
    Keyword arguments:
    nb -- nombre entier
    tab -- liste de nombres entiers triés
    """
    g, d = 0, len(tab)-1
    while g <= d:
        m = (g + d) // 2
        if tab[m] == nb:
            return m
        if tab[m] < nb:
            g = m+1
        else:
            d = m-1
    return None
# Exemple :
#nb1,nb2,liste = 4,9,[1,2,3,5,9]
#print(is_number_in_list_dicho(nb1,liste))
#print(is_number_in_list_dicho(nb2,liste))



def calcul_moyenne(tab):
    """ 
	Renvoie la moyenne des éléments d'un tableau.
    
	Keyword arguments:
    tab -- liste de nombres entiers
    """
    res = 0
    for i in range(len(tab)):
        res = res+tab[i]
    
    return res/(len(tab))
# Exemple :
#liste = [1,2,3,5,9]
#print(calcul_moyenne(liste))

def calcul_variance(tab):
    """ 
	Calcule la variance des éléments d'un tableau.
    
	Keyword arguments:
    tab -- liste de nombres entiers
    """
    m = calcul_moyenne(tab)
    res = 0
    for i in range(len(tab)):
        res = res+(tab[i]-m)**2
    
    return res/(len(tab))
# Exemple :
#liste = [1,2,3,5,9]
#print(calcul_moyenne(liste))
#print(calcul_variance(liste))


def index_of_word_in_text(mot, texte):
    """ 
	Recherche si le mot est dans le texte.
    Renvoie l'index si le mot est présent, None sinon.
    
    Keyword arguments:
    mot -- mot recherché
    texte -- texte
    """
    for i in range(1 + len(texte) - len(mot)):
        j = 0
        while j < len(mot) and mot[j] == texte[i + j]:
            j += 1
        if j == len(mot):
            return i
    return None

# Exemple
#Texte = "Chuck Norris has a grizzly bear carpet in his room. The bear isn't dead it is just afraid to move."
#Mot = "ove."
#print(index_of_word_in_text(Mot,Texte))

# =================
# Calcul numérique
# =================

def integrale_rectangles_gauche(f,a,b,nb):
    """
    Calcul de la valeur approchée de l'intégrale de f(x) entre a et b par la 
    méthode des rectangles à gauche.
    Keywords arguments :
    f -- fonction à valeur dans IR
    a -- flt, borne inférieure de l'intervalle d'intégration
    b -- flt, borne supérieure de l'intervalle d'intégration
    nb -- int, nombre d'échantillons pour le calcul
    """
    res = 0
    pas = (b-a)/nb    
    x = a
    while x<b-pas:
        res = res + pas *f(x)
        x = x + pas
    return res


def integrale_rectangles_droite(f,a,b,nb):
    """
    Calcul de la valeur approchée de l'intégrale de f(x) entre a et b par la 
    méthode des rectangles à droite.
    Keywords arguments :
    f -- fonction à valeur dans IR
    a -- flt, borne inférieure de l'intervalle d'intégration
    b -- flt, borne supérieure de l'intervalle d'intégration
    nb -- int, nombre d'échantillons pour le calcul
    """
    res = 0
    pas = (b-a)/nb
    x = a+pas
    while x<b-pas:
        res = res + pas *f(x)
        x = x + pas
    return res

def integrale_rectangles_milieu(f,a,b,nb):
    """
    Calcul de la valeur approchée de l'intégrale de f(x) entre a et b par la 
    méthode du point milieu.
    Keywords arguments :
    f -- fonction à valeur dans IR
    a -- flt, borne inférieure de l'intervalle d'intégration
    b -- flt, borne supérieure de l'intervalle d'intégration
    nb -- int, nombre d'échantillons pour le calcul
    """
    res = 0
    pas = (b-a)/nb
    x = a+pas
    while x<b-pas:
        res = res + pas *(f(x)+f(x+pas))/2
        x = x + pas
    return res

# Exemple :    
#def ff(x):
#    return 2#x*x       
#print(integrale_rectangles_gauche(ff,0,1,10000))
#print(integrale_rectangles_droite(ff,0,1,10000))
#print(integrale_rectangles_milieu(ff,0,1,5000))
#print(1/3)

def euler_explicite(tau,y0,yf,tf,nb):
    """
    Résolution d'une équation différentielle d'ordre 1 en utilisant la méthode
    d'Euler explicite.
    Keywords arguments :
    tau -- flt, constante de temps de l'équation différentielle 
    y0 -- flt, valeur initiale de y(t)
    yf -- flt valeur finale de y(t)
    tf -- flt temps de fin de la simulation
    nb -- int, nombre d'échantillons pour la simulation
    """
    t = 0
    y = y0 
    pas = tf / nb
    res = []
    while t < tf:
        res.append((t,y))
        y = y + pas*(yf-y)/tau
        t = t + pas
    return res

#res = euler_explicite(1,0,5,25,1000)
#x,y = [],[]
#for i in range(len(res)):
#    x.append(res[i][0])
#    y.append(res[i][1])
#plot(x,y)


def recherche_pivot(A,i):
    n = len(A) # le nombre de lignes
    j = i # la ligne du maximum provisoire
    for k in range(i+1, n):
        if abs(A[k][i]) > abs(A[j][i]):
            j = k # un nouveau maximum provisoire
    return j
    
def echange_lignes(A,i,j):
    # Li <-->Lj
    A[i][:],A[j][:]=A[j][:],A[i][:]


def transvection_ligne(A, i, j, mu):
    # L_i <- L_i + mu.L_j """
    nc = len(A[0]) # le nombre de colonnes
    for k in range(nc):
        A[i][k] = A[i][k] + mu * A[j][k]

def resolution_gauss_jordan(AA, BB):
    """Résolution de AA.X=BB; AA doit etre inversible"""
    A, B = AA.copy(), BB.copy()
    n = len(A)
    assert len(A[0]) == n
    # Mise sous forme triangulaire
    for i in range(n):
        j = recherche_pivot(A, i)
        if j > i:
            echange_lignes(A, i, j)
            echange_lignes(B, i, j)
        for k in range(i+1, n):
            x = A[k][i] / float(A[i][i])
            transvection_ligne(A, k, i, -x)
            transvection_ligne(B, k, i, -x)
    # Phase de remontée
    X = [0.] * n
    for i in range(n-1, -1, -1):
        X[i] = (B[i][0]-sum(A[i][j]*X[j] for j in range(i+1,n))) / A[i][i]
    return X



AA = [[-1,-2,-3],[0,-1,-4],[-3,-4,-1]]
BB = [[1],[3],[1]]
       
res1 = resolution_gauss_jordan(AA,BB)
res2 = np.linalg.solve(AA,BB)
print(res1)
print(res2)





# ====================
# Algorithmes de tris
# ====================

def tri_insertion_01(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i]
        j=0
        while j<=i-1 and tab[j]<x:
            j = j+1
        for k in range(i-1,j-1,-1):
            tab[k+1]=tab[k]
        tab[j]=x

# Exemple :
#liste = [1,9,7,6,5]
#print(liste)
#tri_insertion_01(liste)
#print(liste)


def tri_insertion_02(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i]
        j=i
        while j>0 and tab[j-1]>x:
            tab[j]=tab[j-1]
            j = j-1
        tab[j]=x

# Exemple :
#liste = [1,8,7,6,5]
#print(liste)
#tri_insertion_02(liste)
#print(liste)
        
def exponentiation_naive(x,n):
    """ 
	Renvoie x**n par la méthode naïve.
    
    Keyword arguments:
    x -- un nombre réel
    n -- un nombre entier
    """
    
    j=n
    res = 1
    while j>=1:
        res = res * x
        j=j-1
    return res

#print(exponentiation_naive(3,2))
#print(exponentiation_naive(3,0))