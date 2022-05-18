from task01.task01 import run as run_task01
from task02.task02 import run as run_task02
from task03.task03 import run as run_task03

task_map = {
    1: run_task01,
    2: run_task02,
    3: run_task03
}

if __name__ == '__main__':
    t = int(input("Escolha uma task para executar: "))
    choosenTask = task_map[t]
    choosenTask()
