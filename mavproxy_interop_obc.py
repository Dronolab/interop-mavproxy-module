#!/usr/bin/env python

import os
import socket
import json
from MAVProxy.modules.lib import mp_module

#
# Module for the on-board computer (OBC)
#


class InteropModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(InteropModule, self).__init__(mpstate, "interopobc", "interoperability module")

        # The drone/autopilot firmware ip address like 127.0.0.1
        self.ip = "127.0.0.1"

        # The port you want to use in order to send your json via UDP
        self.port = 5006

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def mavlink_packet(self, m):
        mtype = m.get_type()

        # https://pixhawk.ethz.ch/mavlink/#ATTITUDE
        if mtype == "ATTITUDE":
            response = {
                "packet_id": 30,
                "time_boot_ms": m.time_boot_ms,
                "roll": m.roll,
                "pitch": m.pitch,
                "yaw": m.yaw,
                "rollspeed": m.rollspeed,
                "pitchspeed": m.pitchspeed,
                "yawspeed": m.yawspeed
            }
            self.sock.sendto(json.dumps(response), (self.ip, self.port))

        # https://pixhawk.ethz.ch/mavlink/#GLOBAL_POSITION_INT
        elif mtype == "GLOBAL_POSITION_INT":
            response = {
                "packet_id": 33,
                "time_boot_ms": m.time_boot_ms,
                "lat": m.lat,
                "lon": m.lon,
                "alt": m.alt,
                "relative_alt": m.relative_alt,
                "vx": m.vx,
                "vy": m.vy,
                "vz": m.vz,
                "hdg": m.hdg
            }
            self.sock.sendto(json.dumps(response), (self.ip, self.port))

def init(mpstate):
    return InteropModule(mpstate)
