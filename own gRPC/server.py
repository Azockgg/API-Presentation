from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc


class TodoServiceServicer(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def AddTask(self, request, context):
        task = todo_pb2.Task(id=self.next_id, title=request.title, completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return todo_pb2.AddTaskResponse(success=True)

    def GetTasks(self, request, context):
        return todo_pb2.GetTasksResponse(tasks=self.tasks)

    def CompleteTask(self, request, context):
        for task in self.tasks:
            if task.id == request.id:
                task.completed = True
                return todo_pb2.CompleteTaskResponse(success=True)
        return todo_pb2.CompleteTaskResponse(success=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("TodoService läuft auf Port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
