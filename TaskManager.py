```python
import json
import os

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'])
        task.completed = data['completed']
        return task

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return [Task.from_dict(task) for task in json.load(f)]
        return []

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f'Задача "{title}" добавлена.')

    def list_tasks(self):
        if not self.tasks:
            print('Нет задач.')
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = '✓' if task.completed else '✗'
            print(f'{idx}. {task.title} - {status} ({task.description})')

    def complete_task(self, index):
        try:
            self.tasks[index - 1].completed = True
            self.save_tasks()
            print('Задача помечена как выполненная.')
        except IndexError:
            print('Некорректный номер задачи.')

def main():
    manager = TaskManager()
    
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Завершить задачу")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи: ")
            manager.add_task(title, description)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            index = int(input("Введите номер задачи для завершения: "))
            manager.complete_task(index)
        elif choice == '4':
            print('Выход из программы.')
            break
        else:
            print('Некорректный выбор, попробуйте еще раз.')

if __name__ == "__main__":
    main()
```