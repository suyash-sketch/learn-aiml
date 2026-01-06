import threading
import time
chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100_000):
        temp = chai_stock
        time.sleep(0)
        chai_stock = temp + 1
    

threads = [ threading.Thread(target=restock) for _ in range(10) ]


for t in threads: t.start()
for t in threads: t.join()

print("Chai stock:", chai_stock)