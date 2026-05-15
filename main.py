class ToDoList:
    def __init__(self) -> None:
        """Инициализирует пустой словарь задач."""
        self.tasks = {}

    def add_task(self, task_name: str) -> None:
        """Добавляет новую задачу в словарь."""
        if task_name in self.tasks:
            print(f"Задача '{task_name}' уже существует.")
            return

        self.tasks[task_name] = False
        print(f"Задача '{task_name}' успешно добавлена.")

    def complete_task(self, task_name: str) -> None:
        """Отмечает задачу как выполненную."""
        if task_name in self.tasks:
            if self.tasks[task_name]:
                print(f"Задача '{task_name}' уже была выполнена.")
            else:
                self.tasks[task_name] = True
                print(f"Задача '{task_name}' отмечена как выполненная.")
        else:
            print(f"Задача '{task_name}' не найдена.")

    def remove_task(self, task_name: str) -> None:
        """Удаляет задачу."""
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Задача '{task_name}' успешно удалена.")
        else:
            print(f"Задача '{task_name}' не найдена.")

    def list_tasks(self) -> None:
        """Выводит список всех задач."""
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\nСписок задач:")
        for i, (task_name, completed) in enumerate(self.tasks.items(), 1):
            status = "✓" if completed else "☐"
            print(f"{i}. [{status}] {task_name}")


def show_menu():
    print("\n" + "="*50)
    print("              TO-DO LIST")
    print("="*50)
    print("1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Удалить задачу")
    print("4. Показать все задачи")
    print("0. Выход")
    print("="*50)



todo = ToDoList()

while True:
    show_menu()
    choice = input("Выберите действие (0-4): ").strip()
    if choice == '1':
        task = input("Введите название задачи: ").strip()
        if task:
            todo.add_task(task)
        else:
            print("Название задачи не может быть пустым.")
    elif choice == '2':
        task = input("Введите название задачи для отметки: ").strip()
        if task:
            todo.complete_task(task)
        else:
            print("Название задачи не еможет быть пустым.")
    elif choice == '3':
        task = input("Введите название задачи для удаления: ").strip()
        if task:
            todo.remove_task(task)
        else:
            print("Название задачи не может быть пустым.")
    elif choice == '4':
        todo.list_tasks()
    elif choice == '0':
        print("\nПрограмма завершена. Всего Хорошего!!!")
        break

    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 4.")
1