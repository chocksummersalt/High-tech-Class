/*#include <stdio.h>

void main()
{
	int i, k;

	for (i = 0; i < 3; i++)
	{
		for (k = 0; k < 2; k++)
		{
			printf("��ø for���Դϴ�. (i��: %d, k��: %d)\n", i, k);
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
		printf("���� �� �� �Է� (���߷��� ��Ʈ�� ��) : ");
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
		printf("|10���� : %d| 16���� : %x| �ƽ�Ű�ڵ� : %c|\n", a, a, a);
	}
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
	printf("������ �� ���ڸ� �Է� : ");
	scanf("%s, str");

}*/

/*#include <stdio.h>

void main()
{
	int i;
	i = 0;

	while (i < 5) {
		printf("while���� �����մϴ�.\n");
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
	printf("1���� 10������ ��: %d\n", hap);
}*/


/* {
	int a, b;

	while (1)
	{
		printf("���� �� �� �Է�( ���߷��� ��Ʈ�Ѿ�) : ");
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
		printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
		scanf("%d %d", &a, &b);

		printf("����� �����ڸ� �Է��ϼ��� : ");
		scanf("%c", &ch);

		switch (ch)
		{
			case'+':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
				break;
			case'-':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
				break;
			case'*':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
				break;
			case'/':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
			case'%':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
				break;
			case'//':
				printf("����� �� ���� �Է� (���߷��� ��Ʈ�Ѿ�) : ");
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
		printf("while�� ���ο� ���Խ��ϴ�. \n");
	}

	do {
		printf("do~while�� ���ο� ���Խ��ϴ�. \n");

	} while(a == 200);
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
	int i;
	char menu;

	

	printf("������ �ֹ� �Ͻðڽ��ϱ�? : \n <1>ī��� <2>īǪġ�� <3>�Ƹ޸�ī�� <4>�׸���ų����");
	scanf("%d", &i);
	

}�� �غ��� �ֹ��޴� �ý��� �����*/

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
		printf("for���� %dȸ �����߽��ϴ�.\n", i);
		break;
	}

	printf("for���� �����߽��ϴ�. \n");
}*/

/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main()
{
	int a, b;

	for (a = 1; a <= 100; a++)
	for (b = 1; b <= 100; b++)

	{
		printf("for���� %dȸ �����߽��ϴ�.\n", i);
		break;
			if(a = 0)

	}
printf(0�� �Է��ؼ� for���� Ż���߽��ϴ�.)
	printf("for���� �����߽��ϴ�. \n");
}*/

/*#include <stdio.h>

void main()
{
	int hap = 0;
	int i;

	for (i = 1; i <= 100; i++)//i�� 1�ε� 1���� ++�ؼ� 100������ ��� for(�ݺ�) �Ѵ�.
	{
		hap = hap + i; //�� ���� �տ� �����ǰ� ���� ��� �����Ǿ 1000�� �ѱ�����

		if (hap >= 1000)
			break; //�������´�.
	}
	printf("1~100�� �տ��� ���ʷ� 1000�� �Ѵ� ��ġ��? : %d\n", i);
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
	printf("1~ 100������ ��(3�� ��� ����):%d\n", hap);
}