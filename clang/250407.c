/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int coffee;

	printf("Ŀ�� �� ���� �帱���? (1��, 2��, 3��)");
	scanf("%d", &coffee);

	printf("\n #1. �߰ſ� ���� �غ��Ѵ�\n");
	printf("#2. �������� �غ��Ѵ�\n");

	switch (coffee)
	{

	case 1: printf("#3. %d ���� Ŀ�Ǹ� ź��\n", coffee); break;
	case 2: printf("#3. %d ���� Ŀ�Ǹ� ź��\n", coffee); break;
	case 3: printf("#3. %d ���� Ŀ�Ǹ� ź��\n", coffee); break;
	default:printf("#4. ���� �ֹ����ּ���~\n"); break;
	}
	
}
*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int coffee_machine(int button)
{
	printf("\n #1. �߰ſ� ���� �غ��Ѵ�\n");
	printf("#2. �������� �غ��Ѵ�\n");

	switch (button)
	{
	case 1: printf("#3. ����Ŀ�Ǹ� ź��\n"); break;
	case 2: printf("#3. ����Ŀ�Ǹ� ź��\n"); break;
	case 3: printf("#3.  ��Ŀ�Ǹ� ź��\n"); break;
	default:printf("#3. �ƹ��ų� �ֹ����ּ���~\n"); break;
	}

	printf("#4. ���� �״´�\n");
	printf("#5. ��Ǭ���� ��� ���δ�\n");

}

void main()
{
	int coffee;
	int ret;

	printf("� Ŀ�Ǹ� �帱���?(1:����Ŀ��, 2:����Ŀ��, 3:��Ŀ��) : ");
	scanf("%d", &coffee);

	ret = coffee_machine(coffee);

	printf("\n#6. Ŀ�Ǹ� �帰��\n");
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
	default: printf("�߸��� �������Դϴ�.\n"); break;

	}
	return result;
}
void main()
{
	int a, b, c;
	int op;
	printf("ù ��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &a);
	printf("�� ��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &b);
	printf("������(1: +, 2: -, 3: *, 4: /) : ");
	scanf("%d", &op);
	c = calc(a, b, op);
	printf("����� %d�Դϴ�.\n"), c;
}*/

/*#include <stdio.h>

int a = 100;

void func1()
{
	int a = 200;
	printf("func1()���� a = %d\n", a);

}

void main() {
	func1();
	printf("main()���� a = %d\n", a);
}*/

/*#include <stdio.h>

void func1()

{
	printf("void �� �Լ��� ������ �� ����.\n");
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
	printf("func2()���� ���ϵ� ���� %d\n", a);
}*/

/*#include <stdio.h>
void func1(int a)

{
	a = a + 1;
	printf("���޹��� a ==> %d\n", a);
}

void main()
{
	int a = 10;

	func1(a);
	printf("func1() ���� ���� a ==> %d", a);
}*/

/*#include <stdio.h>

void func1(int* a)
{
	*a = *a + 1;
	printf("���޹��� a ==> %d\n", *a);
}

void main()
{
	int a = 10;

	func1(&a);
	printf("func1() ���� ���� a ==> %d\n", a);
}*/

//������
/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void gugu(int dan) //�Ű����� ���
{
	int i; // ���� ����
	for (i = 1; i <= 9; i++)
	{
		printf("%d * %d = %d\n", dan, i, dan * i);
	}
}
void main() //���
{
	int input;
	printf("������ �� ���� ����ұ��? : ");
	scanf("%d", &input);

	gugu(input);
}
*/

//��ҹ��� ��ȯ
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*int main()
{
	char str[100];
	int i;

	// ���ڿ� �ʱ�ȭ (��� �����ص� ������)
	for (i = 0; i < 100; i++)
		str[i] = '\0';

	// ���ڿ� �Է�
	printf("���ڿ��� �Է��ϼ��� : ");
	scanf("%s", str);  // ���� ���� �Է��� ��츸 ��ȿ

	// ��ҹ��� ��ȯ
	for (i = 0; i < strlen(str); i++)
	{
		if (str[i] >= 'a' && str[i] <= 'z')  // �ҹ��ڸ�
		{
			str[i] = str[i] - ('a' - 'A');  // �빮�ڷ�
		}
		else if (str[i] >= 'A' && str[i] <= 'Z')  // �빮�ڸ�
		{
			str[i] = str[i] + ('a' - 'A');  // �ҹ��ڷ�
		}
		// �ٸ� ����(����, ��ȣ ��)�� ����
	}

	// ��ȯ�� ���ڿ� ���
	printf("��ȯ�� ���ڿ� : %s\n", str);

	return 0;
}  // main
*/
//�ζ� ��÷

/*int val[6]; // �ζ� ��ȣ�� ������ �迭
int i, j, k;
int temp;
int num[45]; // 1~45������ ���ڸ� ������ �迭
int main()
{
	for (i = 0; i < 45; i++)
		num[i] = i + 1; // 1~45������ ���� ����
	// ���� �߻��� ���� �ʱ�ȭ

srand(time(NULL)); // ���� �ʱ�ȭ
for (i = 0; i < 6; i++)
{
	k = rand() % (45 - i); // 0~(44-i)������ ���� �߻�
	val[i] = num[k]; // ������ �ش��ϴ� ��ȣ�� val�� ����
	num[k] = num[44 - i]; // ���õ� ��ȣ�� �迭�� ���������� �̵�
}
// ����
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
printf("�ζ� ��ȣ : ");
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

	printf("������ �Է� :");
	scanf("%d", &a);
	printf("�Ǽ��� �Է� :");
	scanf("%f", &b);
	printf("���ڸ� �Է� :");
	scanf(" %c", &ch); // ������ �־��ָ� ���ۿ� �����ִ� ���๮�ڸ� ������
	printf("���ڿ��� �Է� :");
	scanf("%s", s);
	
	print("\n ������ ������ ==? %d\n", a);
	printf("������ 8���� ==? %o\n", a);
	printf("������ 16���� ==> %x\n", a);
}*/

/*#include <stdio.h>

void main()
{
	char s[20];

	printf("���ڿ��� �Է� :");
	gets(s); //�ִ� 19�� ���� �Է°���.

	puts(s);
}*/

/*#include	<stdio.h>
#include	<string.h>

void main()
{
	char password[5] = "5678";
	char input[5];
	int i;

	printf("��й�ȣ�� �Է��ϼ��� : ");
	for(i=0; i<=4; i++)
		input[i] = getch();

	if (strncmp(password, input, 4) == 0)
	{
		printf("��й�ȣ�� ��ġ�մϴ�.\n");
	}
	else
	{
		for (i = 0; i <= 4; i++)
			putch(input[i]); // �Էµ� ��й�ȣ �ʱ�ȭ
		printf("��й�ȣ�� Ʋ���ϴ�.\n");
	}
}*/

#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	//char s[20];//�о�� �� �ִ� ���ڿ��� ��, ������ �迭"
	/*FILE* rfp; //�����̸�
	int hap = 0;
	int in, i;

	rfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "r");

	for (i = 0; i < 5; i++)
	{
		fscanf(rfp, "%d", &in);
		hap = hap + in;
	}

	printf("�հ� ==> %d\n", hap);

	fclose(rfp);//ansi�� ���ڵ��� �� ���дµ� utf=8�� �Ѱ� �۾��� ��������.
}*/
	char s[20];
	FILE* wfp;

	wfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "w");
	printf("���ڿ��� �Է��ϼ��� : ");
	gets(s);

	fputs(s, wfp);
	fclose(wfp);
}