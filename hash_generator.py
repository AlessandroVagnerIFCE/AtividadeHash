HASH_TABLE_SIZE = 32

#Métodos de criação de hash

#Método da soma
#Soma os valores ASCII dos caractéres
def sum_method(s):
    total_sum = 0
    for c in s:
        total_sum += ord(c)

    return total_sum

#Método da soma polinomial
#Soma os valores ASCII utilizando peso
def pol_sum_method(s):
    total_sum = 0
    prime_multiplier = 31
    i = 0
    for c in s:
        total_sum += (ord(c)*pow(prime_multiplier, i))
        i += 1

    return total_sum

#Método do deslocamento crítico
#Faz o XOR dos valores ASCII deslocados por uma posição
def critical_shift(s):
    result = 0
    for c in s:
        result = ((ord(c) << 1) ^ result)

    return result


#Métodos de compressão

#Método da divisão
#Utiliza o módulo e o tamanho da tabela hash
def mod_compression(h):
    return (h % HASH_TABLE_SIZE)


#Método da dobra
#Divide o hash em partes menores e faz ou-exclusivo entre essas partes
def fold_compression(h):
    result = 0
    aux_list = []
    aux_string = str(h)
    while len(aux_string) > 1:
        aux_list.append(aux_string[0] + aux_string[1]) #Adiciona à lista auxiliar
        aux_string = aux_string[2:] #Remove os caractéres da string

    if len(aux_string) > 0: #No caso de ter sobrado um dígito
        aux_list.append(aux_string[0])

    for item in aux_list:
        result = (int(item) ^ result)

    if result >= HASH_TABLE_SIZE: #Ainda muito grande, dobrar ao meio
        aux_string = str(result)
        result = (int(aux_string[0])) ^ (int(aux_string[1]))
    
    return result

#Método Multiplicação-Adição-Divisão (MAD)
#Multiplica o hash por uma constante, soma por outra, e depois usa o módulo com um número primo e com o tamanho da tabela hash
def mad_compression(h):
    a = 2
    b = 3
    p = 5387 #710º número primo

    return ((a*h + b) % p) % HASH_TABLE_SIZE