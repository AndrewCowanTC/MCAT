# MCAT
This code allows for the calculation of the Minimally Compliant Analytical Track (MCAT) amplitude parameters for US/CA.
The MCATTable.py file must be modified to include the appropriate Country, Gauges, Chords, and Classes.  Valid examples are as follows:

CFR 213 Appendix D Table 4:
        self.Cants = [0]
        self.Gauges = [56.5]
        self.Chords = [31,62,124]
        self.Classes = [6,7,8,9]
        self.Country = "US"

CFR 213 Appendix D Table 5:
        self.Cants = [3]
        self.Gauges = [56.5,57]
        self.Chords = [31,62,124]
        self.Classes = [6,7,8,9]
        self.Country = "US"

CFR 213 Appendix D Table 6:
        self.Cants = [5]
        self.Gauges = [56.5,57]
        self.Chords = [31,62,124]
        self.Classes = [6,7,8,9]
        self.Country = "US"

CFR 213 Appendix D Table 7:
        self.Cants = [6]
        self.Gauges = [56.5,57]
        self.Chords = [31,62]
        self.Classes = [1,2,3,4,5]
        self.Country = "US"

CFR 238 Appendix C Table  4:
        self.Cants = [0]
        self.Gauges = [56.5]
        self.Chords = [31,62]
        self.Classes = [2,3,4,5]
        self.Country = "US"

CFR 238 Appendix C Table  5:
        self.Cants = [3]
        self.Gauges = [56.5,57]
        self.Chords = [31,62]
        self.Classes = [2,3,4,5]
        self.Country = "US"

CFR 238 Appendix C Table  6:
        self.Cants = [6]
        self.Gauges = [56.5,57]
        self.Chords = [31,62]
        self.Classes = [3,4,5]
        self.Country = "US"