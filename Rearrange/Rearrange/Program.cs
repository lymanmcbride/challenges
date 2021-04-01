//Write a function that takes in 2 strings.
//If at least a portion of the first string can be rearranged to form the second string, return true.
//Otherwise, return false. No punctuation or numbers will be used as input.
//
//4/1/2021.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Rearrange
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Enter a word");
            string word1 = Console.ReadLine().ToLower();
            Console.WriteLine("Enter another word");
            string word2 = Console.ReadLine().ToLower();

            Console.WriteLine(rearrange(word1, word2));
            Main();

        }
        public static bool rearrange(string string1, string string2)
        {
            foreach (char letter in string2)
            {
                if (string1.Contains(letter))//if the letter is in the first word
                {
                    //if there are more of this letter in the second word then the first word
                    if (string2.Count(f => f == letter) > string1.Count(f => f == letter)) 
                    {
                        return false;
                    }
                    continue;
                }
                else //if the letter is not found in the first word
                {
                    return false;
                }
            }
            return true; //if we get to this, it passed all of the logic. 
        }
    }
}
