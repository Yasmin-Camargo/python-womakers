'''
Crie uma classe que modele o objeto "carro".
Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
Crie uma instância da classe carro.
Faça o carro "andar" utilizando os métodos da sua classe.
Faça o carro "parar" utilizando os métodos da sua classe.
'''

class Carro:
    def __init__(self, ligado, cor, modelo, velocidade):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def liga(self):
        self.ligado = True
        print('\nCarro ligado')
    
    def desliga(self):
        self.ligado = False
        self.velocidade = 0
        print('\nCarro desligado')
    
    def acelera(self):
        if self.ligado and self.velocidade < 200:
            self.velocidade += 10
            print('\nCarro acelerando')
            print(f'Velocidade atual: {self.velocidade}')
        elif not self.ligado:
            print('\nCarro desligado. Não é possível acelerar')
    
    def desacelera(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
            print('\nCarro desacelerando')
            print(f'Velocidade atual: {self.velocidade}')
        elif not self.ligado:
            print('\nCarro desligado. Não é possível desacelerar')
    
    def __str__(self) -> str:
        return f'\n\nMeu Carro: \n- ligado: {self.ligado} \n- cor: {self.cor} \n- modelo: {self.modelo} \n- velocidade: {self.velocidade}'


carro = Carro(False, 'amarelo', 'siena', 0)
print(carro)
carro.acelera()
carro.liga()

for _ in range(3):
    carro.acelera()

for _ in range(5):
    carro.desacelera()

carro.desliga()
print(carro)