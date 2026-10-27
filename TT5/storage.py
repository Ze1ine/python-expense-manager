import json

def file_load():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError: 
        return []
    except json.JSONDecodeError:
        print("Неккоректный файл JSON")
        return None

def file_save(parameter):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(parameter, file, ensure_ascii=False, indent=4)