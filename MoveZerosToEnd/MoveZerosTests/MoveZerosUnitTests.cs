using MoveZerosToEnd;
using NUnit.Framework;

namespace MoveZerosTests
{
    public class Tests
    {
        [Test]
        public void StandardPass()
        {
            // Arrange
            int[] controlArray = new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0};
            int[] testArray = new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }

        [Test]
        public void AllZeros()
        {
            // Arrange
            int[] controlArray = new int[] {0,0,0,0, 0, 0, 0, 0};
            int[] testArray = new int[] {0,0,0,0,0,0,0,0};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
        
        [Test]
        public void OneZero()
        {
            // Arrange
            int[] controlArray = new int[] {0};
            int[] testArray = new int[] {0};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
        
        [Test]
        public void OneNumber()
        {
            // Arrange
            int[] controlArray = new int[] {2};
            int[] testArray = new int[] {2};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
        
        [Test]
        public void NoZeros()
        {
            // Arrange
            int[] controlArray = new int[] {1,2,3,4,5,6,7};
            int[] testArray = new int[] {1,2,3,4,5,6,7};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
        
        [Test]
        public void EmptyArrays()
        {
            // Arrange
            int[] controlArray = new int[]{};
            int[] testArray = new int[]{};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
        [Test]
        public void ArraysNumberTwo()
        {
            // Arrange
            int[] controlArray = new int[]{1,2,3,4,5,6,7,0,0,0,0};
            int[] testArray = new int[]{1,0,2,0,3,4,5,6,0,7,0};
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }

        [Test]
        public void LongArray()
        {
            // Arrange
            int[] testArray = new int[]
            {
                3, 3, 0, 3, 2, 3, 3, 1, 5, 1, 5, 3, 0, 5, 5, 4, 0, 5, 3, 0, 2, 1, 0, 1, 3, 0, 3, 5, 0, 2, 3, 0, 0, 3, 1,
                5, 4, 1, 4, 3, 4, 2, 3, 0, 4, 5, 1, 0, 1, 1, 4, 1, 3, 5
            };
            int[] controlArray = new int[]
            {
                3, 3, 3, 2, 3, 3, 1, 5, 1, 5, 3, 5, 5, 4, 5, 3, 2, 1, 1, 3, 3, 5, 2, 3, 3, 1,
                5, 4, 1, 4, 3, 4, 2, 3, 4, 5, 1, 1, 1, 4, 1, 3, 5,0,0,0,0,0,0,0,0,0,0,0
            };
            // Act
            Kata.MoveZeroes(testArray);
            // Assert
            Assert.AreEqual(controlArray, testArray);
        }
    }
}