"""Task 2: To-Do-List Application

Features:
  1. Add tasks
  2. View current tasks
  3. Remove a task once it is completed
  4. Display a progress bar (completed / total tasks ever added)
"""

BAR_WIDTH = 30


def show_progress(completed, total):
    """Print a text progress bar."""
    if total == 0:
        percent = 0
    else:
        percent = completed / total * 100
    filled = int(BAR_WIDTH * percent / 100)
    bar = "#" * filled + "-" * (BAR_WIDTH - filled)
    print(f"\nProgress: [{bar}] {percent:.0f}% ({completed}/{total} completed)")


def add_task(tasks, total):
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return total
    tasks.append(title)
    print(f"Added: '{title}'")
    return total + 1


def view_tasks(tasks):
    if not tasks:
        print("\nNo pending tasks. Great job!")
        return
    print("\nCurrent tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"  {i}. {task}")


def remove_task(tasks, completed):
    if not tasks:
        print("\nNothing to remove.")
        return completed
    view_tasks(tasks)
    try:
        number = int(input("Enter the number of the completed task: "))
        if 1 <= number <= len(tasks):
            done = tasks.pop(number - 1)
            print(f"Completed and removed: '{done}'")
            return completed + 1
        print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    return completed


def main():
    tasks = []
    total = 0        # all tasks ever added
    completed = 0    # tasks removed as completed

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove completed task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            total = add_task(tasks, total)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            completed = remove_task(tasks, completed)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

        show_progress(completed, total)


if __name__ == "__main__":
    main()