import java.util.Scanner;

public class practice_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	/*	Scanner scanner = new Scanner(System.in);
		int dividend;
		int divisor;
	
		System.out.print("나뉨수를 입력하세요");
		dividend = scanner.nextInt();
		System.out.print("나눗 수를 입력하시오");
		divisor = scanner.nextInt();
		System.out.println(dividend + "를" +divisor +"로 나누면 몫은" + dividend/divisor +"입니다");
		scanner.close();
	*/
		
	//try(예외 발생할거 같은거 catch(처리할 예외 타입 선언 예외시 처리, finally(예외가 발생하든 말든 실행할 코드) 

	
/*		Scanner scanner = new Scanner(System.in);
		
		while(true) {
			System.out.print("나뉨 입력");
			int dividend = scanner.nextInt();
			System.out.print("나눗수 임녁");
			int divisor = scanner.nextInt();
			try {
				System.out.println(dividend +"를"+ divisor+"로 나누면? 몫은"+ dividend / divisor);
				break;
			}
			catch(ArithmeticException e) {
				System.out.println("0으로 나눌 수 없음");
				
			}
		}
	
	*/
		/*int[] intArray = new int[5];
		intArray[0]=0;
		try {
			for(int i =0 ; i<5; i++) {
				intArray[i+1] = i + 1 + intArray[i];
				System.out.println("intArray["+i+"]"+"="+intArray[i]);
			}
		}
	
		catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("룰루");
		}
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("정수 3개 입");
		int sum = 0, n = 0;
		for(int i=0;i<3;i++) {
			System.out.print(i+">>");
			try {
				n = scanner.nextInt();
			}
			catch(InputMismatchException e) {
				System.out.println()=("re입력");
		
{
		        String[] stringNumber = {"123", "456", "abc", "789"}; // 예시 배열
		        int i = 0;

		        try {
		            for (i = 0; i < stringNumber.length; i++) {
		                int j = Integer.parseInt(stringNumber[i]);
		                System.out.println(stringNumber[i] + " 를 숫자로 변환하면? " + j);
		            }
		        } catch (NumberFormatException e) {
		            System.out.println("숫자로 변환할 수 없는 값이 있습니다: " + stringNumber[i]);
		        }
		    }
		    */
