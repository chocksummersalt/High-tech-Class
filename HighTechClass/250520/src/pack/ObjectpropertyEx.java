package pack;
class Point5{
	private int x, y;
	public Point5(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
public class ObjectpropertyEx {
	public static void print(Object obj) {
		System.out.println(obj.getClass().getName());
		System.out.println(obj.hashCode());
		System.out.println(obj.toString());
		System.out.println(obj);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Point5 p = new Point5(2,3);
		print(p);
	}

}
