import re
from re import *  # para não ser preciso o re.
import matplotlib.pyplot as plt
import json
import os
from numpy import arange




## ================= Cria estruturas =================##


# recebe um array de strings: ['nome',' entidade ', ...]
# Esta função retira os primeiros e ultimos espaços de uma string
def RetiraEspaços(array, length):
    arrayNovo = []
    for i in range(0, length):
        variavel = array[i].strip()
        arrayNovo.append(variavel)

    return arrayNovo




def cria_estruturas(linhas_texto):
    nomes = []
    emails = []
    entidades = []
    niveis = []
    nb = []
    for linha in linhas_texto:
        inscricao2 = split(r'::', linha.strip('\n'))  ## o strip é para tirar o \n da ultima posição

        # Vamos tirar os primeiros e ultimos espaços do nome, email,etc... , ou seja, '  joao   ' fica 'joao'
        inscricao = RetiraEspaços(inscricao2, len(inscricao2))

        if inscricao != ['']:
            if inscricao[0] == '':
                nomes.append('(Não há nome)')
            else:
                nomes.append(inscricao[0])

            if inscricao[1] == '':
                emails.append('(Não há email)')
            elif(search(r'^[A-z0-9\_\.\+\-]+@[A-z0-9\-]+\.[A-z0-9\-\.]+$',inscricao[1])==None):
                emails.append('(Inválido)')
            else:
                emails.append(inscricao[1])
            if inscricao[2] == '':
                entidades.append('(Não há entidade)')
            elif(search(r'^ent\_[A-z0-9\-\.]+$',inscricao[2])==None):
                entidades.append('(Inválido)')
            else:
                entidades.append(inscricao[2])
            if inscricao[3] == '':
                niveis.append('(Não há nivel)')
            elif (search(r'^([0-9]*[.])?[0-9]+$',inscricao[3])==None):
                niveis.append('(Inválido)')
            else:
                niveis.append(inscricao[3])
            if inscricao[4] == '':
                nb.append('(Não há NB)')
            elif (search(r'^([0-9]*[.])?[0-9]+$',inscricao[4])==None):
                nb.append('(Inválido)')
            else:
                nb.append(inscricao[4])

    return [nomes, emails, entidades, niveis, nb]



## ================= lista_erros =================##

def lista_erros(l):
    
    lista_de_erros = []
    for i in range(0, len(l)):
        if (l[i][0]!='(Não há email)' and l[i][0]!='(Inválido)'):
            if (len(l[i][1:]) > 1):
                x = 'O email ' + l[i][0] + ' está presente nos utilizador/es: ' + str(l[i][1:])

                lista_de_erros.append(x)



    return lista_de_erros



## ================= imprime... =================##

def imprime_nomes_inv_ou_emfalta(nomes):


    nao_ha=[]
    for i in range(0,len(nomes)):
        if (nomes[i]=='(Não há nome)'):
            nao_ha.append(nomes[i])


    if (len(nao_ha)!=0):
        print('Há '+str(len(nao_ha))+' utilizadores que não têm nome')


def imprime_emails_inv_ou_emfalta(emails):
    invalidos = []
    nao_ha = []
    for i in range(0, len(emails)):
        if (emails[i] == '(Não há email)'):
            nao_ha.append(emails[i])
        elif (emails[i] == '(Inválido)'):
            invalidos.append(emails[i])

    if (len(nao_ha) != 0):
        print('Há '+str(len(nao_ha))+' utilizadores que não têm email')
    if (len(invalidos) != 0):
        print('Há '+str(len(invalidos))+' utilizadores que têm emails inválidos')



def imprime_entidades_inv_ou_emfalta(entidades):
    invalidos = []
    nao_ha = []
    for i in range(0, len(entidades)):
        if (entidades[i] == '(Não há entidade)'):
            nao_ha.append(entidades[i])
        elif (entidades[i] == '(Inválido)'):
            invalidos.append(entidades[i])

    if (len(nao_ha) != 0):
        print('Há '+str(len(nao_ha))+' utilizadores que não têm entidade')
    if (len(invalidos) != 0):
        print('Há '+str(len(invalidos))+' utilizadores que têm entidades inválidas')


