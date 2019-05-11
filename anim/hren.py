from multiprocessing import Process, Queue

sentinel = -1


def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:
        q.put(item)



if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]

    process_one = Process(target=creator, args=(data, q))

    process_one.start()
    while 1:
        if q.empty():
            continue
            print("test")
        print(q.get())