import socket
import json

from proto_py.packet_pb2 import Environment, Packet
from proto_py.common_pb2 import Ball, Robot, Field, Frame
from proto_py.command_pb2 import Command, Commands
from proto_py.replacement_pb2 import Replacement, RobotReplacement, BallReplacement


class Communication():
    def __init__(self, settings = "setting.json") -> None:

        file = open(settings)
        file = json.load(file)

        self.visionAddress = file["address"]["visionAddress"]
        self.visionPort = file["address"]["visionPort"]

        self.refereeAddress = file["address"]["refereeAddress"]
        self.refereePort = file["address"]["refereePort"]

        self.firaReceiveAddress = file["address"]["firaReceiveAddress"]
        self.firaReceivePort = file["address"]["firaReceivePort"]

        self.firaSendAddress = file["address"]["firaSendAddress"]
        self.firaSendPort = file["address"]["firaSendPort"]

    def firaReceive(self) -> str:
        address = (self.firaReceiveAddress, self.firaReceivePort)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind(address)
        data, addr = sock.recvfrom(2048)
        return data

    def firaSend(self, package) -> None:
        address = (self.firaSendAddress, self.firaSendPort)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.sendto(package, address)

    def environment(self) -> Environment:
        data = self.firaReceive()

        environment = Environment()
        environment.ParseFromString(data)

        return environment

    def field(self) -> Field:
        env = self.environment()

        return env.field

    def frame(self) -> Frame:
        env = self.environment()

        return env.frame

    def ball(self) -> Ball:
        frame = self.frame()

        return frame.ball

    def robot(self, id = 0, team = True):
        frame = self.frame()

        if team:
            return frame.robots_yellow[id]
        else:
            return frame.robots_blue[id]
