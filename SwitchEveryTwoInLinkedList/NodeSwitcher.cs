namespace SwitchEveryTwoInLinkedList;

public static class NodeSwitcher
{
    public static Node? SwitchNodes(Node? head)
    {
        Node? newHead = head;
        var isNewHeadFound = false;
        Node? previousNode = null;
        while (head?.Next != null)
        {
            var node2 = head.Next;
            var node3 = node2.Next;
            node2.Next = head;
            head.Next = node3;
            if (previousNode != null)
            {
                previousNode.Next = node2;
            }

            if (!isNewHeadFound)
            {
                newHead = node2;
                isNewHeadFound = true;
            }

            previousNode = head;
            head = node3;
        }

        return newHead;
    }
}

public class Node
{
    public char Value { get; set; }
    public Node? Next { get; set; }
}