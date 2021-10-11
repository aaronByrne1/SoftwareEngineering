
public class TestFile {

	public static void main(String[] args) {
		Tree a=new Tree(2);
		Tree b=new Tree(3);
		a.left=b;
		
		Tree c=new Tree(4);
		a.right=c;
		
		Tree d=new Tree(5);
		Tree e=new Tree(6);
		b.right=e;
		b.left=d;
				
		Tree f=new Tree(7);
		Tree g=new Tree(8);
		Tree h=new Tree(9);
		c.right=g;
		c.left=f;
		
		d.left=h;
		
		LCA test= new LCA();
		
		Tree ans=test.lowestCommonAncestor(a, c, g);
		
		System.out.println("LCA IS: "+ ans.val);

	}

}