def imprime_niveis_inv_ou_emfalta(niveis):
    invalidos = []
    nao_ha = []
    for i in range(0, len(niveis)):
        if (niveis[i] == '(Não há nivel)'):
            nao_ha.append(niveis[i])
        elif (niveis[i] == '(Inválido)'):
            invalidos.append(niveis[i])

    if (len(nao_ha) != 0):
        print('Há '+str(len(nao_ha))+' utilizadores que não têm nivel')
    if (len(invalidos) != 0):
        print('Há '+str(len(invalidos))+' utilizadores que têm niveis inválidos')

def imprime_nb_inv_ou_emfalta(nb):
    invalidos = []
    nao_ha = []
    for i in range(0, len(nb)):
        if (nb[i] == '(Não há NB)'):
            nao_ha.append(nb[i])
        elif (nb[i] == '(Inválido)'):
            invalidos.append(nb[i])

    if (len(nao_ha) != 0):
        print('Há '+str(len(nao_ha))+' utilizadores que não têm nb')
    if (len(invalidos) != 0):
        print('Há '+str(len(invalidos))+' utilizadores que têm nbs inválidos')



## ================= imprimeerros =================##

def imprimeerros(lista_de_erros):
    if (len(lista_de_erros) != 0):
        print('\033[1;31mUsuários com emails repetidos(erro):\033[m')
        for i in range(0, len(lista_de_erros)):
            print(lista_de_erros[i])




## ================= Exercicio 1 =================##

def juntaNomesEntidades(nomes, entidades):
    utilizadores=[]
    utilizadores_sem_nome=[]
    for a in zip(nomes, entidades):
        utilizadores.append(a)

    return utilizadores


def printa2Parametros(NomEent_Ordenados):

    for x in range(0, len(NomEent_Ordenados)):
        print('Nome: ', NomEent_Ordenados[x][0], ' || Entidade: ', NomEent_Ordenados[x][1])



def Exercicio1(nomes, entidades):
    # Criar um array do genero: [['joao','ent_joao'] , ['Maria','ent_Maria'], ...]
    NomesEentidades = juntaNomesEntidades(nomes, entidades)

    # Ordenar o array anterior em função dos nomes
    NomEent_Ordenados = sorted(NomesEentidades)  # por default o sorted ordena segundo o 1 parametro

    # Fazer o print dos nomes ordenados alfabeticamente e as entidades respetivas
    printa2Parametros(NomEent_Ordenados)






## ================= Exercicio 2 =================##


def Exercicio2(nomes, emails, entidades):
    # Lista entidades sem elementos repetidos
    newEntidades = list(set(entidades))
    # Retirar elemento '(Não há entidade)' de newEntidades, se existir
    semEnt = entidades.count('(Não há entidade)')

    if (semEnt > 0):
        newEntidades.remove('(Não há entidade)')

    # Retirar elemento '(Inválido)' de newEntidades, se existir
    semEnt2 = entidades.count('(Inválido)')
    if (semEnt2 > 0):
        newEntidades.remove('(Inválido)')


    # Ordenar a lista newEntidades por ordem alfabética
    newEntidades = sorted(newEntidades)

    # Número de entidades
    numEntidades = len(newEntidades)

    # Lista que irá conter o núm de utilizadores de cada entidade (numUtilizadoresEntidade[i] corresponde a newEntidades[i])
    numUtilizadoresEntidade = [0 for i in range(0, numEntidades)]

    # Percorrer a lista entidades para preencher a lista numUtilizadoresEntidade
    for n in range(0, len(entidades)):

        for i in range(0, numEntidades):

            if (entidades[n] == newEntidades[i]):
                numUtilizadoresEntidade[i] += 1

    print('\033[1;31mEntidades referenciadas e respetivos número e lista de utilizadores:\033[m\n')

    # Percorrer a lista newEntidades para imprimir utilizadores de cada entidade
    for i in range(0, numEntidades):
        print('\n' + newEntidades[i] + ' (' + str(numUtilizadoresEntidade[i]) + ' utilizador(es))\n')

        for n in range(0, len(entidades)):

            if (entidades[n] == newEntidades[i]):
                print('\tNome: ' + nomes[n] + ' ; Email: ' + emails[n] + '.')

    # Caso haja utilizadores sem entidade:
    if (semEnt > 0):
        print('\n\033[1;31mOs seguintes utilizadores não têm entidade:\033[m')
        # Imprimir utilizadores sem entidade
        for n in range(0, len(entidades)):
            if (entidades[n] == '(Não há entidade)'):
                print('\tNome: ' + nomes[n] + ' ; Email: ' + emails[n] + '.')

    # Caso haja utilizadores com entidades inválidas:
    if (semEnt2 > 0):
        print('\n\033[1;31mOs seguintes utilizadores têm uma entidade inválida:\033[m')
        # Imprimir utilizadores com entidade inválida
        for n in range(0, len(entidades)):
            if (entidades[n] == '(Inválido)'):
                print('\tNome: ' + nomes[n] + ' ; Email: ' + emails[n] + '.')




