/*#include <stdio.h>

void main()
{
	int i, k;

	for (i = 0; i < 3; i++)
	{
		for (k = 0; k < 2; k++)
		{
			printf("중첩 for문입니다. (i값: %d, k값: %d)\n", i, k);
		}
	}
}*/

/*#include <stdio.h>

void main()
{
	int i, k;

	for (i = 2; i <= 9; i++)
	{
		for (k = 1; k <= 9; k++)
		{
			printf(" %d X %d = %2d \n", i, k, i * k);
		}
		printf("\n");
	}
		
}*/

/*#include <stdio.h>

void main()
{
	int i, k;

	for (i = 1, k = 1; i <= 9; i++, k++)
		printf(" %d X %d = %d \n", i, k, i * k);
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main()
{
	int a, b;
	for (; ; )
	{
		printf("더할 두 수 입력 (멈추려면 컨트롤 씨) : ");
		scanf("%d %d", &a, &b);
			
		printf("%d + %d = %d \n", a, b, a + b);
	}
}*/

/*#include <stdio.h>

void main()
{

	int a;

	for (a = 0; a <= 127; a++)

	{
		printf("|10진수 : %d| 16진수 : %x| 아스키코드 : %c|\n", a, a, a);
	}
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
	printf("영문자 및 숫자를 입력 : ");
	scanf("%s, str");

}*/

/*#include <stdio.h>

void main()
{
	int i;
	i = 0;

	while (i < 5) {
		printf("while문을 공부합니다.\n");
		i++;
	}
}*/

/*#include <stdio.h>

void main()
{
	int hap = 0;
	int i;

	i = 0;
	while(i <= 10){
		hap = hap + i;
		i++;

		}
	printf("1에서 10까지의 합: %d\n", hap);
}*/


/* {
	int a, b;

	while (1)
	{
		printf("더할 두 수 입력( 멈추려면 컨트롤씨) : ");
		scanf("%d%d", &a, &b);

		printf("%d + %d = %d \n", a, b, a + b);
	}
}*/
/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
void main()
{
	int a, b;
	char ch;

	while (1)
	{
		printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
		scanf("%d %d", &a, &b);

		printf("계산할 연산자를 입력하세요 : ");
		scanf("%c", &ch);

		switch (ch)
		{
			case'+':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
				break;
			case'-':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
				break;
			case'*':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
				break;
			case'/':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
			case'%':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
				break;
			case'//':
				printf("계산할 두 수를 입력 (멈추려면 컨트롤씨) : ");
				break;
		}

	}
}*/

/*#include <stdio.h>

void main()
{
	int a = 100;

	while (a == 200)
	{
		printf("while문 내부에 들어왔습니다. \n");
	}

	do {
		printf("do~while문 내부에 들어왔습니다. \n");

	} while(a == 200);
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
	int i;
	char menu;

	

	printf("무엇을 주문 하시겠습니까? : \n <1>카페라떼 <2>카푸치노 <3>아메리카노 <4>그만시킬래요");
	scanf("%d", &i);
	

}더 해보자 주문받는 시스템 만들기*/

/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main()
{

	int i, k;
	char str[100];

	for (i = 2; i <= 9; i++) 
	{
		for (k = 2; k <= 9; k++) 
		{
			printf("%d X %d = %2d \t", k, i, i * k);
			if (k == 8) {
				printf("break");
				break;
			}
		}
	}
}*/

/*#include<stdio.h>

void main()
{
	int i;

	for (i = 1; i <= 100; i++)
	{
		printf("for문을 %d회 실행했습니다.\n", i);
		break;
	}

	printf("for문을 종료했습니다. \n");
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main()
{
	int a, b;

	for (a = 1; a <= 100; a++)
	for (b = 1; b <= 100; b++)

	{
		printf("for문을 %d회 실행했습니다.\n", i);
		break;
			if(a = 0)

	}
printf(0을 입력해서 for문을 탈출했습니다.)
	printf("for문을 종료했습니다. \n");
}*/

/*#include <stdio.h>

void main()
{
	int hap = 0;
	int i;

	for (i = 1; i <= 100; i++)//i는 1인데 1부터 ++해서 100전까지 계속 for(반복) 한다.
	{
		hap = hap + i; //그 값이 합에 누적되고 합은 계속 누적되어서 1000을 넘기전에

		if (hap >= 1000)
			break; //빠져나온다.
	}
	printf("1~100의 합에서 최초로 1000이 넘는 위치는? : %d\n", i);
}*/

#include <stdio.h>

void main()
{
	int hap = 0;
	int i;

	for (i = 1; i <= 100; i++)
	{
		if (i % 3 == 0)
			continue;

		hap = hap + i;
	}
	printf("1~ 100까지의 합(3의 배수 제외):%d\n", hap);
}