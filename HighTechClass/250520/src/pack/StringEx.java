package pack;

public class StringEx {

	public static void main(String[] args) {
		String a = new String(" C#");
		String b = new String(",C++ ");// TODO Auto-generated method stub

		System.out.println( a + "의 길이는 " + a.length());
		System.out.println(a.contains("#"));
		
		a = a.concat(b);
		System.out.println(a);

		a = a.trim();
		System.out.println(a);
		
		a = a.replace("C#","java");
		System.out.println(a);
		
		String s[] = a.split(",");
		System.out.println(a);
		
	}

}
