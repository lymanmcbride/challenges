using System;
using System.Collections.Generic;

namespace Sudoku
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine(ValidateSolution(new int[][]
            //    {
            //      new int[] {5, 3, 4, 6, 7, 8, 9, 1, 2},
            //      new int[] {6, 7, 2, 1, 9, 5, 3, 4, 8},
            //      new int[] {1, 9, 8, 3, 4, 2, 5, 6, 7},
            //      new int[] {8, 5, 9, 7, 6, 1, 4, 2, 3},
            //      new int[] {4, 2, 6, 8, 5, 3, 7, 9, 1},
            //      new int[] {7, 1, 3, 9, 2, 4, 8, 5, 6},
            //      new int[] {9, 6, 1, 5, 3, 7, 2, 8, 4},
            //      new int[] {2, 8, 7, 4, 1, 9, 6, 3, 5},
            //      new int[] {3, 4, 5, 2, 8, 6, 1, 7, 9},
            //    }
            //));
            Console.WriteLine(ValidateSolution(new int[][]
                {
                    new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9},
                    new int[] {2, 3, 1, 5, 6, 4, 8, 9, 7},
                    new int[] {3, 1, 2, 6, 4, 5, 9, 7, 8},
                    new int[] {4, 5, 6, 7, 8, 9, 1, 2, 3},
                    new int[] {5, 6, 4, 8, 9, 7, 2, 3, 1},
                    new int[] {6, 4, 5, 9, 7, 8, 3, 1, 2},
                    new int[] {7, 8, 9, 1, 2, 3, 4, 5, 6},
                    new int[] {8, 9, 7, 2, 3, 1, 5, 6, 4},
                    new int[] {9, 7, 8, 3, 1, 2, 6, 4, 5},
                }
            ));
            Console.ReadLine();
        }

        public static bool ValidateSolution(int[][] board)
        {
            // Validate Rows
            foreach (int[] array in board)
            {
                List<int> check = new List<int>();
                for (int i=0; i < array.Length; i++)
                {
                    if (array[i] > 0 && array[i] < 10 && !check.Contains(array[i]))
                    {
                        check.Add(array[i]);
                    }
                    else
                    {
                        return false;
                    }
                }
            }

            //Validate Columns
            for (int i = 0; i < 9; i++)
            {
                List<int> check = new List<int>();
                foreach (int[] array in board)
                {
                    if (array[i] > 0 && array[i] < 10 && !check.Contains(array[i]))
                    {
                        check.Add(array[i]);
                    }
                    else
                    {
                        return false;
                    }
                }                
            }

            //Validate SubGrids
            bool sub = true;
            sub = ValidateSubGrid(board, 0, 0);
            if (sub == true) { sub = ValidateSubGrid(board, 3, 0); }
            if (sub == true) { sub = ValidateSubGrid(board, 6, 0); }
            if (sub == true) { sub = ValidateSubGrid(board, 0, 3); }
            if (sub == true) { sub = ValidateSubGrid(board, 3, 3); }
            if (sub == true) { sub = ValidateSubGrid(board, 6, 3); }
            if (sub == true) { sub = ValidateSubGrid(board, 0, 6); }
            if (sub == true) { sub = ValidateSubGrid(board, 3, 6); }
            if (sub == true) { sub = ValidateSubGrid(board, 6, 6); }

            return sub;
        }
        private static bool ValidateSubGrid(int[][] board, int startX, int startY)
        {
            var check = new List<int>();
            for (int i = startY; i < startY+3; i++)
            {
                for (int j = startX; j < startX+3; j++)
                {
                    if (board[i][j] > 0 && board[i][j] < 10 && !check.Contains(board[i][j]))
                    {
                        check.Add(board[i][j]);
                    }
                    else
                    {
                        return false;
                    }
                }
            }
            return true;
        }
    }
}
