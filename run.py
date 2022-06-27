from P1.task01.task01 import run as run_taskp1_01
from P1.task02.task02 import run as run_taskp1_02
from P1.task03.task03 import run as run_taskp1_03
from P2.task01.task01 import run as run_taskp2_01
from P2.task02.task02 import run as run_taskp2_02
from P2.task03.task03 import run as run_taskp2_03

task_map = {
    11: run_taskp1_01,
    12: run_taskp1_02,
    13: run_taskp1_03,
    21: run_taskp2_01,
    22: run_taskp2_02,
    23: run_taskp2_03
}

if __name__ == '__main__':
    print("""Codificação das tasks:
    
    11: P1 - Task 01
    12: P1 - Task 02
    13: P1 - Task 03
    21: P2 - Task 01
    22: P2 - Task 02
    23: P2 - Task 03
    """)
    t = int(input("Escolha uma task para executar: "))
    choosenTask = task_map[t]
    choosenTask()
