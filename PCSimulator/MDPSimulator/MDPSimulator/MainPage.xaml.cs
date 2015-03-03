﻿using System;
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
        public MainPage()
        {
            InitializeComponent();
            setUpMap();

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
            //Array.Clear(arena, 0, arena.Length);
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
            //robot.RobotMoving += new EventHandler(updateRobotPosition);
            this.map = new Map(mapDescriptor);
            this.robot.ChangePosition += new Robot.RobotMovingHandler(updateRobotPosition);
            this.simulator = new Simulator(robot, map);
            Thread thread = new Thread(this.simulator.simulateExplore);
            thread.Start();
            //this.simulator.simulateExplore() ;
        }
        public void updateRobotPosition(int x, int y)
        {
            //Console.WriteLine("Inside main thread");
            //Console.WriteLine("X: {0}", x);
            //Console.WriteLine("Y: {0}", y);
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
                    if(i<3 && j < 3 || i>16 && j>11)
                    {
                        //Grid.SetColumn(label, j);
                        //Grid.SetRow(label, 19 - i);
                        //this.mapGrid.Children.Add(label);
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
            for (int i = x-1; i <= x+1; i++)
            {
                for (int j = y-1; j <= y+1; j++)
                {
                    Label label = this.mapGrid.Children.Cast<Label>().First(e => Grid.GetRow(e) == 19 - j && Grid.GetColumn(e) == i);
                    label.Background = (Brush)bc.ConvertFrom("#FF171361");
                }
            }
            //draw maze

        }
        private void robotMovingHandler(object sender, PropertyChangedEventArgs ev)
        {
            Robot robot = (Robot)sender;
            int x = robot.X;
            int y = robot.Y;
            //displayRobotPos(robot.X, robot.Y);
            var bc = new BrushConverter();
            Label label = mapGrid.Children.Cast<Label>().First(e => Grid.GetRow(e) == 19 - y && Grid.GetColumn(e) == x);
            label.Background = (Brush)bc.ConvertFrom("#FF171361");
        }

        private void runButton_Click(object sender, RoutedEventArgs e)
        {
            Thread thread = new Thread(this.simulator.simulateFastestRun);
            thread.Start();
        }

        private void testButton_Click(object sender, RoutedEventArgs e)
        {
            this.robot = new Robot();
            //robot.RobotMoving += new EventHandler(updateRobotPosition);
            this.map = new Map(mapDescriptor);
            this.robot.ChangePosition += new Robot.RobotMovingHandler(updateRobotPosition);
            this.simulator = new Simulator(robot, map);
            Thread thread = new Thread(this.simulator.test);
            thread.Start();
            //this.simulator.simulateExplore() ;
        }

        private void settingsButton_Click(object sender, RoutedEventArgs e)
        {
            Settings settings = new Settings();
            settings.Show();
        }

    }
}
