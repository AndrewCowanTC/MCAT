# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:23:27 2023

@author: Andrew Cowan
"""

import ToleranceTables

class MCAT_Class:
    
    def __init__(self,Class,Chord,Gauge,Cant,Country):
        self.Cant = Cant
        self.Gauge = Gauge
        self.Chord = Chord
        self.Class = Class
        self.Country = Country
        self.Table = ToleranceTables.TSRTable(self.Country)
        
        if self.Cant > 5:
            self.HighCant = True
            self.Cant = 5
        else:
            self.HighCant = False
        
        self.GaugeTable = self.Table.GaugeTable()
        self.AlinementTable = self.Table.AlinementTable()
        self.SurfaceTable = self.Table.SurfaceTable()
        self.WarpTable = self.Table.WarpTable()
        
        self.GaugeMax = self.SearchTable(self.GaugeTable,"GaugeMax","Class",self.Class)
        self.GaugeMin = self.SearchTable(self.GaugeTable,"GaugeMin","Class",self.Class)
        self.GaugeDelta = self.SearchTable(self.GaugeTable,"GaugeDelta","Class",self.Class)
        self.Alinement = self.SearchTable(self.AlinementTable,"Tolerance","Class",self.Class,"Chord",self.Chord,"Cant",self.Cant)
        self.Surface = self.SearchTable(self.SurfaceTable,"Tolerance","Class",self.Class,"Chord",self.Chord,"Cant",self.Cant)
        self.Warp = self.SearchTable(self.WarpTable,"Tolerance","Class",self.Class,"Cant",self.Cant)
    
    def SearchTable(self,Table,Request,Searchable1,Condition1,Searchable2=None,Condition2=None,Searchable3=None,Condition3=None):
        
        for Dict in Table:
            if Dict[Searchable1] == Condition1:
                if Searchable2 == None:
                    return Dict.get(Request)
                elif Dict[Searchable2] == Condition2:
                    if Searchable3 == None:
                        return Dict.get(Request)
                    elif Dict[Searchable3] == Condition3:
                        return Dict.get(Request)
                    
    def a2(self):
        #Gauge narrowing
        if self.Class >= 6:
            if self.Chord == 31 and self.Gauge - self.GaugeMin > self.GaugeDelta:
                a2 = self.GaugeDelta
            else:
                a2 = self.Gauge - self.GaugeMin   
            if a2 > self.Alinement:
                a2 = self.Alinement
            return a2
        else: #Class 5 (US/CA) and below calculations
            if self.Gauge - self.GaugeMin > self.Alinement:
                return self.Alinement
            else:
               return self.Gauge - self.GaugeMin
            
    def a3(self):
        #a3 - Gauge Widdening
        
        if self.Class >= 6:
            if self.Chord == 31 and self.GaugeMax - self.Gauge > self.GaugeDelta:
                a3 = self.GaugeDelta
            else:
                a3 = self.GaugeMax - self.Gauge
            if self.GaugeMax - self.Gauge > self.Alinement:
                a3 = self.Alinement
            return a3
        else: #Class 5 and below calculations
            if self.GaugeMax - self.Gauge > self.Alinement:
                return self.Alinement
            else:
               return self.GaugeMax - self.Gauge
    
    def a4(self):
        #a4 - Repeated Alinement
        if self.Class >= 6:
            AlinementRepeatTable = self.Table.AlinementRepeatTable()
            return self.SearchTable(AlinementRepeatTable,"Tolerance","Class",self.Class,"Chord",self.Chord)
        else: #Class 5 --- NOTE: Alignment tolerance applied downwards across N/A
            return self.Alinement
        
    def a5(self):
        #a5 - Single Alinement
        AlinementTable = self.Table.AlinementTable()
        
        return self.SearchTable(AlinementTable,"Tolerance","Class",self.Class,"Chord",self.Chord,"Cant",self.Cant)
    
    def a6(self):
        #a6 - Single Alinement
        if self.Class >=6:
            if self.Alinement + self.Gauge > self.GaugeMax:
                a6 = self.Gauge + self.Alinement - self.GaugeMax
            else:
                a6 = 0
            if self.Chord == 31 and self.Alinement > self.GaugeDelta and self.Alinement-self.GaugeDelta > a6:
                a6 = self.Alinement-self.GaugeDelta
            return a6
        else:
            if self.Alinement + self.Gauge > self.GaugeMax:
                return self.Gauge + self.Alinement - self.GaugeMax
            else:
                return 0
    
    def a9(self):
        #a9 - Repeated Surface
        if self.Class >= 6:
            SurfaceRepeatTable = self.Table.SurfaceRepeatTable()
            return self.SearchTable(SurfaceRepeatTable,"Tolerance","Class",self.Class,"Chord",self.Chord)
        else:
            return self.SearchTable(self.SurfaceTable,"Tolerance","Class",self.Class,"Chord",self.Chord,"Cant",self.Cant)
        
    def a10(self):
        #a10 - Single Surface
        return self.SearchTable(self.SurfaceTable,"Tolerance","Class",self.Class,"Chord",self.Chord,"Cant",self.Cant)
    
    def a11(self):
        #a11 - Single Surface
        if self.Class >= 6:
            if self.Surface > self.Warp and self.Chord <= 62:
                a11 = self.Surface - self.Warp
            else:
                a11 = 0
            return a11
        else:
            Cant = 6 if self.HighCant else self.Cant
            Warp = self.SearchTable(self.WarpTable,"Tolerance","Class",self.Class,"Cant",Cant)
            if self.Surface > Warp and self.Chord <= 62:
                a11 = self.Surface - Warp
            else:
                a11 = 0
            return a11
    
    def a7(self):
        if self.Class == 9 or self.HighCant:
            a7 = (2/3)*self.a5()
            return a7
        else:
            return None
    
    def a8(self):
        if self.Class == 9 or self.HighCant:
            if self.a6() > 0:
                a8 = self.a7() - (self.a5() - self.a6())
                if a8>0:
                    return a8
                else:
                    return 0
            else:
                return 0
        else:
            return None
        
    def a13(self):
        if self.Class == 9 or self.HighCant:
            a13 = (2/3)*self.a10()
            return a13
        else:
            return None
        

