class Results:
    def __init__(self,full_array):
        self.full_array = full_array
        self.phi_array = full_array[0]
        self.time = full_array[1]

    def setResults(self):
        i=0
        k=0
        with open('results.txt', 'w') as f:
            f.writelines("t,phi Iz,phi De\n")
            Count=1
            for line in self.phi_array:
                i+=1
                if(i<=len(self.phi_array) and (Count-1)%2==0):
                    f.writelines(self.time[k])
                    k+=1
                    f.writelines(",")
                f.writelines(self.phi_array[i-1])
                if(Count%2!=0):
                    f.writelines(",")
                else:
                    f.writelines("\n")
                Count+=1    
        return "Completed Succesfully"
