from LCA import LCA
from Tree import Tree

def main():
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
        print(answer.val)
        print(" this is the answer")
if __name__ == "__main__":
    main()

        




