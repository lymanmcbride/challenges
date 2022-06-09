using System;
using System.Collections.Generic;
using System.Linq;

namespace Roman_Numerals_To_Integer
{
    public class RomanNumeralConverter
    {
        public int ConvertToInteger(string romanNumeral)
        {
            int result = 0;

            for (int i = 0; i < romanNumeral.Length; i++)
            {
                char currentLetter = romanNumeral[i];
                if (i != romanNumeral.Length - 1 && CheckForSubtractionCase(currentLetter, romanNumeral[i + 1]))
                {
                    result += RomanNumeralMappings.RomanNumeralToInteger[romanNumeral[i + 1]] -
                              RomanNumeralMappings.RomanNumeralToInteger[romanNumeral[i]];
                    i++;
                }
                else
                {
                    result += RomanNumeralMappings.RomanNumeralToInteger[currentLetter];
                }
            }
            
            return result;
        }

        private bool CheckForSubtractionCase(char currentCharacter, char nextCharacter)
        {
            bool subtractionCaseExists = false;
            if (RomanNumeralMappings.SubtractingNumerals.ContainsKey(currentCharacter))
            {
                if (RomanNumeralMappings.SubtractingNumerals[currentCharacter].Contains(nextCharacter))
                {
                    subtractionCaseExists = true;
                }
            }

            return subtractionCaseExists;
        }

        private static class RomanNumeralMappings
        {
            public static readonly Dictionary<char, int> RomanNumeralToInteger = new Dictionary<char, int>
            {
                {'I',1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000},
            };

            public static readonly Dictionary<char, char[]> SubtractingNumerals = new Dictionary<char, char[]>
            {
                { 'I', new[] { 'V', 'X' } },
                { 'X', new[] { 'L', 'C' } },
                { 'C', new[] { 'D', 'M' } },
            };
        }
    }
}