## ================= Exercicio 3 =================##



def Exercicio3(niveis, nomes, emails):
    emails_filter = sorted(list(set(emails)))  ## lista de emails sem repetições e ordenada
    niveis_filter = sorted(list(set(niveis)))  ## lista de niveis sem repetições e ordenada

    ## tive de criar esta lista pois vou precisar de criar listas do tipo: [[1,utilizadores+email],[2,utilizadores+email]....]
    niveis_utilizadores = []
    emails_sublistas = []

    ## começo por preencher os níveis na sua devida posição
    for p in range(0, len(niveis_filter)):
        niveis_utilizadores.append([])  ## crio uma sublista
        niveis_utilizadores[p].append(
            niveis_filter[p])  ## preencho com os níveis na posição que pretendia para a lista niveis_utilizadores

    ## começo por preencher os emails na sua devida posição
    for e in range(0, len(emails_filter)):
        emails_sublistas.append([])  ## crio uma sublista
        emails_sublistas[e].append(emails_filter[e])

    ## agora vou reagrupar os utilizadores por nivel de acesso e preencher os emails com os utilizadores
    for n in range(0, len(nomes)):

        ## inicio do preenvhimento dos utilizadores+email
        for i in range(0, len(niveis_filter)):
            if (niveis[n] == niveis_filter[i]):
                niveis_utilizadores[i].append('Nome:' + nomes[n] + ' Email:' + emails[n])
        for j in range(0, len(emails_filter)):
            if (emails[n] == emails_filter[j]):
                emails_sublistas[j].append(nomes[n])

    # vou retornar para utilizar na 5.4
    return [niveis_utilizadores, emails_sublistas]


## imprime os niveis e os utilizadores correspondentes, se houver omissão de níveis, retorna erro
##  e indica quais utilizadores isso aconteceu

def imprimir_niveis_nomes(l):
    ##  aqui serve somente para imprimir de forma apelativa na tela
    for i in range(0, len(l)):
        if (l[i][0] == '(Não há nivel)'):

            print('Há omissão de niveis nos seguintes utilizadores:', l[i][1:])
            print('\n\n')
        elif (l[i][0] == '(Inválido)'):
            print('Os seguintes utilizadores têm níveis inválidos:', l[i][1:])
            print('\n\n')

        else:
            print("\033[1;31mNivel:\033[m", l[i][0])
            print("\033[1;31mUtilizadores e emails:\033[m", l[i][1:])
            print('\n\n')





# ================== Exericico 4 =================#


def EliminaRepetidos(array):
    return list(dict.fromkeys(array))


def printaArray(array):
    for x in range(0, len(array)):
        print(array[x])


