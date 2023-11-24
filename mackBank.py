Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
import re

def menu(): # Função Menu e todas as variáveis que serão usadas

    opcao = 0
    opcaoSair = None
    cadastrado = False
    voltarMenu = True
    bloqueado = False
    lista = []
    extrato = [
        ["Movimentações", "Saldo Atual", "Limite Atual"]
    ]
    def sair(): # Função Sair usada após o término das funções de cada opção no Menu
        opcaoSair = int(input("DESEJA VOLTAR AO MENU? \n 1 - VOLTAR AO MENU \n 2 - Sair \n"))
        if opcaoSair == 1:
            voltarMenu = True

        elif opcaoSair == 2:
            voltarMenu = False

        else:
            print("VALOR INVÁLIDO, VOLTANDO AO MENU")
            voltarMenu = True
        return voltarMenu

    while cadastrado == False: # Caso o usuário não tenha se cadastrado, mostrar apenas a opção 1
        print("MACK BANK - ESCOLHA UMA OPÇÃO")
        print("(1) - CADASTRAR CONTA CORRENTE")
        print("Crie sua conta para liberar as outras opções")
        opcao = int(input("SUA OPÇÃO: "))
        if opcao == 1:
            lista, cadastrado = cadastro()
        else:
            print("CRIE SUA CONTA PARA LIBERAR AS OUTRAS OPÇÕES ")


    while voltarMenu == True or bloqueado == False: #Após o cadastro mostrar opções do menu

        print(f"Seja Bem-Vindo, {lista[1]}")
        print("(2) - DEPOSITAR ")
        print("(3) - SACAR ")
        print("(4) - CONSULTAR SALDO ")
        print("(5) - CONSULTAR EXTRATO ")
        print("(6) - Investimentos ")
        print("(7) - SAIR ")
        opcao = int(input("ESCOLHA SUA OPÇÃO: ")) #Após escolher a opção levar a respectiva função
        if opcao == 2:
            deposito(lista,extrato)
            voltarMenu = sair()
        elif opcao == 3:
            lista, bloqueado = saque(lista,extrato)
            voltarMenu = sair()
        elif opcao == 4:
            lista, bloqueado = saldo(lista)
            voltarMenu = sair()
        elif opcao == 5:
            lista, bloqueado = tabela(lista,extrato)
            voltarMenu = sair()
        elif opcao == 6:
            investimentos(lista)
            sair()
        elif opcao == 7: #Caso selecione 7 saia da função retornando None
            return None
        else:
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")


def verificaSenha(senha, cliente): #Função para criação e verificação se as duas senhas criadas são iguais
        repitaSenha = input("REPITA A SENHA: ")
        senhaTeste = senha.upper()
        repitaTeste = repitaSenha.upper()
        while senhaTeste != repitaTeste: #Comparação da senha digitada com a armazenada
            print("AS SENHAS NÃO SÃO IGUAIS, DIGITE NOVAMENTE")
            repitaSenha = input("REPITA A SENHA: ")
            repitaTeste = repitaSenha.upper()
        cliente.append(senha)
        cadastrado = True
        print("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU \n\n\n\n")
        input()
        return cadastrado

