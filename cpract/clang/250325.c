//#include <stdio.h>

//int main() {
//	char a = 0x20;

//	printf("원본값 a = %X, 1비트 왼쪽 시프트한 값 %X \n", a, a << 24);

//	printf("원본값 a = %X, 2비트 왼쪽 시프트한 값 %X \n", a, a << 25);

//	printf("원본값 a = %X, 3비트 왼쪽 시프트한 값 %X \n", a, a << 26);

//	printf("원본값 a = %X, 4비트 왼쪽 시프트한 값 %X \n", a, a << 27);

//	return 0;
//}

//#include <stdio.h>

//void main()
//{
	//int a = 100, result;
	//int i;

	//for(i = 1; i <= 5; i ++)
		//i는 1이고 i는 5보다 작고, i는 1씩 증가한다.
//	{
	//	result = a << i;
		//printf("a << %d = %d\n", i, result);
	//}

	//for (i = 1; i <= 5; i++)
	//{
		//result = a >> i;
		//printf("%d >> %d = %d\n", a, i, result);
	//}
//}

/*#define CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{

	float a, b;
	printf("첫 번째 계산할 값을 입력하세요 ==> ");
	scanf("%f", &a);
	printf("두 번째 계산할 값을 입력하세요 ==>");
	scanf("%f", &b);
	printf("%2.2f + %2.2f = %2.2f\n", a, b, a + b);
	printf("%2.2f - %2.2f = %2.2f\n", a, b, a - b);
	printf("%2.2f * %2.2f = %3.2f\n", a, b, a * b);
	printf("%2.2f / %2.2f = %2.2f\n", a, b, a / b);
	printf("%.0f %% .0f = %d\n", a, b, (int)a % (int)b);

}*/

/*#include<stdio.h>

void main()
{
	int a = 99;

	if (a < 100)
		printf("100보다 작군여..\n");
}*/

/*#include <stdio.h>

void main()
{
	int a = 200;

	if (a < 100)
	{
		printf("100보다 작군여..\n");
		printf("거짓이므로 이 문장은 안 보이겠죠?ㅜ \n");
	}
	printf("프로그램 끝!\n");

}*/

/*#include <stdio.h>

void main()
{
	int a = 200;

	if (a < 100)
		printf("100보다 작군여..\n");
	else
		printf("100보다 크군여..\n");

}*/

/*#include <stdio.h>

void main()
{

	int a = 200;

	if (a < 100)
	{
		printf("100보다 작군여..\n");
		printf("참이면 이 문장도 보이겠져?\n");
	}
	else
	{
		printf("100보다 크군여..\n");
		printf("거짓이면 이 문장도 보이겠져?\n");
	}
	printf("프로그램 끝!\n");
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int a;

	printf("정수를 입력하세요 : ");
	scanf("%d", &a);

	if (a % 2 == 0)
	{
		printf("짝수입니다 ..\n");

	}
	else
	{
		printf("홀수를 입력했군요..\n");
	}
}*/

/*#include<stdio.h>

void main()
{
	int a = 75;

	if (a > 50)
	{
		if (a < 100)
		{
			printf("50보다 크고 100보다 작네여..\n");
		}
		else
		{
			printf("와~~ 100보다 크다~\n");
		}
	}
}*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
/*void main()
{
	int a;

	printf("점수를 입력하시오 : ");
	scanf("%d", &a);

	if (a >= 90)
		printf("당신의 학점은 A입니다.\n");
	else
	{
		if (a >= 80)
			printf("당신의 학점은 B입니다.\n");
		else 
			if (a >= 70)
				printf("당신의 학점은 C입니다.\n");
			else
				printf("당신의 학점은 D입니다.\n");
	}
}*/

/*void main()
{
	int a;

	printf("1~4 중에 선택하세여 : ");
	scanf("%d%", &a);

	switch (a)
	{
	case 1:
		printf("1조\n");
		break;
	
	case 2:
		printf("2조\n");
		break;

	case 3:
		printf("3조\n");
		break;

	case 4:
		printf("4조\n");
		break;

	default:
		printf("이상한 걸 선택했다.\n");

	}
}*/

/*void main()
{
	int year;

	printf("출생연도를 입력하세요 : ");
	scanf("%d", &year);

	switch (year % 12)
	{
	case 0: printf("원숭이띠\n"); break;
	case 1: printf("닭띠\n");break;
	case 2: printf("개띠\n");break;
	case 3: printf("돼지띠\n");break;
	case 4: printf("쥐띠\n");break;
	case 5: printf("소띠\n");break;
	case 6: printf("호랑이띠\n");break;
	case 7: printf("토끼띠\n");break;
	case 8: printf("용띠\n");break;
	case 9: printf("뱀띠\n");break;
	case 10: printf("말띠\n");break;
	case 11: printf("양띠\n");break;
	}
}*/

/*void main()
{
	int a, b;
	char c;
	
	printf("첫번째 수를 입력하세요 : ");
	scanf("%d", &a);

	printf("계산할 연산자를 입력하세요 : ");
	scanf(" %c", &c);

	printf("두 번째 수를 입력하세요 : ");
	scanf("%d", &b);

	if (c ==  "+")
		printf("%d %c %d = %d 입니다.\n", a, c, b, a + b);
	if (c ==  "-")
		printf("%d %c %d = %d 입니다.\n", a, c, b, a - b);
	if (c == "*")
		printf("%d %c %d = %d 입니다.\n", a, c, b, a * b);
	if (c == "/")
		printf("%d %c %d = %.2f 입니다.\n", a, c, b, (float)a / b);
	if (c == "%")
		printf("%d %c %d = %d 입니다.\n", a, c, b, a % b);
}*/

/*void main()
{
	int a, b;
	char c;
	float result;

	printf("수식을 한 줄로 띄어쓰기 해서 입력하세요 : ");
	scanf("%d %c %d", &a, &c, &b);

	switch (c) {
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	default: printf("잘못입력함");
	}
	printf("%d %c %d = %d 입니다." a, b)
}*/

/*#include <stdio.h>

void main()
{
	int i;
	for (i = 0; i < 3; i++)
	{
		printf("하이요\n");
		printf("##리하이요##\n");
	}

	printf("\n\n");
	
	for (i = 0; i < 3; i++)
		printf("하이요 \n");
		printf("##리하이요##\n");
	int i;
	for (i = 0; i < 100; i = i + 3)
		printf(" %d번 실행 : 안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n", i);
	
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
	printf("안녕하세요? 빙글빙글 for문을 공부 중입니다. ^^\n");
}*/

#include<stdio.h>

void main()
{
	int hap = 0;
	int i;


	/*for (i = 5; i > 0; i--)
	{
		printf("%d : 안녕하세여? 빙글빙글 for문을 공부중입니다. ^^\n", i);
	}
	for (i = 1; i <= 5; i++)
	{
		printf("%d : 안녕하세여? 빙글빙글 for문을 공부중입니다. ^^\n", i);
	}*/
	for (i = 501; i <= 1000; i= i+2)
	{
		hap = hap + i;
		
	}
	printf("%d ", hap);
}
