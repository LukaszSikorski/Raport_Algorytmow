from Executor import Executor,ExecutorFasde
from Algorithm import bubleSorting,bubleSortingNoFlag
import copy
import threading
import random

lenList=50000
randRange=(0,10)

lista = [random.randrange(*randRange) for _ in range(lenList)]
fasada1= ExecutorFasde(bubleSortingNoFlag,lista,1)
fasada1.executeProcess()


fasada2= ExecutorFasde(bubleSorting,lista,1)
fasada2.executeProcess()