login1 = "paciuk1267"
password1 = "542347657"
list_grade1 = [
    "Географія:8 (Задовільно)",
    "Захист України:9 (Задовільно)",
    "Іноземна мова:4 (Незадовільно)",
    "Історія України:11 (Задовільно)",
    "Основи програмування:10 (Задовільно)",
    "Комп'ютерна графіка:11 (Задовільно)",
    "Математика:3 (Незадовільно)",
    "Укр мова:6 (Задовільно)",
]

login2 = "fshk1488"
password2 = "428703412"
list_grade2 = [
    "Географія:2 (Незадовільно)",
    "Захист України:12 (Задовільно)",
    "Іноземна мова:10 (Незадовільно)",
    "Історія України:3 (Незадовільно)",
    "Основи програмування:7 (Задовільно)",
    "Комп'ютерна графіка:8 (Задовільно)",
    "Математика:1 (Незадовільно)",
    "Укр мова:10 (Задовільно)",
]

login3 = "petruk5673"
password3 = "432748237"
list_grade3 = [
    "Географія:10 (Задовільно)",
    "Захист України:4 (Незадовільно)",
    "Іноземна мова:7 (Задовільно)",
    "Історія України:12 (Задовільно)",
    "Основи програмування:3 (Незадовільно)",
    "Комп'ютерна графіка:7 (Задовільно)",
    "Математика:5 (Задовільно)",
    "Укр мова:9 (Задовільно)",
]

login4 = "kostyuk1234"
password4 = "846732452"
list_grade4 = [
    "Географія:3 (Незадовільно)",
    "Захист України:2 (Незадовільно)",
    "Іноземна мова:8 (Незадовільно)",
    "Історія України:5 (Задовільно)",
    "Основи програмування:12 (Задовільно)",
    "Комп'ютерна графіка:12 (Задовільно)",
    "Математика:6 (Задовільно)",
    "Укр мова:9 (Задовільно)",
]

current_grades = []

while True:
  my_login = input("введіть логін: ")
  my_password = input("введіть пароль: ")

  if my_login == login1 and my_password == password1:
    current_grades = list_grade1
  elif my_login == login2 and my_password == password2:
    current_grades = list_grade2
  elif my_login == login3 and my_password == password3:
    current_grades = list_grade3
  elif my_login == login4 and my_password == password4:
    current_grades = list_grade4

  if current_grades != []:
    print("Вхід виконано!")
    print("Ваші оцінки:", current_grades)
    break
  else:
    print("Неправильний логін або пароль!")

satisfactory_count = 0
unsatisfactory_count = 0

for grades in current_grades:
  if "Задовільно" in grades:
    satisfactory_count += 1
  elif "Незадовільно" in grades:
    unsatisfactory_count += 1

print()
print(f"Задовільні: {satisfactory_count}")
print(f"Незадовільні: {unsatisfactory_count}")