def Exercicio4(nomes, entidades):
    # criar uma lista que vai ter as entidades possiveis [en_a,en_b,en_c...] sem repetições
    entidadesSemRep = entidades
    entidadesSemRep = EliminaRepetidos(entidadesSemRep)

    # Ordenar as entidadesSemRep
    entidadesSemRep = sorted(entidadesSemRep)

    # Juntar os nomes e as entidades correspondentes(como se fez na 1)
    # Criar um array do genero: [['joao','ent_joao'] , ['Maria','ent_Maria'], ...]
    NomesEentidades = juntaNomesEntidades(nomes, entidades)

    # Ordenar NomesEentidades pela entidade
    NomEent_Ordenados = sorted(NomesEentidades, key=lambda x: x[1])

    # Printar
    for ent in range(0, len(entidadesSemRep)):
        arrayAux = []
        if entidadesSemRep[ent] != '(Não há entidade)' and entidadesSemRep[ent] != '(Inválido)':
            print('\n\n')
            print('\033[1;31m//============ Entidade\033[m ', entidadesSemRep[ent], '\033[1;31m ===========//\033[m')

            for utilizador in range(0, len(NomEent_Ordenados)):
                # ver se as entidades sao iguais, se sim vamos guardar os nomes de todos os utilizadores com a mesma entidade
                if (NomEent_Ordenados[utilizador][1] == entidadesSemRep[ent]):
                    arrayAux.append(NomEent_Ordenados[utilizador][0])

            # agora vamos ordena-los alfabeticamente
            arrayAux = sorted(arrayAux)

            # printar os nomes
            printaArray(arrayAux)
        elif (entidadesSemRep[ent] == '(Não há entidade)'):
            print('\n\n')
            print('Os seguintes utilizadores não têm entidade:')
            for utilizador_erro in range(0, len(NomEent_Ordenados)):
                if (NomEent_Ordenados[utilizador_erro][1] == entidadesSemRep[ent]):
                    # ver se as entidades sao iguais, se sim vamos guardar os nomes de todos os utilizadores com a mesma entidade
                    arrayAux.append(NomEent_Ordenados[utilizador_erro][0])

            # agora vamos ordena-los alfabeticamente
            arrayAux = sorted(arrayAux)
            # printar os nomes
            printaArray(arrayAux)
        else:
            print('\n\n')
            print('Os seguintes utilizadores têm entidade Inválida:')
            for utilizador_erro in range(0, len(NomEent_Ordenados)):
                if(NomEent_Ordenados[utilizador_erro][1] == entidadesSemRep[ent]):
                    # ver se as entidades sao iguais, se sim vamos guardar os nomes de todos os utilizadores com a mesma entidade
                    arrayAux.append(NomEent_Ordenados[utilizador_erro][0])
                    # agora vamos ordena-los alfabeticamente
            arrayAux = sorted(arrayAux)
    # printar os nomes
            printaArray(arrayAux)




# ================== Exericico 5 =================#




def EliminaEmails_NaoHa_Invalidos(EmailsSemRepetidos):

    EmailsSem_NaoHa_Invalidos=[]
    for i in range(0,len(EmailsSemRepetidos)):
        if(EmailsSemRepetidos[i]!='(Não há email)' and EmailsSemRepetidos[i]!='(Inválido)'):
            EmailsSem_NaoHa_Invalidos.append(EmailsSemRepetidos[i])

    return EmailsSem_NaoHa_Invalidos



def Exercicio5(emails, EmailsRepetidos):

    #emails Invalidos = emails com (Não há email) e (Inválido)
    print('Número de utilizadores total(incluido emails repetidos + inválidos + sem email): ', len(emails))

    # Saber o numero de emails sem repeticoes
    EmailsSemRepetidos = EliminaRepetidos(emails)
    NumEmailsSemRepetidos = len(EmailsSemRepetidos)

    #Eliminar os emails=nao_ha e emails=invalido
    NumEmailsSemRepetidos_eValidos = len(EliminaEmails_NaoHa_Invalidos(EmailsSemRepetidos))

    # O numero de utilizadores que não têm os seus emails repetidos sao:
    # emails sem repetiçoes - numero de emails com repeticoes(repetidos + inválidos)
    # Ex: Consideremos que sao emails [j,s,x,c,j,d,r,s,nao_ha,nao_ha,invalido]
    # NumEmailsSemRepetidos_eValidos = len([j,s,x,c,d,r]) = 6
    # numero de emais com repeticoes([j,s]) = 2 -> o array EmailsRepetidos apenas tem os emails repetidos(sem invalidos e sem (Nao ha))
    # Numero emails validos = 6 - 2 = 4

    print('Número de utilizadores válido: ', NumEmailsSemRepetidos_eValidos - len(EmailsRepetidos))



