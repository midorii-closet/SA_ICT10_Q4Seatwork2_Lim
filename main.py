from pyscript import display, document, window
import json

# Load existing classmates from localStorage
def load_classmates():
    stored = window.localStorage.getItem("classmates")
    if stored:
        data = json.loads(stored)
        return [Classmate(c["name"], c["section"], c["miss"]) for c in data]
    return []

classmates = load_classmates()

def add_classmate(e):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    miss = document.getElementById("miss").value

    new_student = Classmate(name, section, miss)
    classmates.append(new_student)
    
    # Save to localStorage
    data = [{"name": c.name, "section": c.section, "miss": c.miss} for c in classmates]
    window.localStorage.setItem("classmates", json.dumps(data))

    display(f"{name} added successfully!\n", append=True, target='output')