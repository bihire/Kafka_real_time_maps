from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time


input_file = open('./data/bus2.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']

# Generate uuid


def generate_uuid():
    return uuid.uuid4()


# Kafaka producer
client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test_kafka2']
producer = topic.get_sync_producer()


# Generate all coordinates
def generate_coordinates(coordinates):
    # new_coordinates = []
    i = 0
    while i < len(coordinates):
        data = {}
        data['busline'] = 202
        data['key'] = str(data['busline']) + '_' + str(generate_uuid())
        data['time_stamp'] = str(datetime.utcnow())
        data['longitude'] = coordinates[i][0]
        data['latitude'] = coordinates[i][1]
        message = json.dumps(data)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        # If buses reaches last coordinaates
        if i == len(coordinates)-1:
            coordinates = coordinates[::-1]
            i = 0
        else:
            i += 1
    # return new_coordinates


generate_coordinates(coordinates)


print('every thing works fine')
