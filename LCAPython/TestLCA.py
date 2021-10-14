import unittest
from LCA import LCA
from Tree import Tree

class TestLCA(unittest.TestCase):

    def test1(self):
        a=Tree(1)

        b=Tree(2)
        c=Tree(3)
        a.left=b
        a.right=c

        d=Tree(4)
        b.left=d
        e=Tree(5)
        b.right=e

        f=Tree(6)
        c.left=f
        g=Tree(7)
        c.right=g
        h=Tree(8)
        d.left=h

        solution=LCA()
        answer=solution.lowestCommonAncestor(a,d,c)
        self.assertEqual(answer.val, 1)

    def test2(self):
        a=Tree(1)

        b=Tree(2)
        c=Tree(3)
        a.left=b
        a.right=c

        d=Tree(4)
        b.left=d
        e=Tree(5)
        b.right=e

        f=Tree(6)
        c.left=f
        g=Tree(7)
        c.right=g
        h=Tree(8)
        d.left=h

        solution=LCA()
        answer=solution.lowestCommonAncestor(a,g,f)
        self.assertEqual(answer.val, 3)

    def test3(self):
        a=Tree(1)

        b=Tree(2)
        c=Tree(3)
        a.left=b
        a.right=c

        d=Tree(4)
        b.left=d
        e=Tree(5)
        b.right=e

        f=Tree(6)
        c.left=f
        g=Tree(7)
        c.right=g
        h=Tree(8)
        d.left=h

        solution=LCA()
        answer=solution.lowestCommonAncestor(a,d,h)
        self.assertEqual(answer.val, 4)

if __name__ == '__main__':
    unittest.main()