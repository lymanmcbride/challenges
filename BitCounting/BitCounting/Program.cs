using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BitCounting
{
    class Program
    {
        static void Main(string[] args)
        {
            //using .net
            int value = 10;
            string binary = Convert.ToString(value, 2);
            Console.WriteLine(binary);
            int bits = binary.Count(f => (f == (char)'1'));
            Console.WriteLine(bits);
            Console.ReadLine();

            //using strictly C#
            Console.WriteLine(binary);
            int bitCount = 0;
            foreach (char num in binary)
            {
                if (num == (char)'1')
                {
                    bitCount++;
                }
            }
            Console.WriteLine(bitCount);
            Console.ReadLine();
        }
    }
}
