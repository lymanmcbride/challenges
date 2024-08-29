using System.Text;

namespace SwitchEveryTwoInLinkedList;

public class NodeSwitcherTests
{
    [Theory]
    [InlineData("clozed", "lczode")]
    [InlineData("clozd", "lczod")]
    [InlineData("c", "c")]
    [InlineData(null, "")]
    [InlineData("abcdefgh", "badcfehg")]
    [InlineData("abcdefg", "badcfeg")]
    public void SwitchNodes_WhenCalled_ShouldSwitchAllNodes(string input, string output)
    {
        var head = SetUpList(input);
        
        var result = NodeSwitcher.SwitchNodes(head);
        var finalString = GetResult(result);
        
        Assert.Equal(output, finalString);
    }

    private string GetResult(Node? head)
    {
        StringBuilder resultString = new StringBuilder();
        while (head != null)
        {
            resultString.Append(head.Value);
            head = head.Next;
        }

        return resultString.ToString();
    }

    private Node? SetUpList(string? word)
    {
        Node? workingNode = null;
        Node? previousNode = null;
        Node? head = workingNode;
        if (word != null)
            foreach (char character in word)
            {
                workingNode = new Node { Value = character };
                if (previousNode != null)
                {
                    previousNode.Next = workingNode;
                }
                else
                {
                    head = workingNode;
                }

                previousNode = workingNode;
            }

        return head;
    }
}