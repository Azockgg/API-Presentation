from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
tasks = [
    {"id": 1, "title": "Einkaufen", "description": "Milch, Brot, Butter kaufen", "done": False},
    {"id": 2, "title": "Workout", "description": "30 Minuten laufen", "done": True},
]

# Route: Alle Aufgaben abrufen
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Route: Eine Aufgabe nach ID abrufen
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

# Route: Neue Aufgabe erstellen
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not "title" in data:
        return jsonify({"error": "Title is required"}), 400
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": data["title"],
        "description": data.get("description", ""),
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route: Aufgabe aktualisieren
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

# Route: Aufgabe löschen
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

# Hauptprogramm starten
if __name__ == "__main__":
    app.run(debug=True)
