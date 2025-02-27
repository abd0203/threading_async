import threading
import time

def task(i):
    for j in range(4):
        print(f"task {i},{j}")
        time.sleep(1)

def task_without_sleep(i):
    for j in range(4):
        print(f"task_without sleep {i},{j}")

task_1 = threading.Thread(target=task_without_sleep,args=(1,))
task_2 = threading.Thread(target=task,args=(2,))
task_4 = threading.Thread(target=task_without_sleep,args=(4,))
task_3 = threading.Thread(target=task,args=(3,))

print("first")
task_1.start()
task_2.start()
print("middle")
task_3.start()
task_4.start()
task_1.join()
task_2.join()
task_3.join()
task_4.join()
print("last")
