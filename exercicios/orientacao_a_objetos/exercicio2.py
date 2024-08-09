from abc import ABC, abstractmethod

class ContaCorrente:
    def __init__(self, cheque_especial, saldo):
        self.__saldo = saldo
        self.__lista_operacoes = []
        self.__cheque_especial = cheque_especial
        self.__lista_operacoes.append(f'Saldo Inicial: {saldo}')

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def lista_operacoes(self):
        return self.__lista_operacoes

    def depositar(self, valor):
        if valor < 0:
            raise ValueError('Valor do depósito não pode ser negativo')
        self.saldo += valor
        self.__lista_operacoes.append(f'Depósito: {valor} --> Saldo: {self.saldo}')
    
    def sacar(self, valor):
        if valor < 0:
            raise ValueError('Valor do saque não pode ser negativo')
        if valor > self.__saldo + self.__cheque_especial:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        self.__lista_operacoes.append(f'Saque: {valor} --> Saldo: {self.saldo}')

    def __str__(self) -> str:
        return f'Saldo: {self.saldo}, Cheque especial: {self.__cheque_especial}\nOperações: \n{self.print_operacoes()}'

    def print_operacoes(self):
        lista_operacoes_formatadas = ''
        i = 1
        for operacao in self.__lista_operacoes:
            lista_operacoes_formatadas += f' {i}. {operacao}\n'
            i += 1
        return lista_operacoes_formatadas


class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self.__telefone = telefone  # Usa o setter para validação
        self.__renda_mensal = renda_mensal  # Usa o setter para validação
        self.__conta = None

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if len(telefone) != 11:
            raise ValueError('Telefone deve ter 11 dígitos (DDD + número)')
        self.__telefone = telefone

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, renda_mensal):
        if renda_mensal < 0:
            raise ValueError('Renda mensal não pode ser negativa')
        self.__renda_mensal = renda_mensal

    @property
    def conta(self):
        return self.__conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @abstractmethod
    def criar_conta(self):
        pass

    def __str__(self) -> str:
        return f'\n=== Nome: {self.nome} ===\nTelefone: {self.telefone} \nRenda mensal: {self.renda_mensal}\nConta:  {self.conta}'


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
    
    def criar_conta(self, saldo=0):
        self.conta = ContaCorrente(self.renda_mensal, saldo)

    def __str__(self) -> str:
        return f'{super().__str__()}\n---> Cliente Mulher, tem direito a cheque especial'


class ClienteHomem(Cliente):  # Corrigido o nome da classe
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
    
    def criar_conta(self, saldo=0):
        self.conta = ContaCorrente(0, saldo)

    def __str__(self) -> str:
        return f'{super().__str__()}---> Cliente Homem, não tem direito a cheque especial'


# Testando o código
cliente = ClienteMulher('Yasmin', '53911112222', 700)
cliente.criar_conta(1000)
cliente.conta.sacar(1700)  # usando o cheque especial
cliente.conta.sacar(0)  # Deve levantar uma exceção: saldo insuficiente
cliente.conta.depositar(50)
print(cliente)


cliente2 = ClienteHomem('Osmar', '51987654321', 1300)
cliente2.criar_conta(1000)
cliente2.conta.depositar(50)
cliente2.conta.depositar(200)
cliente2.conta.sacar(1000)  
cliente2.conta.sacar(10) 
cliente2.conta.depositar(100)
print(cliente2)