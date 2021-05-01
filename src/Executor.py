import time
import threading
import multiprocessing
import copy

class Executor:
    def __init__(self,algorithm,data: list):
        self.algorithm = algorithm
        self.data = copy.deepcopy(data)
        self.deltaTime:float=float()
        
    def execute(self):
        start= time.perf_counter()
        result= self.algorithm(self.data)
        end= time.perf_counter()
        self.deltaTime = end - start

class ExecutorFasde:
    def __init__(self,algorithm,data:list,repeats:int):
        self.executors = [Executor(algorithm,data) for _ in range(repeats)]
        self.repeats:int = int(repeats)
        
    def executeThread(self):
        threads=  []
        for e in self.executors:
            threads.append(threading.Thread(target=e.execute))
            
        start= time.perf_counter()
        for t in threads:
            t.start()
        for t in threads:
            t.join()     
        end= time.perf_counter()
        deltaTime= end - start
        print('Thread ',deltaTime)
            
    def executeProcess(self):
        threads=  []
        for e in self.executors:
            threads.append(multiprocessing.Process(target=e.execute))
        start= time.perf_counter()
        for t in threads:
            t.start()
        for t in threads:
            t.join()          
        end= time.perf_counter()
        deltaTime= end - start
        print('Process ',deltaTime)