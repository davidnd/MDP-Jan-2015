using System;
using System.Text;
using System.Net;
using System.Net.Sockets;


public class UdpClient : IDisposable{
   
UdpClient udpClient = new UdpClient(11000);
    try{
         udpClient.Connect("192.168.9.1", 11000);

         // Sends a message to the host to which you have connected.
         Byte[] sendBytes = Encoding.ASCII.GetBytes("Is anybody there?");

         udpClient.Send(sendBytes, sendBytes.Length);

         //IPEndPoint object will allow us to read datagrams sent from any source.
         IPEndPoint RemoteIpEndPoint = new IPEndPoint(IPAddress.Any, 0);

         // Blocks until a message returns on this socket from a remote host.
         Byte[] receiveBytes = udpClient.Receive(ref RemoteIpEndPoint); 
         string returnData = Encoding.ASCII.GetString(receiveBytes);

         // Uses the IPEndPoint object to determine which of these two hosts responded.
         Console.WriteLine("This is the message you received " +
    	                              returnData.ToString());
         Console.WriteLine("This message was sent from " +
                                     RemoteIpEndPoint.Address.ToString() +
                                     " on their port number " +
                                     RemoteIpEndPoint.Port.ToString());

          udpClient.Close();
          udpClientB.Close();

          }  
       catch (Exception e ) {
                  Console.WriteLine(e.ToString());
        }
}
