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
        public void GroupAndSum_ShouldReturnSumOfTwoGroups()
        {
            List<Item> items = new List<Item>()
            {
                _item1, _item2, _item1, _item2, _item1
            };

            var sortedAndSummed = Program.GroupAndSum(items);
            
            Assert.AreEqual(15, sortedAndSummed[0].Amount);
        }
    }
}