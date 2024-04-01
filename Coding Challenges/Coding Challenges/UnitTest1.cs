using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace Coding_Challenges
{
    public class Tests
    {
        [Test]
        public void FindDuplicates_WhenCalledWithOneDuplicateAndNoOtherNumbers_ReturnsDuplicateNumber()
        {
            List<int> integersWithOneDuplicate = new List<int> { 1, 1 };
            
            Assert.AreEqual(1, FindDuplicateSpaceEdition.FindDuplicates(integersWithOneDuplicate));
        }
        
        [Test]
        public void FindDuplicates_WhenCalledWithMultipleDuplicates_ReturnsDuplicateNumber()
        {
            List<int> integersWithOneDuplicate = new List<int> { 1, 2, 3, 4, 2, 5, 7 };
            
            Assert.AreEqual(2, FindDuplicateSpaceEdition.FindDuplicates(integersWithOneDuplicate));
        }
        
        [Test]
        public void FindDuplicates_WhenCalledWithLotsOfDuplicates_ReturnsFirstDuplicateNumberFound()
        {
            List<int> integersWithOneDuplicate = new List<int> { 1, 2, 3, 4, 8, 5, 7, 3, 2, 5, 3, 4, 6, 2, 3, 4, 2, 3, 1 };
            
            Assert.AreEqual(3, FindDuplicateSpaceEdition.FindDuplicates(integersWithOneDuplicate));
        }
    }

    public static class FindDuplicateSpaceEdition
    {
        public static int FindDuplicates(List<int> integers)
        {
            return FindDuplicatesSolution1(integers);
        }
        
        private static int FindDuplicatesSolution1(List<int> integers)
        {
            HashSet<int> seenIntegers = new HashSet<int>();
            foreach (int integer in integers)
            {
                if (!seenIntegers.Add(integer))
                {
                    return integer;
                }
            }

            throw new Exception("none found");
        }
    }
}