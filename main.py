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


todo = ToDoList()

menu = {
    '1': ("Добавить задачу", lambda: add_task_interactive(todo)),
    '2': ("Отметить задачу как выполненную", lambda: complete_task_interactive(todo)),
    '3': ("Удалить задачу", lambda: remove_task_interactive(todo)),
    '4': ("Показать все задачи", lambda: todo.list_tasks()),
    '0': ("Выход", lambda: print("\nПрограмма завершена. Всего Хорошего!!!") or exit(0))
}


def show_menu():
    print("\n" + "="*50)
    print("              TO-DO LIST")
    print("="*50)
    for key, (text, _) in menu.items():
        print(f"{key}. {text}")
    print("="*50)


while True:
    show_menu()
    choice = input("Выберите действие (0-4): ").strip()

    if choice in menu:
        action = menu[choice][1]
        action()
    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 4.")