package basic;

import java.util.Scanner;

public class basic3_250513 {
	enum Week{월, 화, 수, 목, 금, 토, 일}
	static int[] makeArray() {
		int temp[] = new int[4];
		for (int i = 0 ; i <temp.length; i++)
			temp[i] = i;
		return temp;
	}
	
	public static void main(String[] args) {
	/*	int a= 3, b = 3, c=3;
		
				
//대입 연산자  사례
				
		a += 3 ;
		b *= 3;
		c %= 2;
		
		System.out.println("a=" + a +", b= "+b +", c=" +c);
		
		int d =3;
		
		a = d++;
		System.out.println("a=" +a+ ", d="+d );
		a = ++d;
		System.out.println("a=" +a+ ", d="+d );
		a = d--;
		System.out.println("a=" +a+ ", d="+d );
		a = --d;
		System.out.println("a=" +a+ ", d="+d );
		
//비교 연산
		System.out.println('a' >'b');
		System.out.println('a' >='b');
		System.out.println(-1 <0);
		System.out.println(3.45<=2);
		System.out.println(3 == 2);
		System.out.println(3 != 2);
		System.out.println(!(3!=2));
		
//논리 연산 복합
		
		System.out.println((3>2) && (3>4));
		System.out.println((3!=2) || (-1>0));
		System.out.println((3!=2)^(-1>0));
		
		
//비트 논리 연산
		
		short g = (short)0x55ff;
		short h = (short)0x00ff;
		
		System.out.println("[비트 연산 결과]");
		System.out.printf("%04x\n" ,(short)(g&h));
		System.out.printf("%04x\n" ,(short)(g|h));
		System.out.printf("%04x\n" ,(short)(g^h));
		System.out.printf("%04x\n" ,(short)(~g));
		
		byte i = 20;
		byte j = -8;
		
		System.out.println("시프트 연산 결과");
		System.out.println(i<<2);
		System.out.println(i>>2);
		System.out.println(j>>2);
		System.out.printf("%x\n", (j>>>2));
//if문	
	Scanner scanner = new Scanner(System.in);
	
		System.out.print("뭘 드릴깝쇼?:");
		String order = scanner.next();
		//if (score >= 90)
			//grade = 'A';
		//else if(score >=80)
			//grade ='B';
		//else if(score >=70)
			//grade ='C';
		//else if(score >=60)
			//grade ='D';
		//else
			//grade = 'F';
	
//switch문
		/*switch (score/10) {
		case 10:
		case 9:
			grade = 'A';
			break;
		case 8:
			grade = 'B';
			break;
		case 7:
			grade = 'C';
			break;
		case 6:
			grade = 'D';
			break;
		default:
			grade = 'F';
		}
		
		int price = 0;
		switch (order) {
		case "에스프레소":
		case"카푸치노":
		case"카페따떼":
			price = 3500;
			break;
		default:
			System.out.println("메뉴에 없습니다!");
			
		}
		if(price != 0)
		System.out.println(order + "는 "+price+ "원입니다");
		
		scanner.close();
		
		
		//System.out.print("수를 입력하세요:");
		//int number = in.nextInt();
		
		//if(number%3==0)

		 */

//scanner 활용
	//Scanner scanner = new Scanner(System.in);
		
		//System.out.print("정수를 입력하세요:");
		//int time = scanner.nextInt(); //정수입력
		//int second = time % 60; //60으로 나눈 나머지 초
		//int minute = (time / 60) % 60 ; //60으로나눈 몫을 다시 60으로 나눈 나머지는 분
		
		//System.out.print(time + "초는");

		//System.out.print(minute + "분");

		//System.out.print(second + "초입니다");
		//scanner.close();
/*		
		Scanner scanner2= new Scanner(System.in);
		
		System.out.print("점수를 입력하세요");
		int score = scanner2.nextInt();
		if(score>=80)
			System.out.println("축하합니다! 합격입니다.");
		else
			System.out.println("불합격입니다.");
		
		scanner2.close();
		

		// if 랑 else에 중괄호 빼먹지 말기
		int sum = 0;
		for (int i = 1; i<=10; i++) {
			sum += i;
			System.out.print(i);
			
			if(i<= 9) {
				System.out.print("+");
			}else { 
				System.out.print("=");
				System.out.print(sum);
			}
		}
		
		int count = 0;
		int sum = 0;
		Scanner scanner = new Scanner(System.in);
		System.out.println("정수를 입력하고 마지막에 -1을 입력하세요");
		
		int n = scanner.nextint();
		while(n!=-1) {
			sum +=n;
			count++;
			n= scanner.nextint()
		}
		if(count == 0) System.out.println("입력된 수가 없습니다");
		else {
			System.out.print("정수의 갯수는 " +count+ "개이며");
			System.out.println("평균은 " + (double)sum/count +"입니다.");
		}
		scanner.close();
		
		//do 작업문 while 조건  
		
		char c = 'a';
		
		do {
			System.out.print(c);
			c = (char)(c+1);
		}while(c <='z');
		
		for(int i = 1; i<10; i++) {
			for (int j = 1; j<10; j++) {
				System.out.print(i + "*" + j + "=" + i*j);
				System.out.print('\t');
			}
			System.out.println();
		}


		Scanner scanner = new Scanner(System.in);
		
		System.out.println("정수를 5개 입력하세요");
		int sum = 0;
		for(int i = 0; i<5; i++) {
			int n = scanner.nextInt();
			if(n<=0)
				continue;
			else
				sum +=n;
		}
		System.out.println("양수의 합은" + sum);
		
		scanner.close();
				*/
/*		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("exit를 입력하면 종료합니다.");
		while(true) {
			System.out.print("!!");
			String text = scanner.nextLine();
			if(text.equals("exit"))
				break;
		}
		System.out.println("종료함니다!!");
		
		scanner.close();
		
//배열 new는 객체를 만드는 연산자 즉 배열도 객체다
		Scanner scanner= new Scanner(System.in);
		int intArray[]= new int[5];
		
		int max = 0;
		System.out.println("양수 다섯개 입력 ㄱ");
		for(int i =0; i<5; i++) {
			intArray[i] = scanner.nextInt();
			if(intArray[i] > max)
				max = intArray[i];
		}
		System.out.print("가장 큰 수는 " +max+ "입니다.");
		
		int intArray[] = new int[5];
		int sum = 0;
		
		Scanner scanner = new Scanner(System.in);
		System.out.print(intArray.length+ "개의 정수를 입력하세요 >>");
		for(int i = 0; i <intArray.length; i++)
			intArray[i] = scanner.nextInt();
		
		for(int i = 0 ; i<intArray.length; i++)
			sum += intArray[i];
		
		System.out.print(" 평균은 "+ (double)sum/intArray.length);
		
		
		int [] n = {1,2,3,4,5};
		String names[] = {"사과","배","딸기","포도"};
		
		int sum = 0;
		
		for (int k : n) {
			System.out.print(k+" ");
			sum+=k;
		}
		System.out.println("합은"+sum);
		
		for(String s : names) 
			System.out.print(s + " ");
		System.out.println();
		
		for (Week day: Week.values())
			System.out.print(day + "요일 ");
		System.out.println();

		        double score[][] = {
		            {3.3, 3.4}, // 1학년 1, 2학기 평점
		            {3.5, 3.6}, // 2학년 1, 2학기 평점
		            {3.7, 4.0}, // 3학년 1, 2학기 평점
		            {4.1, 4.2}  // 4학년 1, 2학기 평점
		        };

		        double sum = 0;
		        for (int year = 0; year < score.length; year++)      // 각 학년별로 반복
		            for (int term = 0; term < score[year].length; term++)  // 각 학년의 학기별로 반복
		                sum += score[year][term];                    // 전체 평점 합

		        int n = score.length;      // 배열의 행 개수, 4
		        int m = score[0].length;   // 배열의 열 개수, 2
		        System.out.println("4년 전체 평점 평균은 " + sum / (n * m));
			
		int intArray[][]= new int[4][];
		intArray[0] = new int[3];
		intArray[1] = new int[2];
		intArray[2] = new int[3];
		intArray[3] = new int[2];
	
		for (int i = 0; i< intArray.length; i++) {
			for(int j = 0 ; j< intArray[i].length;j++)
				intArray[i][j] = (i+1)*10+j;
		
		for (int i = 0; i<intArray.length; i++) {
			for(int j = 0; j< intArray[i].length; j++)
				System.out.print(intArray[i][j] + " ");
			System.out.println();
		}
	*/
		


		int intArray[];
		intArray = makeArray();
		for(int i = 0; i < intArray.length; i++)
			System.out.print(intArray[i] + " ");
	}
	
}
	
	