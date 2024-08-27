
#deposito#
def deposito(saldo):
    print("--------------------Deposito--------------------")
    deposito = float(input("Digite o valor que deseja depositar: "))
    if deposito < 0:
        print("Erro ao realizar deposito, valor nao pode ser negativo. Tente novamente.")
        print("------------------------------------------------")
        print("\n")
        return(saldo)
    else:
        extrato.append(f"{saldo:.2f} + {deposito:.2f} = R${(saldo + deposito):.2f}")
        saldo += deposito
        print(f'Deposito de {deposito:.2f}R$ efetuado com sucesso! Agora voce possui {saldo:.2f}R$ em sua conta.')
        print("------------------------------------------------")
        print("\n")
        return(saldo)
    

#saque#
def sacar(saldo, limite_saque): 
    print("----------------------Saque---------------------")
    valor = float(input("digite o valor que deseja sacar: "))
    if valor > saldo:
        print("Não foi possivel sacar o valor digitado, saldo insuficiente")
        print("------------------------------------------------")
        print("\n")
        return(saldo, limite_saque)
    elif valor > 500:
        print('Limite de saque (500R$) excedido, favor diminuir valor que deseja sacar')
        print("------------------------------------------------")
        print("\n")
        return(saldo, limite_saque)
    elif valor <= saldo:
        extrato.append((f"{saldo:.2f} - {valor:.2f} = R${(saldo - valor):.2f}"))
        saldo -= valor
        print(f'Saque de {valor} realizado com sucesso! Agora voce possui {saldo} R$ em conta.')
        limite_saque += 1
        print("------------------------------------------------")
        print("\n")
        return(saldo, limite_saque)
    
#main#

saldo = 2000.00 
extrato =  []
limite_saque = 0
while 1==1:
    print("--------Bem vindo ao Banco virtual EMSS!--------")
    opcao = int(input('''Escolha a operação que deseja realizar:
    [1] Saque.
    [2] Deposito.
    [3] Extrato.
    [4] Sair do banco.
------------------------------------------------\n'''))
    
    if opcao == 1:
        if limite_saque >= 3:
           print("limite diario de saques alcançado, tentar mais tarde\n\n")
        else:
            (saldo, limite_saque) = sacar(saldo, limite_saque)
            
    elif opcao == 2:
        saldo = deposito(saldo)
        

    elif opcao == 3:
        print("--------------------Extrato---------------------")
        [print(transacao) for transacao in extrato]
        print("------------------------------------------------")
        print("\n")
    elif opcao == 4:
        print("Encerrando aplicativo.")
        break
    else:
        print("Opcao invalida:")    
        
