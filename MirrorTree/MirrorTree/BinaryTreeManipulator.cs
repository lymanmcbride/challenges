using System.Collections;
using System.Collections.Generic;

namespace MirrorTree
{
    public class BinaryTreeManipulator
    {
        public TreeNode Root { get; set; }
        public void Add(int value)
        {
            TreeNode before = null, after = Root;
 
            while (after != null)
            {
                before = after;
                if (value < after.val) //Is new node in left tree? 
                    after = after.left; 
                else if (value > after.val) //Is new node in right tree?
                    after = after.right;
                else if (value == after.val)
                {
                    after = after.left;
                }
            }
 
            TreeNode newNode = new TreeNode
            {
                val = value
            };

            if (Root == null)//Tree ise empty
                Root = newNode;
            else
            {
                if (value < before.val)
                    before.left = newNode;
                else
                    before.right = newNode;
            }
 
        }

        public void CreateTree(List<int> nodeValues)
        {
            foreach (int value in nodeValues)
            {
                Add(value);
            }
        }
        public class TreeNode {
            public int val;
            public TreeNode left;
            public TreeNode right;

            public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
            {
                this.val = val;
                this.left = left;
                this.right = right;
            }
        }
        public bool IsSymmetric(TreeNode root)
        {
            Queue<int?> leftSideValues = new Queue<int?>();
            TraverseLeftSide(root.left, leftSideValues);
            
            return TraverseRightSide(root.right, leftSideValues);
        }

        private void TraverseLeftSide(TreeNode root, Queue<int?> leftSideValues)
        {
            if (root is null)
            {
                leftSideValues.Enqueue(null);
                return;
            }
            
            TraverseLeftSide(root.left, leftSideValues);
            TraverseLeftSide(root.right, leftSideValues);
            leftSideValues.Enqueue(root.val);
        }
        
        private bool TraverseRightSide(TreeNode root, Queue<int?> leftSideValues)
        {
            if (root is null)
                
                return leftSideValues.Count > 0 && leftSideValues.Dequeue() is null;
            
            bool rightNodeResult = TraverseRightSide(root.right, leftSideValues);
            if (!rightNodeResult)
                return false;
            bool leftNodeResult = TraverseRightSide(root.left, leftSideValues);
            if (!leftNodeResult)
                return false;

            return leftSideValues.Count > 0 && root.val == leftSideValues.Dequeue();
        }
    }
}