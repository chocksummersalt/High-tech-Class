// Circle 클래스 같은 폴더에 클래스 중복되어있으면 오류남
class Circle2 {
	int radius;
    // 생성자
    public Circle2(int radius) {
        this.radius = radius;
    }

    // 면적 계산 메서드
    public double getArea() {
        return 3.14 * radius * radius;
    }
}

// CircleArray 클래스: main 메서드를 포함
public class CircleArray {
    public static void main(String[] args) {
        Circle2[] c = new Circle2[5]; // 크기 5인 Circle 배열 선언

        // 각 인덱스에 반지름 i 값을 갖는 Circle 객체 생성
        for (int i = 0; i < c.length; i++)
            c[i] = new Circle2(i);

        // 각 원의 면적을 정수형으로 출력
        for (int i = 0; i < c.length; i++)
            System.out.print((int)(c[i].getArea()) + " ");
    }
}
