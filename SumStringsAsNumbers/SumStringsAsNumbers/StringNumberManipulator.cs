using System;
using System.Text;

namespace SumStringsAsNumbers
{
    public static class StringNumberManipulator
    {
        public static string sumStrings(string number1, string number2)
        {
            StringBuilder summedNumbers = new StringBuilder();
            int remainder = 0;
            int number2Index = number2.Length - 1;
            for (int number1Index = number1.Length - 1; number1Index >= 0 || number2Index >= 0; number1Index--, number2Index--)
            {
                int addedDigits = GetValueToAdd(number1, number1Index) + GetValueToAdd(number2, number2Index);
                addedDigits += remainder;
                remainder = 0;
                if (addedDigits > 9)
                {
                    addedDigits -= 10;
                    remainder = 1;
                }
                
                summedNumbers.Insert(0, addedDigits);
            }

            if (remainder > 0)
            {
                summedNumbers.Insert(0, remainder);
            }

            while (summedNumbers[0] == '0')
            {
                summedNumbers.Remove(0, 1);
            }
            return summedNumbers.ToString();
        }

        private static int GetValueToAdd(string number, int index)
        {
            return index < 0 ? 0 : Convert.ToInt32(char.GetNumericValue(number[index]));
        }
    }
}