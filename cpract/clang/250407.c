/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int coffee;

	printf("커피 몇 잔을 드릴까요? (1잔, 2잔, 3잔)");
	scanf("%d", &coffee);

	printf("\n #1. 뜨거운 물을 준비한다\n");
	printf("#2. 종이컵을 준비한다\n");

	switch (coffee)
	{

	case 1: printf("#3. %d 잔의 커피를 탄다\n", coffee); break;
	case 2: printf("#3. %d 잔의 커피를 탄다\n", coffee); break;
	case 3: printf("#3. %d 잔의 커피를 탄다\n", coffee); break;
	default:printf("#4. 빨리 주문해주세요~\n"); break;
	}
	
}
*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int coffee_machine(int button)
{
	printf("\n #1. 뜨거운 물을 준비한다\n");
	printf("#2. 종이컵을 준비한다\n");

	switch (button)
	{
	case 1: printf("#3. 보통커피를 탄다\n"); break;
	case 2: printf("#3. 설탕커피를 탄다\n"); break;
	case 3: printf("#3.  블랙커피를 탄다\n"); break;
	default:printf("#3. 아무거나 주문해주세요~\n"); break;
	}

	printf("#4. 물을 붓는다\n");
	printf("#5. 스푼으로 저어서 녹인다\n");

}

void main()
{
	int coffee;
	int ret;

	printf("어떤 커피를 드릴까요?(1:보통커피, 2:설탕커피, 3:블랙커피) : ");
	scanf("%d", &coffee);

	ret = coffee_machine(coffee);

	printf("\n#6. 커피를 드린다\n");
}

*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
int calc(int v1, int v2, int op)
{
	int result = 0;

	switch(op)


	{
	case 1: result = v1 + v2; break;
	case 2: result = v1 - v2; break;
	case 3: result = v1 * v2; break;
	case 4: result = v1 / v2; break;
	default: printf("잘못된 연산자입니다.\n"); break;

	}
	return result;
}
void main()
{
	int a, b, c;
	int op;
	printf("첫 번째 숫자를 입력하세요 : ");
	scanf("%d", &a);
	printf("두 번째 숫자를 입력하세요 : ");
	scanf("%d", &b);
	printf("연산자(1: +, 2: -, 3: *, 4: /) : ");
	scanf("%d", &op);
	c = calc(a, b, op);
	printf("결과는 %d입니다.\n"), c;
}*/

/*#include <stdio.h>

int a = 100;

void func1()
{
	int a = 200;
	printf("func1()에서 a = %d\n", a);

}

void main() {
	func1();
	printf("main()에서 a = %d\n", a);
}*/

/*#include <stdio.h>

void func1()

{
	printf("void 형 함수는 돌려줄 게 없음.\n");
}

int func2()
{
	return 100;
}

void main()
{
	int a;

	func1();

	a = func2();
	printf("func2()에서 리턴된 값은 %d\n", a);
}*/

/*#include <stdio.h>
void func1(int a)

{
	a = a + 1;
	printf("전달받은 a ==> %d\n", a);
}

void main()
{
	int a = 10;

	func1(a);
	printf("func1() 실행 후의 a ==> %d", a);
}*/

/*#include <stdio.h>

void func1(int* a)
{
	*a = *a + 1;
	printf("전달받은 a ==> %d\n", *a);
}

void main()
{
	int a = 10;

	func1(&a);
	printf("func1() 실행 후의 a ==> %d\n", a);
}*/

//구구단
/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void gugu(int dan) //매개변수 몇단
{
	int i; // 변수 선언
	for (i = 1; i <= 9; i++)
	{
		printf("%d * %d = %d\n", dan, i, dan * i);
	}
}
void main() //출력
{
	int input;
	printf("구구단 몇 단을 출력할까요? : ");
	scanf("%d", &input);

	gugu(input);
}
*/

