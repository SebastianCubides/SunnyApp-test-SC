import matplotlib.pyplot as plt
import numpy

class Graphs:
    def __init__(self,full_array):
        self.full_array = full_array
        self.phi_array = full_array[0]
        self.time = full_array[1]

    def genGraph(self):
        # Datos
        x1 = self.time
        y1 = []
        y2 = []
        i=0
        j=1
        for items in self.phi_array:
            if (i<len(self.phi_array)):
                y1.append(float(self.phi_array[i]))
                i+=2
            else:
                break
        for items in self.phi_array:
            if (j<len(self.phi_array)):
                y2.append(float(self.phi_array[j]))
                j+=2
            else:
                break
        # Gráfico de líneas
        fig, ax = plt.subplots()
        ax.plot(x1, y1, marker = "o", label = "phi Iz vs t")
        ax.plot(x1, y2, marker = "o", label = "phi De vs t")
        ax.legend()
        plt.show()