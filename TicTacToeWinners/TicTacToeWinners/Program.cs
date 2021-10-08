using System;
using Microsoft.Extensions.DependencyInjection;

namespace TicTacToeWinners
{
    class Program
    {
        static void Main(string[] args)
        {
            var serviceProvider = new ServiceCollection()
                .AddScoped<ITicTacToe, TicTacToe>();
        }
    }
}
