package scanner;

import java.util.Scanner;

public class scannerproj {

	public static void main(String[] args) {
		System.out.println("이름,도시,나이,체중 적으세요");
		Scanner scanner = new Scanner(System.in);
		
		String name = scanner.next();
		System.out.print("이름은" + name + ",");

		scanner.close(); 
	}

}
