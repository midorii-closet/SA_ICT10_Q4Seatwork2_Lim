class Classmate:
    def __init__(self, name, section, miss):
        self.name = name
        self.section = section
        self.miss = miss

from pyscript import display, document, window

def load_classmates():
    stored = window.localStorage.getItem("classmates")
    if stored:
        data = json.loads(stored)
        return [Classmate(c["name"], c["section"], c["miss"]) for c in data]
    return []

classmates = load_classmates()

def add_classmate(_e=None):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    miss = document.getElementById("miss").value

    new_student = Classmate(name, section, miss)
    classmates.append(new_student)

    data = [{"name": c.name, "section": c.section, "miss": c.miss} for c in classmates]
    window.localStorage.setItem("classmates", json.dumps(data))

    display(f"{name} added successfully!\n", append=True, target="output")
