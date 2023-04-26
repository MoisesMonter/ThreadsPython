import random
class MatrizCalc():

    def __init__(self):
        self.m1 = []
        self.m2 = []
        self.create=False
        self.vf = []
    
    def criarmatriz(self,l,c):
        linha=[]
        coluna=[]
        for x in range(l):
            coluna=[random.randint(0,100) for x in range(c)]
            linha.append(coluna)
            coluna=[]
            if self.create == False:
                coluna=[0 for x in range(c)]
                self.vf.append(coluna)
                coluna=[]
        self.create = True
        return linha




    def main(self):
        l=4
        c=4
        self.m1 = self.criarmatriz(l,c)
        print(self.m1,'\n')
        self.m2 = self.criarmatriz(l,c)
        print(self.m2,'\n')
        print(self.vf,'\n')

        for i in range(l): 
            for j in range(c): 
                for k in range(l): 
                    self.vf[i][j] += self.m1[i][k] * self.m2[k][j] 
        print(self.vf)
if __name__ == "__main__":
    info = MatrizCalc()
    info.main()
