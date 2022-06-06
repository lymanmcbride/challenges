using System;
using NUnit.Framework;

namespace Roman_Numerals_To_Integer
{
    [TestFixture]
    public class RomanNumeralsToIntegerTests
    {
        private readonly RomanNumeralConverter _romanNumeralConverter;
        public RomanNumeralsToIntegerTests()
        {
            _romanNumeralConverter = new RomanNumeralConverter();
        }
        [Test]
        public void Test1()
        {
            string romanNumeral = "I";
            int expectedInteger = 1;
            Assert.True(_romanNumeralConverter.ConvertToInteger(romanNumeral) == expectedInteger);
        }
    }
}