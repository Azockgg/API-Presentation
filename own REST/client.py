import requests
import json

BASE_URL = "http://127.0.0.1:5000/tasks"



#Get all json repsonce
def get_all_tasks():
    response = requests.get(BASE_URL)
    print("GET /tasks")
    print(response.status_code, response.json())


#nur Workout nachfragen
def get_task(task_id):
    response = requests.get(f"{BASE_URL}/{task_id}")
    print(f"GET /tasks/{task_id}")
    print(response.status_code, response.json())

def create_task(title, description=""):
    task_data = {
        "title": title,
        "description": description
    }
    response = requests.post(BASE_URL, json=task_data)
    print("POST /tasks")
    print(response.status_code, response.json())

def update_task(task_id, title=None, description=None, done=None):
    task_data = {}
    if title is not None:
        task_data["title"] = title
    if description is not None:
        task_data["description"] = description
    if done is not None:
        task_data["done"] = done
    
    response = requests.put(f"{BASE_URL}/{task_id}", json=task_data)
    print(f"PUT /tasks/{task_id}")
    print(response.status_code, response.json())

def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/{task_id}")
    print(f"DELETE /tasks/{task_id}")
    print(response.status_code, response.json())

# Testfälle
if __name__ == "__main__":
    # 1. Alle Aufgaben abrufen
    get_all_tasks()

    # 2. Eine einzelne Aufgabe abrufen
    get_task(1)

    # 3. Eine neue Aufgabe erstellen
    create_task("Programm schreiben", "REST API mit Python erstellen")

    # 4. Eine bestehende Aufgabe aktualisieren
    update_task(1, title="Einkaufen erledigt", done=True)

    # 5. Eine Aufgabe löschen
    delete_task(1)

    # 6. Nochmals alle Aufgaben abrufen
    get_all_tasks()
