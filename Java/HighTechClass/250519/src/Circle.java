
	public class Circle {
	    int radius;
	    String name;

	    public Circle() {
	    	radius = 1; name = "";
	        // 기본 생성자 초기화 하기
	    }
	    public Circle(int r ,String n) {
	    	radius = r; name = n;
	    }

	    public double getArea() {
	    	return 3.14*radius*radius;
	    }

	    

	    public static void main(String[] args) {
	        Circle pizza = new Circle(10, "자바피자");
	        pizza.radius = 10;
	        pizza.name = "자바피자";
	        double area = pizza.getArea();
	        System.out.println(pizza.name + "의 면적은 " + area);
	    
	     
	  

	}
}
