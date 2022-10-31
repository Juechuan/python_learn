from redis import from_url

client = from_url('redis://localhost:6379/1')

client.ping()

client.set(name='str-key', value='hello redis.')

client.hset(name='hash-key', mapping={'key1': 'value1', 'key2': 'value2'})

client.delete('hash-key')

