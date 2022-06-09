using System;
using NUnit.Framework;

namespace Roman_Numerals_To_Integer
{
    [TestFixture]
    public class RomanNumeralConverterTests
    {
        private readonly RomanNumeralConverter _romanNumeralConverter;
        public RomanNumeralConverterTests()
        {
            _romanNumeralConverter = new RomanNumeralConverter();
        }
        [Test]
        public void ShouldWorkIfTestCaseIsOnlyAddition()
        {
            const string romanNumeral = "XXVII";
            const int expectedInteger = 27;
            Assert.True(_romanNumeralConverter.ConvertToInteger(romanNumeral) == expectedInteger);
        }
        [Test]
        public void ShouldWorkIfTestCaseIsSimpleSubtraction()
        {
            const string romanNumeral = "IV";
            const int expectedInteger = 4;
            Assert.True(_romanNumeralConverter.ConvertToInteger(romanNumeral) == expectedInteger);
        }
        
        [Test]
        public void ShouldWorkIfTestCaseIsAdditionAndOneSubtraction()
        {
            const string romanNumeral = "XIV";
            const int expectedInteger = 14;
            Assert.True(_romanNumeralConverter.ConvertToInteger(romanNumeral) == expectedInteger);
        }
        
                
        [Test]
        public void ShouldWorkIfTestCaseHasComplicatedAdditionAndSubtraction()
        {
            const string romanNumeral = "MCMXCIV";
            const int expectedInteger = 1994;
            Assert.True(_romanNumeralConverter.ConvertToInteger(romanNumeral) == expectedInteger);
        }
    }
}