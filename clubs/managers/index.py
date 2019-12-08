class manager:
    def creatManager(self=0):
        name = input('Digite o nome do técnico: ')
        arq  = open('maneger.txt','r')
 
        count = 0
        for id in arq:
            count += 1
        file = open('maneger.txt', 'a')
        line = f'#{count+1};{name}\n'
        file.write(line)
