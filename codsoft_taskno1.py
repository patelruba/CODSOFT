#CODSOFT

#Task 1 to do list 

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f'\n✅ Task "{task}" added successfully!')
        else:
            print("\n❌ Task cannot be empty. Please enter a valid task.")

    def remove_task(self, task_number):
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f'\n✅ Task "{removed_task}" removed successfully!')
            else:
                print(f"\n❌ Invalid task number. Please enter a number between 1 and {len(self.tasks)}.")
        except ValueError:
            print("\n❌ Invalid input. Please enter a valid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("\n📝 Your to-do list is currently empty.")
        else:
            print("\n📝 Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"   {idx}. {task}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f'\n✅ Task "{task}" added successfully!')
        else:
            print("\n❌ Task cannot be empty. Please enter a valid task.")

    def remove_task(self, task_number):
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f'\n✅ Task "{removed_task}" removed successfully!')
            else:
                print(f"\n❌ Invalid task number. Please enter a number between 1 and {len(self.tasks)}.")
        except ValueError:
            print("\n❌ Invalid input. Please enter a valid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("\n📝 Your to-do list is currently empty.")
        else:
            print("\n📝 Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f" {idx}. {task}")

def main():
    todo_list = ToDoList()
    print("\nWelcome to the To-Do List Application!")
    print("You can manage your tasks easily with this simple application.\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit the application")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ").strip()
            todo_list.add_task(task)
        elif choice == '2':
            if not todo_list.tasks:
                print("\n❌ There are no tasks to remove.")
            else:
                todo_list.show_tasks()
                task_number = input("Enter the number of the task you want to remove: ").strip()
                todo_list.remove_task(task_number)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("\nThank you for using the To-Do List Application. Have a great day!")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
