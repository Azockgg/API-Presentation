import grpc
import todo_pb2
import todo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)

        # Aufgabe hinzufügen
        response = stub.AddTask(todo_pb2.AddTaskRequest(title="Einkaufen gehen"))
        print(f"Aufgabe hinzugefügt: {response.success}")

        # Aufgaben abrufen
        tasks_response = stub.GetTasks(todo_pb2.GetTasksRequest())
        print("Aktuelle Aufgaben:")
        for task in tasks_response.tasks:
            print(f"- [{task.id}] {task.title} (Erledigt: {task.completed})")

        # Aufgabe als erledigt markieren
        complete_response = stub.CompleteTask(todo_pb2.CompleteTaskRequest(id=1))
        print(f"Aufgabe erledigt: {complete_response.success}")

        # Aufgaben erneut abrufen
        tasks_response = stub.GetTasks(todo_pb2.GetTasksRequest())
        print("Aktualisierte Aufgaben:")
        for task in tasks_response.tasks:
            print(f"- [{task.id}] {task.title} (Erledigt: {task.completed})")


if __name__ == '__main__':
    run()
