import json


def get_gps_data():
    path = "/tmp/gps_feed"
    fifo = open(path, "r")

    for line in fifo:
        packet = json.loads(json.dumps(line))
        fifo.close()
        return packet
