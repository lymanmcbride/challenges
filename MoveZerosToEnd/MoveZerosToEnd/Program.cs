using System;


// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
// Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}
namespace MoveZerosToEnd
{
    public static class Kata
    {
        public static int[] MoveZeroes(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == 0)
                {
                    int temp = arr[i];
                    if (arr.Length > 0)
                    {
                        int indexToReplace = arr.Length - 1;
                        while (arr[indexToReplace] == 0)
                        {
                            indexToReplace -= 1;
                        }

                        if (i < indexToReplace)
                        {
                            arr[i] = arr[indexToReplace];
                            arr[indexToReplace] = temp;
                        }
                    }
                } 
            }
            return arr;
        }
    }
}