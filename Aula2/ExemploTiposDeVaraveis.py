# Números inteiros
idade = 17
quantidade_produtos = 100

# Números de ponto flutuante (float)
preco_unitario = 29.99
pi = 3.14159

# Strings simples
nome = "Leonardo"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem_formatada)

# listas e tuplas 
# listas usa "[]" e tuplas usa "()"
# listas mutaveis
frutas = ["maça","banana","uva"]

# adicionando elementos a uma lista 
frutas.append("Laranja")

# tuplas (imutaveis)
coordenadas = (4,5)
cores_rgb = (255, 0, 0)

# print(frutas)
# com faz pra imprimir apenas uma fruta 
# print(frutas[1])

# 4. Dicionários:

# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))

# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"



