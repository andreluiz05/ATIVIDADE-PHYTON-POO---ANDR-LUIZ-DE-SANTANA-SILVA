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


class Caminhao_irado:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f'{self.marca}, e seu modelo {self.modelo}, ano {self.ano}, acelera muito! Ele tem um motor de 16 cilindros. É um veículo com aerodinâmica bem trabalhada - meticulosamente pensada para os apaixonados de velocidade!')

    def freiar(self):
        print(f'{self.marca},e seu modelo {self.modelo}, ano {self.ano}, tem bom freio para freiar, pois utiliza da tecnologia ABS em suas rodas!')

    def andar(self):
        print(f'{self.marca},e seu modelo {self.modelo}, ano {self.ano} anda demais!' )

caminhao = Caminhao_irado('Volvo', 'FH', '2020')
caminhao.acelerar()
caminhao.freiar()
caminhao.andar()

class Moto_irada:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f'{self.marca}, e seu modelo {self.modelo}, ano {self.ano}, acelera demais! Equipada com motor de alta rotação e leveza ideal para agilidade nas ruas e estradas!')

    def freiar(self):
        print(f'{self.marca}, e seu modelo {self.modelo}, ano {self.ano}, tem excelente freio, contando com sistema ABS que garante segurança nas frenagens!')

    def andar(self):
        print(f'{self.marca}, e seu modelo {self.modelo}, ano {self.ano} anda como um foguete!' )

moto = Moto_irada('Honda', 'CB 500F', '2023')
moto.acelerar()
moto.freiar()
moto.andar()
