import requests
import os
from multiprocessing import Process

def get_url():
    get_url.url = input('Enter url (full path): ')
    confirm_url = input('Confirm this url?(y/N): ')

    if confirm_url == 'y' or confirm_url == 'Y':
        main(get_url.url)
    elif confirm_url == 'n' or confirm_url == 'N' or confirm_url == '':
        print('abort')
        get_url()
    else:
        print('abort with error')
        get_url()

def main(url):
    response = requests.get(url)

    if response.status_code == 200:
        print('Connected')
        
    elif response.status_code == 404:
        print('Not found')
    elif response.status_code == 500:
        print('Server error')
    else:
        print("Can't connect to server")

    concurrency = int(input('Enter concurrency: '))
    print('Worker1 up')
    print('Worker2 up\n')
    for _ in range(concurrency):
        print('On going...')
        Process(target=worker1(url)).start()
        Process(target=worker2(url)).start()
    print('Done')
    finish_task()

def finish_task(): 
    os.system('pause')

def worker1(url):
    requests.get(url)

def worker2(url):
    requests.get(url)

if __name__ == '__main__':
    get_url()