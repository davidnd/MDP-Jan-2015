using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;
using System.Diagnostics;
namespace MDPModel
{
    public class Robot:INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;
        private int x;
        private int y;
        public int X
        {   get{return x;}
            set
            {
                x = value;
                OnPropertyChanged("X");
            }
        }

        
        public int Y 
        { 
            get {return this.y;} 
            set
            {
                this.y = value;
                OnPropertyChanged("Y");
            } 
        }
        public int Dir{ get;set; }

        public int Range { get; set; }

        public Map Env { get; set; }

        public Map Memory { get; set; }

        public Robot(int x, int y, int r, char d)
        {
            this.X = x;
            this.Y = y;
            this.Range = r;
            this.Dir = d;
            //empty memory for robot
            this.Memory = new Map();
        }

        public Robot()
        {
            this.X = 1;
            this.Y = 1;
            this.Range = 1;
            this.Dir = 'U';
            this.Memory = new Map();
        }


        public void turnLeft()
        {
            switch (this.Dir)
            {
                case 'U':
                    this.Dir = 'L';
                    break;
                case 'D':
                    this.Dir = 'R';
                    break;
                case 'R':
                    this.Dir = 'U';
                    break;
                case 'L':
                    this.Dir = 'D';
                    break;
                default:
                    break;
            }
        }

        public void turnRight()
        {
            switch (this.Dir)
            {
                case 'U':
                    this.Dir = 'R';
                    break;
                case 'D':
                    this.Dir = 'L';
                    break;
                case 'R':
                    this.Dir = 'D';
                    break;
                case 'L':
                    this.Dir = 'U';
                    break;
                default:
                    break;
            }
        }


        public void moveForward(int dis)
        {
            switch (this.Dir)
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

        public void turnAround()
        {
            switch (this.Dir)
            {
                case 'U':
                    this.Dir = 'D';
                    break;
                case 'D':
                    this.Dir = 'U';
                    break;
                case 'R':
                    this.Dir = 'L';
                    break;
                case 'L':
                    this.Dir = 'R';
                    break;
                default:
                    break;
            }
        }

        public void simulateExplore()
        {
            bool isBlockedLeft, isBlockedRight, isBlockedFront;
            //turnRight();
            bool moved = false;
            do
            {
                Console.WriteLine("Current X = {0}, Y = {1}", this.X, this.Y);
                try
                {
                    isBlockedFront = scanFront();
                    isBlockedLeft = scanLeft();
                    isBlockedRight = scanRight();
                    if (!isBlockedRight)
                    {
                        Console.WriteLine("Turn right");
                        turnRight();
                        moveForward(1);
                    }
                    else if (!isBlockedFront)
                    {
                        Console.WriteLine("Move");
                        moved = true;
                        moveForward(1);
                    }
                    else if (!isBlockedLeft)
                    {
                        Console.WriteLine("Turn left");
                        turnLeft();
                        moveForward(1);
                    }
                    else
                    {
                        Console.WriteLine("Turn around");
                        turnAround();
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            } while ((this.X != 1 || this.Y != 1) || !moved);
        }


        public bool scanFront()
        {
            switch (this.Dir)
            {
                case 'R':
                    return checkRightSide();
                case 'L':
                    return checkLeftSide();
                case 'U':
                    return checkUp();
                case 'D':
                    return checkDown();
                default:
                    return true;
            }    
        }

        public bool scanLeft()
        {
            switch (this.Dir)
            {
                case 'R':
                    return checkUp();
                case 'L':
                    return checkDown();
                case 'U':
                    return checkLeftSide();
                case 'D':
                    return checkRightSide();
                default:
                    return true;
            }
        }

        public bool scanRight()
        {
            switch (this.Dir)
            {
                case 'R':
                    return checkDown();
                case 'L':
                    return checkUp();
                case 'U':
                    return checkRightSide();
                case 'D':
                    return checkLeftSide();
                default:
                    return true;
            }
        }

        public bool checkUp()
        {
            bool isBlocked = false;
            if (this.Y + this.Range + 1 >= this.Env.Grid.GetLength(0))
                return true;
            int y = this.Y + this.Range + 1;
            for (int i = this.X - this.Range; i <= this.X + this.Range; i++)
            {
                if (this.Env.Grid[y, i].Status == 1)
                {
                    isBlocked = true;
                    //explored and has obstacle
                    this.Memory.Grid[y, i].Status = 1;
                }
                else
                {
                    //empty cell
                    this.Memory.Grid[y, i].Status = 2;
                }

            }
            return isBlocked;
        }

        
        public bool checkRightSide()
        {
            bool isBlocked = false;

            if (this.X + this.Range + 1 >= this.Env.Grid.GetLength(1))
                return true;
            int x = this.X + this.Range + 1;
            for (int i = this.Y - this.Range; i <= this.Y + this.Range; i++)
            {
                if (this.Env.Grid[i,x].Status == 1)
                {
                    isBlocked = true;
                    //explored and has obstacle
                    this.Memory.Grid[i, x].Status = 1;
                }
                else
                {
                    //empty cell
                    this.Memory.Grid[i, x].Status = 2;
                }
            }
            return isBlocked;
        }

        public bool checkLeftSide()
        {
            bool isBlocked = false;
            if (this.X - this.Range - 1 < 0)
                return true;
            int x = this.X - this.Range - 1;
            for (int i = this.Y - this.Range; i <= this.Y + this.Range; i++)
            {
                if (this.Env.Grid[i, x].Status == 1)
                {
                    isBlocked = true;
                    //explored and has obstacle
                    this.Memory.Grid[i, x].Status = 1;
                }
                else
                {
                    //empty cell
                    this.Memory.Grid[i, x].Status = 2;
                }
            }
            return isBlocked;
        }

        public bool checkDown()
        {
            bool isBlocked = false;
            if (this.Y - this.Range - 1 < 0)
                return true;
            int y = this.Y - this.Range - 1;
            for (int i = this.X - this.Range; i <= this.X + this.Range; i++)
            {
                if (this.Env.Grid[y, i].Status == 1)
                {
                    isBlocked = true;
                    //explored and has obstacle
                    this.Memory.Grid[y, i].Status = 1;
                }
                else
                {
                    //empty cell
                    this.Memory.Grid[y, i].Status = 2;
                }
            }
            return isBlocked;
        }

        private void OnPropertyChanged(string p)
        {
            PropertyChangedEventHandler handler = PropertyChanged;
            if (handler != null)
            {
                handler(this, new PropertyChangedEventArgs(p));
            }
        }
    }
}
