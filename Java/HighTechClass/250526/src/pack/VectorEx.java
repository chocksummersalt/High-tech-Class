package pack;
import java.util.Vector;

class Point{
private int x, y ;
public Point(int x, int y) {
	this.x = x;
	this.y = y;
	
}
public String toString() {
	return"("+ x+ "," + y + ")";
}
}
	
public class VectorEx {

	public static void main(String[] args) {
		
		Vector<Point> v = new Vector<Point>();
		v.add(new Point(2,3));
		v.add(new Point(-5,20));
				
		v.add(new Point(30,-8));

		
		v.remove(1);
		
		for(int i = 0 ; i< v.size(); i++) {
			Point p = v.get(i);
			System.out.println(p);
		}
		// TODO Auto-generated method stub

/*
		Vector<Integer> v = new Vector<Integer>();
	
	
		v.add(5);
		v.add(4);
		v.add(-1);
		
		v.add(2,100);
		
		System.out.println("백터 내의 요소 수:" + v.size());
		System.out.println("백터의 용량 :" + v.capacity());
		
		
		for(int i = 0; i<v.size(); i++) {
			int n = v.get(i);
			System.out.println(n);
			
			int sum = 0;
				for(int i = 0; i<v.size(); i++) {
				int n = v.elementAt(i);
				sum = sum + n;
			}
			
		}
		
		
		System.out.println("백터에 있는 정수의 합:" + sum);
	*/	

	}

}
