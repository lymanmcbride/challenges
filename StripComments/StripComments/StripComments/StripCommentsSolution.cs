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
                        returnText += $"{line.Trim()}{text[i]}";
                        line = "";
                        add = true;
                    }

                }
                else
                {
                    line += text[i];
                    if (text[i] == '\n')
                    {
                        returnText += $"{line.Trim()}{text[i]}";
                        line = "";
                        add = true;
                    }

                }
                if (i == text.Length-1)
                {
                    returnText += line.Trim();
                }


            }
            
            return returnText;
        }
    }
}