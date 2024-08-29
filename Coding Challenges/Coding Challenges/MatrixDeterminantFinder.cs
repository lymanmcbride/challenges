using NUnit.Framework;

namespace Coding_Challenges;

public class MatrixDeterminantFinderTests
{
    private static readonly int[][][] Matrix =
    {
        new int[][] { new [] { 1 } },
        
    };

    private static readonly int[] Expected = { 1, -1, -20 };

    private static readonly string[] Msg = { "Determinant of a 1 x 1 matrix yields the value of the one element", "", "" };

    [Test]
    public void Determinant_WhenCalledWith2x2Matrix_ReturnsDeterminant()
    {
        var twoByTwoMatrix = new[] { new[] { 1, 3 }, new[] { 2, 5 } };
        Assert.AreEqual(-1, Coding_Challenges.Matrix.Determinant(twoByTwoMatrix), "Should return 1 * 5 - 3 * 2 == -1");
    }
    
    [Test]
    public void Determinant_WhenCalledWith3x3Matrix_ReturnsDeterminant()
    {
        var threeByThreeMatrix = new[] { new [] { 2, 5, 3 }, new [] { 1, -2, -1 }, new [] { 1, 3, 4 } };
        Assert.AreEqual(-20, Coding_Challenges.Matrix.Determinant(threeByThreeMatrix));
    }
}

public static class Matrix
{
    public static int Determinant(int[][] matrix)
    {
        int matrixSize = matrix.Length;
        for (int i = 0; i < matrixSize; i++)
        {
            return 
                matrix[matrixSize - 2][matrixSize - 2] * matrix[matrixSize - 1][matrixSize - 1] -
                matrix[matrixSize - 2][matrixSize - 1] * matrix[matrixSize - 1][matrixSize - 2];
        }
        return 0;
    }
}
