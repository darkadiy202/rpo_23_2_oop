# import time
# import multiprocessing
#
#
# def f():
#     print("ФУНКЦИЯ НАЧАЛА РАБОТУ!!!!")
#     time.sleep(5)
#     print("Функция сделала важные дела!")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     p1 = multiprocessing.Process(target=f)
#     p2 = multiprocessing.Process(target=f)
#     p1.start()
#     p2.start()
#     p1.join()
#
#     p2.join()
#     print(time.time() - start_time)
#
#
#
#
# import time
# import threading
#
#
# def f():
#     print("ФУНКЦИЯ НАЧАЛА РАБОТУ!!!!")
#     time.sleep(5)
#     print("Функция сделала важные дела!")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     p1 = threading.Thread(target=f)
#     p2 = threading.Thread(target=f)
#     p1.start()
#     p2.start()
#     p1.join()
#
#     p2.join()
#     print(time.time() - start_time)
#
# import threading
#
#
# def max1():
#     print(sum(arr))
#
# def min1():
#     print(sum(arr) / len(arr))
#
# arr = []
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     arr.append(x)
#
# t1 = threading.Thread(target=max1)
# t2 = threading.Thread(target=min1)
# t1.start()
# t2.start()