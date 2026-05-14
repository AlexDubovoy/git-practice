class ToDoList:
    def __init__(self) -> None:
        """Инициализирует пустой список задач."""
        self.tasks = []

    def add_task(self, task: str) -> None:
        """Добавляет новую задачу в список задач."""
        self.tasks.append({"name": task, "completed": False})
        print(f"Задача '{task}' добавлена.")

    def complete_task(self, task: str) -> None:
        """Помечает задачу как выполненную."""
        for t in self.tasks:
            if t["name"] == task:
                t["completed"] = True
                print(f"Задача '{task}' отмечена как выполненная.")
                return
        print(f"Задача '{task}' не найдена.")

    def remove_task(self, task: str) -> None:
        """Удаляет задачу из списка."""
        for i, t in enumerate(self.tasks):
            if t["name"] == task:
                del self.tasks[i]
                print(f"Задача '{task}' удалена.")
                return
        print(f"Задача '{task}' не найдена.")

    def list_tasks(self) -> None:
        """Выводит список всех задач."""
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("Список задач:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['name']}")


todo = ToDoList()

# Добавляем задачи
todo.add_task("Купить продукты")
todo.add_task("Сделать домашнее задание")
todo.add_task("Сделать уборку")

print("====================")

# Отмечаем задачу как выполненную
todo.complete_task("Купить продукты")
todo.complete_task("Сделать уборку")
todo.complete_task("Погулять с собакой")

print("====================")

# Удаляем задачу
todo.remove_task("Сделать уборку")
todo.remove_task("Поспать")

print("====================")

# Выводим список задач
todo.list_tasks()