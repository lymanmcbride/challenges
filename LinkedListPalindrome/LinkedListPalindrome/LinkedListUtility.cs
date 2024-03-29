using System;
using System.Collections;
using System.Collections.Generic;

namespace LinkedListPalindrome
{
    
    public class ListNode 
    {
        public int val;
        public ListNode next;
        public ListNode(int val=0, ListNode next=null) 
        {
            this.val = val;
            this.next = next;
        }
    }

    public class LinkedList
    {
        public ListNode Head;
        public void InsertFront(int data)
        {
            ListNode node = new ListNode(data, Head);
            Head = node;
        }
    }
    
    public class LinkedListUtility
    {
        public ListNode CreateLinkedList(List<int> list)
        {
            LinkedList linkedList = new LinkedList();
            foreach (int number in list)
            {
                linkedList.InsertFront(number);
            }

            return linkedList.Head;
        }
        public bool IsPalindrome(ListNode head)
        {
            bool isPalindrome = true;
            var reverseList = new Stack<int>();
            int length = 0;
            ListNode tempHead = head;
            while (tempHead != null)
            {
                reverseList.Push(tempHead.val);
                length++;
                tempHead = tempHead.next;
            }

            var middle = length / 2;
            while (length >= middle && length > 0)
            {
                if (head.val != reverseList.Pop())
                {
                    isPalindrome = false;
                }

                head = head.next;
                length--;
            }
            return isPalindrome;
        }
    }
}