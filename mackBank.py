import random


''' 

Lista Cliente - Índices 

0 - Número Conta
1 - Nome
2 - Telefone
3 - Email
4 - Saldo Inícial
5 - Limite de Crédito
6 - Senha 



aaaa
'''
def menu():
    
    opcao = 0
    opcaoSair = None
    cadastrado = False
    voltarMenu = True
    bloqueado = False
    lista = []
    extrato = [
        ["Movimentações", "Saldo Atual", "Limite Atual"]
    ]
    def sair():
        opcaoSair = int(input("DESEJA VOLTAR AO MENU? \n 1 - VOLTAR AO MENU \n 2 - Sair \n"))
        if opcaoSair == 1:
            voltarMenu = True
            
        elif opcaoSair == 2:
            voltarMenu = False
            
        else:
            print("VALOR INVÁLIDO, VOLTANDO AO MENU")
            voltarMenu = True
        return voltarMenu
    
    while cadastrado == False:
        print("MACK BANK - ESCOLHA UMA OPÇÃO")
        print("(1) - CADASTRAR CONTA CORRENTE")
        print("Crie sua conta para liberar as outras opções")
        opcao = int(input("SUA OPÇÃO: "))
        if opcao == 1:
            lista, cadastrado = cadastro()
        else:
            print("CRIE SUA CONTA PARA LIBERAR AS OUTRAS OPÇÕES ")

            
    while voltarMenu == True or bloqueado == False:
    
        print(f"Seja Bem-Vindo, {lista[1]}")
        print("(2) - DEPOSITAR ")
        print("(3) - SACAR ")
        print("(4) - CONSULTAR SALDO ")
        print("(5) - CONSULTAR EXTRATO ")
        print("(6) - Investimentos ")
        print("(7) - SAIR ")
        opcao = int(input("ESCOLHA SUA OPÇÃO: "))
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
            return None
        elif opcao == 7:
            return None
        else:
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")



def cadastro():
    def verificaSenha(senha):
        repitaSenha = input("REPITA A SENHA: ")
        senhaTeste = senha.upper()
        repitaTeste = repitaSenha.upper()
        while senhaTeste != repitaSenha:
            print("AS SENHAS NÃO SÃO IGUAIS, DIGITE NOVAMENTE")
            repitaSenha = input("REPITA A SENHA: ")
            senhaTeste = senha.upper()
            repitaTeste = repitaSenha.upper()
        cliente.append(senha)
        cadastrado = True
        print("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU \n\n\n\n")
        input()
        return cadastrado

    cadastrado = False
    cliente = []
    numConta = random.randint(1000,9999)
    cliente.append(numConta)
    print(f"NÚMERO DA CONTA: {numConta}")
    nome = input("NOME DO CLIENTE: ")
    if nome != '':
        cliente.append(nome)
    else:
        while nome == '':
            print("NOME DIGITADO EM BRANCO, POR FAVOR DIGITE SEU NOME")
            nome = input("NOME DO CLIENTE: ")
            if nome != '':
                cliente.append(nome)
    telefone = input("TELEFONE: ")
    if telefone != '':
        cliente.append(telefone)
    else:
        while telefone == '':
            print("TELEFONE DIGITADO EM BRANCO, POR FAVOR DIGITE SEU TELEFONE")
            telefone = input("TELEFONE")
            if telefone != '':
                cliente.append(telefone)
    email = input("EMAIL: ")
    if telefone != '':
        cliente.append(email)
    else:
        while email == '':
            print("EMAIL DIGITADO EM BRANCO, POR FAVOR DIGITE SEU E-MAIL ")
            email = input("EMAIL: ")
            if email != '':
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
    if caracter != 6:
        while caracter != 6:
            print("SUA SENHA NÃO TEM 6 CARACTERES, POR FAVOR DIGITE NOVAMENTE")
            senha = input("SENHA: ")
            if len(senha) == 6:
                cadastrado = verificaSenha(senha)
                return cliente, cadastrado
    else:
        cadastrado = verificaSenha(senha)
        return cliente, cadastrado


def deposito(lista,extrato):
    print("\n\n\n\nMACK BANK - DEPÓSITO NA CONTA")
    numConta = int(input("INFORME O NÚMERO DE SUA CONTA: "))
    while numConta != lista[0]:
        print("NUMERO DE CONTA DIGITADO NÃO CONDIZ COM O CADASTRADO")
        numConta = int(input("DIGITE NOVAMENTE O NÚMERO DA CONTA: "))

    print(f"NOME DO CLIENTE: {lista[1]}")
    deposito = float(input("VALOR DO DEPÓSITO: "))
    lista[4] = lista[4] + deposito
    saldoAtual = lista[4]
    limiteAtual = lista[5]
    extrato.append(["+ R$ {}".format(deposito), "R$ {}".format(saldoAtual), "R$ {}".format(limiteAtual)])
    print("\n\nDEPOSITO REALIZADO COM SUCESSO\n\n")

    return lista

def saque(lista,extrato):
    print("\n\n\n\nMACK BANK - SAQUE DA CONTA")
    bloqueado = verifica(lista) 

    if bloqueado == False:

        saque = float(input("VALOR DE SAQUE: "))
        while saque < 0:
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
            if limite >= saque:
                print("VOCÊ ESTÁ USANDO SEU LIMITE DE CRÉDITO")
                lista[4] = lista[4] - saque
                lista[5] = lista[5] - saque
                return lista, bloqueado
            else:
                print("SAQUE RECUSADO - SEM SALDO E LIMITE DISPONÍVEL PARA EFETUAR O SAQUE")
                return lista, bloqueado
    else:
        return lista,bloqueado

def saldo(lista):
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

def tabela (lista,extrato):
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

def investimentos(lista):
    print("\n\n\nSeja bem vindo ao MACK INVEST - A sua nova plataforma de projeção de investimentos ")
    bloqueado = verifica(lista)
    opcao = None
    if bloqueado == False:
        while opcao <= 0 or opcao >=3:

            print("MENU -- Escolha a modalidade de investimentos\n")
            print("1 - Renda Fixa")
            print("2 - Fundos de investimentos ")
            print("3 - Calculadora de Rendimentos")
            opcao = int(input("ESCOLHA SUA OPÇÃO: "))
        if opcao == 1:
            rendaFixa(lista)

    else:
        return lista, bloqueado


def rendaFixa(lista):
    print("teste")

def fundos(lista):
    print("Teste")

def calculadora(lista):
    

def verifica(lista):
    numConta = int(input("INFORME O NÚMERO DE SUA CONTA: "))
    while numConta != lista[0]:
        print("NUMERO DE CONTA DIGITADO NÃO CONDIZ COM O CADASTRADO")
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