# ================== Exercicio 6 =================#



def Exercicio6(entidades):  # retorna o número de elementos na lista entidades
    # Lista entidades sem elementos repetidos
    newEntidades = list(set(entidades))
    # Retirar elemento '(Não há entidade)' de newEntidades, se existir
    if (newEntidades.count('(Não há entidade)') > 0):
        newEntidades.remove('(Não há entidade)')

    # Retirar elemento '(Inválido)' de newEntidades, se existir

    if (newEntidades.count('(Inválido)')>0):
        newEntidades.remove('(Inválido)')

    return len(newEntidades)



# ================== Exercicio 7  =================#




def Exercicio7_lista(entidades):  # imprime lista das entidades indicando o número de utilizadores de cada uma
    # Lista entidades sem elementos repetidos
    newEntidades = list(set(entidades))
    # Retirar elemento '(Não há entidade)' de newEntidades, se existir
    semEnt = entidades.count('(Não há entidade)')
    if (semEnt > 0):
        newEntidades.remove('(Não há entidade)')

    # Retirar elemento '(Inválido)' de newEntidades, se existir
    semEnt2 = entidades.count('(Inválido)')
    if (semEnt2 > 0):
        newEntidades.remove('(Inválido)')

    # Ordenar a lista newEntidades por ordem alfabética
    newEntidades = sorted(newEntidades)

    # Número de entidades
    numEntidades = len(newEntidades)

    # Lista que irá conter o núm de utilizadores de cada entidade (numUtilizadoresEntidade[i] corresponde a newEntidades[i])
    numUtilizadoresEntidade = [0 for i in range(0, numEntidades)]

    # Percorrer a lista entidades para preencher a lista numUtilizadoresEntidade
    for n in range(0, len(entidades)):

        for i in range(0, numEntidades):

            if (entidades[n] == newEntidades[i]):
                numUtilizadoresEntidade[i] += 1

    print('\033[1;31mDistribuição em número por entidade\033[m\n')

    # Percorrer a lista newEntidades para imprimir o número de utilizadores de cada entidade
    for i in range(0, numEntidades):
        print('\n' + newEntidades[i] + ': ' + str(numUtilizadoresEntidade[i]) + ' utilizador(es)\n')

    # Caso haja utilizadores sem entidade:
    if (semEnt > 0):
        print('\n\033[1;31mHá omissão de entidade em ' + str(semEnt) + ' utilizador(es).\033[m')

    # Caso haja utilizadores com entidade inválida
    if (semEnt2 > 0):
        print('\n\033[1;31mHá entidades inválidas em ' + str(semEnt2) + ' utilizador(es).\033[m')


