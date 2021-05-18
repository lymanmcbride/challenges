using System;
using System.Collections.Generic;

namespace Brackets
{
    public class Program
    {

        static void Main()
        {
            string brackets = "{akls{()()zyx}";
            Console.WriteLine(Program.TestBrackets(brackets));
            Console.ReadLine();
        }

        public static bool TestBrackets(string brackets)
        {
            string completeBrackets = "{}";
            var stack = new Stack<char>();
            foreach (char bracket in brackets)
            {
                if (bracket == completeBrackets[0])
                {
                    stack.Push(bracket);
                }
                else if (bracket == completeBrackets[1])
                {
                    if (stack.Count == 0 || $"{stack.Pop()}{bracket}" != completeBrackets)
                    {
                        return false;
                    }
                }
            }
            if (stack.Count == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
            
        }
    }
}
