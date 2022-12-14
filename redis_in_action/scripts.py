import time
from uuid import uuid4

from redis import from_url

client = from_url('redis://localhost:6379/1')

print(client.ping())


# client.set(name='str-key', value='hello redis.')
#
# client.hset(name='hash-key', mapping={'key1': 'value1', 'key2': 'value2'})
#
# client.delete('hash-key')

def acquire_lock(lock_name, acquire_time=10):
    identifier = str(uuid4())
    end = time.time() + acquire_time
    while time.time() < end:
        if client.setnx('lock:' + lock_name, identifier):
            return identifier
        time.sleep(0.1)
    return False


print(acquire_lock('match'))
