using MoveZerosToEnd;
using NUnit.Framework;

namespace MoveZerosTests
{
    public class Tests
    {
        [Test]
        public void StandardPass()
        {
            Assert.AreEqual(new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}, Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}));
        }

        [Test]
        public void Test1()
        {
            Assert.Pass();
        }
    }
}