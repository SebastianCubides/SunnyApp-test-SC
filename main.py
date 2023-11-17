from data import DataImport
from transformation import Transformation
from results import Results
from graph import Graphs
from threading import Thread
import time

class CustomThread(Thread):
    
    def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,**self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def main():

    startT = time.perf_counter()
    read_data = DataImport()
    data = read_data.getData()
    convert_data = Transformation(data)
    #converted_data = convert_data.Convert()
    t1 = CustomThread(target=convert_data.Convert)
    t1.start()
    results_data  = Results(t1.join())
    graphics = Graphs(t1.join())
    final_data = results_data.setResults()
    print(final_data)

    finishT = time.perf_counter()
    print(f'Finished in {round(finishT-startT,2)} seconds')

    graphics.genGraph()

if __name__ == "__main__":
    main()