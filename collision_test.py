import hash_generator

#Lista de strings para ser utilizada nos testes
strings = ["apple", "voadora", "banjo", "banana", "cherry", "date",
"elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
"mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
"raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
"IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco"]

#Listas para contar colisões
#Método da soma
tabela_hash_sum_mod = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_sum_fold = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_sum_mad = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições


#Método da soma polinomial
tabela_hash_pol_mod = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_pol_fold = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_pol_mad = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições


#Método do deslocamento crítico
tabela_hash_shift_mod = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_shift_fold = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

tabela_hash_shift_mad = [0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,
                     0, 0, 0, 0,] #32 posições

#Como o teste irá funcionar:
#A cada vez que um hash para a tabela for gerado, será somado 1 na posição que seria ocupada
#Para cada posição onde o valor é maior que 0, o número de colisões pode ser determinado por (valor - 1)
#Todas as strings irão passar por todas as combinações de geração de hash e compressão

for item in strings:
    #Criar hash com diferentes métodos
    sum_hash = hash_generator.sum_method(item)
    pol_hash = hash_generator.pol_sum_method(item)
    shift_hash = hash_generator.critical_shift(item)

    #Algoritmos de compressão aplicados ao hash criado por método da soma
    sum_mod = hash_generator.mod_compression(sum_hash)
    sum_fold = hash_generator.fold_compression(sum_hash)
    sum_mad = hash_generator.mad_compression(sum_hash)

    #Algoritmos de compressão aplicados ao hash criado por método da soma polinomial
    pol_mod = hash_generator.mod_compression(pol_hash)
    pol_fold = hash_generator.fold_compression(pol_hash)
    pol_mad = hash_generator.mad_compression(pol_hash)

    #Algoritmos de compressão aplicados ao hash criado por método do deslocamento crítico
    shift_mod = hash_generator.mod_compression(shift_hash)
    shift_fold = hash_generator.fold_compression(shift_hash)
    shift_mad = hash_generator.mad_compression(shift_hash)


    #Adicionar 1 aos valores correspondentes nas tabelas
    tabela_hash_sum_mod[sum_mod] += 1
    tabela_hash_sum_fold[sum_fold] += 1
    tabela_hash_sum_mad[sum_mad] += 1

    tabela_hash_pol_mod[pol_mod] += 1
    tabela_hash_pol_fold[pol_fold] += 1
    tabela_hash_pol_mad[pol_mad] += 1

    tabela_hash_shift_mod[shift_mod] += 1
    tabela_hash_shift_fold[shift_fold] += 1
    tabela_hash_shift_mad[shift_mad] += 1


#Imprimir resultados
print("Método da soma + compressão por divisão")
print(tabela_hash_sum_mod)
print("")

print("Método da soma + compressão por dobra")
print(tabela_hash_sum_fold)
print("")

print("Método da soma + compressão por MAD")
print(tabela_hash_sum_mad)
print("")


print("")


print("Método da soma polinomial + compressão por divisão")
print(tabela_hash_pol_mod)
print("")

print("Método da soma polinomial + compressão por dobra")
print(tabela_hash_pol_fold)
print("")

print("Método da soma polinomial + compressão por MAD")
print(tabela_hash_pol_mad)
print("")


print("")


print("Método do deslocamento crítico + compressão por divisão")
print(tabela_hash_shift_mod)
print("")

print("Método do deslocamento crítico + compressão por dobra")
print(tabela_hash_shift_fold)
print("")

print("Método do deslocamento crítico + compressão por MAD")
print(tabela_hash_shift_mad)
print("")