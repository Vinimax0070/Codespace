# Exemplo de código em Python abordando concatenação, for, while, listas e tuplas

# Concatenação de Strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

# Usando f-strings (Python 3.6+)
print(f"Nome completo: {nome} {sobrenome}")

# Estruturas de Repetição - For
print("Iterando com for:")
for i in range(1, 5):
    print(i, end=' ')
print()  # apenas para pular uma linha

# Estruturas de Repetição - While
print("Iterando com while:")
contador = 0
while contador < 5:
    print(contador, end=' ')
    contador += 1
print()  # apenas para pular uma linha

# Listas
print("Trabalhando com listas:")
frutas = ['maçã', 'banana', 'laranja']
print("Lista de frutas:", frutas)
frutas.append('morango')
print("Após adicionar 'morango':", frutas)

# Iterando sobre uma lista com for
print("Iterando sobre a lista de frutas:")
for fruta in frutas:
    print(fruta, end=' ')
print()  # apenas para pular uma linha

# Concatenando listas
outras_frutas = ['uva', 'abacaxi']
todas_frutas = frutas + outras_frutas
print("Todas as frutas:", todas_frutas)

# Tuplas
print("Trabalhando com tuplas:")
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)
# Acessando elementos de uma tupla
x, y = coordenadas
print(f"Coordenada x: {x}, Coordenada y: {y}")

# Comparação entre Listas e Tuplas
print("Comparação entre listas e tuplas:")
numeros_lista = [1, 2, 3]
numeros_tupla = (1, 2, 3)
print("Lista:", numeros_lista)
print("Tupla:", numeros_tupla)

# Exemplo de uso de for com tupla
print("Iterando sobre a tupla de números:")
for num in numeros_tupla:
    print(num, end=' ')
print()  # apenas para pular uma linha

# Exemplo completo
print("Exemplo completo:")
frutas.append('pêssego')
print("Lista de frutas atualizada:", frutas)
print(f"Todas as frutas agora são: {todas_frutas}")

# Considerações finais
print("Considerações finais:")
print("- Listas são mutáveis, tuplas são imutáveis.")
print("- Use listas quando precisar de mutabilidade, use tuplas para dados imutáveis.")
print("- Escolha entre for e while dependendo do problema e da lógica de controle necessária.")