def Exercicio7_plot(entidades):  # imprime gráfico de barras do número de utilizadores para cada entidade
    # Lista entidades sem elementos repetidos
    newEntidades = list(set(entidades))

    # Retirar elemento '(Não há entidade)' de newEntidades, se existir
    semEnt = entidades.count('(Não há entidade)')
    if (semEnt > 0):
        newEntidades.remove('(Não há entidade)')

    # Retirar elemento '(Inválido)' de newEntidades, se existir
    semEnt2 = entidades.count('(Inválido)')
    if (semEnt2 > 0):
        newEntidades.remove('(Inválido)')

    # Ordenar a lista newEntidades por ordem alfabética
    newEntidades = sorted(newEntidades)

    # Número de entidades
    numEntidades = len(newEntidades)

    # Lista que irá conter o núm de utilizadores de cada entidade (numUtilizadoresEntidade[i] corresponde a newEntidades[i])
    numUtilizadoresEntidade = [0 for i in range(0, numEntidades)]

    # Percorrer a lista entidades para preencher a lista numUtilizadoresEntidade
    for n in range(0, len(entidades)):

        for i in range(0, numEntidades):

            if (entidades[n] == newEntidades[i]):
                numUtilizadoresEntidade[i] += 1

    # Caso haja utilizadores sem entidade:
    if (semEnt > 0):
        numUtilizadoresEntidade.append(semEnt)
        newEntidades.append('Sem entidade')
    
    # Caso haja utilizadores com entidade inválida:
    if (semEnt2 > 0):
        numUtilizadoresEntidade.append(semEnt2)
        newEntidades.append('Inválida')

    indices = arange(len(newEntidades))
    plt.bar(indices, numUtilizadoresEntidade)
    plt.xticks(indices, newEntidades, rotation='vertical')
    plt.title("Distribuição em número por entidade")
    plt.ylabel("Número de utilizadores")
    plt.xlabel("Entidades")
    plt.show()




# ================== Exercicio 8  =================#





##Qual a distribuição em número por nível?
def Exercicio8(nivelutilizador):
    # lista_nivel_entidade=nivel_utilizador(linhas_texto) ## vou buscar a função anterior e guardo a lista de retorno

    ## lista que vou utilizar para colocar: [[nivel,frequencia],...]
    nova_lista = []

    for i in range(0, len(nivelutilizador)):
        nova_lista.append([])
        nova_lista[i].append(nivelutilizador[i][0])  ## nivel
        nova_lista[i].append(len(nivelutilizador[i][1:]))  # frequencia

    return nova_lista


## se quiser imprimir chamo isto
def imprimir5_4(nivel_nomes):
    for i in range(0, len(nivel_nomes)):
        if (nivel_nomes[i][0] == '(Não há nivel)'):

            print('Há omissão de niveis em', nivel_nomes[i][1], ' utilizador/es.')
            print('\n\n')
        elif (nivel_nomes[i][0]=='(Inválido)'):
            print('Há niveis inválidos em', nivel_nomes[i][1],'utilizadores')
            print('\n\n')

        else:
            print("\033[1;31mNivel:\033[m", nivel_nomes[i][0])
            print("\033[1;31mNúmero de utilizadores:\033[m", nivel_nomes[i][1])
            print('\n\n')


## se quiser um plot uso isto
def plot5_4(nova_lista):
    x = []
    y = []
    for i in nova_lista:
        x.append(i[0])
        y.append(i[1])
    print(x)
    print(y)
    plt.figure()
    plt.bar(x, y, width=0.1, align='center')
    plt.xlabel('Nivel')
    plt.ylabel('Frequencia')
    plt.title('Distribuição em número por nível')
    plt.show()





# ================== Exercicio 9  =================#



def Exercicio9(nomes, emails, entidades, niveis, nb, filename):
    numero = 1
    ## lista de chaves para o meu dicionário:
    chave = ['Nome', 'Email', 'Entidade', 'Nivel', 'Numero de chamadas ao backend']

    out_file = open(filename, "w", encoding='utf8')  ## para não desformatar, preciso de gravar em utf8

    out_file.write('{\n')
    ## prencher os dicionários
    for i in range(0, min(len(nomes),20)):

        # atualizar string
        stringJson = ''

        ##dicionário secundário
        secundario = {}

        ## preencher dicionário

        secundario[chave[0]] = nomes[i]
        secundario[chave[1]] = emails[i]
        secundario[chave[2]] = entidades[i]
        secundario[chave[3]] = niveis[i]
        secundario[chave[4]] = nb[i]

        ## Id de identificação de cada utilizador:
        id = 'utilizador' + str(numero)

       

        stringJson = '    ' + id + ': {\n'
        stringJson = stringJson + '        ' + chave[0] + ': ' + secundario[chave[0]] + ',\n'
        stringJson = stringJson + '        ' + chave[1] + ': ' + secundario[chave[1]] + ',\n'
        stringJson = stringJson + '        ' + chave[2] + ': ' + secundario[chave[2]] + ',\n'
        stringJson = stringJson + '        ' + chave[3] + ': ' + secundario[chave[3]] + ',\n'
        stringJson = stringJson + '        ' + chave[4] + ': ' + secundario[chave[4]] + ',\n'
        if (i != 19):
            stringJson = stringJson + '    },\n'
        else:
            stringJson = stringJson + '    }\n'

        out_file.write(stringJson)
        numero = numero + 1

    stringJson = '}\n'
    out_file.write(stringJson)
    out_file.close()