def cadastro(): #Função de Cadastro de Conta
    cadastrado = False
    cliente = []
    numConta = random.randint(1000,9999)
    cliente.append(numConta)
    print(f"NÚMERO DA CONTA: {numConta}")
    nome = input("NOME DO CLIENTE: ")
    verificaNome = nome.isnumeric()
    if nome != '' and verificaNome == False:
        cliente.append(nome)
    else:
        while nome == '' or verificaNome == True:
            print("NOME INVÁLIDO , POR FAVOR DIGITE NOVAMENTE")
            nome = input("NOME DO CLIENTE: ")
            verificaNome = nome.isnumeric()
            if nome != '' and verificaNome == False:
                cliente.append(nome)

    telefone = input("TELEFONE: ")
    telefone.replace(" ","")
    verificaTel = telefone.isnumeric()
    if telefone != '' and verificaTel == True:
        cliente.append(telefone)
    else:
        while telefone == '' or verificaTel == False:
            print("TELEFONE INVÁLIDO, POR FAVOR DIGITE SEU TELEFONE")
            telefone = input("TELEFONE: ")
            telefone.replace(" ","")
            verificaTel = telefone.isnumeric()
            if telefone != '' and verificaTel == True:
                cliente.append(telefone)

    email = input("EMAIL: ")
    testeArroba = email.find("@")

    
    if email != '' and testeArroba > 3:
        cliente.append(email)
    else:
        while email == '' or testeArroba < 3:
            print("EMAIL DIGITADO EM BRANCO, POR FAVOR DIGITE SEU E-MAIL ")
            email = input("EMAIL: ")
            testeArroba = email.find("@")

            if email != '' and testeArroba > 3:
                cliente.append(email)


    saldoInicio = float(input("SALDO INICIAL: "))
    if saldoInicio >= 1000:
        cliente.append(saldoInicio)
    else:
        while saldoInicio < 1000.00:
            print("O SEU SALDO INICIAL DEVERÁ SER MAIOR QUE 1.000,00 REAIS")
            saldoInicio = float(input("SALDO INICIAL: "))
            if saldoInicio >= 1000.00:
                cliente.append(saldoInicio)
    limite = float(input("LIMITE DE CRÉDITO: "))
    if limite >= 0:
        cliente.append(limite)
    else:
        while limite < 0:
            print("LIMITES NEGATIVOS SÃO CONSIDERADOS INVÁLIDOS, POR FAVOR DIGITE NOVAMENTE")
            limite = float(input("LIMITE DE CRÉDITO: "))
            if limite >= 0:
                cliente.append(limite)
    senha = input("SENHA:" )
    caracter = len(senha)
    if caracter != 6: #definição da senha que obrigatoriamente deverá ter 6 digitos
        while caracter != 6:
            print("SUA SENHA NÃO TEM 6 CARACTERES, POR FAVOR DIGITE NOVAMENTE")
            senha = input("SENHA: ")
            if len(senha) == 6:
                cadastrado = verificaSenha(senha, cliente)
                return cliente, cadastrado #retorna o valor da função cadastrado que se for True vai liberar as outras opções do menu
    else:
        cadastrado = verificaSenha(senha, cliente)
        return cliente, cadastrado


def deposito(lista,extrato): #Função de Depósito
    print("\n\n\n\nMACK BANK - DEPÓSITO NA CONTA")
    numConta = int(input("INFORME O NÚMERO DE SUA CONTA: "))
    while numConta != lista[0]:
        print("NUMERO DE CONTA DIGITADO NÃO CONDIZ COM O CADASTRADO")
        numConta = int(input("DIGITE NOVAMENTE O NÚMERO DA CONTA: "))

    print(f"NOME DO CLIENTE: {lista[1]}")
    deposito = float(input("VALOR DO DEPÓSITO: "))
    while deposito <= 0:
        print("VALOR DE DEPÓSITO INVÁLIDO Digite novamente")
        deposito = float(input("VALOR DO DEPÓSITO: "))

    lista[4] = lista[4] + deposito #no indice 4 da lista será somado ao valor atual o valor do depósito
    saldoAtual = lista[4]
    limiteAtual = lista[5]
    extrato.append(["+ R$ {}".format(deposito), "R$ {}".format(saldoAtual), "R$ {}".format(limiteAtual)])
    print("\n\nDEPOSITO REALIZADO COM SUCESSO\n\n")

    return lista

def saque(lista,extrato):
    print("\n\n\n\nMACK BANK - SAQUE DA CONTA")
    bloqueado = verifica(lista) #Bloqueado recebe o retorno da função verifica que realiza a verificação de senha diferente da comparação de senhas no inicio

    if bloqueado == False:

        saque = float(input("VALOR DE SAQUE: "))
        while saque <= 0:
            print("VALOR INVÁLIDO PARA SAQUE DIGITE NOVAMENTE")
            saque = float(input("VALOR DO SAQUE "))
        saldoAtual = lista[4]
        limite = lista[5]
        if saldoAtual >= saque:
            print("SAQUE FEITO COM SUCESSO \n")
            lista[4] = lista[4] - saque
            saldoAtual = lista[4]
            limiteAtual = lista[5]
            extrato.append(["- R$ {}".format(saque), "R$ {}".format(saldoAtual), "R$ {}".format(limiteAtual)])
            return lista, bloqueado
        else:
            if limite >= saque: #Se  o limite for maior ou igual ao saque o valor será descontato do limite
                print("VOCÊ ESTÁ USANDO SEU LIMITE DE CRÉDITO")
                lista[4] = lista[4] - saque
                lista[5] = lista[5] - saque
                return lista, bloqueado
            else:
                print("SAQUE RECUSADO - SEM SALDO E LIMITE DISPONÍVEL PARA EFETUAR O SAQUE")
                return lista, bloqueado
    else:
        return lista,bloqueado

