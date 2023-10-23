#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('https://sdcaf.hungrybeagle.com/menu.php')
data = req.text
data = json.loads(data)

# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains
class skoolweb():
    def __init__(self):
        menu = data['menu']
        
        for i in menu:
            i.pop('date')
            i.pop('notes')
            print("\n")
            for j in i:print(i[j])

            



g=skoolweb()