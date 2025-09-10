class Carro_irado:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f'{self.marca}, e seu modelo {self.modelo}, ano {self.ano}, acelera muito! Ele tem um motor 1.6 e dotado 4 cilindros. É um veículo com aerodinâmica bem trabalhada - meticulosamente pensada para os apaixonados de velocidade!')

    def freiar(self):
        print(f'{self.marca},e seu modelo {self.modelo}, ano {self.ano}, tem bom freio para freiar, pois utiliza da tecnologia ABS em suas rodas!')
        
    def andar(self):
        print(f'{self.marca},e seu modelo {self.modelo}, ano {self.ano} anda demais!' )

carro = Carro_irado('JEEP', 'Renegade', '2015')

carro.acelerar()
carro.freiar()
carro.andar()
