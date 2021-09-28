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
            var items = GroupAndSum(input);
            Console.ReadLine();
        }

        public static List<Item> GroupAndSum(List<Item> items)
        {
            var listOfGroups = items.GroupBy(
                x => new { CategoryAndSelector = $"{x.Category}{x.Selector}"});
            foreach (var grouping in listOfGroups)
            {
                var l = grouping.ToList();
                foreach (var x in l)
                {
                    Console.WriteLine($"{x.Category}, {x.Selector}");

                }
            }
            return items;
        }
    }
}