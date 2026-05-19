import json
from pyscript import document, window

import json
from pyscript import document, window

window.localStorage.removeItem("classmates")

class Classmate:
    def __init__(self, name, section, favorite_subject, miss):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
        self.miss = miss
    
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}, and I miss {self.miss}."

default_classmates = [
    Classmate("Audrey", "Topaz", "English", "my classmates"),
    Classmate("Philia", "Amethyst", "Science", "school activities"),
    Classmate("Miguel", "Emerald", "Mathematics", "him"),
    Classmate("Boreas", "Sapphire", "Filipino", "group work"),
    Classmate("Nathan", "Ruby", "ICT", "my turtle")
]

def load_added_classmates():
    stored = window.localStorage.getItem("classmates")
    if stored:
        data = json.loads(stored)
        return [Classmate(c["name"], c["section"], c["favorite_subject"], c["miss"]) for c in data]  # Fixed: data instead of classmates
    return []

def save_added_classmates():  # Added this missing function
    data = [{"name": c.name, "section": c.section, "favorite_subject": c.favorite_subject, "miss": c.miss} for c in added_classmates]
    window.localStorage.setItem("classmates", json.dumps(data))

added_classmates = load_added_classmates()
classmates = default_classmates + added_classmates

def add_classmate(_e=None):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    favorite_subject = document.getElementById("favorite_subject").value
    miss = document.getElementById("miss").value
    
    if name == "" or section == "" or favorite_subject == "" or miss == "":
        document.getElementById("output").innerHTML = "<p class='text-danger'>Please fill out all fields.</p>"
        return
    
    new_student = Classmate(name, section, favorite_subject, miss)
    added_classmates.append(new_student)
    classmates.append(new_student)
    
    save_added_classmates()
    
    document.getElementById("classmate1").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favorite_subject").value = ""
    document.getElementById("miss").value = ""
    
    document.getElementById("output").innerHTML = f"<p class='text-success'>{name} was added successfully!</p>"

def show_classmates(_e=None):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    for student in classmates:
        output.innerHTML += f"<p>{student.introduce()}</p>"
