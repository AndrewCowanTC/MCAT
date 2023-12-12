# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 07:37:23 2023

@author: Andrew Cowan
"""

class TSRTable:

    def __init__(self,Country):
      self.Country = Country 
        
    def GaugeTable(self):
        if self.Country == "US":
            GaugeTable = [{"Class":6,"GaugeMin":56,"GaugeMax":57.25,"GaugeDelta":0.75},
                          {"Class":7,"GaugeMin":56,"GaugeMax":57.25,"GaugeDelta":0.5},
                          {"Class":8,"GaugeMin":56,"GaugeMax":57.25,"GaugeDelta":0.5},
                          {"Class":9,"GaugeMin":56.25,"GaugeMax":57.25,"GaugeDelta":0.5},
                          #Class 5 and Below
                          {"Class":1,"GaugeMin":56,"GaugeMax":58,"GaugeDelta":0},
                          {"Class":2,"GaugeMin":56,"GaugeMax":57.75,"GaugeDelta":0},
                          {"Class":3,"GaugeMin":56,"GaugeMax":57.75,"GaugeDelta":0},
                          {"Class":4,"GaugeMin":56,"GaugeMax":57.5,"GaugeDelta":0},
                          {"Class":5,"GaugeMin":56,"GaugeMax":57.5,"GaugeDelta":0}]
        else: #Canadian Class 5 and Below
            GaugeTable = [{"Class":1,"GaugeMin":55.75,"GaugeMax":58,"GaugeDelta":0},
                          {"Class":2,"GaugeMin":55.75,"GaugeMax":57.75,"GaugeDelta":0},
                          {"Class":3,"GaugeMin":56,"GaugeMax":57.75,"GaugeDelta":0},
                          {"Class":4,"GaugeMin":56,"GaugeMax":57.5,"GaugeDelta":0},
                          {"Class":5,"GaugeMin":56,"GaugeMax":57.5,"GaugeDelta":0}]
        
        return GaugeTable
        
    def AlinementRepeatTable(self):
        
        AlinementRepeatTable = [{"Class":6,"Chord":31,"Tolerance":0.375},
                                {"Class":6,"Chord":62,"Tolerance":0.5},
                                {"Class":6,"Chord":124,"Tolerance":1},
                                {"Class":7,"Chord":31,"Tolerance":0.375},
                                {"Class":7,"Chord":62,"Tolerance":0.375},
                                {"Class":7,"Chord":124,"Tolerance":0.875},
                                {"Class":8,"Chord":31,"Tolerance":0.375},
                                {"Class":8,"Chord":62,"Tolerance":0.375},
                                {"Class":8,"Chord":124,"Tolerance":0.5},
                                {"Class":9,"Chord":31,"Tolerance":0.375},
                                {"Class":9,"Chord":62,"Tolerance":0.375},
                                {"Class":9,"Chord":124,"Tolerance":0.5}]
        
        return AlinementRepeatTable
        
    def AlinementTable(self):
        
        if self.Country == "US":
            AlinementTable = [{"Class":6,"TrackType":"Tangent","Chord":31,"Tolerance":0.5,"Cant":0},
                              {"Class":6,"TrackType":"Tangent","Chord":62,"Tolerance":0.75,"Cant":0},
                              {"Class":6,"TrackType":"Tangent","Chord":124,"Tolerance":1.5,"Cant":0},
                              {"Class":7,"TrackType":"Tangent","Chord":31,"Tolerance":0.5,"Cant":0},
                              {"Class":7,"TrackType":"Tangent","Chord":62,"Tolerance":0.75,"Cant":0},
                              {"Class":7,"TrackType":"Tangent","Chord":124,"Tolerance":1.25,"Cant":0},
                              {"Class":8,"TrackType":"Tangent","Chord":31,"Tolerance":0.5,"Cant":0},
                              {"Class":8,"TrackType":"Tangent","Chord":62,"Tolerance":0.75,"Cant":0},
                              {"Class":8,"TrackType":"Tangent","Chord":124,"Tolerance":1,"Cant":0},
                              {"Class":9,"TrackType":"Tangent","Chord":31,"Tolerance":0.5,"Cant":0},
                              {"Class":9,"TrackType":"Tangent","Chord":62,"Tolerance":0.5,"Cant":0},
                              {"Class":9,"TrackType":"Tangent","Chord":124,"Tolerance":0.75,"Cant":0},
                              {"Class":6,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":6,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":3},
                              {"Class":6,"TrackType":"Curved","Chord":124,"Tolerance":1.5,"Cant":3},
                              {"Class":7,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":7,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":3},
                              {"Class":7,"TrackType":"Curved","Chord":124,"Tolerance":1.25,"Cant":3},
                              {"Class":8,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":8,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":3},
                              {"Class":8,"TrackType":"Curved","Chord":124,"Tolerance":0.75,"Cant":3},
                              {"Class":9,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":9,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":3},
                              {"Class":9,"TrackType":"Curved","Chord":124,"Tolerance":0.75,"Cant":3},
                              {"Class":6,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":6,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":5},
                              {"Class":6,"TrackType":"Curved","Chord":124,"Tolerance":1.25,"Cant":5},
                              {"Class":7,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":7,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":5},
                              {"Class":7,"TrackType":"Curved","Chord":124,"Tolerance":1,"Cant":5},
                              {"Class":8,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":8,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":5},
                              {"Class":8,"TrackType":"Curved","Chord":124,"Tolerance":0.75,"Cant":5},
                              {"Class":9,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":9,"TrackType":"Curved","Chord":62,"Tolerance":0.5,"Cant":5},
                              {"Class":9,"TrackType":"Curved","Chord":124,"Tolerance":0.75,"Cant":5},
                              #Class 5 and Below
                              {"Class":1,"TrackType":"Tangent","Chord":31,"Tolerance":5,"Cant":0},
                              {"Class":2,"TrackType":"Tangent","Chord":31,"Tolerance":3,"Cant":0},
                              {"Class":3,"TrackType":"Tangent","Chord":31,"Tolerance":1.75,"Cant":0},
                              {"Class":4,"TrackType":"Tangent","Chord":31,"Tolerance":1.25,"Cant":0},
                              {"Class":5,"TrackType":"Tangent","Chord":31,"Tolerance":0.75,"Cant":0},
                              {"Class":1,"TrackType":"Tangent","Chord":62,"Tolerance":5,"Cant":0},
                              {"Class":2,"TrackType":"Tangent","Chord":62,"Tolerance":3,"Cant":0},
                              {"Class":3,"TrackType":"Tangent","Chord":62,"Tolerance":1.75,"Cant":0},
                              {"Class":4,"TrackType":"Tangent","Chord":62,"Tolerance":1.25,"Cant":0},
                              {"Class":5,"TrackType":"Tangent","Chord":62,"Tolerance":0.75,"Cant":0},
                              {"Class":1,"TrackType":"Curved","Chord":31,"Tolerance":5,"Cant":3},
                              {"Class":2,"TrackType":"Curved","Chord":31,"Tolerance":3,"Cant":3},
                              {"Class":3,"TrackType":"Curved","Chord":31,"Tolerance":1.25,"Cant":3},
                              {"Class":4,"TrackType":"Curved","Chord":31,"Tolerance":1,"Cant":3},
                              {"Class":5,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":1,"TrackType":"Curved","Chord":62,"Tolerance":5,"Cant":3},
                              {"Class":2,"TrackType":"Curved","Chord":62,"Tolerance":3,"Cant":3},
                              {"Class":3,"TrackType":"Curved","Chord":62,"Tolerance":1.75,"Cant":3},
                              {"Class":4,"TrackType":"Curved","Chord":62,"Tolerance":1.5,"Cant":3},
                              {"Class":5,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":3},
                              {"Class":1,"TrackType":"Curved","Chord":31,"Tolerance":1.25,"Cant":5},
                              {"Class":2,"TrackType":"Curved","Chord":31,"Tolerance":1.25,"Cant":5},
                              {"Class":3,"TrackType":"Curved","Chord":31,"Tolerance":0.75,"Cant":5},
                              {"Class":4,"TrackType":"Curved","Chord":31,"Tolerance":0.75,"Cant":5},
                              {"Class":5,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":1,"TrackType":"Curved","Chord":62,"Tolerance":1.25,"Cant":5},
                              {"Class":2,"TrackType":"Curved","Chord":62,"Tolerance":1.25,"Cant":5},
                              {"Class":3,"TrackType":"Curved","Chord":62,"Tolerance":1.25,"Cant":5},
                              {"Class":4,"TrackType":"Curved","Chord":62,"Tolerance":0.875,"Cant":5},
                              {"Class":5,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":5}]
        else: #Canadian Class 5 and Below
            AlinementTable = [{"Class":1,"TrackType":"Tangent","Chord":31,"Tolerance":5,"Cant":0},
                              {"Class":2,"TrackType":"Tangent","Chord":31,"Tolerance":3,"Cant":0},
                              {"Class":3,"TrackType":"Tangent","Chord":31,"Tolerance":1.75,"Cant":0},
                              {"Class":4,"TrackType":"Tangent","Chord":31,"Tolerance":1.5,"Cant":0},
                              {"Class":5,"TrackType":"Tangent","Chord":31,"Tolerance":0.75,"Cant":0},
                              {"Class":1,"TrackType":"Tangent","Chord":62,"Tolerance":5,"Cant":0},
                              {"Class":2,"TrackType":"Tangent","Chord":62,"Tolerance":3,"Cant":0},
                              {"Class":3,"TrackType":"Tangent","Chord":62,"Tolerance":1.75,"Cant":0},
                              {"Class":4,"TrackType":"Tangent","Chord":62,"Tolerance":1.5,"Cant":0},
                              {"Class":5,"TrackType":"Tangent","Chord":62,"Tolerance":0.75,"Cant":0},
                              {"Class":1,"TrackType":"Curved","Chord":31,"Tolerance":5,"Cant":3},
                              {"Class":2,"TrackType":"Curved","Chord":31,"Tolerance":3,"Cant":3},
                              {"Class":3,"TrackType":"Curved","Chord":31,"Tolerance":1.25,"Cant":3},
                              {"Class":4,"TrackType":"Curved","Chord":31,"Tolerance":1,"Cant":3},
                              {"Class":5,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":3},
                              {"Class":1,"TrackType":"Curved","Chord":62,"Tolerance":5,"Cant":3},
                              {"Class":2,"TrackType":"Curved","Chord":62,"Tolerance":3,"Cant":3},
                              {"Class":3,"TrackType":"Curved","Chord":62,"Tolerance":1.75,"Cant":3},
                              {"Class":4,"TrackType":"Curved","Chord":62,"Tolerance":1.5,"Cant":3},
                              {"Class":5,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":3},
                              {"Class":1,"TrackType":"Curved","Chord":31,"Tolerance":5,"Cant":5},
                              {"Class":2,"TrackType":"Curved","Chord":31,"Tolerance":3,"Cant":5},
                              {"Class":3,"TrackType":"Curved","Chord":31,"Tolerance":1.25,"Cant":5},
                              {"Class":4,"TrackType":"Curved","Chord":31,"Tolerance":1,"Cant":5},
                              {"Class":5,"TrackType":"Curved","Chord":31,"Tolerance":0.5,"Cant":5},
                              {"Class":1,"TrackType":"Curved","Chord":62,"Tolerance":5,"Cant":5},
                              {"Class":2,"TrackType":"Curved","Chord":62,"Tolerance":3,"Cant":5},
                              {"Class":3,"TrackType":"Curved","Chord":62,"Tolerance":1.75,"Cant":5},
                              {"Class":4,"TrackType":"Curved","Chord":62,"Tolerance":1.5,"Cant":5},
                              {"Class":5,"TrackType":"Curved","Chord":62,"Tolerance":0.625,"Cant":5}]        
        return AlinementTable
        
    def SurfaceRepeatTable(self):
        
        SurfaceRepeatTable = [{"Class":6,"Chord":31,"Tolerance":0.75},
                              {"Class":6,"Chord":62,"Tolerance":0.75},
                              {"Class":6,"Chord":124,"Tolerance":1.25},
                              {"Class":7,"Chord":31,"Tolerance":0.75},
                              {"Class":7,"Chord":62,"Tolerance":0.75},
                              {"Class":7,"Chord":124,"Tolerance":1},
                              {"Class":8,"Chord":31,"Tolerance":0.5},
                              {"Class":8,"Chord":62,"Tolerance":0.75},
                              {"Class":8,"Chord":124,"Tolerance":0.875},
                              {"Class":9,"Chord":31,"Tolerance":0.375},
                              {"Class":9,"Chord":62,"Tolerance":0.5},
                              {"Class":9,"Chord":124,"Tolerance":0.625}]
        
        return SurfaceRepeatTable
    
    def SurfaceTable(self):
        if self.Country == "US":
            SurfaceTable = [{"Class":6,"Chord":31,"Tolerance":1,"Cant":0},
                            {"Class":6,"Chord":62,"Tolerance":1,"Cant":0},
                            {"Class":6,"Chord":124,"Tolerance":1.75,"Cant":0},
                            {"Class":7,"Chord":31,"Tolerance":1,"Cant":0},
                            {"Class":7,"Chord":62,"Tolerance":1,"Cant":0},
                            {"Class":7,"Chord":124,"Tolerance":1.5,"Cant":0},
                            {"Class":8,"Chord":31,"Tolerance":0.75,"Cant":0},
                            {"Class":8,"Chord":62,"Tolerance":1,"Cant":0},
                            {"Class":8,"Chord":124,"Tolerance":1.25,"Cant":0},
                            {"Class":9,"Chord":31,"Tolerance":0.5,"Cant":0},
                            {"Class":9,"Chord":62,"Tolerance":0.75,"Cant":0},
                            {"Class":9,"Chord":124,"Tolerance":1,"Cant":0},
                            {"Class":6,"Chord":31,"Tolerance":1,"Cant":3},
                            {"Class":6,"Chord":62,"Tolerance":1,"Cant":3},
                            {"Class":6,"Chord":124,"Tolerance":1.75,"Cant":3},
                            {"Class":7,"Chord":31,"Tolerance":1,"Cant":3},
                            {"Class":7,"Chord":62,"Tolerance":1,"Cant":3},
                            {"Class":7,"Chord":124,"Tolerance":1.5,"Cant":3},
                            {"Class":8,"Chord":31,"Tolerance":0.75,"Cant":3},
                            {"Class":8,"Chord":62,"Tolerance":1,"Cant":3},
                            {"Class":8,"Chord":124,"Tolerance":1.25,"Cant":3},
                            {"Class":9,"Chord":31,"Tolerance":0.5,"Cant":3},
                            {"Class":9,"Chord":62,"Tolerance":0.75,"Cant":3},
                            {"Class":9,"Chord":124,"Tolerance":1,"Cant":3},
                            {"Class":6,"Chord":31,"Tolerance":1,"Cant":5},
                            {"Class":6,"Chord":62,"Tolerance":1,"Cant":5},
                            {"Class":6,"Chord":124,"Tolerance":1.5,"Cant":5},
                            {"Class":7,"Chord":31,"Tolerance":1,"Cant":5},
                            {"Class":7,"Chord":62,"Tolerance":1,"Cant":5},
                            {"Class":7,"Chord":124,"Tolerance":1.25,"Cant":5},
                            {"Class":8,"Chord":31,"Tolerance":0.75,"Cant":5},
                            {"Class":8,"Chord":62,"Tolerance":1,"Cant":5},
                            {"Class":8,"Chord":124,"Tolerance":1.25,"Cant":5},
                            {"Class":9,"Chord":31,"Tolerance":0.5,"Cant":5},
                            {"Class":9,"Chord":62,"Tolerance":0.75,"Cant":5},
                            {"Class":9,"Chord":124,"Tolerance":1,"Cant":5},
                            #Class 5 and Below
                            {"Class":1,"Chord":31,"Tolerance":3,"Cant":0},
                            {"Class":2,"Chord":31,"Tolerance":2.75,"Cant":0},
                            {"Class":3,"Chord":31,"Tolerance":2.25,"Cant":0},
                            {"Class":4,"Chord":31,"Tolerance":2,"Cant":0},
                            {"Class":5,"Chord":31,"Tolerance":1.25,"Cant":0},
                            {"Class":1,"Chord":62,"Tolerance":3,"Cant":0},
                            {"Class":2,"Chord":62,"Tolerance":2.75,"Cant":0},
                            {"Class":3,"Chord":62,"Tolerance":2.25,"Cant":0},
                            {"Class":4,"Chord":62,"Tolerance":2,"Cant":0},
                            {"Class":5,"Chord":62,"Tolerance":1.25,"Cant":0},
                            {"Class":1,"Chord":31,"Tolerance":3,"Cant":3},
                            {"Class":2,"Chord":31,"Tolerance":2.75,"Cant":3},
                            {"Class":3,"Chord":31,"Tolerance":2.25,"Cant":3},
                            {"Class":4,"Chord":31,"Tolerance":2,"Cant":3},
                            {"Class":5,"Chord":31,"Tolerance":1.25,"Cant":3},
                            {"Class":1,"Chord":62,"Tolerance":3,"Cant":3},
                            {"Class":2,"Chord":62,"Tolerance":2.75,"Cant":3},
                            {"Class":3,"Chord":62,"Tolerance":2.25,"Cant":3},
                            {"Class":4,"Chord":62,"Tolerance":2,"Cant":3},
                            {"Class":5,"Chord":62,"Tolerance":1.25,"Cant":3},
                            {"Class":1,"Chord":31,"Tolerance":2.25,"Cant":5},
                            {"Class":2,"Chord":31,"Tolerance":2.25,"Cant":5},
                            {"Class":3,"Chord":31,"Tolerance":1,"Cant":5},
                            {"Class":4,"Chord":31,"Tolerance":1,"Cant":5},
                            {"Class":5,"Chord":31,"Tolerance":1,"Cant":5},
                            {"Class":1,"Chord":62,"Tolerance":2.25,"Cant":5},
                            {"Class":2,"Chord":62,"Tolerance":2.25,"Cant":5},
                            {"Class":3,"Chord":62,"Tolerance":1.75,"Cant":5},
                            {"Class":4,"Chord":62,"Tolerance":1.25,"Cant":5},
                            {"Class":5,"Chord":62,"Tolerance":1,"Cant":5}]
        else: #Canadian Class 5 and Below
            SurfaceTable = [{"Class":1,"Chord":31,"Tolerance":3,"Cant":0},
                            {"Class":2,"Chord":31,"Tolerance":2.75,"Cant":0},
                            {"Class":3,"Chord":31,"Tolerance":2.25,"Cant":0},
                            {"Class":4,"Chord":31,"Tolerance":2,"Cant":0},
                            {"Class":5,"Chord":31,"Tolerance":1.25,"Cant":0},
                            {"Class":1,"Chord":62,"Tolerance":3,"Cant":0},
                            {"Class":2,"Chord":62,"Tolerance":2.75,"Cant":0},
                            {"Class":3,"Chord":62,"Tolerance":2.25,"Cant":0},
                            {"Class":4,"Chord":62,"Tolerance":2,"Cant":0},
                            {"Class":5,"Chord":62,"Tolerance":1.25,"Cant":0},
                            {"Class":1,"Chord":31,"Tolerance":3,"Cant":3},
                            {"Class":2,"Chord":31,"Tolerance":2.75,"Cant":3},
                            {"Class":3,"Chord":31,"Tolerance":2.25,"Cant":3},
                            {"Class":4,"Chord":31,"Tolerance":2,"Cant":3},
                            {"Class":5,"Chord":31,"Tolerance":1.25,"Cant":3},
                            {"Class":1,"Chord":62,"Tolerance":3,"Cant":3},
                            {"Class":2,"Chord":62,"Tolerance":2.75,"Cant":3},
                            {"Class":3,"Chord":62,"Tolerance":2.25,"Cant":3},
                            {"Class":4,"Chord":62,"Tolerance":2,"Cant":3},
                            {"Class":5,"Chord":62,"Tolerance":1.25,"Cant":3},
                            {"Class":1,"Chord":31,"Tolerance":3,"Cant":5},
                            {"Class":2,"Chord":31,"Tolerance":2.75,"Cant":5},
                            {"Class":3,"Chord":31,"Tolerance":2.25,"Cant":5},
                            {"Class":4,"Chord":31,"Tolerance":2,"Cant":5},
                            {"Class":5,"Chord":31,"Tolerance":1.25,"Cant":5},
                            {"Class":1,"Chord":62,"Tolerance":3,"Cant":5},
                            {"Class":2,"Chord":62,"Tolerance":2.75,"Cant":5},
                            {"Class":3,"Chord":62,"Tolerance":2.25,"Cant":5},
                            {"Class":4,"Chord":62,"Tolerance":2,"Cant":5},
                            {"Class":5,"Chord":62,"Tolerance":1.25,"Cant":5}]
        
        return SurfaceTable
    
    def WarpTable(self):
        
        if self.Country == "US":
            WarpTable = [{"Class":6,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":7,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":8,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":9,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":6,"TrackType":"Curved","Tolerance":1.5,"Cant":3},
                         {"Class":7,"TrackType":"Curved","Tolerance":1.5,"Cant":3},
                         {"Class":8,"TrackType":"Curved","Tolerance":1.25,"Cant":3},
                         {"Class":9,"TrackType":"Curved","Tolerance":1,"Cant":3},
                         {"Class":6,"TrackType":"Curved","Tolerance":1.5,"Cant":5},
                         {"Class":7,"TrackType":"Curved","Tolerance":1.5,"Cant":5},
                         {"Class":8,"TrackType":"Curved","Tolerance":1.25,"Cant":5},
                         {"Class":9,"TrackType":"Curved","Tolerance":1,"Cant":5},
                         #Class 5 and Below
                         {"Class":1,"TrackType":"Tangent","Tolerance":3,"Cant":0},
                         {"Class":2,"TrackType":"Tangent","Tolerance":2,"Cant":0},
                         {"Class":3,"TrackType":"Tangent","Tolerance":1.75,"Cant":0},
                         {"Class":4,"TrackType":"Tangent","Tolerance":1.25,"Cant":0},
                         {"Class":5,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":1,"TrackType":"Curved","Tolerance":3,"Cant":3},
                         {"Class":2,"TrackType":"Curved","Tolerance":2.25,"Cant":3},
                         {"Class":3,"TrackType":"Curved","Tolerance":2,"Cant":3},
                         {"Class":4,"TrackType":"Curved","Tolerance":1.75,"Cant":3},
                         {"Class":5,"TrackType":"Curved","Tolerance":1.5,"Cant":3},
                         {"Class":1,"TrackType":"Curved","Tolerance":3,"Cant":5},
                         {"Class":2,"TrackType":"Curved","Tolerance":2.25,"Cant":5},
                         {"Class":3,"TrackType":"Curved","Tolerance":2,"Cant":5},
                         {"Class":4,"TrackType":"Curved","Tolerance":1.75,"Cant":5},
                         {"Class":5,"TrackType":"Curved","Tolerance":1.5,"Cant":5},
                         {"Class":1,"TrackType":"Curved","Tolerance":1.5,"Cant":6},
                         {"Class":2,"TrackType":"Curved","Tolerance":1.5,"Cant":6},
                         {"Class":3,"TrackType":"Curved","Tolerance":1.5,"Cant":6},
                         {"Class":4,"TrackType":"Curved","Tolerance":1.5,"Cant":6},
                         {"Class":5,"TrackType":"Curved","Tolerance":1.5,"Cant":6}]
        else:
            WarpTable = [{"Class":1,"TrackType":"Tangent","Tolerance":3,"Cant":0},
                         {"Class":2,"TrackType":"Tangent","Tolerance":2,"Cant":0},
                         {"Class":3,"TrackType":"Tangent","Tolerance":1.75,"Cant":0},
                         {"Class":4,"TrackType":"Tangent","Tolerance":1.25,"Cant":0},
                         {"Class":5,"TrackType":"Tangent","Tolerance":1,"Cant":0},
                         {"Class":1,"TrackType":"Curved","Tolerance":3,"Cant":3},
                         {"Class":2,"TrackType":"Curved","Tolerance":2.25,"Cant":3},
                         {"Class":3,"TrackType":"Curved","Tolerance":2,"Cant":3},
                         {"Class":4,"TrackType":"Curved","Tolerance":1.75,"Cant":3},
                         {"Class":5,"TrackType":"Curved","Tolerance":1.5,"Cant":3},
                         {"Class":1,"TrackType":"Curved","Tolerance":3,"Cant":5},
                         {"Class":2,"TrackType":"Curved","Tolerance":2.25,"Cant":5},
                         {"Class":3,"TrackType":"Curved","Tolerance":2,"Cant":5},
                         {"Class":4,"TrackType":"Curved","Tolerance":1.75,"Cant":5},
                         {"Class":5,"TrackType":"Curved","Tolerance":1.5,"Cant":5}]        
        return WarpTable
        
        