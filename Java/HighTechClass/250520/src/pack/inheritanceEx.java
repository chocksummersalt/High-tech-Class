package pack;

// 부모 클래스
class Person {
    private int weight;
    int age;
    protected int height;
    public String name;

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }
}

// 자식 클래스
class Student extends Person {
    public void set() {
        age = 30;          // default 접근 가능
        height = 175;      // protected 접근 가능
        // weight = 99;    // private 접근 불가 → 오류 발생
        setWeight(99);     // 대신 public setter 사용
    }
}

// 메인 클래스
public class inheritanceEx {
    public static void main(String[] args) {
        Student s = new Student();
        s.set();

        System.out.println("나이: " + s.age);
        System.out.println("키: " + s.height);
        System.out.println("몸무게: " + s.getWeight());
    }
}
