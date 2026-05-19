import json
from pyscript import display, document, window

class Classmate:
    def __init__(self, name, section, miss):
        self.name = name
        self.section = section
        self.miss = miss
    
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. And I miss {self.miss}."

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

    # Save to localStorage
    data = [{"name": c.name, "section": c.section, "miss": c.miss} for c in classmates]
    window.localStorage.setItem("classmates", json.dumps(data))

    display(f"{name} added successfully!\n", append=True, target="output")
    
    # Clear input fields
    document.getElementById("classmate1").value = ""
    document.getElementById("section").value = ""
    document.getElementById("miss").value = ""

def show_classmates(_e=None):
    document.getElementById('output').innerHTML = ""
    
    if not classmates:
        display("No classmates added yet!\n", append=True, target='output')
        return
    
    for student in classmates:
        intro = student.introduce()
        display(intro + "\n", append=True, target='output')        
