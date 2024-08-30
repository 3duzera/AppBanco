def menu():
    menu = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair
    => """
    return int(input(menu))

def depositar(saldo, extrato, /):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n")
            print("Deposito realizado com Sucesso!".center(41, " "))

        else:
            print("\n")
            print("Operação falhou! O valor informado é inválido.". center(41, " "))
        return saldo, extrato

def sacar(*, saldo, extrato, numero_saques, limite_saques, limite):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n")
            print("Operação falhou! Você não tem saldo suficiente.". center(41, " "))

        elif excedeu_limite:
            print("\n")
            print("Operação falhou! O valor do saque excede o limite.". center(41, " "))

        elif excedeu_saques:
            print("\n")
            print("Operação falhou! Número máximo de saques excedido.". center(41, " "))

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n")
            print("Saque realizado com Sucesso!".center(41, " "))

        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

def exibir_extrato(saldo,/, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente números): ")
     usuario = verificar_usuario(cpf, usuarios)

     if usuario:
          print("\n")
          print("Erro! CPF já está cadastrado.". center(41, " "))
          return
    
     nome = input("Informe nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/ sigla estado): ")

     usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
     print("\n")
     print("Usuário cadastrado com Sucesso!". center(41, " "))
     

def verificar_usuario(cpf, usuarios):
     for usuario in usuarios:
         if cpf == usuario["cpf"]:
              return True
         else:
              return False
             
def criar_conta(agencia, numero_conta, contas, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = vincular_usuario_conta(cpf, usuarios)

     if usuario == None:
          print("\n")
          print("Erro! Usuário não encontrado.". center(41, " "))
          return
     conta_usuario = verificar_conta_usuario(usuario, contas)
     if conta_usuario:
        print("\n")
        print("Erro! Usuário já possui uma conta.". center(41, " "))
        return
    
     numero_conta = len(contas) + 1
     contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
     print("\n")
     print("Conta criada com Sucesso!". center(41, " "))


def vincular_usuario_conta(cpf, usuarios):
     for usuario in usuarios: 
          if cpf == usuario["cpf"]:
            return usuario["nome"]
     return None    
               

def verificar_conta_usuario(usuario, contas):
     for conta in contas:
          if usuario == conta["usuario"]:
               return True
          else:
               return False

def listar_contas(contas):
     for conta in contas:
          print(conta["agencia"], conta["numero_conta"], conta["usuario"])
          
def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    contas = []
    usuarios = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    boas_vindas = "Bem Vindo ao Banco EMSS"
    print("==========================================")
    print(boas_vindas.center(41, " "))
    print("==========================================")


    while True:

        opcao = menu()

        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 2:
            saldo, extrato, numero_saques = sacar(saldo=saldo, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, limite=limite, extrato=extrato)

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
             global numero_conta 
             numero_conta = len(contas) + 1
             criar_conta(AGENCIA, numero_conta, contas, usuarios)

        elif opcao == 5:
             listar_contas(contas)

        elif opcao == 6:
             criar_usuario(usuarios)

        elif opcao == 7:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
