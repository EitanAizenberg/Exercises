# ליצור סקריפט שיבקש מהמשתמש סטרינג ויאמר אם הסטרינג הוא פלינדרום (נכתב אותו הדבר מימין לשמאל ומשמאל לימין)

word = input("please type in a word or scentence: ")

if word == word[::-1]: # אם המילה היא אותו הדבר הפוך השני נקודותיים וה 1- מסמלים על ברברס
     print("palindrom")
else:
     print("not a palindrom")