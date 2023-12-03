# Esse eu vou digitar toodo parece que só t o d o tudo junto é uma palavra reservada

"""
comentarios em multiplas linhas no pythonzera
"""
#######################################################

# variaveis e tipos

nome = "josé"
frase = "Sejam todos bem vindos por aqui, cursinho de python em 6 horas meu nobre"
sobrenome = "Silva"

# Numeros três tipos
# Tipo FLOAT
altura = 1.80

# Tipo INT
idade = 30

# Complex
numero_complexo = 1 + 2j
# Utilizado em estatística, e em engenharia elétrica

# parece que no python não gostam de ; no final da linha não rs

#######################################################

# Tipo boolean
possui_carro = True
tem_filhos = False
""" Esse tipo basicamente tem só dois estados né,
true verdadeiro ou false falso mesmo"""

#######################################################

# Listas
# Tipo Array
carros = ["Camaro", "Lamborghini", "Ferrari"]

# Operações com arrays

carros.append("Hilux")
"""
Vai inserir um objeto na útima posição do array, tipo um push do js
"""
carros.insert(0, "Hilux")
"""
Vai inserir um objeto numa posição especifica do array. 
tipo um shit ou push só que melhorado tipo um slice mesmo.
porque aqui você inseri aonde você quiser, de um jeito bem simples
e lógico além de verificar se tem e retirar né achei bem legal ser simples de fazer
legalzinho gostei.
o primeiro parametro é o index né, e o segundo é o que você quer appendar
ou adicionar no array
"""
carros.remove("Hilux")
"""
vai remover o objeto que você passar aqui do array. então talvez
ele busque e depois remova.
"""

#######################################################

umaString = "errado pela convenção do python"
uma_string = "certo pela convenção do python"
"""
pelo o que eu entendi, o python segui a convenção
snake_case e não a camelCase a qual eu estou aconstumado
"""

#######################################################

type(uma_string)
"""
No javascript a gente tem o typeof,
no python é type(passa a variavel) e ela retorna 
o tipo que você passou na função type() 
"""

#######################################################
# Lista tipo chave:valor - dict( dicionario )

livros = {}
livros["titulo"] = "Aprendendo a programar em python meu nobre"
livros["ano"] = 2018

pessoa = {"nome": "John doe", "idade": 30, "altura": 1.8, "peso": 90}
"""
os métodos do dicionario são parecidos com uma função,
possuem parametros e retornam valores, mas a sintaxe é diferente 
"""
pessoa.keys()  # => Retorna a lista com os indices

pessoa.values()  # => Retorna a lista com o valores

#######################################################

# Entendendo sobre tuplas

# Declaração de uma Lista  do tipo tuplas
dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
dias_da_semana2 = "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"

# print(type(dias_da_semana))
# => Resulta em <class 'tuple'>

# print(type(dias_da_semana2))
# => Resulta em <class 'tuple'>


# Tuplas de um unico elemento

tupla1 = ("a",)
tupla2 = ("b",)

# print(type(tupla1))
# => Resulta em <class 'tuple'>

# print(type(tupla2))
# => Resulta em <class 'tuple'>