//대소문자 변환
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*int main()
{
	char str[100];
	int i;

	// 문자열 초기화 (사실 생략해도 괜찮음)
	for (i = 0; i < 100; i++)
		str[i] = '\0';

	// 문자열 입력
	printf("문자열을 입력하세요 : ");
	scanf("%s", str);  // 공백 없이 입력할 경우만 유효

	// 대소문자 변환
	for (i = 0; i < strlen(str); i++)
	{
		if (str[i] >= 'a' && str[i] <= 'z')  // 소문자면
		{
			str[i] = str[i] - ('a' - 'A');  // 대문자로
		}
		else if (str[i] >= 'A' && str[i] <= 'Z')  // 대문자면
		{
			str[i] = str[i] + ('a' - 'A');  // 소문자로
		}
		// 다른 문자(숫자, 기호 등)는 무시
	}

	// 변환된 문자열 출력
	printf("변환된 문자열 : %s\n", str);

	return 0;
}  // main
*/
//로또 추첨

/*int val[6]; // 로또 번호를 저장할 배열
int i, j, k;
int temp;
int num[45]; // 1~45까지의 숫자를 저장할 배열
int main()
{
	for (i = 0; i < 45; i++)
		num[i] = i + 1; // 1~45까지의 숫자 저장
	// 난수 발생을 위한 초기화

srand(time(NULL)); // 난수 초기화
for (i = 0; i < 6; i++)
{
	k = rand() % (45 - i); // 0~(44-i)까지의 난수 발생
	val[i] = num[k]; // 난수에 해당하는 번호를 val에 저장
	num[k] = num[44 - i]; // 선택된 번호를 배열의 마지막으로 이동
}
// 정렬
for (i = 0; i < 5; i++)
{
	for (j = i + 1; j < 6; j++)
	{
		if (val[i] > val[j])
		{
			temp = val[i];
			val[i] = val[j];
			val[j] = temp;
		}
	}
}
printf("로또 번호 : ");
for (i = 0; i < 6; i++)
	printf("%d ", val[i]);
printf("\n");
return 0;
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int a;
	float b;
	char ch;
	char s[20];

	printf("정수를 입력 :");
	scanf("%d", &a);
	printf("실수를 입력 :");
	scanf("%f", &b);
	printf("문자를 입력 :");
	scanf(" %c", &ch); // 공백을 넣어주면 버퍼에 남아있는 개행문자를 무시함
	printf("문자열을 입력 :");
	scanf("%s", s);
	
	print("\n 정수의 십진수 ==? %d\n", a);
	printf("정수의 8진수 ==? %o\n", a);
	printf("정수의 16진수 ==> %x\n", a);
}*/

/*#include <stdio.h>

void main()
{
	char s[20];

	printf("문자열을 입력 :");
	gets(s); //최대 19자 까지 입력가능.

	puts(s);
}*/

/*#include	<stdio.h>
#include	<string.h>

void main()
{
	char password[5] = "5678";
	char input[5];
	int i;

	printf("비밀번호를 입력하세요 : ");
	for(i=0; i<=4; i++)
		input[i] = getch();

	if (strncmp(password, input, 4) == 0)
	{
		printf("비밀번호가 일치합니다.\n");
	}
	else
	{
		for (i = 0; i <= 4; i++)
			putch(input[i]); // 입력된 비밀번호 초기화
		printf("비밀번호가 틀립니다.\n");
	}
}*/

#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	//char s[20];//읽어올 수 있는 문자열의 수, 저장할 배열"
	/*FILE* rfp; //변수이름
	int hap = 0;
	int in, i;

	rfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "r");

	for (i = 0; i < 5; i++)
	{
		fscanf(rfp, "%d", &in);
		hap = hap + in;
	}

	printf("합계 ==> %d\n", hap);

	fclose(rfp);//ansi로 인코딩된 건 잘읽는데 utf=8로 한건 글씨가 깨지더라.
}*/
	/*char s[20];
	FILE* wfp;

	wfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "w");
	printf("문자열을 입력하세요 : ");
	gets(s);

	fputs(s, wfp);
	fclose(wfp);*/

	FILE* wfp;
	int hap = 0;
	int in, i;

	wfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "w");

	for (i = 0; i < 5; i++)
	{
		printf("숫자 %d : ", i + 1);
		scanf(" %d", &in);
		hap = hap + in;
	}
	fprintf(wfp, "합계 ==> : %d\n", hap);

	fclose(wfp);
}

//code line for commit add
