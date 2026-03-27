students = [
    {'name': 'Ivan', 'grades': [80, 90, 70]},
    {'name': 'Petr', 'grades': [75, 80, 64]},
    {'name': 'Fedor', 'grades': [40, 50, 67]},
    {'name': 'Alex', 'grades': [90, 98, 95]}
]


def calculate_average(grades):
    """Возвращает средний балл по списку оценок"""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def print_student_info(student):
    """Выводит информацию о студенте в требуемом формате"""
    avg = calculate_average(student['grades'])
    status = "Успешен" if avg >= 75 else "Отстающий"

    print(f"Студент: {student['name']}")
    print(f"Средний балл: {avg:.2f}")
    print(f"Статус: {status}")
    print("-" * 30)


def print_all_students(students_list, title=""):
    """Выводит информацию обо всех студентах"""
    if title:
        print(f"\n=== {title} ===")
    else:
        print("\n=== Результаты студентов ===")

    for student in students_list:
        print_student_info(student)


new_student = {'name': 'Maria', 'grades': [85, 92, 88]}
students.append(new_student)

students = [student for student in students
            if calculate_average(student['grades']) > 75]

print_all_students(students, "Студенты с баллом выше среднего")

if students:
    overall_avg = sum(sum(s['grades']) for s in students) / \
                  sum(len(s['grades']) for s in students)
    print(f"\nОбщий средний балл по всей группе: {overall_avg:.2f}")
else:
    print("\nВ группе не осталось студентов.")