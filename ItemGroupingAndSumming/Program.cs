using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace ItemGroupingAndSumming
{
    public static class Program
    {
        public static List<Item> GroupAndSum(List<Item> items)
        {
            return items.GroupBy(x => new { x.Category, x.Selector}).Select(grouping => new Item(grouping.Key.Category, grouping.Key.Selector, grouping.Sum(x => x.Amount))).ToList();
        }
    }
    public class Item
    {
        public string Category { get; }
        public string Selector { get; }
        public int Amount { get; }
        
        public Item(string category, string selector, int amount)
        {
            Category = category;
            Selector = selector;
            Amount = amount;
        }
    }
}