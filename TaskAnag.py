# Напишите программу, которая принимает на вход 2 строки и определяет, являюся ли они анаграммами.

string_1 = "Цари, вино и сало"
string_2 = "Лисица и ворона"


string_1 = string_1.replace(" ", "")
string_1 = string_1.replace(".", "")
string_1 = string_1.replace(",", "")
string_1 = string_1.lower()
string_2 = string_2.replace(",", "")
string_2 = string_2.replace(".", "")
string_2 = string_2.replace(" ", "")
string_2 = string_2.lower()

dict_1 = {}
dict_2 = {}

for i in string_1:
    dict_1[i] = 0
for i in string_1:
    if i in string_1:
        dict_1[i] += 1

for i in string_2:
    dict_2[i] = 0
for i in string_2:
    if i in string_2:
        dict_2[i] += 1

if dict_1 == dict_2:
    print("Введенные строки являются анаграммами")
else:
    print("Введенные строки не являются анаграммами")