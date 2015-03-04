using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;
using System.IO;
namespace MDPSimulator
{
    public class WifiConnector
    {
        private TcpClient clientSocket;
        private string IpAddr {set;get;}
        public WifiConnector()
        {
            clientSocket = new TcpClient();
            IpAddr = "192.168.9.9";
        }

        public bool connect()
        {
            IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Parse(IpAddr), 3000);
            bool isConnected = false;
            int trial = 3;
            while (!isConnected && trial>0)
            {
                trial--;
                try
                {
                    clientSocket.Connect(serverEndPoint);
                    if (clientSocket.Connected)
                    {
                        isConnected = true;
                    }
                }
                catch (Exception)
                {
                    Console.WriteLine("Failed to connect");
                }
            }
            if (!isConnected && trial == 0)
            {
                Console.WriteLine("Cannot connect to server!");
                return false;
            }
            else
            {
                send("Hello");
                return true;
            }
        }

        public void send(string s)
        {
            if (clientSocket.Connected)
            {
                NetworkStream stream = clientSocket.GetStream();
                StreamWriter writer = new StreamWriter(stream);
                StreamReader reader = new StreamReader(stream);
                writer.WriteLine(s);
                writer.Flush();
            }
            else
            {
                Console.WriteLine("No connection!");
            }
        }
        public void listen()
        {
        }
    }
}
