#Work Setup Automation - I
#Including applications

import webbrowser as wb
import os

def workauto():

    #Part 1: Opeaning Application
    CodeEditor="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #Path of program
    #\ is replaced by \\
    #NOTE: Use own application location
    os.startfile(CodeEditor)

    #Part 2: Opeaning Websites
    BravePath='C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe %s' #converting into a string
    #NOTE: Use own browser location

    #Taking Website as Input From User
    url=input("Enter The Website Name: ")
    wb.get(BravePath).open(url) #open all websites into a new tab one by one
        
workauto()