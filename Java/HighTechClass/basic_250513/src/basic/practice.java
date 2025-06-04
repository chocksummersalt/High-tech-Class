package basic;
import java.util.Scanner;

public class practice {
public static void main(String[] args){
//1번문제 원화를 달러의 환율을 적용시켜서 변경하시오
/*	Scanner scanner = new Scanner(System.in);
	System.out.print("원화를 입력하세요:");
	
	int won = scanner.nextInt();
	int dollar = (int)(won * 1.4);
	
	System.out.print("환산 금액은 $"+dollar+"입니다.");
	
	
	
//2번 문제 화폐마다 몇개로 반환되는지 출력하세요~
	Scanner scanner = new Scanner(System.in);
	System.out.print("원화를 입력하세요:");
	
	int won = scanner.nextInt();
	int sinsaim = won / 50000;
	int sejong = won / 10000;
	int ehwang = won / 5000;
	int ee = won / 1000;
	int kkiruk = won / 500;
	int sunsin = won / 100;
	int bori = won / 50;
	int top = won / 10 ;

	System.out.print(sinsaim+ "매\n");
	System.out.print(sejong+ "매\n");
	System.out.print(ehwang+ "매\n");
	System.out.print(ee+ "매\n");
	System.out.print(kkiruk+ "매\n");
	System.out.print(sunsin+ "매\n");
	System.out.print(bori+ "매\n");
	System.out.print(top+ "매\n");
	
	scanner.close();
	
//3번 문제 삼각형의 변의 길이 3개를 입력받고 이걸로 삼각형을 만들 수 있는지 판별하라
	Scanner scanner = new Scanner(System.in);
	System.out.print("1번째 변의 길이를 입력하세요\n");
	System.out.print("2번째 변의 길이를 입력하세요\n");
	System.out.print("3번째 변의 길이를 입력하세요\n");
	
	int first = scanner.nextInt();
	int second = scanner.nextInt();
	int third = scanner.nextInt();
	
	if ((first + second > third)&&(second+third>first)&&(third+first>second))
			System.out.print("삼각형이 될 수 있다.");
	else
		System.out.print("삼각형 못해~");
		
	scanner.close();
*/
//4번 문제 
	
//5번 문제
	
	
//6번 문제 숫자를 입력받고 3~5는 봄 , 6~8은 여름 9~11 은 가을 12,1,2는 겨울을 출력하게
	String wol = "";
	Scanner scanner = new Scanner(System.in);
	System.out.print("월을 입력하세요");
	
	
	int season = scanner.nextInt();
	
	switch(season) {
	
	case 3:
		wol = "봄";
		break;
	case 4:
		wol = "봄";
		break;
	case 5:
		wol = "봄";
		break;
	case 6:
		wol = "여름";
		break;
	case 7:
		wol = "여름";
		break;
	case 8:
		wol = "여름";
		break;
	case 9:
		wol = "가을";
		break;
	case 10:
		wol = "가을";
		break;
	case 11:
		wol = "가을";
		break;
	case 12:
		wol = "겨울";
		break;
	case 1:
		wol = "겨울";
		break;
	case 2: 
		wol = "겨울";
		break;
		
	default:
		wol = "잘못된 입력";
	}
	System.out.print("무슨 계절인가 보아하니 " +wol+ "이구나~");
	
	
	}
}
