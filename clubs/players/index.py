class player:
    def countId(self):
        arq = open('player.txt')
        count = 0
        for i in arq:
            count += 1
        return count + 1

    def createPlayer(self=0):
        r = 'S'
        while r == 'S':
            quantityPlayers = int(
                input('Quantos jogadores você deseja cadastrar? '))
            if quantityPlayers <= (6):
                for i in range(quantityPlayers):
                    name = input('\nDigite o nome do jogador: ')
                    birthdate = input(
                        'Digite a data de nascimento no formato [dia/mês/ano]: ')
                    wheight = input('Digite o peso: ')
                    height = input('Digite a altura: ')
                    position = input('Digite a posição: ')
                    force = input(
                        'Digite a força (baixa, média, forte): ')
                    file = open('player.txt', 'a')
                    line = f'#{countId()}; {name}; {birthdate}; {wheight}; {height}; {position}; {force}\n'
                    file.write(line)
                    file.close()
            else:
                print(
                    'Você só pode cadastrar até 6 jogadores. Por favor tente novamente')

            r = str(input('Deseja fazer um novo cadastro? [S/N]: ')).upper()
            if r == 'Nn':
                print('Cadastro Cancelado')
                break

    def deletePlayerID(self=0):
        playerName = input(
            'Digite o id do jogador que deseja deletar [#num]:')
        file = open('player.txt', 'r')
        lines = file.readlines()
        file = open('player.txt', 'w')

        for line in lines:

            if playerID not in line.strip('\n'):
                file.writelines(line)
