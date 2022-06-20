using System;
using NUnit.Framework;

namespace TestProject1
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void CreateFizzBuzzResponse_ShouldReturnFizzForNumberDivisibleByThree()
        {
            const int numberDivisibleByThree = 3;
            const string expectedResponse = "fizz";

            var fizzBuzzResponse = FizzBuzz.CreateFizzBuzzResponse(numberDivisibleByThree);
            
            Assert.AreEqual(expectedResponse, fizzBuzzResponse);
        }
        
        [Test]
        public void CreateFizzBuzzResponse_ShouldThrowExceptionForNonFizzBuzzNumber()
        {
            const int nonFizzBuzzNumber = 2;

            Assert.Throws<FizzBuzzException>(() => FizzBuzz.CreateFizzBuzzResponse(nonFizzBuzzNumber));
        }
        
        [Test]
        public void CreateFizzBuzzResponse_ShouldThrowExceptionForNonFizzBuzzNumber1()
        {
            const int nonFizzBuzzNumber = 2;
            const string exceptionMessage = "Number is not divisible by 3 or 5";

            void Response() => FizzBuzz.CreateFizzBuzzResponse(nonFizzBuzzNumber);

            Exception ex = Assert.Throws<FizzBuzzException>(Response);
            Assert.AreEqual(exceptionMessage, ex.Message);
        }
    }
}