# ================== #### MENU ####  =================#


def menu():
    # abrir ficheiro:
    f = open("teste.txt",encoding='UTF-8')  ##encoding='UTF-8' é a codificação do arquivo, senão dava erro de compilação

    # colocar em listas de linhas
    linhas_texto = f.readlines()  ## texto=['linha1','linha2',....]
    f.close()

    list = cria_estruturas(linhas_texto)  ## listas de nomes,emails,entidades,...
   
    list3 = Exercicio3(list[3], list[0], list[
        1])  # list3[0]=[[niveisl,nomes],[nivel,nomes]..]  e list3[1]=[[email,nomes],[email,nomes],...]

    erro_test = lista_erros(list3[1])
    print('\n\033[1;31mAvisos(casos existam):\033[m')
    # imprimir faltas e inavilidices:
    imprime_nomes_inv_ou_emfalta(list[0])
    imprime_emails_inv_ou_emfalta(list[1])
    imprime_entidades_inv_ou_emfalta(list[2])
    imprime_niveis_inv_ou_emfalta(list[3])
    imprime_nb_inv_ou_emfalta(list[4])

    press = -1
    while press != '0':
        print('\n')
        print('\033[1;31m############\033[m     ')
        print('\033[1;31m### MENU ###\033[m                                                     ')
        print('\033[1;31m############\033[m     ')
        print(
            '\033[1;31m[1]:\033[mProduzir uma listagem apenas com o nome e a entidade do utilizador, ordenada alfabeticamente por nome                                   \033[m')
        print(
            '\033[1;31m[2]:\033[mProduzir uma lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos utilizadores estão registados\033[m')
        print(
            '\033[1;31m[3]:\033[mDistribuição de utilizadores por níveis de acesso                                                                                       \033[m')
        print(
            '\033[1;31m[4]:\033[mProduzir uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta pelo nome                \033[m')
        print(
            '\033[1;31m[5]:\033[mNúmero de utilizadores                                                                                                                  \033[m')
        print(
            '\033[1;31m[6]:\033[mNúmero de entidades                                                                                                                     \033[m')
        print(
            '\033[1;31m[7]:\033[mDistribuição em número por entidade                                                                                                     \033[m')
        print(
            '\033[1;31m[8]:\033[mDistribuição em número por nível                                                                                                        \033[m')
        print(
            '\033[1;31m[9]:\033[mConverter os 20 primeiros registos num ficheiro JSON                                                                                    \033[m')
        print(
            '\033[1;31m[0]:\033[mSair do programa                                                                                                                       ')

        press = (input('Seleciona a opção:'))

        if (press == '1'):
            print('\n' * 100)

            if (len(erro_test) == 0):
                Exercicio1(list[0], list[2])
            else:
                imprimeerros(erro_test)
                print('\n\n')
                Exercicio1(list[0], list[2])

            x = input('Clica em Enter para continuar:')


        elif (press == '2'):
            print('\n' * 100)
            if (len(erro_test) == 0):
                Exercicio2(list[0], list[1], list[2])
            else:
                imprimeerros(erro_test)
                print('\n\n')
                Exercicio2(list[0], list[1], list[2])

            x = input('Clica em Enter para continuar:')
        elif (press == '3'):
            print('\n' * 100)
            if len(erro_test) == 0:
                # só preciso de imprimir, pois a função foi invocada em cima do while
                imprimir_niveis_nomes(list3[0])
            else:
                imprimeerros(erro_test)
                print('\n\n')
                imprimir_niveis_nomes(list3[0])
            x = input('Clica em Enter para continuar:')
        elif (press == '4'):
            print('\n' * 100)
            if (len(erro_test) == 0):
                Exercicio4(list[0], list[2])
            else:
                imprimeerros(erro_test)
                print('\n\n')
                Exercicio4(list[0], list[2])

            x = input('Clica em Enter para continuar:')

        elif (press == '5'):
            print('\n' * 100)

            if (len(erro_test) == 0):
                Exercicio5(list[1], erro_test)
            else:
                imprimeerros(erro_test)
                print('\n\n')
                Exercicio5(list[1], erro_test)

            x = input('Clica em Enter para continuar:')

        elif (press == '6'):
            print('\n' * 100)
            if (len(erro_test) == 0):
                numEnt = Exercicio6(list[2])
                print('\033[1;31mNúmero de entidades:\033[m ', numEnt)
            else:
                imprimeerros(erro_test)
                print('\n\n')
                numEnt = Exercicio6(list[2])
                print('\033[1;31mNúmero de entidades:\033[m ', numEnt)

            x = input('Clica em Enter para continuar:')

        elif (press == '7'):

            print('\n' * 100)
            print('\033[1;31m [1]:\033[mGráfico de barras do número de utilizadores para cada entidade')
            print('\033[1;31m [2]:\033[mListagem das entidades e respetivo número de utilizadores')
            select = (input('Seleciona opção:'))
            if (select == '1'):
                if len(erro_test) == 0:
                    Exercicio7_plot(list[2])
                    print('\n' * 100)

                else:
                    imprimeerros(erro_test)
                    print('\n\n')
                    Exercicio7_plot(list[2])
                    print('\n' * 100)

                x = input('Clica em Enter para continuar:')
            elif (select == '2'):

                if len(erro_test) == 0:
                    print('\n' * 100)
                    Exercicio7_lista(list[2])

                else:
                    print('\n' * 100)
                    imprimeerros(erro_test)
                    print('\n\n')
                    Exercicio7_lista(list[2])

                x = input('Clica em Enter para continuar:')
            else:
                print('\n' * 100)
                print('Opção inválida')
                x = input('Clica em Enter para continuar:')


        elif (press == '8'):

            q_8 = Exercicio8(list3[0])
            print('\n' * 100)
            print('\033[1;31m [1]:\033[mGráfico de barras ')
            print('\033[1;31m [2]:\033[mListagem ')
            select = (input('Seleciona opção:'))
            if (select == '1'):
                if len(erro_test) == 0:
                    plot5_4(q_8)
                    print('\n' * 100)

                else:
                    imprimeerros(erro_test)
                    print('\n\n')
                    plot5_4(q_8)
                    print('\n' * 100)

                x = input('Clica em Enter para continuar:')
            elif (select == '2'):

                if len(erro_test) == 0:
                    print('\n' * 100)
                    imprimir5_4(q_8)

                else:
                    print('\n' * 100)
                    imprimeerros(erro_test)
                    print('\n\n')
                    imprimir5_4(q_8)

                x = input('Clica em Enter para continuar:')
            else:
                print('\n' * 100)
                print('Opção inválida')
                x = input('Clica em Enter para continuar:')
        elif (press == '9'):
            print('\n' * 100)
            file = input('Introduz o nome que pretende dar ao ficheiro JSON:')
            Exercicio9(list[0], list[1], list[2], list[3], list[4], file + '.json')
            x = input('Clica em Enter para continuar:')

        elif (press == '0'):

            print('\n' * 100)

            print('Foi um prazer')


        else:
            print('\n' * 100)
            print('Opção inválida')
            x = input('Clica em Enter para continuar:')


menu()