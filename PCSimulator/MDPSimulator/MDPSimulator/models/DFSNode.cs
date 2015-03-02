using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MDPModel
{
    public class DFSNode:System.Object
    {
        public int X { get; set; }
        public int Y { get; set; }
        public DFSNode RightChild { get; set; }
        public DFSNode TopChild { get; set; }
        public DFSNode LeftChild { get; set; }
        public DFSNode BottomChild { get; set; }
        public bool isVisited { get; set; }
        public DFSNode(int x, int y)
        {
            this.X = x;
            this.Y = y;
            isVisited = false;
        }
        public void print()
        {
            Console.WriteLine("Current Node at X = {0}, Y = {1}", this.X, this.Y);
        }

        public override bool Equals(Object other)
        {
            if (other == null || !this.GetType().Equals(other.GetType()))
                return false;
            else
            {
                DFSNode n = (DFSNode)other;
                return (n.X == this.X) && (n.Y == this.Y);
            }

        }
    }
}
