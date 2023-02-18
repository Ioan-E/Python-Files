import arrow
import operator

class Task:
    def __init__(self, task_text, due_at):
        self.text = task_text
        if isinstance(due_at, arrow.arrow.Arrow):
            self.due_at = due_at
        else:
            self.due_at = arrow.get(due_at, 'YYYY-MM-DD HH:mm')
        self.completed = False

    def is_overdue(self):
        return self.due_at < arrow.now()

    def __repr__(self):
        if self.is_overdue() and not self.completed:
            return(f'!!!OVERDUE!!! {self.text} task was due on {self.due_at}')
        elif self.completed:
            return(f'This task is completed: {self.text}')
        else:
            return(f'{self.text} task is due on {self.due_at}')
    

class ToDoList():                          
    def __init__(self):
        self.todo = []

    def add_tasks(self, *args):                     #can be replaced if ToDoList inherits from list -> append will work on the class
        for task in args:
            self.todo.append(task)

    # def __repr__(self):
    #     sorted_date_todo = sorted(self.todo, key=lambda task: task.due_at)
    #     string = ''
    #     for task in sorted_date_todo:
    #         string += repr(task) + '\n'
    #     return(string)
    
    def __repr__(self):                             #option if I want to sort using two fields
        return '\n'.join(str(one_task)
                    for one_task in sorted(self.todo,
                        key=operator.attrgetter('due_at', 'text')))
    
    def __len__(self):
        return len([one_task
            for one_task in self.todo
            if not one_task.completed])
    
    def get_overdue_tasks(self):
        return [one_task
                for one_task in self.todo
                if one_task.is_overdue()]

    def get_tasks_on(self, arrow_date=arrow.now()):
        if not isinstance(arrow_date, arrow.arrow.Arrow):
            arrow_date = arrow.get(arrow_date, 'YYYY-MM-DD')
        for task in self.todo:
            if arrow_date.date() == task.due_at.date():
                print(task)


mytask1 = Task('Learn Python', '2025-02-18 14:34')
# mytask1.completed = True
# print(mytask1)
# print(mytask1.is_overdue())

d = arrow.get('2023-07-17 12:34')
mytask2 = Task('Update LinkedIn', d)
# print(mytask2)

mytodo = ToDoList()
mytodo.add_tasks(mytask1, mytask2)
print(len(mytodo))
print(mytodo)
print(mytodo.get_overdue_tasks())
mytodo.get_tasks_on('2025-02-18')