package circleareajava;

public class CircleArea {

	public static void main(String[] args) {
		final double PI;
		PI = 3.14;
		
		double radius = 10.0;
		double circlearea = radius * radius * PI;
		
		System.out.println(circlearea);

	}

}

class TypeConversion{
	public static void main(String[] args) {
		byte b = 127;
		int i = 100;
		
		System.out.println(10/4);
		System.out.println(10.0/4);
		System.out.println((byte)(b+i));
		System.out.println((int)2.9+1.8);
	}
}