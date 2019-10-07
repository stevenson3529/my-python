'''
favourite_foods = {'Simon': 'pizza', 'Katie':'Pasta','Mary':'Noodles', 'Josh': 'Sushi'}
favourite_foods['Alex'] = 'sausages'
favourite_foods['Alex'] = 'meatballs'
del favourite_foods['Josh']
print(favourite_foods)
print("Mary's favourite food is " , favourite_foods['Mary'])

myDictionary = {'Cinderella':'blue', 'Belle':'yellow', 'Mulan':'red', 'Tiana':'green', 'Rapunzel':'purple'}
print(myDictionary['Mulan'])
print(myDictionary['Belle'])
#print(myDictionary['Snow White'])
myPrincess = myDictionary['Rapunzel']
print(myPrincess)
                
monthlySpending = {'food':150, 'rent': 750, 'electricity':100}
monthlySpending['Gas'] = 100
print(monthlySpending)
'''
names = {'Dave':'01547548', 'Lucy':'54684416', 'Ryan':'4646484'}

if 'Dave' in names:
    print("Dave is already in the dictionary!")
    names['Dave2'] = '01547548'
else:
    names['Dave'] = '01547548'
    print("Dave has been added to the dictionary.")

print(names)
