using System;
using System.Collections.Generic;
using System.Linq;

namespace ItemGroupingAndSumming
{
    class Program
    {
        // Alright, I’ll post the first problem. Given a List of the following object:
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
        // Write an algorithm that will return a list of “collapsed” similar items. Items are considered similar if they have the same Category and Selector .
        // Collapsed items should have their Amount summed.
        //     Example:
        // List<Item> input = new List<Item>
        // {
        //     new Item("c1", "s1", 5),
        //     new Item("c1", "s2", 10),
        //     new Item("c1", "s1", 15)
        // }
        //
        // List<Item> expected = new List<Item>
        // {
        //     new Item("c1", "s1", 20),
        //     new Item("c1", "s2", 10),
        // }
        static void Main(string[] args)
        {
            List<Item> input = new List<Item>
            {
                new Item("c1", "s2", 25),
                new Item("c1", "s1", 5),
                new Item("c1", "s2", 20),
                new Item("c1", "s2", 10),
                new Item("c1", "s1", 15)


            };
            var items = input.GroupBy(x => new { x.Category, x.Selector}).Select(grouping => new Item(grouping.Key.Category, grouping.Key.Selector, grouping.Sum(x => x.Amount))).ToList();

            foreach (var item in items)
            {
                Console.WriteLine($"{item.Category}, {item.Selector}, {item.Amount}");
            }
            Console.ReadLine();
        }
    }
}