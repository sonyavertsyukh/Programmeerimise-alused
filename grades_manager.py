from file_handler import read_grades, write_grade
def add_grade():
    """Kogub õpilase nime ja hinded ning salvestab need faili."""
    name = input("Sisesta õpilase nimi: ")
    grades = list(map(int, input("Sisesta hinded (eralda komaga): ").split(", ")))
    write_grade(name, grades)
    print(f"Õpilase {name} hinded on lisatud.")

def view_grades():
    """Kuvab kõik õpilased ja nende hinded."""
    students = read_grades()
    if not students:
        print("Ei leitud ühtegi õpilast.")
        return
    for student in students:
        print(f"Nimi: {student['name']}\nHinded: {', '.join(map(str, student['grades']))}\n---")

def calculate_average(name):
    """Arvutab õpilase keskmise hinde."""
    students = read_grades()
    for student in students:
        if student["name"].lower() == name.lower():
            avg = sum(student["grades"]) / len(student["grades"])
            return avg
    return None

def search_student():
    """Otsib õpilast nime järgi ja kuvab tema hinded."""
    name = input("Sisesta õpilase nimi otsimiseks: ")
    avg = calculate_average(name)
    if avg is not None:
        print(f"{name} keskmine hinne: {avg:.2f}")
    else:
        print(f"Õpilast {name} ei leitud.")