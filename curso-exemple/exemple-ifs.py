"""
como em muitas linguagens o python nao faz diferente
tem o comparador 
== qual compara duas expressões 
True == True resultado -> True
True == False resultado -> False

True != False resultado -> True
True != True resultado -> False

and - aqui é tipo assim
se tiver uma condicao as duas terao que atender no caso vai ter que ser
True e True, pra tal coisa acontecer.
se for 
True e False, nao vai acontecer

or
o ou ja funciona diferente,
o or é ou
entao é um ooooou outro
nao precisa ser os dois 
tipo você tem 3 condicões pra acontecer alguma coisa,
True ou True ou False -> a coisa vai acontecer 
True ou True ou True -> a coisa vai acontecer 

False ou False ou False -> a coisa aqui, já nao vai acontecer 

Operadores Lógicos em Python:

== compara duas expressões
True == True -> True
True == False -> False

!= compara duas expressões
True != False -> True
True != True -> False

and - ambas as condições devem ser verdadeiras
True and True -> True
True and False -> False

or - pelo menos uma condição deve ser verdadeira
True or True or False -> True
False or False or False -> False
"""


# Vamos para as condicões - if
if True:
    print("A condicao foi verdadeira e entao, eu cheguei aqui.")
else:
    print("A condicao foi false e entao, eu cheguei aqui.")

x = 10
if x % 2 == 0:
    print(f"{x} e um numero par")
else:
    print(f"{x} e um numero impar")


a = 11
b = 20

if a > b:
    print(f"{a}, e maior que {b}")
elif a == b:
    print(f"{a} e igual a {b}")
else:
    print(f"{a}, e menor que {b}")


# Exemplo - Condição para tirar CNH;
pessoa1 = {"name": "Henrique", "age": 16}


if pessoa1["age"] >= 18:
    print(f"{pessoa1['name']}, tem idade suficiente para tirar sua CNH.")
else:
    print(f"{pessoa1['name']}, nao tem idade suficiente para tirar sua CNH.")
