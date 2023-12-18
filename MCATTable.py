# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:01:43 2023

@author: Andrew Cowan
"""


import MCAT_File
from tabulate import tabulate

class MCATTable:
    
    def __init__(self):
        self.Cants = [6]
        self.Gauges = [56.5,57]
        self.Chords = [31,62]
        self.Classes = [3,4,5]
        self.Country = "US"
        
        
    def GenerateTable(self):
        
        for el in self.Cants:
            for g in self.Gauges:
                if el == 0 and g == 57 and self.Country == "US": continue
                for ch in self.Chords:
                    Parameters = self.PrintTableSetup()
                    Headers = [""]
                    for c in self.Classes:

                        # print("Gauge: ",g," Class: ",c," Chord: ",ch," Cant: ",el)
                        Headers.append("Class: "+str(c))
                        MCAT = MCAT_File.MCAT_Class(c,ch,g,el,self.Country)
                        Parameters[0].append(MCAT.a2())
                        Parameters[1].append(MCAT.a3())
                        Parameters[2].append(MCAT.a4())
                        Parameters[3].append(MCAT.a5())
                        Parameters[4].append(MCAT.a6())
                        Parameters[5].append(MCAT.a7())
                        Parameters[6].append(MCAT.a8())
                        Parameters[7].append(MCAT.a9())
                        Parameters[8].append(MCAT.a10())
                        Parameters[9].append(MCAT.a11())
                        Parameters[10].append(MCAT.a13())
                        
                    self.PrettyPrint(Parameters,c,ch,g,el,Headers)
    
    def PrintTableSetup(self):
        
        Parameters = []
        for i in range(12):
            if i != 10:
                Parameters.append([["a"+str(i+2)]])

        return Parameters
    
    def PrettyPrint(self,Parameters,Class,Chord,Gauge,Cant,Headers):
        
        print("Gauge: ",Gauge," Chord: ",Chord," Cant: ",Cant)
        print(tabulate(Parameters, tablefmt="grid",headers = Headers))

if __name__ == "__main__":
    Table = MCATTable()
    Table.GenerateTable()