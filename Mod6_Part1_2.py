
'''Напишите функцию get_thread(thread_name), которая принимает
 один аргумент - название потока. Функция должна ждать одну 
 секунду, затем выводить в стандартный вывод (print) 
 название потока.
 Ожидание в одну секунду реализуйте с помощью библиотеки time.
 Запустите 5 потоков с данной функцией и разными именами в 
 качестве аргументов.
'''

import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
	time.sleep(1)
	print (f'get_thread {thread_name}')

t1 = datetime.now() 
threads = [Thread(target=get_thread, args=str(i+1))for i in range(5)]
for t in threads:
	t.start()
for t in threads:
	t.join()
print ('Время выполнения программы при параллельном запуске потока', (datetime.now() -t1).microseconds)
 
threads = [Thread(target=get_thread, args=str(i+1))for i in range(5)]
for t in threads:
	t.start()
	t.join()
print ('Время выполнения программы при последовательном запуске потока', (datetime.now() -t1).microseconds)
