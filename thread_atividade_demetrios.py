import threading

m1 = [  [16,15,14,13],    
        [12,11,10,9],
        [8,7,6,5],
        [4,3,2,1],

]

m2 = [  [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,13],
     ]


class matriz():
    def __init__(self,mat1,mat2,result):
        self.m1 = mat1
        self.m2 = mat2
        self.rf = result
    
    def validate(self):
        m1=[len(self.m1),len(self.m1[0])]
        m2=[len(self.m2),len(self.m2[0])]
        if m1 == m2 or (m1[0] == m2[1] and m1[1] == m2[0]):
            return 1
        else:
            return 0
    
    
    def division(self):
        l,c=0,0
        if len(self.m1)/2 is not int:
            l =(len(self.m1)/2)-0.5
        else:
            l = len(self.m1)/2
        
        return int(l),int(len(m1[0]))

    
    def main(self):
        validate = int(self.validate())
        if validate == 0:
            return "Matrizes incorrespondentes"
        if validate == 1:
            l,c= self.division()

            thread1= threading.Thread(target=self.matriz_matriz, args=[int(l),int(c),0])
            thread2 = threading.Thread(target=self.matriz_matriz,args=[int(len(self.m1)),int(c),int(l)-1])
            thread1.start()
            thread2.start()
        return self.rf

        
    def matriz_matriz(self,l,c,pi):
        for i in range(l): 
            for j in range(c): 
                for k in range(l): 
                    self.rf[i][j] += self.m1[i][k] * self.m2[k][j] 
            
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
if __name__ == "__main__":
    info = matriz(m1,m2,result)
    print(info.main())