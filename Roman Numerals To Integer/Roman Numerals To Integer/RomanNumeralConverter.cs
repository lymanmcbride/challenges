using System.Collections.Generic;

namespace Roman_Numerals_To_Integer
{
    public class RomanNumeralConverter
    {
        public int ConvertToInteger(string romanNumeral) 
        {
            Dictionary<string, int> romanNumeralMappings = new Dictionary<string, int>()
            {
                {"I",1},
                {"V", 5},
                {"X", 10},
                {"L", 50},
                {"C", 100},
                {"D", 500},
                {"M", 1000},
            };
            return romanNumeralMappings[romanNumeral];
        }
    }
}