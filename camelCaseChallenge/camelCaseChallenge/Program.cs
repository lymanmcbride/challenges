using System;
using System.Globalization;

namespace camelCaseChallenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = "the_stealth_warrior";
            string[] words = str.Replace('-', ' ').Replace('_', ' ').Split(" ");
            TextInfo myTI = new CultureInfo("en-US", false).TextInfo;
            for (int i = 0; i < words.Length; i++)
            {
                if (i != 0)
                {
                    words[i] = myTI.ToTitleCase(words[i]);
                }
            }
            string returnString = String.Join("", words);
            Console.WriteLine(returnString);
            Console.ReadLine();
        }
    }
}
