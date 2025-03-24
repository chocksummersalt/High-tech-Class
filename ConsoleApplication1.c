//#include<stdio.h>

//int main()
//{
	//printf("%d + %d = %d",100, 200, 100 + 200);
	//printf("\n");
	//printf("%s %.1f", "100 / 200 =", 100.0 / 200.0);
	//printf("\n");
//}
// Output:100

//#include<stdio.h>

//void main()
//{
//	printf("%d / %d = %.1f \n", 100, 200, 0.5);
//	printf("%c %c \n", 'a', 'K');
//	printf("%s %s \n", "안녕", "c언어");
//}

//#include <stdio.h>

//void main()
//{
	//printf("%d\n", 123);
	//printf("%5d\n", 123);
	//printf("%05d\n", 123);

	//printf("%f\n", 123.45);
	//printf("%7.1f\n", 123.45);
	//printf("%07.3f\n", 123.45);

//}

//int main() {
//	int a = 100;

	//return 0;
//}

//#include <stdio.h>

//void main()

//{
	//printf("\n 줄바꿈 \n 연습 \n");
	//printf("\t 탭 \t 연습 \n");
	//printf("이것을\r 덮어씁니다 \n");
	//printf("삐소리 \a \a \a 세번 \n");
	//printf("글자가 \"강조\"되는 효과 \n");
	//printf("\\\\\\ 역슬래시 세개 출력 \n");
//}

//#include <stdio.h>

//void main()
//{
//	int a;
//	float b;

//	a = 123.45;
//	b = 200;

//	printf("a의 값 ==> %d \n", a);
//	printf("b의 값 ==> %f \n", b);
//}

//#include <stdio.h>

//void main()
//{
	//int a, b;
	//float c, d;

	//a = 100;
	//b = a;

	//c = 111.1f;
	//d = c;

	//printf("a, b의 값 ==> %d, %d \n", a, b);
	//printf("c, d의 값 ==> %5.1f, %5.1f \n", c, d);
//}

#include <stdio.h>

void main()
{
	int a, b, c, d;

	a = 100 + 100;
	b = a + 100;
	c = a + b - 100;
	printf("d = %d + %d = %d \n", a, b, c);

	a = b = c = d = 100;
	printf("a, b, c, d 의 값 ==> %d, %d, %d, %d \n", a, b, c, d);

	a = 100;
	a = a + 200;
	printf("a 의 값 ==> %d \n", a);

}