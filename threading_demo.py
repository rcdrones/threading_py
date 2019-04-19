import threading
import time
from queue import Queue

q = Queue()


def Task1():
    print("in to t1")
    
    time.sleep(1)
    
    print("end t1")


def Task2(a):
    print("in to t2 "+ str(a))
    
    

def main():
    print("in main")
    
    t1 = threading.Thread(target = Task1)
    
    
    t2 = threading.Thread(target = Task2,args=(111,))
    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("end main")


def makesquart(aa):
    for i in range(len(aa)):
        aa[i] = aa[i]**2
        
    q.put(aa)

def do_somthing_single():
    
    result = []
    data = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
    for i in range(3):
        makesquart(data[i])
        result.append(q.get())
        
    print(result)

def do_somthing_multi():
    
    result = []
    data = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
    time.sleep(3)
    for i in range(3):
        t = threading.Thread(target = makesquart, args=(data[i],))
        t.start()
    
    for i in range(3):
        result.append(q.get())
        
    print(result)


if __name__ == "__main__":
    do_somthing_multi()
    
    print("end of pro")
    #main()
