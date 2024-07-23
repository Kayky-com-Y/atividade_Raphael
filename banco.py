class conta ():
    _lista_clientes = ["Fulano"]
    nome_cliente = str("Fulano")
    __dinheiro = float(0)
    def dizer_nome(self):
        print(f"""
    ===========================================
        O nome do cliente é {self.nome_cliente}
    ===========================================
    """)
    def mudar_nome(self):
        self.nome_cliente = str(input("Escreva o novo nome do cliente: "))
        return self.nome_cliente
    
    def dizer_lista_de_clientes(self):
        for cliente in self._lista_clientes:
            print(f"Cliente: {cliente}")
            
    def adicionar_lista_de_clientes(self):
        return self._lista_clientes.append(self.nome_cliente)
        
    def dizer_dinheiro(self):
        return print(f"Vc tem {self.__dinheiro} no banco")

    def Deposite_dinheiro(self):
        depositar = float(input("Deposite R$: "))
        self.__dinheiro += depositar
        return self.__dinheiro
    
    def retire_dinheiro(self):
        retirar = float(input("Retire R$: "))
        self.__dinheiro -= retirar
        return self.__dinheiro