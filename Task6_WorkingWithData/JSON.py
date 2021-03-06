import json
import os


def open_json(path):
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return []


def save_json(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def print_data(data):
    for a in range(0, len(data)):
        print("\nNo. " + str(a+1))
        print("name:", data[a]["name"])
        print("description:", data[a]["description"])
        print("date:", data[a]["date"])


def add_note():
    print()
    name = input("\t" + "name: ")
    des = input("\t" + "description: ")
    date = input("\t" + "date: ")

    note = {"name": name, "description": des, "date": date}
    return note


def remove_note():
    print()
    n = int(input("\t" + "Which one u want to remove?: "))
    return n-1


def main():

    path = "JSON_Used.json"
    data = open_json(path)

    while(True):
        print_data(data)
        print("\n" + "Choose action: ")
        print("\t" + "1. Add note")
        print("\t" + "2. Remove note")
        print("\t" + "0. Exit")
        choice = int(input("Choose number: "))
        if choice == 1:
            data.append(add_note())
        elif choice == 2:
            data.pop(remove_note())
        elif choice == 0:
            break

    save_json(data, path)


if __name__ == '__main__':
    main()
