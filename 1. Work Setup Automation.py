#Work Setup Automation - I

#impirting a web browser
import webbrowser as wb

def workauto():
    BravePath='C:\Program Files\BraveSoftware\Brave-Browser\Application.exe %s' #converting into a string
    #NOTE: Use own browser location

    URLS=("stackoverflow.com","github.com", "gmail.com") #websites we want to use in our browser
    
    for url in URLS:
        wb.get(BravePath).open(url) #open all websites into a new tab one by one
        
workauto()