import time
import threading


def func_001():
    print('--- func_001 / start')
    time.sleep(5)
    print('--- func_001 / stop')


def func_002():
    print('--- func_002 / start')
    time.sleep(2)
    print('--- func_002 / stop')


if __name__ == '__main__':
    print('// START //')

    thread_001 = threading.Thread(target=func_001)
    thread_002 = threading.Thread(target=func_002)

    thread_001.start()
    thread_002.start()

    thread_001.join()
    thread_002.join()

    print('// STOP //')
