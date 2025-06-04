package pack;
class Shape{
	public Shape next;
	public Shape() {next = null;}
	
	public void draw() {
		System.out.println("shape");
	}
}

class Line extends Shape{
	public void draw() {
		System.out.println("Line");
	}
}

class Rect extends Shape{
	public void draw() {
		System.out.println("Rect");
	}
}
public class MethodOverridingEx {
	static void paint(Shape p) {
		p.draw();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Line line = new Line();
		paint(line);
		paint(new Shape());
		paint(new Line());
		paint(new Rect());
	}

}
/*
Shape start, last, obj;

start = new Line();
last = start;
obj = new Rect();
last.next = obj;
last = obj;
obj = new Line();
last.nect = obj;
last = obj;

Shape p = start;
while(p != null){
p.draw();
p = p.next;
		}
	}
}

//추상 메서드는 abstrat를 하나라도 가지고 있으면 그 클래스는 추상클래스가 된다
//abstract로 선언된 클래스. 추상클래스는 객체를 만들 수 없다. 원형은 있되 내용이 없다.
//상속을 받아서 미구현된걸 구현하는 것.*/