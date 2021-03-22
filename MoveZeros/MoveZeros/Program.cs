using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MoveZeros
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> array = new List<object>() { false, 1, 0, 1, 2, 0, 1, 3, "a" };
            List<object> newArray = new List<object>();

            foreach (object item in array)
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();
            int zeroCount = 0;
            for (int i = 0; i < array.Count; i++)
            {
                if (array[i] is bool)
                {
                    newArray.Add(array[i]);
                }
                else
                {
                    try
                    {
                        int int_item = Convert.ToInt32(array[i]);
                        if (int_item == 0)
                        {
                            zeroCount++;
                        }
                        else
                        {
                            newArray.Add(array[i]);
                        }
                    }
                    catch (Exception)
                    {
                        newArray.Add(array[i]);
                    }
                }
            }
            for (int i = zeroCount; i > 0; i--)
            {
                newArray.Add(0);
            }

            foreach (object item in newArray)
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();
        }
    }
}
