#!/usr/bin/env python

# Legacy WOL protocol
# Intel vPro systems will have Intel AMT technology integrated
# which is DMTF DASH compliant. The WOL magic packet is legacy
# technology.

import struct, socket

def WakeOnLan(ethernet_address):

  # Construct a six-byte hardware address

  addr_byte = ethernet_address.split(':')
  hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16),
    int(addr_byte[1], 16),
    int(addr_byte[2], 16),
    int(addr_byte[3], 16),
    int(addr_byte[4], 16),
    int(addr_byte[5], 16))

  # Build the Wake-On-LAN "Magic Packet"...

  msg = '\xff' * 6 + hw_addr * 16

  # ...and send it to the broadcast address using UDP

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  s.sendto(msg, ('<broadcast>', 9))
  s.close()

#WakeOnLan('00:03:56:0d:89:56') 

# Intel 82566DM

# mncarsnas -> 00:12:3f:5f:2c:1d
# mncars001 -> 00:d0:b7:b2:92:86
# mncars002 -> 00:0f:fe:4d:64:eb
# mncars003 -> 00:0f:fe:7b:f2:02
# mncars004 -> 00:18:71:70:f1:7b
# mncars005 -> 00:0f:fe:7b:f4:30

WakeOnLan('00:0F:FE:4D:64:69')

