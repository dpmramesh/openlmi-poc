/*
 * Code from jibble.org.
 *
 * Wake-on-LAN packet is an ordinary UDP packet which contains the MAC address 
 * of the target computer. The UDP packet must be 16 times larger than the byte
 * representation of the MAC address, plus an extra 6 bytes for a header. 
 * A MAC address is usually specified as a string of hexadecimal digits, for 
 * example 00:0D:61:08:22:4A, so can be represented using just 6 bytes. 
 * This makes the total packet size 6 + 16*6 = 102 bytes.
 *
 *  - The first 6 bytes of the packet are filled with 0xff.
 *  - The next 6 bytes are the MAC address of the target computer.
 *  - Each subsequent set of 6 bytes is also filled with the MAC address of the
 *    target computer, until the packet is full.
 *
 * If UDP packet is sent to a broadcast address, such as 192.168.0.255. This 
 * will cause it to be received by all computers on your local LAN, but only 
 * those with a matching MAC address will respond by powering on. 
 */

import java.io.*;
import java.net.*;

public class WakeOnLan {
    
    public static final int PORT = 9;    
    
    public static void main(String[] args) {
        
        if (args.length != 2) {
            System.out.println("Usage: java WakeOnLan <broadcast-ip> <mac-address>");
            System.out.println("Example: java WakeOnLan 192.168.0.255 00:0D:61:08:22:4A");
            System.exit(1);
        }
        
        String ipStr = args[0];
        String macStr = args[1];
        
        try {
            byte[] macBytes = getMacBytes(macStr);
            byte[] bytes = new byte[6 + 16 * macBytes.length];
            for (int i = 0; i < 6; i++) {
                bytes[i] = (byte) 0xff;
            }
            for (int i = 6; i < bytes.length; i += macBytes.length) {
                System.arraycopy(macBytes, 0, bytes, i, macBytes.length);
            }
            
            InetAddress address = InetAddress.getByName(ipStr);
            DatagramPacket packet = new DatagramPacket(bytes, bytes.length, 
                                                            address, PORT);
            DatagramSocket socket = new DatagramSocket();
            socket.send(packet);
            socket.close();
            
            System.out.println("Wake-on-LAN packet sent.");
        }
        catch (Exception e) {
            System.out.println("Failed to send Wake-on-LAN packet: + e");
            System.exit(1);
        }
        
    }
    
    private static byte[] getMacBytes(String macStr) 
                                throws IllegalArgumentException {
        byte[] bytes = new byte[6];
        String[] hex = macStr.split("(\\:|\\-)");
        if (hex.length != 6) {
            throw new IllegalArgumentException("Invalid MAC address.");
        }
        try {
            for (int i = 0; i < 6; i++) {
                bytes[i] = (byte) Integer.parseInt(hex[i], 16);
            }
        }
        catch (NumberFormatException e) {
            throw new IllegalArgumentException("Invalid hex digit in MAC address.");
        }
        return bytes;
    }
    
   
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
