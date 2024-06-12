import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            print(f"Updated task {index + 1} to: {new_task}")
        else:
            print("Invalid task index")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed task {index + 1}: {self.tasks[index]['task']}")
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Deleted task {index + 1}: {removed_task['task']}")
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{idx + 1}. {task['task']} [{status}]")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Update task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. List tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            to_do_list.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter the task number to complete: ")) - 1
            to_do_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            to_do_list.delete_task(index)
        elif choice == '5':
            to_do_list.list_tasks()
        elif choice == '6':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
