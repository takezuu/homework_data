import csv
import json

HEADER = ('title', 'author', 'pages', 'genre')
JSON_HEADER = ('name', 'gender', 'address', 'age', 'books')
all_books = []
all_users = []

# Создаю из csv файла список со всеми книгами
with open('books.csv', newline='') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        new_row = (row['Title'], row['Author'], row['Pages'], row['Genre'])
        csv_dict = (dict(zip(HEADER, new_row)))
        all_books.append(csv_dict)

# Из json файла создаю список со всеми пользователями
with open('users.json', 'r') as file:
    json_file = json.load(file)
    for row in json_file:
        new_json_row = (row['name'], row['gender'], row['address'], row['age'], [])
        new_json_dict = (dict(zip(JSON_HEADER, new_json_row)))
        all_users.append(new_json_dict)

# Раздача книг пользователям
number_of_users = len(all_users)
user_count = 0
for book in all_books:
    all_users[user_count]["books"].append(book)
    user_count += 1
    if user_count >= number_of_users:
        user_count = 0

# Запись в финальный файл пользователей с розданными книгами
with open('result.json', 'w') as final_file:
    json.dump(all_users, final_file, indent=4)
