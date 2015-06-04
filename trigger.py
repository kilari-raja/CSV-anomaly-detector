""" This file integrates all other files. Function below is where it all begins and ends"""

from DisplayerIII import *
from Classifier import *
from Calculator import *
from commonFunc import *

def startTool(filesname,start,end,returnCommaChecker,returnRowCount):  
    if returnCommaChecker == returnRowCount :  #this line checks for improper commas
        global you,datum        
        datum = get_real_data(filesname)        
        bdictReturn = bdictFunction()
        for i in range(1,len(datum)):            
            datatypeClassifier(datum[i][start],email_array,bdictReturn)
            #Above function classifies incoming entry into differnt dataypes 
        observations(filesname,start,end,returnCommaChecker,datum,bdictReturn,print_array)
        #the above function (observations) identifies "defects" and prints them out.
    return "return from startTool"