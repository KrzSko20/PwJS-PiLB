def personal_data():
    first_name, last_name, year_of_birth = input("Provide your name and year of birth followed by space bar.").split()
    print(first_name, last_name, year_of_birth)


if __name__ == "__main__":
    personal_data()
