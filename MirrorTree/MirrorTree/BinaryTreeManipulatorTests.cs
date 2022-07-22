using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace MirrorTree
{
    [TestFixture]
    public class BinaryTreeManipulatorTests
    {
        private readonly BinaryTreeManipulator _binaryTreeManipulator;
        public BinaryTreeManipulatorTests()
        {
            _binaryTreeManipulator = new BinaryTreeManipulator();
        }

        [Test]
        public void CreateTree_ShouldCreateTree()
        {
            _binaryTreeManipulator.CreateTree(new List<int>{1,2,2,3,4,4,3});
            Assert.True(false);
        }
    }
}