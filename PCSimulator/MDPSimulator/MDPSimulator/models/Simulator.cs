using System;
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
        public double computeCoverage()
        {
            Map robotMemory = this.Robot.Memory;
            int firstDm = robotMemory.Grid.GetLength(0);
            int secondDm = robotMemory.Grid.GetLength(1);
            int explored = 0;
            for (int i = 0; i < firstDm; i++)
            {
                for (int j = 0; j < secondDm; j++)
                {
                    if (robotMemory.Grid[i, j].Status != 0)
                    {
                        explored++;
                    }
                }
            }
            return (double)explored/(firstDm*secondDm)*100;
        }
    }
}
