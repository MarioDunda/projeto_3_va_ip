from random import choice

class simulation:
    def games(self):
        dic = {}
        file = open("clubes.txt")
        lines = file.readlines()
        for line in lines:
            teste = line.split(";")
            dic[teste[0]] = teste
        file.close()
        file = open("championschip.txt", "a")
        for i in dic:
            for jogo in range(2):
                resultado = choice('03')
                line = f'{i, dic[i][1], {resultado}}\n'
                file.write(line)


simulation = simulation()
simulation.games()