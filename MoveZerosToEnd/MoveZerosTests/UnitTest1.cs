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
    }
}