#!/usr/local/bin/python
import socket

class CodRcon:
  def __init__(self, host, port=28960, password='', timeout=10):
    self.password = password
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.settimeout(timeout)
    self.sock.connect((host, port))

  def sendCommand(self, command, recvBuffSize=4096):
    buff = '\xFF\xFF\xFF\xFFrcon '+self.password+' '+command+'\x00'
    try:
      if self.sock.send(buff) < len(buff):
        print "ERROR: Greska pri slanju komande %s", command
      buff = self.sock.recv(recvBuffSize)
      if len(buff) > 0:
        return buff
      else:
        print "ERROR: No data was returned from the command %s", command
        return 0
    except socket.timeout:
      print "ERROR: The socket used for sending command %s has timed out.", command
      raise

