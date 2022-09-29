a = -1 
b = 1
c = 1
r = a+b+c
for i in range (1,21,1):
    print(r)
    c = b
    b = a
    a = r
    r = a+b+c
# Seuencia de soma com números impáres 2 + 3  = 5 + 5 
#Sequencia_de_n_impares = 3, 5, 7, 9, 11, 12, 13
#Sequencia_de_resultados = 5, 10, 17, 26, 37

