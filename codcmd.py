import sys
from codrcon import CodRcon

if __name__ == "__main__":
  cmd = ' '.join(map(str, sys.argv[1:]))
  srv = CodRcon("vps1.bkrsta.co.cc", 28960, "rconpw123")
  r = srv.sendCommand(cmd)
  if r[:4] == "\xFF"*4:
    if r[4:r.find("\n")] == "print":
      print "OUTPUT:"
      print r[r.find("\n")+1:]

