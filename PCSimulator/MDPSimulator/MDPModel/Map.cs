using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MDPModel
{
    public class Map
    {
        public const int width = 15;
        public const int height = 20;
        private Cell[,] grid;
        
        public Cell[,] Grid
        {
            get { return this.grid; }
        }
        public Map(int[,] data)
        {
            grid = new Cell[height, width];
            for (int i = 0; i < data.GetLength(0); i++)
            {
                for (int j = 0; j < data.GetLength(1); j++)
                {
                    if (data[i, j] == 0)
                    {
                        this.grid[i, j] = new Cell(0);
                    }
                    else
                    {
                        this.grid[i, j] = new Cell(1);
                    }
                }
            }
        }
        public void print()
        {
            for (int i = 0; i < this.Grid.GetLength(0); i++)
            {
                for (int j = 0; j < this.Grid.GetLength(1); j++)
                {
                    Console.Write(this.Grid[this.Grid.GetLength(0) - i - 1, j].Status);
                    Console.Write(" ");
                }
                Console.WriteLine();
            }
        }

        public void saveToHardDrive()
        {

        }
    }
}
