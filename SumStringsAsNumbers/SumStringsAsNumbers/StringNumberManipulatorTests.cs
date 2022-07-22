using NUnit.Framework;

namespace SumStringsAsNumbers
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedIfSameLength()
        {
            string number1 = "456";
            string number2 = "123";
            string expectedResult = "579";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
        
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedIfRemaindersExistForDigits()
        {
            string number1 = "99";
            string number2 = "99";
            string expectedResult = "198";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
        
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedIfDifferentLengths()
        {
            string number1 = "456";
            string number2 = "1";
            string expectedResult = "457";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
        
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedIfDifferentLengthsForLongNumbers()
        {
            string number1 = "1";
            string number2 = "45672345";
            string expectedResult = "45672346";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
        
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedForExtremelyLongNumbers()
        {
            string number1 = "78907262512344";
            string number2 = "3736525261718072625";
            string expectedResult = "3736604168980584969";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
        
        [Test]
        public void SumStrings_ShouldReturnStringValueOfNumbersSummedWithoutZerosAtBeginning()
        {
            string number1 = "0123";
            string number2 = "00123";
            string expectedResult = "246";
            
            Assert.AreEqual(expectedResult, StringNumberManipulator.sumStrings(number1, number2));
        }
    }
}