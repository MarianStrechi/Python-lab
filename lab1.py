userName = input('Introduce numele tau:')
print("Salut", userName + "!")


age = 35
activityHours = 74.5
relationshipStatus = "Married"
schedule = "Monday-Friday: Work\nSaturday-Sunday: Resting"


print(type(age), type(activityHours))
print(len(relationshipStatus))

rS = relationshipStatus.upper()
print(rS)

halfText = schedule[3:5]
print(halfText)

finalMessage = "O zi buna {}". format(userName)
print(finalMessage)





#Sarcina 2
#1. Se va afisa textul cu siruri de caractere cu index-uri intre 4 si 12: "Result"
#2. Se va afisa acelasi text, doar ca in forma de lista: ['More', 'results', 'from', 'text...']
#3. Se va afisa: My name is Mary, and I am 36;  Age este afisat in formatul string datorita la txt.format()