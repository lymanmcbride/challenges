using System;
using System.Collections.Generic;

namespace Brackets
{
    public class Program
    {

        static void Main()
        {
            //test cases
            string test1 = "{akls{()()zyx}";
            string test2 = "{()}";
            string test3 = "}{)";
            string test4 = "{{}()";
            string test5 = "\"";

            //write out test cases to view clearly on console
            Console.WriteLine("Testing using Stack Structure:");
            Console.WriteLine("{akls{()()zyx} should be False: " + $"{Program.TestBrackets(test1)}");
            Console.WriteLine("{} should be True: " + $"{Program.TestBrackets(test2)}");
            Console.WriteLine("}{ should be False: " + $"{Program.TestBrackets(test3)}");
            Console.WriteLine("{{} should be False: " + $"{Program.TestBrackets(test4)}");
            Console.WriteLine("\" should be True: " + $"{Program.TestBrackets(test5)}");
            Console.ReadLine();
            Console.WriteLine("Testing using just int counter:");
            Console.WriteLine("{akls{()()zyx} should be False: " + $"{Program.TestBracketsSimple(test1)}");
            Console.WriteLine("{} should be True: " + $"{Program.TestBracketsSimple(test2)}");
            Console.WriteLine("}{ should be False: " + $"{Program.TestBracketsSimple(test3)}");
            Console.WriteLine("{{} should be False: " + $"{Program.TestBracketsSimple(test4)}");
            Console.WriteLine("\" should be True: " + $"{Program.TestBracketsSimple(test5)}");
            Console.ReadLine();
        }

        public static bool TestBrackets(string brackets)
        {
            string completeBrackets = "{}()";
            string openBrackets = "{(";
            //using a stack to track open brackets
            var stack = new Stack<char>();
            foreach (char bracket in brackets)
            {
                //if open bracket
                if (openBrackets.Contains(bracket))
                {
                    stack.Push(bracket);
                }
                //if close bracket
                else if (completeBrackets.Contains(bracket))
                {
                    //checks first for stack empty,
                    //then whether matching it with the first item on the stack makes a complete bracket
                    if (stack.Count == 0 || !completeBrackets.Contains($"{stack.Pop()}{bracket}"))
                    {
                        return false;
                    }
                }
            }
            return true ? stack.Count == 0 : false;
        }

        public static bool TestBracketsSimple(string brackets)
        {
            int openBrackets = 0;
            foreach (char bracket in brackets)
            {
                //if open bracket
                if (bracket == '{' ) { openBrackets += 1; }

                //if close bracket
                else if (bracket == '}')
                {
                    //checks first for if open bracket available, then subtracts from it.
                    if (openBrackets == 0) { return false; }
                    openBrackets -= 1;
                }
            }

            //if arrive back to 0, the brackets match up
            return true ? openBrackets == 0 : false;
        }
    }
}
