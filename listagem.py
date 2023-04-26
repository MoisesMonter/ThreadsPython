import threading
import time

class info():
    def __init__(str,vet):
        str.vet=vet
        str.val=0


    def run(self):
        thread1= threading.Thread(target=self.percorrer_lista, args=[self.vet[:7],self.val,"Trhead1"])
        thread2= threading.Thread(target=self.percorrer_lista, args=[self.vet[7:13],self.val,"Trhead2"])
        thread1.start()
        thread2.start()

        return self.val
    def percorrer_lista(self,lista,val,nucleo):
        
        for posi in range(0,len(self.vet)-1,1):
            self.val +=self.vet[posi]
            print(nucleo,'= ',self.val)


lista = [13,12,11,10,9,8,7,6,5,4,3,2,1,0]


if __name__ == "__main__":
    x = info(lista).run()
    print(x)