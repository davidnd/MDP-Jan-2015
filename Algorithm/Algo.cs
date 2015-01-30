using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MDPModel;
namespace MDPSimulator
{
    class Algo
    {
        private static int[,] virtualMap = new int[Map.height, Map.width];
        private static int[,] fullDottedMap = new int[Map.height+1, Map.width+1];
        private static int[,] movableDottedMap = new int[Map.height - 1, Map.width - 1];
        private static int[,] exploredMap = new int[movableDottedMap.GetLength(0), movableDottedMap.GetLength(1)];
        private static int xStart = 0, yStart = 0, xGoal = movableDottedMap.GetLength(1), yGoal = movableDottedMap.GetLength(0);
        public static void explore(int[,] map)
        {
            //virtual wall and boundaries of obstacles.
            preprocess(map);
            exploreDottedMap(movableDottedMap);
            Console.WriteLine("==========Explored map============");
            printMap(exploredMap);
        }

        public static void fastestRun(int[,] map)
        {

        }

        public static void preprocess(int [,] map)
        {
            for (int i = 0; i < Map.height; i++)
            {
                for (int j = 0; j < Map.width; j++)
                {
                    if (i == 0 || j == 0 || i == Map.height-1 || j == Map.width-1)
                    {
                        //virtual wall
                        virtualMap[i, j] = 1;
                    }
                    if (map[i, j] == 1)
                    {
                        for (int m = i-1; m <= i+1; m++)
                        {
                            for (int n = j-1; n <= j+1; n++)
                            {
                                if (m < 0 || n < 0 || m>Map.height-1 || n>Map.width-1)
                                    continue;
                                try
                                {
                                    virtualMap[m, n] = 1;
                                }
                                catch (Exception exc)
                                {
                                    Console.WriteLine(exc.Message);
                                    Console.WriteLine("{0}, {1}", m, n);
                                }
                            }
                        }
                        //fulllDotmap
                        fullDottedMap[i, j] = 1;
                        fullDottedMap[i + 1, j] = 1;
                        fullDottedMap[i, j + 1] = 1;
                        fullDottedMap[i + 1, j + 1] = 1;
                    }

                }
            }
            for (int i = 1; i < fullDottedMap.GetLength(0)-1; i++)
            {
                for (int j = 1; j < fullDottedMap.GetLength(1)-1; j++)
                {
                    movableDottedMap[i - 1, j - 1] = fullDottedMap[i, j];
                }
            }
            //Console.WriteLine("==========Full dotted map============");
            //printMap(fullDottedMap);
            Console.WriteLine("==========Movable dotted map============");
            printMap(movableDottedMap);
        }

        public static void printMap(int[,] map)
        {
            for (int i = 0; i < map.GetLength(0); i++)
            {
                for (int j = 0; j < map.GetLength(1); j++)
                {
                    Console.Write(map[map.GetLength(0)-i-1, j]);
                }
                Console.WriteLine();
            }
        }

        public static void exploreDottedMap(int[,] map)
        {
            //dirs are U, D, L, R
            char dir = 'R';
            int currentX = xStart;
            int currentY = yStart;
            exploredMap[currentX, currentY] = 1;
            do
            {
                try
                {
                    Console.WriteLine(dir);
                    Console.WriteLine("{0}, {1}", currentX, currentY);       
                    switch (dir)
                    {
                        case 'R':
                            {                         
                                if (currentY > 0 && map[currentX, currentY - 1] == 0)
                                {
                                    Console.WriteLine("heading down");
                                    dir = 'D';
                                    currentY--;
                                }
                                else if (currentX < map.GetLength(1) - 1 && map[currentX + 1, currentY] == 0)
                                {
                                    Console.WriteLine("keep heading right");
                                    currentX++;
                                }
                                else if (currentY < map.GetLength(0) - 1 && map[currentX, currentY + 1] == 0)
                                {
                                    currentY++;
                                    dir = 'U';
                                    Console.WriteLine("heading up");
                                }
                                else
                                {
                                    currentX--;
                                    dir = 'L';
                                    Console.WriteLine("heading left");
                                }
                                break;
                            }
                        case 'D':
                            {
                                if (currentX > 0 && map[currentX - 1, currentY] == 0)
                                {
                                    Console.WriteLine("heading down");
                                    dir = 'L';
                                    currentX--;
                                }
                                else if (currentY > 0 && map[currentX, currentY - 1] == 0)
                                {
                                    currentY--;
                                }
                                else if (currentX < map.GetLength(1) - 1 && map[currentX + 1, currentY] == 0)
                                {
                                    currentX++;
                                    dir = 'R';
                                }
                                else
                                {
                                    dir = 'U';
                                    currentY++;
                                }
                                break;
                            }
                        case 'L':
                            {
                                if (currentY < map.GetLength(0) - 1 && map[currentX, currentY + 1] == 0)
                                {
                                    dir = 'U';
                                    currentY++;
                                }
                                else if (currentX > 0 && map[currentX - 1, currentY] == 0)
                                {
                                    currentX--;
                                }
                                else if (currentY > 0 && map[currentX, currentY - 1] == 0)
                                {
                                    dir = 'D';
                                    currentY--;
                                }
                                else
                                {
                                    dir = 'R';
                                    currentX++;
                                }
                                break;
                            }
                        case 'U':
                            {
                                if (currentX < map.GetLength(1) - 1 && map[currentX + 1, currentY] == 0)
                                {
                                    dir = 'R';
                                    currentX++;
                                }
                                else if (currentY < map.GetLength(0) - 1 && map[currentX, currentY + 1] == 0)
                                {
                                    currentY++;
                                }
                                else if (currentX > 0 && map[currentX - 1, currentY] == 0)
                                {
                                    dir = 'L';
                                    currentX--;
                                }
                                else
                                {
                                    dir = 'D';
                                    currentY--;
                                }
                                break;
                            }
                        default:
                            break;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                
                exploredMap[currentX, currentY] = 1;
            } while (currentX != 0 || currentY != 0);
        }
    }
}
