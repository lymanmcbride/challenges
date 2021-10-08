
using System.Collections.Generic;

namespace TicTacToeWinners
{
    public class TicTacToe : ITicTacToe
    {
        public bool CheckForWinner(char?[][] board)
        {
            bool winnerExists = false;
            Dictionary<char?, Dictionary<int,int>> results = new Dictionary<char?, Dictionary<int,int>>
            {
                {'x', new Dictionary<int,int>
                {
                    {0, 0},
                    {1,0},
                    {2,0}
                }},
                {'o', new Dictionary<int,int>
                {
                    {1, 0},
                    {2,0},
                    {0,0}
                }}
            };
            foreach (var row in board)
            {
                for (var i = 0; i < row.Length; i++)
                {
                    if (row[i] != null)
                    {
                        results[row[i]][i]++;
                        if (results[row[i]][i] == 3)
                        {
                            winnerExists = true;
                            break;
                        }

                        if (results[row[i]][0] > 0 &&
                            results[row[i]][1] > 0 &&
                            results[row[i]][2] > 0)
                        {
                            winnerExists = true;
                            break;
                        }
                    }
                }
            }

            return winnerExists;
        }
    }
}