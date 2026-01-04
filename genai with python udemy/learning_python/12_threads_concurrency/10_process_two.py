from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers....")
    total = 0
    for i in range(10**9):
        total+=1
    print(f"✅ DONE")

if __name__ == "__main__":
    start = time.time()

    processes = [ Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processes]
    [p.join() for p in processes]


    end = time.time()

    print(f"Time taken is {end - start:.2f} seconds")
