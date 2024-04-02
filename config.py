import json

class Misha:
    def __init__(self, name, age, birthday, hobby, is_married, pets):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.hobby = hobby
        self.is_married = is_married
        self.pets = pets

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Birthday: {self.birthday}\n"
            f"Hobby: {self.hobby}\n"
            f"Married: {self.is_married}\n"
            f"Pets: {', '.join(self.pets)}"
        )

misha = Misha(
    'Misha',  # имя
    16,  # возраст
    '22 октября',  # дата рождения
    'футбол',  # хобби
    False,  # замужем
    ['кошка', 'собака']  # питомцы
)

with open('settings.json', 'w', encoding='utf-8') as file:
    json.dump(misha.__dict__, file, indent=4, ensure_ascii=False)  # вывод в файл settings.json

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4, ensure_ascii=False))  # вывод в консоль settings.json

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write('Результат settings.json:\n')
    file.write(json.dumps(data, indent=4, ensure_ascii=False))  # вывод в файл text.txt в json формате
    
    file.write('\n\nРезультат в более простом виде:\n')
    file.write(misha.display_info()) # вывод в файл text.txt в более простом виде