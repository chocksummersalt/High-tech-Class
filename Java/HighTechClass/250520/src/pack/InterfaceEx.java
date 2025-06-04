interface PhoneInterface { // 인터페이스 선언
    final int TIMEOUT = 10000; // 상수 필드 선언

    void sendCall();          // 추상 메서드
    void receiveCall();       // 추상 메서드

    default void printLogo() { // default 메서드
        System.out.println("** Phone **");
    }
}

interface MobilePhoneInterface extends PhoneInterface {
    void sendSMS();
    void receiveSMS();
}

interface MP3Interface {
    void play();
    void stop();
}

class PDA { // 클래스 작성
    public int calculate(int x, int y) {
        return x + y;
    }
}

// SmartPhone 클래스: PDA를 상속받고, 두 개의 인터페이스 구현
class SmartPhone extends PDA implements MobilePhoneInterface, MP3Interface {

    // PhoneInterface 구현
    @Override
    public void sendCall() {
        System.out.println("따르릉따르릉...");
    }

    @Override
    public void receiveCall() {
        System.out.println("전화 왔어요.");
    }

    // MobilePhoneInterface 구현
    @Override
    public void sendSMS() {
        System.out.println("문자갑니다.");
    }

    @Override
    public void receiveSMS() {
        System.out.println("문자왔어요.");
    }

    // MP3Interface 구현
    @Override
    public void play() {
        System.out.println("음악 연주합니다.");
    }

    @Override
    public void stop() {
        System.out.println("음악 중단합니다.");
    }

    // SmartPhone에만 있는 추가 메서드
    public void schedule() {
        System.out.println("일정 관리합니다.");
    }
}

public class InterfaceEx {
    public static void main(String[] args) {
        SmartPhone phone = new SmartPhone();
        
        phone.printLogo();                  // default 메서드
        phone.sendCall();                  // 오버라이딩
        phone.play();                      // MP3
        System.out.println("3과 5를 더하면 " + phone.calculate(3, 5)); // PDA
        phone.schedule();                  // SmartPhone 고유 메서드
    }
}
