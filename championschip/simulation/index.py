from random import shuffle

class simulation:
    def games(self):
        dic = {}
        file = open("clubes.txt")
        lines = file.readlines()
        for line in lines:
            teste = line.split(";")
            dic[teste[0]] = teste
        file.close()
        ordem = []
        for i in dic:
            ordem.append(i)
        shuffle(ordem)
        for i in ordem:
            file = open("championschip.txt", "a")
            line = f'{i}, {dic[i][1]}\n'
            file.writelines(line)
            file.close()
        file = open("championschip.txt")
        lines = file.readlines()
        print(f"""
          ************************
        
        Time vencedor: {lines[0]}
          ************************
        """)
        print("Classificação")
        count = 1
        print("""
# | Clube
        """)
        for line in lines:
            club = line.split(",  ")
            print(f"""{count} | {club[1]}""")
            count += 1
            

    def ranking(self):
        file = open("championschip.txt")
        lines = file.readlines()
        print("Classificação")
        count = 1
        print("""
# | Clube
        """)
        for line in lines:
            club = line.split(",  ")
            print(f"""{count} | {club[1]}""")
            count += 1