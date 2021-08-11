using NUnit.Framework;
using StripComments;

namespace StripCommentsUnitTests
{
    public class Tests
    {
        [Test]
        public void StripComments_ShouldEvaluateSuccessfulStrippingOfCommentsAndWhiteSpace()
        {
            Assert.AreEqual(
                "apples, pears\ngrapes\nbananas",
                StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new string[] { "#", "!" }));
        }

        [Test]
        public void StripComments_ShouldEvaluateSuccessfulStrippingOfWhiteSpaceWithoutComments()
        {
            Assert.AreEqual("a\n b\nc", StripCommentsSolution.StripComments("a \n b \nc ", new string[]{"#", "$"}));
        }

        [Test]
        public void StripComments_ShouldWork()
        {
            Assert.AreEqual("\n\n", StripCommentsSolution.StripComments("\n\n", new string[]{"#", "$", "!", "-"}));
        }
    }
}