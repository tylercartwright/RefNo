# RefNo
# Version 1.0
# Tyler Cartwright

from pathlib import Path
import re, os, pyperclip

zerosString = ""
refNo = ""
refNoFile = open('C:\\Users\TCartwright\OneDrive\RefNo\RefNo.txt')
refNo_NoLeads = refNoFile.read()
refNoFile.close()
#print("Reference number taken from file: " + refNo_NoLeads)
refNo_NoLeads2 = (str(int(refNo_NoLeads)+1))
#print("Reference number to be passed leading zeros: " + refNo_NoLeads2)
numberOfZeros = 5-(len(str(int(refNo_NoLeads2))))
#print("Number of zeros: " + str(numberOfZeros))
for i in range(numberOfZeros):
    zerosString += "0"
#print("Zeros string: " + zerosString)
refNo = zerosString + refNo_NoLeads2
    
def copyClipboard(writeText):
    pyperclip.copy(writeText)
    
def updateLine(writeText):
    refNoFile = open('C:\\Users\TCartwright\OneDrive\RefNo\RefNo.txt', 'w')
    refNoFile.write(writeText)
    refNoFile.close()

updateLine(refNo)
copyClipboard("TWC | #" + refNo)
#pasteTheInfo()

#print("Reference number: " + refNo)

os._exit(00000)
