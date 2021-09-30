using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;
using ItemGroupingAndSumming;


namespace ItemGroupingAndSummingUnitTests
{
    public class Tests
    {
        private readonly Item _item1;
        private readonly Item _item2;
        private readonly Item _item3;
        private readonly Item _item4;
        private readonly Item _item5;
        private readonly Item _item6;

        public Tests()
        {
            _item1 = new Item("c1", "s1", 5);
            _item2 = new Item("c1", "s2", 10);
            _item3 = new Item("c2", "s1", 15);
            _item4 = new Item("c2", "s2", 20);
            _item5 = new Item("c3", "s1", 25);
            _item6 = new Item("c3", "s2", 30);
        }

        [Test]
        public void GroupAndSum_ShouldReturnTwoGroupsAndSumAmounts()
        {
            List<Item> items = new List<Item>()
            {
                _item1, _item2, _item1, _item2, _item1
            };

            var sortedAndSummed = Program.GroupAndSum(items);

            Assert.AreEqual(15, sortedAndSummed[FindIndex(sortedAndSummed, _item1)].Amount);
            Assert.AreEqual(20, sortedAndSummed[FindIndex(sortedAndSummed, _item2)].Amount);
        }
        
        [Test]
        public void GroupAndSum_ShouldReturnSixGroupsAndSumAmounts()
        {
            List<Item> items = new List<Item>()
            {
                _item1, _item1, _item1, 
                _item2, _item2, _item2, _item2,
                _item3, _item3,
                _item4, _item4,
                _item5, _item5,
                _item6
            };

            var sortedAndSummed = Program.GroupAndSum(items);

            AssertListMatches(sortedAndSummed);
        }

        private void AssertListMatches(List<Item> sortedAndSummed)
        {
            Assert.AreEqual(15, sortedAndSummed[FindIndex(sortedAndSummed, _item1)].Amount);
            Assert.AreEqual(40, sortedAndSummed[FindIndex(sortedAndSummed, _item2)].Amount);
            Assert.AreEqual(30, sortedAndSummed[FindIndex(sortedAndSummed, _item3)].Amount);
            Assert.AreEqual(40, sortedAndSummed[FindIndex(sortedAndSummed, _item4)].Amount);
            Assert.AreEqual(50, sortedAndSummed[FindIndex(sortedAndSummed, _item5)].Amount);
            Assert.AreEqual(30, sortedAndSummed[FindIndex(sortedAndSummed, _item6)].Amount);
        }

        private int FindIndex(List<Item> sortedAndSummed, Item item)
        {
            return sortedAndSummed.FindIndex(x => x.Selector == item.Selector && x.Category == item.Category);
        }
    }
}