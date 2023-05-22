#לכתוב סקריפט שיאמר לי לרשום מספר והסקריפט יבחן אם המספר שלי זוגי או לא וירשום לי אם הוא זוגי או אי זוגי

num = int(input("Please enter a number: "))

if (num % 2 == 0): #% לשם סימול שארית, אם השארית מהמספר שאני מכניס היא 0 הסקריפט יכתוב שהמספר הוא זוגי
    print("The number you have entered is even!")

elif (num % 2 == 1):
    print("The number you have entered is odd!")