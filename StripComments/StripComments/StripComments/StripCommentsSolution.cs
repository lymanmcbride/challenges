using System;
using System.Linq;

namespace StripComments
{
    public static class StripCommentsSolution
    {
        static void Main(string[] args)
        {
        }

        public static string StripComments(string text, string[] commentSymbols)
        {
            Console.WriteLine(text+"\n\n\n");
            foreach (string symbol in commentSymbols)
            {
                Console.WriteLine(symbol);
            }
            string returnText = "";
            string line = "";
            bool add = true;
            for (int i = 0; i < text.Length; i++)
            {
                if (commentSymbols.Any(x=> x.Contains(text[i])))
                {
                    add = false;
                }
                else if (!add)
                {
                    if (text[i] == '\n')
                    {
                        line = TrimEnd(line);
                        returnText += $"{line}{text[i]}";
                        line = "";
                        add = true;
                    }
                }
                else
                {
                    if (text[i] == '\n')
                    {
                        line = TrimEnd(line);
                        returnText += $"{line}{text[i]}";
                        line = "";
                    }
                    else
                    {
                        line += text[i];
                    }
                }
                if (i == text.Length-1)
                {
                    returnText += line.Trim();
                }

            }
            
            return returnText;
        }

        private static string TrimEnd(string line)
        {
            while (line[line.Length - 1] == ' ')
            {
                line = line.Substring(0, line.Length - 1);
            }

            return line;
        }
    }
}