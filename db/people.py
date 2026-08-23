people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
]

def get_employees(human):
    homo = [person for person in people if person['name'] == human]
    return f"Person with name {homo[0]['name']} and age {homo[0]['age']} found" if homo else "Person not found"



