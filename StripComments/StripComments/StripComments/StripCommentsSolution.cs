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
            bool add = true;
            foreach (var character in text)
            {
                if (string.IsNullOrEmpty(returnText))
                {
                    
                }
                if (commentSymbols.Any(x=> x.Contains(character)))
                {
                    add = false;
                }
                else if (!add)
                {
                    if (character == '\n')
                    {
                        add = true;
                    }
                }
                if (add)
                {
                    returnText += character;
                }
            }
            
            return returnText;
        }
    }
}