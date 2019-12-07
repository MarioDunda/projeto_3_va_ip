class manager:
    def creatManager(self):
        self.name = input('Digite o nome do técnico: ')
        self.arq  = open('maneger.txt','r')
 
        self.count = 0
        for self.id in self.arq:
            self.count += 1
        self.file = open('maneger.txt', 'a')
        self.line = f'#{self.count+1};{self.name}\n'
        self.file.write(self.line)
manager = manager()
manager.creatManager()
class player:
  
    def creatPlayer(self):
        self.name = input('Digite o nome do jogador: ')
        self.birthdate = input('Digite a data de nascimento no formato [dia/mês/ano]: ')
        self.wheight = input('Digite o peso: ')
        self.height = input('Digite a altura: ')
        self.position = input('Digite a posição: ')
        self.force = input('Digite a força (baixa, média, forte): ')
        self.arq = open('player.txt', 'r')
        self.count = 0
        for self.id in self.arq:
            self.count += 1        
        self.file = open('player.txt', 'a')
        self.line = f'#{self.count+1}; {self.name}; {self.birthdate}; {self.wheight}; {self.height}; {self.position}; {self.force}\n'
        self.file.write(self.line)
player = player()
player.creatPlayer()

class club:
    def creatClub(self):
        self.name = input('Adicione um novo clube: ')
        self.arq = open('club.txt', 'r')

        self.count = 0
        for self.id in self.arq:
            self.count += 1
        self.file = open('club.txt', 'a')
        self.line = f'#{self.count+1}; {self.name}\n'
        self.file.write(self.line)

club = club()
club.creatClub()