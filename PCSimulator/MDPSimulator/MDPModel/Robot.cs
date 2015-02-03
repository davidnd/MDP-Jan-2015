using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MDPModel
{
    class Robot
    {
        private int xCoordinate;
        private int yCoordinate;
        private int range;
        private char dir;
        public int X
        {
            get { return xCoordinate; }
            set { this.xCoordinate = value; }
        }
        public int Y
        {
            get { return yCoordinate; }
            set { this.yCoordinate = value; }
        }
        public int Dir
        {
            get { return this.dir; }
        }
        public Robot(int x, int y, int r, char d)
        {
            this.xCoordinate = x;
            this.yCoordinate = y;
            this.range = r;
            this.dir = d;
        }
        public void turnLeft()
        {
            switch (this.dir)
            {
                case 'U':
                    this.dir = 'L';
                    break;
                case 'D':
                    this.dir = 'R';
                    break;
                case 'R':
                    this.dir = 'U';
                    break;
                case 'L':
                    this.dir = 'D';
                    break;
                default:
                    break;
            }
        }
        public void turnRight()
        {
            switch (this.dir)
            {
                case 'U':
                    this.dir = 'R';
                    break;
                case 'D':
                    this.dir = 'L';
                    break;
                case 'R':
                    this.dir = 'D';
                    break;
                case 'L':
                    this.dir = 'U';
                    break;
                default:
                    break;
            }
        }

        public void moveForward(int dis)
        {
            switch (this.dir)
            {
                case 'U':
                    this.Y+=dis;
                    break;
                case 'D':
                    this.Y-=dis;
                    break;
                case 'R':
                    this.X+=dis;
                    break;
                case 'L':
                    this.X-=dis;
                    break;
                default:
                    break;
            }
        }
    }
}
