/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int a, b, c, d;
	int hap;

	printf("1번째 숫자를 입력하세요 : ");
	scanf("%d", &a);
	printf("2번째 숫자를 입력하세요 : ");
	scanf("%d", &b);
	printf("3번째 숫자를 입력하세요 : ");
	scanf("%d", &c);
	printf("4번째 숫자를 입력하세요 : ");
	scanf("%d", &d);

	hap = a + b + c + d;

	printf("합계 ==> %d\n", hap);
}*/

//#define _CRT_SECURE_NO_WARNINGS


/*	printf("1번째 숫자를 입력하세요 : ");
	scanf("%d", &aa[0]);
	printf("2번째 숫자를 입력하세요 : ");
	scanf("%d", &aa[1]);
	printf("3번째 숫자를 입력하세요 : ");
	scanf("%d", &aa[2]);
	printf("4번째 숫자를 입력하세요 : ");
	scanf("%d", &aa[3]);

	for (i = 0; i < 4; i++) {
		hap += aa[i];
	}
	hap = aa[0] + aa[1] + aa[2] + aa[3];

	printf("합계 ==> %d\n", hap);*/


/*#include <stdio.h>
void main()
{
	int aa[4] = { 100, 200, 300, 400 };
	int bb[] = { 100, 200, 300, 400 };
	int cc[4] = { 100, 200 };
	int dd[4] = { 0 };
	int i;

	for (i = 0; i <= 3; i++)
		printf("aa[%d] ==> %d\t", i, aa[i]);
	printf("\n");

	for (i = 0; i <= 3; i++)
		printf("bb[%d] ==> %d\t", i, bb[i]);
	printf("\n");
}*/


/*#include <stdio.h>

void main()
{
	int aa[100], bb[100];
	int i, j;
	for (i = 0, j = 99; i < 100; i++) 
	{
		aa[i] = i * 2;
		print("aa[%d} = a");
	}
	for (i = 0, j = 99; i < 10)
	{
		bb[j] = aa[i];
		print("bb[%d] = b")
	}
	*/
/*#include <stdio.h>

void main()
{
	int aa[] = { 10, 20, 30, 40, 50 };
	int count;

	count = sizeof(aa) / sizeof(int);

	printf("배열 aa[]의 요소의 갯ㅅ수는 %d입니다. \n",count) ;
	
}*/

/*#include <stdio.h>

void main()
{
	char ss[8] = "Basic-C";

	int i;

	ss[5] = '#';
	
	for (i = 0; i < 8;i++)
	{
		printf("ss[%d] ==> %c \n", i, ss[i]);
	}
	printf("문자열 배열 ss ==> %s \n", ss);
}*/

/*#include <stdio.h>

void main()
{
	char ss[5] = "abcd";
	char tt[5];
	int i;

	for (i = 0; i < 4; i++)
	{
		tt[5] = ss[3 - i];
	}
	tt[4] = '\0';

	printf("거꾸로 출력한 결과==> %s \n", tt);
}*/

#define _CRT_SECURE_NO_WARNINGS
#include<string.h>*/
#include<stdio.h>
void main()
/* {
	char ss[] = "XYZ";
	int len;

	len = strlen(ss);

	printf("문자열 \"%s\"의 길이 ==> %d \n", ss, len);
}*/
/* {
	char ss[4];

	strcpy(ss, "XYZ");

	printf("문자열 ss의 내용 ==> %s \n", ss);
}*/

/*	{
char ss[7] = "xyz";

	strcat(ss, "ABC");

	printf("이어진 문자열  sss의 내용 ==> %s \n", ss);*/
	/*char ss[20];
	char tt[20];
	int r1, r2;

	puts("첫 번째 문자열을 입력하세요.");
	gets(ss);

	puts("두 번째 문자열을 입력하세요");
	gets(tt);

	r1 = strlen(ss);
	r2 = strlen(tt);

	printf("첫 번째 문자열의 길이 ==> %d \n", r1);
	printf("두 번째 문자열의 길이 ==> %d \n", r2);

	if(strcmp)

}*/

/* {
	int aa[3][4];
	aa[0][0] = 1; aa[0][1] = 2; aa[0][2] = 3; aa[0][3] = 4;
	aa[1][0] = 5; aa[1][1] = 6; aa[1][2] = 7; aa[1][3] = 8;
	aa[2][0] = 9; aa[2][1] = 10; aa[2][2] = 11; aa[2][3] = 12;

	printf("aa[0][0]부터 aa[2][3]까지 출력\n");

	printf("%3d %3d %3d %3d\n", aa[0][0], aa[0][1], aa[0][2], aa[0][3]);
	printf("%3d %3d %3d %3d\n", aa[1][0], aa[1][1], aa[1][2], aa[1][3]);
	printf("%3d %3d %3d %3d\n", aa[2][0], aa[2][1], aa[2][2], aa[2][3]);


}*/

/* {
	int aa[3][4];
	int i, k;

	int val = 1;

	for (i = 0; i < 3; i++)
	{
		for (k = 0; k < 4; k++)
		{
			aa[i][k] = val;
			val++;
		}
	}
	printf("aa[0][0]부터 aa[2][3]까지 출력 \n");

	for(i= 0 ; i < 3; i++)
	{
		for (k = 0; k < 4; k++)
		{
			printf("%3d", aa[i][k]);
		}
		printf("\n");
	}

}*/
//문자열 거꾸로 출력하는 프로그램 작성
//1. 문자열 입력
//2. 입력받은 값에서 \0문자의 위치를 찾는다.
//3. \0문자 부터 역순으로 반복하여 출력한다.

/* {
	char aa[10];
	int i, count=0;
	printf("문자열을 입력하세여 :");
	scanf("%s", aa);

	for (i = 0; i < 10; i++)
	{
		if (aa[i] == '\0')
		{
			count = i;
				break;
		}
	}
	printf("내용을 거꾸로 출력 ==> ");
	for (i = count; i >= 0; i--)
	printf("%c", aa[i]);
}*/

/*{
	char str[100];//배열하고 변수랑은 같이 둘 수 없음?
	char ch1, ch2;
	int i;

	printf("여러 글자를 입력: ");
	scanf(str);

	printf("기존 문자와 새로운 문자 : ");
	scanf("%c %c", &ch1, &ch2);

	for(i=0; i < strlen(str); i++)//각 문자 하나하나를 검사하기 i가 하나하나 돌아다니는 역할을 함
	{ 
		if (str[i] == ch1)
			str[i] = ch2;
	}
}*/
{
	int i, j;
	for (j = 0; j < 10; j++)
	{
		for (i = 0; i < j+1; i++)
		{
			if (i == 0 || j == 0 || i == j)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
		
}
