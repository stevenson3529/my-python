from tkinter import Tk, simpledialog, messagebox

def readFile():
    with open('capital_cities.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
def writeFile(countryName, cityName):
    with open('capitals_cities.txt', 'a') as file:
        file.write('\n' + countryName + '/' + cityName)

print("Ask the Computer - Capital cities")
root = Tk()
root.withdraw()
the_world = {}

readFile()

while True:
    query_country = simpledialog.askstring('Enter a country', 'Type the name of a country:')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer','The capital city of ' + query_country + ' is ' + result + '.')
    else:
        new_city = simpledialog.askstring("Warning", "I don't know what the capital of " + query_country + ' is. Enter the correct answer')
        the_world[query_country] = new_city
        writeFile(query_country, new_city)

root.mainloop()
                                        
