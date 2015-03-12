﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MDPModel
{
    public class Simulator
    {
        public Robot Robot { get; set; }
        public Map Map { get; set; }
        public Simulator()
        {
            this.Robot = new Robot(1, 1, 1,'U');
            this.Map = new Map();
        }
        public Simulator(Robot r)
        {
            this.Robot = r;
        }
        public Simulator(Robot r, Map m)
        {
            this.Robot = r;
            this.Map = m;
            this.Robot.Env = this.Map;
        }

        public void simulateExplore()
        {
            this.Robot.simulateExplore();
            this.Robot.Memory.print();
        }
        public void simulateFastestRun()
        {
            this.Robot.fastestRun();
        }
        public void test()
        {
            this.Robot.exploreWithDFS();
        }
        public double getCoverage()
        {
            return this.Robot.CurrentCoverage;
        }
        public bool isExplored()
        {
            return this.Robot.isExplored;
        }
        public void reset()
        {

        }
    }
}
