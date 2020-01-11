from pykafka import KafkaClient
import json
from datetime import datetime
import uuid


input_file = open('./data/bus1.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']

# Generate uuid
def generate_uuid():
    return uuid.uuid4()

# Kafaka producer
client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test_topic']
producer = topic.get_sync_producer()


# Generate all coordinates
def generate_coordinates(coordinates):
    # new_coordinates = []
    for coordinate in coordinates:
        data = {}
        data['busline'] = 201
        data['key'] = str(data['busline']) + '_' + str(generate_uuid())
        data['time_stamp'] = str(datetime.utcnow())
        data['longitude'] = coordinate[0]
        data['latitude'] = coordinate[1]
        message = json.dumps(data)
        producer.produce(message.encode('ascii'))
        # new_coordinates.append(data)
    # return new_coordinates


generate_coordinates(coordinates)


print('every thing works fine')


