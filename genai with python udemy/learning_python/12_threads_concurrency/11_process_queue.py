from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala Chai is ready")

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))

    p.start()
    p.join()

    print(queue.get())