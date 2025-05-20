package pack;

class Point2 {
    private int x, y;

    public Point2(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Point(" + x + "," + y + ")";
    }
}

public class ToStringEx {
    public static void main(String[] args) {
        Point2 p = new Point2(2, 3);
        System.out.println(p.toString()); // 명시적 toString()
        System.out.println(p);            // 암시적 toString() 호출
    }
}
