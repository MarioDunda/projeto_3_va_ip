class club:

    def createClub(self):
        
        self.name = input('Digite o nome do clube: ')
        self.city = input('Digite o local do clube: ')
        self.foundationYear = input('Digite o ano de fundação do clube: ')
        self.mascot = input('Diigite o mascote do clube: ')     
        self.president = input('Digite o nome do presidente do clube: ')
        self.colors = input('Digite as cores do clube: ')
        self.manager = input('Digite o nome do técnico do clube: ')
        self.playersId = input('Digite os IDs dos jogadores no formato [#número,]: ')
        self.file = open('clubes.txt', 'r')
            
        self.count = 0
        for self.id in self.file:
            self.count += 1

        self.file = open('clubes.txt', 'a')
        self.line = f'#{self.count}; {self.name}; {self.city}; {self.foundationYear}; {self.mascot}, {self.president}; {self.colors}; {self.manager}; {self.playersId} \n'
        self.file.write(self.line)

club = club()
club.createClub()

