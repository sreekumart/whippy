from whippy import whippy_factory
import time
import requests
import threading
import concurrent.futures


def execute_sync(order):
    a=1/0
    response = requests.get('http://localhost:45443/users/status/check', verify=False)
    if response.status_code == 500:
        raise Exception(response.text)
    return response.text


test_command = whippy_factory.WhippyFactory.get_command('test_command')

execute_sync = whippy_factory.WhippyFactory.create_decorator(test_command, execute_sync)

order = '12345'
for i in range(100):
    try:
        result = execute_sync(order)
        print(result)
    except concurrent.futures.TimeoutError as e:
        print(e)
    except Exception as e:
        print(e)

time.sleep(10)
print('after count ', threading.active_count())

del test_command

time.sleep(10)
print(threading.enumerate())
