package pack;

/*class GStack<T> {
    int tos;
    Object[] stck;

    public GStack() {
        tos = 0;
        stck = new Object[10];
    }

    public void push(T item) {
        if (tos == 10) return;
        stck[tos] = item;
        tos++;
    }

    public T pop() {
        if (tos == 0) return null;
        tos--;
        return (T) stck[tos];
    }
}
*/
public class MyStack {

    // 제네릭 스택 클래스
    static class GStack<T> {
        int tos;
        Object[] stck;

        public GStack() {
            tos = 0;
            stck = new Object[10];
        }

        public void push(T item) {
            if (tos == 10) return;
            stck[tos] = item;
            tos++;
        }

        @SuppressWarnings("unchecked")
        public T pop() {
            if (tos == 0) return null;
            tos--;
            return (T) stck[tos];
        }
    }

    // 스택을 역순으로 복사하는 메서드
    public static <T> GStack<T> reverse(GStack<T> a) {
        GStack<T> s = new GStack<>();  // 새 스택 생성

        while (true) {
            T tmp = a.pop();
            if (tmp == null)
                break;
            s.push(tmp);
        }

        return s;
    }

    public static void main(String[] args) {
        GStack<Double> gs = new GStack<>();

   	
  /*      GStack<String> stringStack = new GStack<>();
        stringStack.push("seoul");
        stringStack.push("busan");
        stringStack.push("LA");

        for (int n = 0; n < 3; n++)
            System.out.println(stringStack.pop());

        GStack<Integer> intStack = new GStack<>();
        intStack.push(1);
        intStack.push(3);
        intStack.push(5);

        for (int n = 0; n < 3; n++)
            System.out.println(intStack.pop());
    */}

