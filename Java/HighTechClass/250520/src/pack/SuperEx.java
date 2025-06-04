package pack;

class Point {
    private int x, y;

    public Point() {
        this.x = this.y = 0;
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void showPoint() {
        System.out.println("(" + x + "," + y + ")");
    }
}

class ColorPoint extends Point {
    private String color;

    public ColorPoint(int x, int y, String color) {
        super(x, y); // Point 클래스 생성자 호출
        this.color = color;
    }

    public void showColorPoint() {
        System.out.print(color + " ");
        showPoint(); // 부모 클래스의 메서드 호출
    }
}

public class SuperEx {
    public static void main(String[] args) {
        ColorPoint cp = new ColorPoint(5, 6, "blue");
        cp.showColorPoint();
    }
}
//타입이 안맞으면 원칙적으로 연산할 수 없다.
//배열, 클래스, 인터페이스 = 레퍼런스 자료형
// int a = 10+ 3.5 라고 하면 자동적으로 소숫점 버림이 일어난다.
//선언의 규칙 자료형 이름 형태. ex) class or int + 이름 + ()함수 [배열]