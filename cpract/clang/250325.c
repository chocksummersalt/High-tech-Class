//#include <stdio.h>

//int main() {
//	char a = 0x20;

//	printf("������ a = %X, 1��Ʈ ���� ����Ʈ�� �� %X \n", a, a << 24);

//	printf("������ a = %X, 2��Ʈ ���� ����Ʈ�� �� %X \n", a, a << 25);

//	printf("������ a = %X, 3��Ʈ ���� ����Ʈ�� �� %X \n", a, a << 26);

//	printf("������ a = %X, 4��Ʈ ���� ����Ʈ�� �� %X \n", a, a << 27);

//	return 0;
//}

//#include <stdio.h>

//void main()
//{
	//int a = 100, result;
	//int i;

	//for(i = 1; i <= 5; i ++)
		//i�� 1�̰� i�� 5���� �۰�, i�� 1�� �����Ѵ�.
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
	printf("ù ��° ����� ���� �Է��ϼ��� ==> ");
	scanf("%f", &a);
	printf("�� ��° ����� ���� �Է��ϼ��� ==>");
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
		printf("100���� �۱���..\n");
}*/

/*#include <stdio.h>

void main()
{
	int a = 200;

	if (a < 100)
	{
		printf("100���� �۱���..\n");
		printf("�����̹Ƿ� �� ������ �� ���̰���?�� \n");
	}
	printf("���α׷� ��!\n");

}*/

/*#include <stdio.h>

void main()
{
	int a = 200;

	if (a < 100)
		printf("100���� �۱���..\n");
	else
		printf("100���� ũ����..\n");

}*/

/*#include <stdio.h>

void main()
{

	int a = 200;

	if (a < 100)
	{
		printf("100���� �۱���..\n");
		printf("���̸� �� ���嵵 ���̰���?\n");
	}
	else
	{
		printf("100���� ũ����..\n");
		printf("�����̸� �� ���嵵 ���̰���?\n");
	}
	printf("���α׷� ��!\n");
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int a;

	printf("������ �Է��ϼ��� : ");
	scanf("%d", &a);

	if (a % 2 == 0)
	{
		printf("¦���Դϴ� ..\n");

	}
	else
	{
		printf("Ȧ���� �Է��߱���..\n");
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
			printf("50���� ũ�� 100���� �۳׿�..\n");
		}
		else
		{
			printf("��~~ 100���� ũ��~\n");
		}
	}
}*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
/*void main()
{
	int a;

	printf("������ �Է��Ͻÿ� : ");
	scanf("%d", &a);

	if (a >= 90)
		printf("����� ������ A�Դϴ�.\n");
	else
	{
		if (a >= 80)
			printf("����� ������ B�Դϴ�.\n");
		else 
			if (a >= 70)
				printf("����� ������ C�Դϴ�.\n");
			else
				printf("����� ������ D�Դϴ�.\n");
	}
}*/

/*void main()
{
	int a;

	printf("1~4 �߿� �����ϼ��� : ");
	scanf("%d%", &a);

	switch (a)
	{
	case 1:
		printf("1��\n");
		break;
	
	case 2:
		printf("2��\n");
		break;

	case 3:
		printf("3��\n");
		break;

	case 4:
		printf("4��\n");
		break;

	default:
		printf("�̻��� �� �����ߴ�.\n");

	}
}*/

/*void main()
{
	int year;

	printf("��������� �Է��ϼ��� : ");
	scanf("%d", &year);

	switch (year % 12)
	{
	case 0: printf("�����̶�\n"); break;
	case 1: printf("�߶�\n");break;
	case 2: printf("����\n");break;
	case 3: printf("������\n");break;
	case 4: printf("���\n");break;
	case 5: printf("�Ҷ�\n");break;
	case 6: printf("ȣ���̶�\n");break;
	case 7: printf("�䳢��\n");break;
	case 8: printf("���\n");break;
	case 9: printf("���\n");break;
	case 10: printf("����\n");break;
	case 11: printf("���\n");break;
	}
}*/

/*void main()
{
	int a, b;
	char c;
	
	printf("ù��° ���� �Է��ϼ��� : ");
	scanf("%d", &a);

	printf("����� �����ڸ� �Է��ϼ��� : ");
	scanf(" %c", &c);

	printf("�� ��° ���� �Է��ϼ��� : ");
	scanf("%d", &b);

	if (c ==  "+")
		printf("%d %c %d = %d �Դϴ�.\n", a, c, b, a + b);
	if (c ==  "-")
		printf("%d %c %d = %d �Դϴ�.\n", a, c, b, a - b);
	if (c == "*")
		printf("%d %c %d = %d �Դϴ�.\n", a, c, b, a * b);
	if (c == "/")
		printf("%d %c %d = %.2f �Դϴ�.\n", a, c, b, (float)a / b);
	if (c == "%")
		printf("%d %c %d = %d �Դϴ�.\n", a, c, b, a % b);
}*/

/*void main()
{
	int a, b;
	char c;
	float result;

	printf("������ �� �ٷ� ���� �ؼ� �Է��ϼ��� : ");
	scanf("%d %c %d", &a, &c, &b);

	switch (c) {
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	case "+": result = a + b; break;
	default: printf("�߸��Է���");
	}
	printf("%d %c %d = %d �Դϴ�." a, b)
}*/

/*#include <stdio.h>

void main()
{
	int i;
	for (i = 0; i < 3; i++)
	{
		printf("���̿�\n");
		printf("##�����̿�##\n");
	}

	printf("\n\n");
	
	for (i = 0; i < 3; i++)
		printf("���̿� \n");
		printf("##�����̿�##\n");
	int i;
	for (i = 0; i < 100; i = i + 3)
		printf(" %d�� ���� : �ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n", i);
	
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
	printf("�ȳ��ϼ���? ���ۺ��� for���� ���� ���Դϴ�. ^^\n");
}*/

#include<stdio.h>

void main()
{
	int hap = 0;
	int i;


	/*for (i = 5; i > 0; i--)
	{
		printf("%d : �ȳ��ϼ���? ���ۺ��� for���� �������Դϴ�. ^^\n", i);
	}
	for (i = 1; i <= 5; i++)
	{
		printf("%d : �ȳ��ϼ���? ���ۺ��� for���� �������Դϴ�. ^^\n", i);
	}*/
	for (i = 501; i <= 1000; i= i+2)
	{
		hap = hap + i;
		
	}
	printf("%d ", hap);
}
