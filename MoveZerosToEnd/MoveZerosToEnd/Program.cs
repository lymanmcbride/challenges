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
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == 0)
                {
                    int temp = arr[i];
                    if (arr.Length > 0)
                    {
                        int currentIndex = i;
                        while (currentIndex < arr.Length - 1)
                        {
                            arr[currentIndex] = arr[currentIndex + 1];
                            currentIndex++;
                        }
                        arr[^1] = temp;
                    }
                } 
            }
            return arr;
        }
    }
}