using Microsoft.VisualStudio.TestTools.UnitTesting;
using Brackets;

namespace BracketTests
{
    [TestClass]
    public class IntTest
    {
        [TestMethod]
        public void TestMethod1()
        {
            //test case
            string brackets = "{akls{()()zyx}";
            //expected outcome
            bool F = false;
            //test
            Assert.AreEqual(F, Program.TestBracketsSimple(brackets));
        }
        [TestMethod]
        public void TestMethod2()
        {
            string brackets = "{}";
            bool T = true;
            Assert.AreEqual(T, Program.TestBracketsSimple(brackets));
        }
        [TestMethod]
        public void TestMethod3()
        {
            string brackets = "}{";
            bool F = false;
            Assert.AreEqual(F, Program.TestBracketsSimple(brackets));
        }
        [TestMethod]
        public void TestMethod4()
        {
            string brackets = "{{}";
            bool F = false;
            Assert.AreEqual(F, Program.TestBracketsSimple(brackets));
        }
        [TestMethod]
        public void TestMethod5()
        {
            string brackets = "{}}";
            bool F = false;
            Assert.AreEqual(F, Program.TestBracketsSimple(brackets));
        }
        [TestMethod]
        public void TestMethod6()
        {
            string brackets = "\"\"\"";
            bool T = true;
            Assert.AreEqual(T, Program.TestBracketsSimple(brackets));
        }
    }
}
