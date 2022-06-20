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
        public void IsPalindrome_ShouldReturnTrue()
        {
            List<int> palindromicList = new List<int>()
            {
                1, 2, 2, 1
            };
            bool isPalindrome = _linkedListUtility.IsPalindrome(_linkedListUtility.CreateLinkedList(palindromicList));
            Assert.True(isPalindrome);
        }
    }
}