#!/usr/bin/env python

import socket
import json
from MAVProxy.modules.lib import mp_module


class InteropModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(InteropModule, self).__init__(mpstate, "interop", "interoperability module")

        self.ip = "127.0.0.1"
        self.port = 5005
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

        elif mtype == "ALTITUDE":
            response = {
                "packet_id": 141,
                "time_usec": m.time_usec,
                "altitude_monotonic": m.altitude_monotonic,
                "altitude_amsl": m.altitude_amsl,
                "altitude_local": m.altitude_local,
                "altitude_relative": m.altitude_relative,
                "altitude_terrain": m.altitude_terrain,
                "bottom_clearance": m.bottom_clearance
            }
            self.sock.sendto(json.dumps(response), (self.ip, self.port))
            
        elif mtype == "HIGHRES_IMU":
            response = {       
                "packet_id": 105,
                "time_usec": m.time_usec,               
                "xacc": m.xacc,
                "yacc": m.yacc,
                "zacc":	m.zacc,
                "xgyro": m.xgyro,
                "ygyro": m.ygyro,
                "zgyro": m.zgyro,
                "xmag": m.xmag,
                "ymag": m.ymag,
                "zmag": m.zmag,
                "abs_pressure": m.abs_pressure,
                "diff_pressure": m.diff_pressure,
                "pressure_alt": m.pressure_alt,
                "temperature": m.temperature,
                "fields_updated": m.fields_updated
            }
            self.sock.sendto(json.dumps(response), (self.ip, self.port))
            
        elif mtype == "GPS_RAW_INT":
            response = {
                "packet_id": 24,
                "time_usec": m.time_usec,
                "fix_type": m.fix_type,
                "lat": m.lat,
                "lon": m.lon,
                "alt": m.alt,
                "eph": m.eph,
                "epv": m.epv,
                "vel": m.vel,
                "cog": m.cog,
                "satellites_visible": m.satellites_visible
            }
            self.sock.sendto(json.dumps(response), (self.ip, self.port))

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
