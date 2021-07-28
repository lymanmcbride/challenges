using NUnit.Framework;
using StripComments;

namespace StripCommentsUnitTests
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
            Assert.AreEqual(
                "apples, pears\ngrapes\nbananas",
                StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new string[] { "#", "!" }));
        }
    }
}