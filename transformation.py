import numpy
import math

class Transformation:
    
    def __init__(self,lines):
        self.lines = lines
    
    def Convert(self):
        data_list = []
        phi_array = []
        time = []
        i=0
        for line in self.lines:
            i+=1 
            #
            cline = line.split(",")
            data_list.append(cline)
            t = (data_list[i-1][0])
            theta = float(data_list[i-1][1])
            v = float(data_list[i-1][2])
            w = float(data_list[i-1][3])
            #
            EI = numpy.matmul(numpy.matrix([[math.cos(theta),math.sin(theta)],
                                            [-math.sin(theta),math.cos(theta)],
                                            [0,1]]),numpy.matrix([[v],[w]]))
            #print(EI)
            ER = numpy.matmul(numpy.matrix([[math.cos(theta),-math.sin(theta),0],
                                            [-math.sin(theta),math.cos(theta),0],
                                            [0,0,1]]),EI)
            #print(ER)
            alphaIz = math.pi/2
            betaIz = math.pi
            alphaDe = -math.pi/2
            betaDe = 0
            l = 80 #mm
            rIz = 35#mm
            rDe = 35#mm
            #
            J1 = numpy.matrix([[math.sin(alphaIz+betaIz),-math.cos(alphaIz+betaIz),-l*math.cos(betaIz)],
                            [math.sin(alphaDe+betaDe),-math.cos(alphaDe+betaDe),-l*math.cos(betaDe)]])
            #
            J2Inv = numpy.matrix([[1/rIz,0],[0,1/rDe]])
            #
            #It's important to note that the equation for phi was wrong in the PDF, (J1*ER*J2^-1)
            #It had to be changed for (J2^-1*J1*ER)
            phi = numpy.matmul(numpy.matmul(J2Inv,J1),ER)
            #
            time.append(t)
            j=0
            for row in phi:
                j+=1
                phi_array.append(numpy.array2string(phi[j-1,0]))
            
        #
        phi_array = list(map(lambda s: s.strip(), phi_array))
        return phi_array, time