#!/usr/bin/env python

import socket
import json
from MAVProxy.modules.lib import mp_module


class InteropModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(InteropModule, self).__init__(mpstate, "interop", "interoperability module")
        
        # The drone/autopilot firmware ip address like 127.0.0.1
        self.ip = "127.0.0.1"
        
        # The port you want to use in order to send your json via UDP
        self.port = 5005
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def mavlink_packet(self, m):
        mtype = m.get_type()

        for attr, value in m.__dict__.iteritems():
            if not attr.startswith('_'):
                print mtype, attr, value


def init(mpstate):
    return InteropModule(mpstate)
