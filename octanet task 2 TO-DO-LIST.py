class Task:
    def __init__(self, description, status="Incomplete"):
        self.description = description
        self.status = status

    def mark_as_done(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.description} - {self.status}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task_status(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task.mark_as_done()
            print(f"Task '{task.description}' marked as complete.")
        except IndexError:
            print("Invalid task index.")

    def __str__(self):
        return "\n".join([str(task) for task in self.tasks])
def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter task description: ")
            new_task = Task(description)
            todo_list.add_task(new_task)
            print(f"Task '{description}' added successfully.")

        elif choice == "2":
            print("\n*** Your To-Do List ***")
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the task index to mark as complete: "))
            todo_list.update_task_status(task_index)

        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
