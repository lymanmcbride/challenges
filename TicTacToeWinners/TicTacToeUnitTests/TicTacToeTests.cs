using Microsoft.VisualStudio.TestTools.UnitTesting;
using TicTacToeWinners;

namespace TicTacToeUnitTests
{
    [TestClass]
    public class TicTacToeTests
    {
        private readonly ITicTacToe _ticTacToeGame;
        public TicTacToeTests()
        {
            _ticTacToeGame = new TicTacToe();
        }
        [TestMethod]
        public void CheckForWinner_ShouldReturnTrueForVerticalWin()
        {
            char?[][] board = new char?[3][]
            {
                new char?[3]
                {
                    'x', 'o', 'x'
                },
                new char?[3]
                {
                    'x', 'o', 'o'
                },
                new char?[3]
                {
                    'x', null, null
                }
            };

            var winnerExists = _ticTacToeGame.CheckForWinner(board);
            
            Assert.IsTrue(winnerExists);
        }
        [TestMethod]
        public void CheckForWinner_ShouldReturnTrueForHorizontalWin()
        {
            char?[][] board = new char?[3][]
            {
                new char?[3]
                {
                    null, null, null
                },
                new char?[3]
                {
                    null, 'o', 'o'
                },
                new char?[3]
                {
                    'x', 'x', 'x'
                }
            };

            var winnerExists = _ticTacToeGame.CheckForWinner(board);
            
            Assert.IsTrue(winnerExists);
        }
        
        [TestMethod]
        public void CheckForWinner_ShouldReturnTrueForDiagonalWin()
        {
            char?[][] board = new char?[3][]
            {
                new char?[3]
                {
                    'x', null, 'o'
                },
                new char?[3]
                {
                    null, 'x', 'o'
                },
                new char?[3]
                {
                    null, null, 'x'
                }
            };

            var winnerExists = _ticTacToeGame.CheckForWinner(board);
            
            Assert.IsTrue(winnerExists);
        }
    }
}