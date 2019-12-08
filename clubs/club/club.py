class class_club():
    def createClub(self=0):
        name = str(input('Digite o nome do clube: '))
        city = input('Digite o local do clube: ')
        foundationYear = input('Digite o ano de fundação do clube: ')
        mascot = input('Diigite o mascote do clube: ')
        president = input('Digite o nome do presidente do clube: ')
        colors = input('Digite as cores do clube: ')
        manager = input('Digite o nome do técnico do clube: ')
        playersId = input(
            'Digite os IDs dos jogadores no formato [#número,]: ')
        file = open('clubes.txt', 'r')

        count = 0
        for id in file:
            count += 1

        file = open('clubes.txt', 'a')
        line = f'#{count}; {name}; {city}; {foundationYear}; {mascot}; {president}; {colors}; {manager}; {playersId}\n'
        file.write(line)
        print("Clube criado")

    def deleteClubByID(self=0):

        clubID = input(
            'Digite o id do clube que deseja deletar [#num]:')
        file = open('clubes.txt', 'r')
        lines = file.readlines()
        file = open('clubes.txt', 'w')

        for line in lines:

            if clubID not in line.strip('\n'):
                file.writelines(line)
        print("Clube deletado")

    def deleteClubByName(self=0):

        clubName = input(
            'Digite o nome do clube que deseja deletar: ')
        file = open('clubes.txt', 'r')
        lines = file.readlines()
        file = open('clubes.txt', 'w')

        for line in lines:

            if clubName not in line.strip('\n'):
                file.writelines(line)
        print("Clube deletado")

    def updateClubByName(self=0):
        clubName = input(
            'Digite o nome do clube que desaja atualizar')
        file = open('clubes.txt', 'r')
        lines = file.readlines()
        file = open('clubes.txt', 'w')

        for line in lines:

            if clubName not in line.strip('\n'):
                file.writelines(line)
            else:
                name = input('Digite o nome do clube: ')
                city = input('Digite o local do clube: ')
                foundationYear = input(
                    'Digite o ano de fundação do clube: ')
                mascot = input('Diigite o mascote do clube: ')
                president = input(
                    'Digite o nome do presidente do clube: ')
                colors = input('Digite as cores do clube: ')
                manager = input('Digite o nome do técnico do clube: ')
                playersId = input(
                    'Digite os IDs dos jogadores no formato [#número,]: ')
                file = open('clubes.txt', 'r')

                count = 0
                for id in file:
                    count += 1

                file = open('clubes.txt', 'a')
                line = f'#{count}; {name}; {city}; {foundationYear}; {mascot}; {president}; {colors}; {manager}; {playersId}\n'
                file.write(line)
        print("Clube alterado")

    def showClubs(self=0):
        file = open('clubes.txt', 'r')
        lines = file.readlines()
        for line in lines:
            line.split(';')
            print(line)
