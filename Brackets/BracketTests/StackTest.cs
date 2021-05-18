using Microsoft.VisualStudio.TestTools.UnitTesting;
using Brackets;

namespace BracketTests
{
    [TestClass]
    public class StackTest
    {
        [TestMethod]
        public void TestMethod1()
        {
            //test case
            string brackets = "{akls{()()zyx}";
            //expected result
            bool F = false;
            //test
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }
        [TestMethod]
        public void TestMethod2()
        {
            string brackets = "{()}";
            bool T = true;
            Assert.AreEqual(T, Program.TestBrackets(brackets));
        }
        [TestMethod]
        public void TestMethod3()
        {
            string brackets = "}{(";
            bool F = false;
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }
        [TestMethod]
        public void TestMethod4()
        {
            string brackets = "{{})";
            bool F = false;
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }
        [TestMethod]
        public void TestMethod5()
        {
            string brackets = "({}}";
            bool F = false;
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }
        [TestMethod]
        public void TestMethod6()
        {
            string brackets = "\"\"\"";
            bool T = true;
            Assert.AreEqual(T, Program.TestBrackets(brackets));
        }

        [TestMethod]
        public void TestMethod7()
        {
            string brackets = "{([})]";
            bool F = false;
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }

        [TestMethod]
        public void TestMethod8()
        {
            string brackets = "(){";
            bool F = false;
            Assert.AreEqual(F, Program.TestBrackets(brackets));
        }
    }
}
