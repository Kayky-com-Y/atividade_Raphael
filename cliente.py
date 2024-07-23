from banco import conta
class abrir_banco():
    minha_conta = conta()
    acessar = str("0")
    opçoes = str("0")

    while acessar != "4":
        minha_conta.dizer_nome()
        acessar = str(input(
"""Se você deseja mudar de nome digite [1]
Se você deseja acesar o banco digite [2]
Se você deseja acesar a lista de clientes digite[3]
Se você deseja sair digite [4]

"""))
        if acessar == "1":
            minha_conta.mudar_nome()
            minha_conta.adicionar_lista_de_clientes()
        elif acessar == "2":
            while opçoes != '4':
                opçoes = str(input(
"""Se você deseja assesar sua conta digite [1]
Se você deseja depositar em sua conta digite [2]
Se você deseja retirar de sua conta digite [3]
Se você deseja sair digite [4]

"""))
                if opçoes == '1':
                    minha_conta.dizer_dinheiro()

                elif opçoes == '2':
                    minha_conta.Deposite_dinheiro()

                elif opçoes == '3':
                    minha_conta.retire_dinheiro()

                elif opçoes == '4':
                    acessar == 'n'
               
                else:
                    print(f"{opçoes} não é uma opção valida")
        elif acessar == "3":
            while opçoes != '3':
                opçoes = str(input("""
Se você deseja ver a lista de clientes digite [1]
Se você deseja adicionar o seu nome a lista de clientes digite [2]
Se você deseja sair digite [3]

"""))
                if opçoes == '1':
                    minha_conta.dizer_lista_de_clientes()
                elif opçoes == '2':
                    minha_conta.adicionar_lista_de_clientes()
                elif opçoes == '3':
                    acessar == 'n'
                else:
                    print(f"{opçoes} não é uma opção valida")
        elif acessar == '4':
            print("Volte sempre")
        else:
            print(f"{acessar} não é uma opção valida")

abrir_banco()