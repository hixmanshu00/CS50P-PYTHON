import sys
def main():
    tasks = []
    load_tasks(tasks)
    print('********* WELCOME TO TODO APPLICATION *********')
    while True:
        print('1. SHOW ALL TASKS')
        print('2. ADD A TASK')
        print('3. UPDATE A TASK')
        print('4. DELETE A TASK')
        print('5. EXIT')
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            showTasks(tasks)
        elif choice == '2':
            task = input('Enter your task: ')
            addTask(tasks,task)
        elif choice == '3':
            showTasks(tasks)
            try:
                choice = int(input('Choose the task number you want to update: '))
                if choice > len(tasks):
                    print('----------------- Choice out of bounds !! -------------------')
                else:   
                    task = input('Enter the updated value: ')
                    updateTask(tasks, task, choice)
            except ValueError:
                print('----------------- choice invalid !! -----------------')

        elif choice == '4':
            showTasks(tasks)
            try:
                choice = int(input('Choose the task number you want to delete: '))
                deleteTask(tasks,choice)    
            except ValueError:
                print('----------------- choice invalid !! -----------------')
        elif choice == '5':
            sys.exit('************ HAVE A GOOD DAY !! *************')

def load_tasks(tasks):
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def addTask(tasks,task):
    tasks.append(task)
    save_tasks(tasks)
    print('********** TASK ADDED SUCCESSFULLY *************')

def updateTask(tasks,task,index):
    tasks[index - 1] = task
    save_tasks(tasks)
    print('**************** TASK UPDATED !!!! ***************')
    print('**************** UPDATED LIST ******************')
    showTasks(tasks)


def deleteTask(tasks,index):
    if index > len(tasks):
        print('----------------- Choice out of bounds !! -------------------')
        return
    del tasks[index-1]
    save_tasks(tasks)
    print('**************** TASK DELETED !! *****************')
    print('**************** UPDATED LIST ******************')
    showTasks(tasks)


def showTasks(tasks):
    if len(tasks) == 0:
        print('************ NO TASKS ADDED !! ****************')
    else:
        print('************** Here are your tasks *************')
        i = 1
        for task in tasks:
           print(f'{i}. {task}')
           i += 1 
    print('****************************************')


if __name__ == "__main__":
    main()