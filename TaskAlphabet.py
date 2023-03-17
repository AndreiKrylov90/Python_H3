# Взять словарь и отсортировать по алфавиту по ключам и результат вывести в одну строку

dict = {'course': 'python', 'lesson': 2, 'challenge': 17, 'task': 'additional', 
        'arrival': "late", 'students': 198}

sorted_dict = {key: value for key, value in sorted(dict.items())}

super_string = ''
for i in sorted_dict:
    super_string = super_string + i + "=" + str(sorted_dict[i]) + str("&")

print(super_string)