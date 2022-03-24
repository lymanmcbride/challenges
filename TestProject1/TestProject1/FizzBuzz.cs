namespace TestProject1
{
    public class FizzBuzz
    {
        public static string CreateFizzBuzzResponse(int fizzBuzzNumber)
        {
            string toReturn;
            if (fizzBuzzNumber % 3 == 0)
            {
                toReturn = "fizz";
            }
            else if (fizzBuzzNumber % 5 == 0)
            {
                toReturn = "buzz";
            }
            else if (fizzBuzzNumber % 15 == 0)
            {
                toReturn = "fizzBuzz";
            }
            else
            {
                throw new FizzBuzzException("Number is not divisible by 3 or 5");
            }

            return toReturn;
        }
    }
}