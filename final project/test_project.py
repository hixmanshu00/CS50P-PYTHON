from project import addTask, updateTask, deleteTask

def test_addTask():
    tasks = []
    addTask(tasks,'go to work')
    assert tasks[0] == 'go to work'

def test_updateTask():
    tasks = ['hit gym']
    updateTask(tasks,'complete homework',1)
    assert tasks[0] == 'complete homework'

def test_deleteTask():
    tasks = ['hit gym']
    deleteTask(tasks,1)
    assert len(tasks) == 0