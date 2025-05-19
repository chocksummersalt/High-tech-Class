public class Book {
    String title;
    String author;

    void show() {
        System.out.println(title + " " + author);
    }

    // 기본 생성자
    public Book() {
        this("", "");
        System.out.println("생성자 호출됨");
    }

    // 제목만 입력하는 생성자
    public Book(String title) {
        this(title, "작자미상");
    }

    // 제목과 저자 모두 입력하는 생성자
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public static void main(String[] args) {
        Book littlePrince = new Book("어린왕자", "생텍쥐페리");
        Book loveStory = new Book("춘향전");
        Book emptyBook = new Book();

        loveStory.show();
    }
}

