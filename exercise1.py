#לכתוב סקריפט שיקבל אינפוט של שם וגיל וירשום מתי הבן אדם יהיה בן 100

name = input("Enter your name please: ")
age = input("Enter your age: ")

years = (100 - int(age)) #החלק שאומר בעוד כמה שנים אהיה בן 100
year = (int(years) + 2023) #החלק שאומר באיזו שנה אהיה בן 100

print(str(name) + " will be 100 years old in " + str(years) + " in the year " + str(year))