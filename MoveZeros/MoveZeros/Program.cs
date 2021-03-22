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
            //initialize original array and array we will append to.
            //I think I could have done this with arrays instead of lists, but that's where I ended up. 
            List<object> array = new List<object>() { false, 1, 0, 1, 2, 0, 1, 3, "a" };
            List<object> newArray = new List<object>();

            //Write out the array to see the original
            foreach (object item in array)
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();

            //the algorithm
            int zeroCount = 0;//how many zeros found. will use at end to append 0s onto new list.
            for (int i = 0; i < array.Count; i++) 
            {
                if (array[i] is bool)//bool converts to 0 or 1, so had to check for this specifically
                {
                    newArray.Add(array[i]);
                }
                else
                {
                    try //use try catch block to find only convertable types.
                    {
                        int int_item = Convert.ToInt32(array[i]); //convert from object to int
                        if (int_item == 0)
                        {
                            zeroCount++; //add to our zero count.
                        }
                        else
                        {
                            newArray.Add(array[i]); //append other numbers
                        }
                    }
                    catch (Exception) //anything else, just append
                    {
                        newArray.Add(array[i]);
                    }
                }
            }
            for (int i = zeroCount; i > 0; i--) //use our zero count variable to add 0s onto the end
            {
                newArray.Add(0);
            }

            foreach (object item in newArray) //print the new array.
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();
        }
    }
}