def saldo(lista): #Função de consulta de saldo através da leitura do indice 4 da lista
    print("\n\n\n\nMACK BANK - CONSULTA SALDO")
    bloqueado = verifica(lista)
    if bloqueado == False:

        saldoAtual = lista[4]
        limiteAtual = lista[5]
        print(f"SALDO EM CONTA: R$ {saldoAtual}")
        print(f"LIMITE DE CRÉDITO: R$ {limiteAtual}")
        return lista, bloqueado
    else:
        return lista,bloqueado

def tabela (lista,extrato): #Função de extrato que será apresentada com uma matriz 
    print("\n\n\n\nMACK BANK - EXTRATO DA CONTA ")
    bloqueado = verifica(lista)
    if bloqueado == False:
        print("\n\nHISTÓRICO DE CONTA - EXTRATO BANCÁRIO\n")
        linhas = len(extrato)
        for i in range(0,linhas):
            for j in range(0,3):
                print("{:<15}".format(extrato[i][j].strip()), end="   ")
            print("\n")
        return lista, bloqueado
    else:
        return lista,bloqueado

def investimentos(lista): #Função da calculadora de investimentos a função Extra do programa
    print("\n\n\nSeja bem vindo ao MACK INVEST - A sua nova plataforma de projeção de investimentos ")
    bloqueado = verifica(lista) #Verificação de segurança para entrar
    opcao = 0
    if bloqueado == False:
        while opcao <= 0 or opcao >=3:

            print("MENU -- Escolha a modalidade de investimentos\n")
            print("1 - Calculadora de Rendimentos")
            opcao = int(input("ESCOLHA SUA OPÇÃO: "))
        if opcao == 1:
            calculadora() #Roda a função calculadora
            return lista,bloqueado

    else:
        return lista, bloqueado





def calculadora(): #Função calculadora de investimentos
    mensal = float(input("Aporte Mensal: ")) # Quanto de aportes mentais?
    taxaMensal = float(input("Taxa ao Ano: ")) #Qual a taxa anual do seu investimento?
    taxaMensal = (taxaMensal / 100) / 12  #Conversão da taxa anual para mensal
    tempo = int(input("Tempo em Anos: ")) #Quantos anos você quer deixar investindo?
    tempo = tempo * 12 #conversão do tempo de anos para meses
    atual = float(input("Aporte Inicial: ")) #Quanto de aporte inicial você vai dar?
    
    while tempo < 1:
        print("OBRIGATORIAMENTE O INVESTIMENTO DEVE SER MAIOR OU IGUAL A 1 ANO")
        tempo = int(input("Tempo em Anos: "))

    valores = []
    inicial = atual
    juros = mensal * tempo
    mesesAno = []
    for meses in range(1, tempo+1):
        atual += mensal
        atual *= (1 + taxaMensal)
        if meses % 4 == 0:
            valores.append(round(atual, 2))
            mesesAno.append(meses)

    totalInvestido = inicial + juros
    juros = atual - (inicial + juros)

    print("Total Investido: R$ {:.2f}".format(totalInvestido))
    print("Ganho em juros: R$ {:.2f}".format(juros))  
    return None

def verifica(lista): #Função de verificação de segurança usada em todos as operações importantes do código
    numConta = int(input("INFORME O NÚMERO DE SUA CONTA: "))
    while numConta != lista[0]:
        print("NUMERO DE CONTA DIGITADO NÃO CONDIZ COM O     CADASTRADO")
        numConta = int(input("DIGITE NOVAMENTE O NÚMERO DA CONTA: "))

    print(f"NOME DO CLIENTE: {lista[1]}")
    senha = input("INFORME SUA SENHA: ")
    bloqueado = False
    cont = 3
    while senha != lista[6]:
        print(f"SENHA ERRADA, VOCÊ AINDA TEM {cont} TENTATIVAS ANTES DO BLOQUEIO")
        senha = input("INFORME SUA SENHA: ")
        cont-=1
        if cont == 0:
            print("SUA CONTA ESTÁ BLOQUEADA POR ERRO DE SENHA \n ENTRE EM CONTATO CONOSCO PARA O DESBLOQUEIO")
            bloqueado = True
            return lista, bloqueado
    return bloqueado
menu()
print("\n\nObrigado por utilizar nosso sistema :) ")
print("Projeto Desenvolvido por Ruan Lima Silva - 32385633")
exit()
