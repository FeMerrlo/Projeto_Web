
for i in range (1,11,1):
 n = int(input("Entre com um valor: "))
 s = 0
 maior = n
while n < 0:
     print("Não pode, digite um valor menor que 0 ")
     n = int(input("Entre com um valor:"))
if i == 1:
     maior = n
if n > maior:
     maior = n
s = s + n
media = 5 / 10
print (f'{n} {s} = {media}')