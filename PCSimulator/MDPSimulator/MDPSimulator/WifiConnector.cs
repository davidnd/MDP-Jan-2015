using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;
using System.IO;
using MDPModel;
namespace MDPSimulator
{
    public class WifiConnector
    {
        private TcpClient clientSocket;
        private string IpAddr { set; get; }
        public delegate void ReceivingData(string s);
        public delegate void UpdatingInfo(string s);
        public delegate void UpdatingConnectionStatus(bool isConnected);
        public event UpdatingConnectionStatus UpdatingConnectionHandler;
        public event ReceivingData ReceivingDataHandler;
        public event UpdatingInfo UpdatingConsoleHandler;
        public string shortestPath;
        public WifiConnector()
        {
            clientSocket = new TcpClient();
            IpAddr = "192.168.9.9";
        }

        public bool connect()
        {
            OnUpdatingConsole("Connecting to RPI");
            IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Parse(IpAddr), 3000);
            bool isConnected = false;
            int trial = 3;
            while (!isConnected && trial > 0)
            {
                trial--;
                try
                {
                    clientSocket.Connect(serverEndPoint);
                    if (clientSocket.Connected)
                    {
                        isConnected = true;
                        OnUpdatingConsole("Connected to RPI");
                        OnStatusUpdating(true);
                    }
                }
                catch (Exception)
                {
                    OnUpdatingConsole("Fail to establish connection.Trying...");
                    OnStatusUpdating(false);
                }
            }
            if (!isConnected && trial == 0)
            {
                Console.WriteLine("Cannot connect to server!");
                OnUpdatingConsole("Fail to establish connection!");
                OnStatusUpdating(false);
                return false;
            }
            else
            {
                send("Hey there");
                return true;
            }
        }
        protected virtual void OnUpdatingConsole(string s)
        {
            if (UpdatingConsoleHandler != null)
            {
                UpdatingConsoleHandler(s);
            }
            else
            {
                Console.WriteLine("No handler for updating console!");
            }
        }
        public void send(string s)
        {
            if (clientSocket.Connected)
            {
                OnUpdatingConsole("Sending " + s + "!");
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
            NetworkStream nw = clientSocket.GetStream();
            clientSocket.ReceiveBufferSize = 400;
            while (true)
            {
                byte[] data = new byte[clientSocket.ReceiveBufferSize];
                int bytesRead = nw.Read(data, 0, clientSocket.ReceiveBufferSize);
                string desc = Encoding.ASCII.GetString(data, 0, bytesRead);
                Console.WriteLine("receiving: " + desc);
                OnReceivingData(desc);
                if (desc[desc.Length - 1] == 'F')
                {
                    Robot robot = new Robot();
                    this.shortestPath = "A";
                    this.shortestPath += robot.realTimeShortestPath(desc);
                    send(this.shortestPath);
                }
            }
        }

        public void run()
        {
            this.connect();
            if (clientSocket.Connected)
                this.listen();
        }

        protected virtual void OnReceivingData(string s)
        {
            if (ReceivingDataHandler != null)
            {
                ReceivingDataHandler(s);
            }
            else
            {
                Console.WriteLine("Receiving data but no event subscriber!");
            }
        }
        protected virtual void OnStatusUpdating(bool b)
        {
            if (UpdatingConnectionHandler != null)
            {
                UpdatingConnectionHandler(b);
            }
            else
            {
                Console.WriteLine("No handler for connection status update!");
            }
        }
    }
}
