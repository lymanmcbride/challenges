using System;


// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
// Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}
namespace MoveZerosToEnd
{
    public static class Kata
    {
        static void Main(string[] args)
        {
        }

        public static int[] MoveZeroes(int[] arr)
        {
            int currentIndex = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[currentIndex] == 0)
                {
                    int temp = arr[currentIndex];
                    if (arr.Length > 0)
                    {
                        int tempIndex = currentIndex;
                        while (tempIndex < arr.Length - 1)
                        {
                            arr[tempIndex] = arr[tempIndex + 1];
                            tempIndex++;
                        }
                        arr[^1] = temp;
                    }
                }
                else
                {
                    currentIndex++;
                }
            }
            return arr;
        }
    }
}