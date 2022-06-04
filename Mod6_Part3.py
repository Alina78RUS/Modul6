
'''Напишите функцию get_html(link), которая принимает
один аргумент-название веб страницы. Функция должна получать
текст веб страницы с помощью библиотеки requests. Запустите 
5 потоков с данной функцией и разными именами в качестве аргументов.
Сравните время работы параллельного и последовательного запуска
с помощью библиотеки time. '''

import requests
from threading import Thread
from datetime import datetime

def get_html(link):                        
	response=requests.get(f'{link}').text
	print (link, len(response) )

s1 = datetime.now()
link=['http://www.google.com', 'http://www.yandex.ru', 'http://www.youtube.com', 'http://www.wikipedia.ru','http://www.netflix.com']
threads = [Thread(target=get_html, args=[link[i]])for i in range(5)]
for t in threads:
	t.start()
	t.join()
print ('Время выполнения программы при последовательном запуске потока', (datetime.now() -s1).microseconds)

s2 = datetime.now()
link=['http://www.google.com', 'http://www.yandex.ru', 'http://www.youtube.com', 'http://www.wikipedia.ru','http://www.netflix.com']
threads = [Thread(target=get_html, args=[link[i]])for i in range(5)]
for t in threads:
	t.start()
for t in threads:
	t.join()
print ('Время выполнения программы при параллельном запуске потока', (datetime.now() -s2).microseconds)