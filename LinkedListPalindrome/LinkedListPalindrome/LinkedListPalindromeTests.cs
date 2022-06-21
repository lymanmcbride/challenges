using System.Collections.Generic;
using NUnit.Framework;

namespace LinkedListPalindrome
{
    [TestFixture]
    public class LinkedListPalindromeTests
    {
        private readonly LinkedListUtility _linkedListUtility;

        public LinkedListPalindromeTests()
        {
            _linkedListUtility = new LinkedListUtility();
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnTrueForPalindromeEvenLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1, 2, 2, 1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.True(isPalindrome);
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnFalseForNonPalindromeEvenLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1, 3, 2, 1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.False(isPalindrome);
        }
                
        [Test]
        public void IsPalindrome_ShouldReturnTrueForOneItemInList()
        {
            List<int> palindromicList = new List<int>()
            {
                1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.True(isPalindrome);
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnTrueForPalindromeOddLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1,3,5,3,1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.True(isPalindrome);
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnFalseForNonPalindromeOddLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1,3,5,4,1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.False(isPalindrome);
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnFalseForNonPalindromeLongLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1,3,5,7,9,11,13,15,12,11,9,7,5,3,1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.False(isPalindrome);
        }
        
        [Test]
        public void IsPalindrome_ShouldReturnTrueForPalindromeLongLength()
        {
            List<int> palindromicList = new List<int>()
            {
                1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.IsTrue(isPalindrome);
        }
    }
}