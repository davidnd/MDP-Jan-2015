﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MDPModel
{
    public class Node : IComparable<Node>
    {
        public int XNode { get; set; }
        public int YNode { get; set; }
        public int GCost { get; set; }
        public int FCost { get; set; }
        public int HCost { get; set; }
        public Node CameFrom { get; set; }
        public Node(int x, int y)
        {
            XNode = x;
            YNode = y;
            GCost = 0;
            HCost = 0;
            FCost = 0;
        }

        public override bool Equals(Object other)
        {
            if (other == null || !this.GetType().Equals(other.GetType())) 
                return false;
            else
            {
                Node n = (Node)other;
                return (n.XNode == this.XNode) && (n.YNode == this.YNode);
            }
            
        }

        public int CompareTo(Node other)
        {
            return this.FCost.CompareTo(other.FCost);
        }
        public void print()
        {
            Console.WriteLine("{0}, {1}", this.XNode, this.YNode);
        }
    }
}
