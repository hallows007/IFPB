# Create a player with health and mana based on the selected class and display the status.

class joagador:
    def __init__(self,nome,classe):
        if classe == 'guerreiro':
            self.vida = 150
        elif classe == 'mago':
            self.vida = 100

        if classe == 'guerreiro':
            self.mana = 100
        elif classe == 'mago':
            self.mana = 200
        self.nome = nome

    def mostrar_status(self):
        print(f"{self.nome}, você possui {self.vida} de vida e {self.mana} de mana")

usuario = input('Digite o seu nome de usuario: ')
mostrando_classe = print('Existe duas classes: guerreiro e mago')
classe = input('Digite a classe que você ira jogar: ')



jogador1 = joagador(usuario,classe)

jogador1.mostrar_status()