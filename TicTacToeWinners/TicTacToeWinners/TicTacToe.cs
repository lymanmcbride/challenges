
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
                {'x', new Dictionary<int,int>() },
                {'o', new Dictionary<int,int>() }
            };
            foreach (var row in board)
            {
                for (var i = 0; i < row.Length; i++)
                {
                    if (row[i] != null)
                    {
                        if (!results[row[i]].ContainsKey(i))
                            results[row[i]].Add(i, 1);
                        else
                            results[row[i]][i]++;
                        
                        if (results[row[i]][i] == 3)
                        {
                            winnerExists = true;
                            break;
                        }

                        for (int j = 0; j < row.Length; j++)
                        {
                            if (results[row[i]].ContainsKey(j))
                            {
                                if (results[row[i]][j] > 0)
                                    continue;
                                winnerExists = true;
                                break;
                            }
                        }
                    }
                }
            }

            return winnerExists;
        }
    }
}