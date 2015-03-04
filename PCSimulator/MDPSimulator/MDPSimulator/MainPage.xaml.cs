using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using MDPModel;
using System.ComponentModel;
using System.Threading;
using System.Windows.Threading;

namespace MDPSimulator.View
{
    /// <summary>
    /// Interaction logic for MainPage.xaml
    /// </summary>
    public partial class MainPage : Window
    {
        public int[,] mapDescriptor = new int[20, 15];
        public Map map;
        public Robot robot;
        public Simulator simulator;
        public int testID = 0;
        private DispatcherTimer timer;
        private int timeLimit;
        private double coverageLimit;
        private Thread exploreThread;
        private WifiConnector Connector {set; get; }
        public MainPage()
        {
            InitializeComponent();
            setUpMap();
            this.timer = new DispatcherTimer();
            this.Connector = new WifiConnector();
        }
        private void setUpMap()
        {
            for (int i = 0; i < 20; i++)
            {
                RowDefinition rowDef = new RowDefinition();
                rowDef.Height = new GridLength(1, GridUnitType.Star);
                mapGrid.RowDefinitions.Add(rowDef);
            }

            for (int i = 0; i < 15; i++)
            {
                ColumnDefinition colDef = new ColumnDefinition();
                colDef.Width = new GridLength(1, GridUnitType.Star);
                mapGrid.ColumnDefinitions.Add(colDef);
            }
            var bc = new BrushConverter();
            mapGrid.ShowGridLines = true;
            for (int i = 0; i < 9; i++)
            {
                Label label = new Label();
                label.Background = (Brush)bc.ConvertFrom("#FF28701C");
                Grid.SetRow(label, 19 - i / 3);
                Grid.SetColumn(label, i % 3);
                mapGrid.Children.Add(label);
            }

            for (int i = 0; i < 9; i++)
            {
                Label label = new Label();
                label.Background = (Brush)bc.ConvertFrom("#FF28701C");
                Grid.SetRow(label, i / 3);
                Grid.SetColumn(label, 14 - i % 3);
                mapGrid.Children.Add(label);
            }
        }
        private void loadMapClick(object sender, RoutedEventArgs e)
        {
            string content = "";
            try
            {
                using (StreamReader sr = new StreamReader("E:/Git/MDP-Jan-2015/PCSimulator/MDPSimulator/map.txt"))
                {
                    string line;
                    while ((line = sr.ReadLine()) != null)
                        content += line;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Failed to read the file!");
                Console.WriteLine(ex.Message);
            }
            Console.WriteLine(content);
            int k = 0;
            for (int i = 0; i < content.Length; i++)
            {
                if (content[i] == '1')
                {
                    mapDescriptor[i / 15, i % 15] = 1;
                }
                else
                    mapDescriptor[i / 15, i % 15] = 0;
            }
            updateMap();
            this.displayConsoleMessage("Map loaded!");
        }
        private void updateMap()
        {
            this.mapGrid.Children.Clear();
            this.mapGrid.RowDefinitions.Clear();
            this.mapGrid.ColumnDefinitions.Clear();
            setUpMap();
            var bc = new BrushConverter();
            for (int i = 0; i < 20; i++)
            {
                for (int j = 0; j < 15; j++)
                {
                    Label label = new Label();
                    if (mapDescriptor[i, j] == 1)
                        label.Background = (Brush)bc.ConvertFrom("#FF952900");
                    else
                    {

                    }
                    //label.BorderThickness = new Thickness(1);
                    //label.BorderBrush = Brushes.DarkGray;
                    Grid.SetColumn(label, j);
                    Grid.SetRow(label, 19 - i);
                    this.mapGrid.Children.Add(label);
                }
            }
        }

        private void exploreButton_Click(object sender, RoutedEventArgs e)
        {
            this.robot = new Robot();
            this.map = new Map(mapDescriptor);
            this.displayConsoleMessage("Exploring using wall follower!!!");
            this.robot.ChangePosition += new Robot.RobotMovingHandler(updateRobotPosition);
            this.simulator = new Simulator(robot, map);
            this.timeLimit = UserSetting.TimeLimit;
            timer.Interval = new TimeSpan(0, 0, 1);
            timer.Tick += new EventHandler(timer_Tick);
            timer.Start();
            exploreThread = new Thread(this.simulator.simulateExplore);
            exploreThread.Start();
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            if (timeLimit > 10)
            {
                timeLimit--;
                timeLabel.Content = string.Format("0{0}:{1}", timeLimit / 60, timeLimit % 60);
            }
            else
            {
                timeLimit--;
                timeLabel.Content = string.Format("0{0}:0{1}", timeLimit / 60, timeLimit % 60);
            }
            if (timeLimit == 0)
            {
                exploreThread.Abort();
                timer.Stop();
                Console.WriteLine("Time is up");
                this.displayConsoleMessage("Time limit reached!");
            }
        }
        public void updateRobotPosition(int x, int y)
        {
            Application.Current.Dispatcher.BeginInvoke(
                System.Windows.Threading.DispatcherPriority.Background,
                new Action(delegate { drawMap(x, y); }));
        }
        public void drawMap(int x, int y)
        {
            var bc = new BrushConverter();
            this.mapGrid.Children.Clear();
            this.mapGrid.RowDefinitions.Clear();
            this.mapGrid.ColumnDefinitions.Clear();
            setUpMap();
            Map robotMemory = robot.Memory;
            for (int i = 0; i < robotMemory.Grid.GetLength(0); i++)
            {
                for (int j = 0; j < robotMemory.Grid.GetLength(1); j++)
                {
                    Label label = new Label();
                    if (i < 3 && j < 3 || i > 16 && j > 11)
                    {
                        continue;
                    }
                    if (robotMemory.Grid[i, j].Status == 1)
                    {
                        label.Background = (Brush)bc.ConvertFrom("#FF952900");
                    }
                    if (robotMemory.Grid[i, j].Status == 2)
                    {
                        label.Background = (Brush)bc.ConvertFrom("#FF1EDED5");
                    }
                    Grid.SetColumn(label, j);
                    Grid.SetRow(label, 19 - i);
                    this.mapGrid.Children.Add(label);
                }
            }
            //draw robot
            for (int i = x - 1; i <= x + 1; i++)
            {
                for (int j = y - 1; j <= y + 1; j++)
                {
                    Label label = this.mapGrid.Children.Cast<Label>().First(e => Grid.GetRow(e) == 19 - j && Grid.GetColumn(e) == i);
                    label.Background = (Brush)bc.ConvertFrom("#FF171361");
                }
            }
            //update index
            this.xLabel.Content = this.robot.X.ToString();
            this.yLabel.Content = this.robot.Y.ToString();
            this.speedLabel.Content = UserSetting.Speed.ToString();
            double currentCoverage = this.simulator.getCoverage();
            this.coverageLabel.Content = String.Format("{0:0.00}", currentCoverage) + " %";
        }

        private void runButton_Click(object sender, RoutedEventArgs e)
        {
            if (this.simulator == null || !this.simulator.isExplored())
            {
                displayConsoleMessage("Maze is not explored yet! Explore before conducting fastest run!");
                return;
            }
            displayConsoleMessage("Computing shortest path.....");       
            Thread fastestRunThread = new Thread(this.simulator.simulateFastestRun);
            fastestRunThread.Start();
            timer.Stop();
        }

        private void dfsExplore_Click(object sender, RoutedEventArgs e)
        {
            this.displayConsoleMessage("Exploring using DFS...");
            this.robot = new Robot();
            this.map = new Map(mapDescriptor);
            this.robot.ChangePosition += new Robot.RobotMovingHandler(updateRobotPosition);
            this.robot.SendingMessage += new Robot.RobotSendingMessage(displayRobotMessage);
            this.simulator = new Simulator(robot, map);
            this.timeLimit = UserSetting.TimeLimit;
            this.coverageLimit = UserSetting.CoverageLimit;
            timer.Interval = new TimeSpan(0, 0, 1);
            timer.Tick += new EventHandler(timer_Tick);
            timer.Start();
            exploreThread = new Thread(this.simulator.test);
            exploreThread.Start();
        }
        private void displayRobotMessage(string s)
        {
            Application.Current.Dispatcher.BeginInvoke(
                System.Windows.Threading.DispatcherPriority.Background,
                new Action(delegate { displayConsoleMessage(s); }));
        }
        private void displayConsoleMessage(string s)
        {
            this.consoleBlock.Inlines.Add(new LineBreak());
            this.consoleBlock.Inlines.Add(new LineBreak());
            this.consoleBlock.Inlines.Add(s);
            this.scrollViewer.ScrollToBottom();
        }

        private void settingsButton_Click(object sender, RoutedEventArgs e)
        {
            Settings settings = new Settings();
            if (settings.ShowDialog() == true)
            {
                UserSetting.Speed = settings.getSpeed();
                UserSetting.TimeLimit = settings.getTimeLimit();
                UserSetting.CoverageLimit = settings.getCoverageLimit();

                Console.WriteLine("Speed = " + settings.getSpeed());
                Console.WriteLine("Time = " + settings.getTimeLimit());
                Console.WriteLine("Coverage = " + settings.getCoverageLimit());
                this.timeLimit = UserSetting.TimeLimit;
                if (timeLimit > 10)
                {
                    timeLabel.Content = string.Format("0{0}:{1}", timeLimit / 60, timeLimit % 60);
                }
                else
                {
                    timeLabel.Content = string.Format("0{0}:0{1}", timeLimit / 60, timeLimit % 60);
                }
                this.speedLabel.Content = UserSetting.Speed.ToString();
                this.displayConsoleMessage("User settings changed!");
            }
        }

        private void connectButton_Click(object sender, RoutedEventArgs e)
        {
            if (this.Connector.connect())
            {
                this.displayConsoleMessage("Connected to RPI!");
            }
            else
            {
                this.displayConsoleMessage("Cannot establish connection!");
            }

        }

    }
}
