class player:

    def countId(self):
        arq = open('player.txt')
        count = 0
        for i in arq:
            count += 1
        return count + 1

    def creatPlayer(self):
        r = 'S'
        while r == 'S':
            quantityPlayers = int(
                input('Quantos jogadores você deseja cadastrar? '))
            if quantityPlayers <= (6):
                for i in range(quantityPlayers):
                    self.name = input('\nDigite o nome do jogador: ')
                    self.birthdate = input(
                        'Digite a data de nascimento no formato [dia/mês/ano]: ')
                    self.wheight = input('Digite o peso: ')
                    self.height = input('Digite a altura: ')
                    self.position = input('Digite a posição: ')
                    self.force = input(
                        'Digite a força (baixa, média, forte): ')
                    self.file = open('player.txt', 'a')
                    self.line = f'#{self.countId()}; {self.name}; {self.birthdate}; {self.wheight}; {self.height}; {self.position}; {self.force}\n'
                    self.file.write(self.line)
                    self.file.close()
            else:
                print(
                    'Você só pode cadastrar até 6 jogadores. Por favor tente novamente')

            r = str(input('Deseja fazer um novo cadastro? [S/N]: ')).upper()
            if r == 'Nn':
                print('Cadastro Cancelado')
                break


    def deletePlayerID(self):
        self.playerName = input(
            'Digite o id do jogador que deseja deletar [#num]:')
        self.file = open('player.txt', 'r')
        self.lines = self.file.readlines()
        self.file = open('player.txt', 'w')

        for self.line in self.lines:

            if self.playerID not in self.line.strip('\n'):
                self.file.writelines(self.line)


player = player()
player.creatPlayer()
# player.deletePlayerID()
