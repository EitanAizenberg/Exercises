#ליצור סקריפט שיקח את האלמנטים משני רשימות וידפיס רק את האלמנטים המשותפים ביניהן

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in a:
    if x in b:
        c.append(x) #אם אלמנט ב a נמצא ב b, הסקריפט מוסיף אותו לרשימה c
print(set(c)) # שורה זאת הופכת את רשימה c לסט, סט לא מאפשר שאלמנטים יחזרו על עצמם