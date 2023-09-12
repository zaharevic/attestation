import json
import datetime

def save_notes(notes, path):
    try:
        if path == None:
           path = input("Введите путь: ")
        with open(path, "w") as file:
            json.dump(notes, file)
    except FileNotFoundError:
        print("Такого файла не найдено!")

def load_notes(path):
    try:
        if path == None:
           path = input("Введите путь: ")
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def create_note():
    notes = load_notes("notes.json")
    note = {}
    note["id"] = str(len(notes))
    note["заголовок"] = input("Введите заголовок заметки: ")
    note["тело"] = input("Введите текст заметки: ")
    note["дата/время"] = str(datetime.datetime.now())
    return note

def find_note_by_id(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

def print_note(note):
    if note:
        print("--- Заметка ---")
        print(f"Идентификатор: {note['id']}")
        print(f"Заголовок: {note['заголовок']}")
        print(f"Тело: {note['тело']}")
        print(f"Дата/время: {note['дата/время']}")
        print()
    else:
        print("Заметка не найдена.")

def add_note():
    notes = load_notes("notes.json")
    note = create_note()
    notes.append(note)
    save_notes(notes, "notes.json")

def edit_note():
    notes = load_notes("notes.json")
    list_notes()
    note_id = input("Введите идентификатор заметки для редактирования: ")
    note = find_note_by_id(notes, note_id)
    if note:
        print_note(note)
        note["заголовок"] = input("Введите новый заголовок заметки: ")
        note["тело"] = input("Введите новый текст заметки: ")
        note["дата/время"] = str(datetime.datetime.now())
        save_notes(notes, "notes.json")
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")

def delete_note():
    notes = load_notes("notes.json")
    list_notes()
    note_id = input("Введите идентификатор заметки для удаления: ")
    note = find_note_by_id(notes, note_id)
    if note:
        print_note(note)
        notes.remove(note)
        save_notes(notes, "notes.json")
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")

def list_notes():
    notes = load_notes("notes.json")
    if notes:
        print("--- Список заметок ---")
        for note in notes:
            print(f"Идентификатор: {note['id']}")
            print(f"Заголовок: {note['заголовок']}")
            print(f"Тело: {note['тело']}")
            print(f"Дата/время: {note['дата/время']}")
            print()
    else:
        print("Заметки не найдены.")

def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Просмотреть список заметок")
        print("5. Экспортировать список")
        print("6. Импортировать список")
        print("0. Выйти")

        choice = input("Введите номер действия: ")
        print()

        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            notes = load_notes("notes.json")
            save_notes(notes, None)
        elif choice == "6":
            notes = load_notes(None)
            save_notes(notes, "notes.json")
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()