/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
	int a, b, c, d;
	int hap;

	printf("1��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &a);
	printf("2��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &b);
	printf("3��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &c);
	printf("4��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &d);

	hap = a + b + c + d;

	printf("�հ� ==> %d\n", hap);
}*/

//#define _CRT_SECURE_NO_WARNINGS


/*	printf("1��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &aa[0]);
	printf("2��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &aa[1]);
	printf("3��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &aa[2]);
	printf("4��° ���ڸ� �Է��ϼ��� : ");
	scanf("%d", &aa[3]);

	for (i = 0; i < 4; i++) {
		hap += aa[i];
	}
	hap = aa[0] + aa[1] + aa[2] + aa[3];

	printf("�հ� ==> %d\n", hap);*/


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

	printf("�迭 aa[]�� ����� �������� %d�Դϴ�. \n",count) ;
	
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
	printf("���ڿ� �迭 ss ==> %s \n", ss);
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

	printf("�Ųٷ� ����� ���==> %s \n", tt);
}*/

#define _CRT_SECURE_NO_WARNINGS
#include<string.h>*/
#include<stdio.h>
void main()
/* {
	char ss[] = "XYZ";
	int len;

	len = strlen(ss);

	printf("���ڿ� \"%s\"�� ���� ==> %d \n", ss, len);
}*/
/* {
	char ss[4];

	strcpy(ss, "XYZ");

	printf("���ڿ� ss�� ���� ==> %s \n", ss);
}*/

/*	{
char ss[7] = "xyz";

	strcat(ss, "ABC");

	printf("�̾��� ���ڿ�  sss�� ���� ==> %s \n", ss);*/
	/*char ss[20];
	char tt[20];
	int r1, r2;

	puts("ù ��° ���ڿ��� �Է��ϼ���.");
	gets(ss);

	puts("�� ��° ���ڿ��� �Է��ϼ���");
	gets(tt);

	r1 = strlen(ss);
	r2 = strlen(tt);

	printf("ù ��° ���ڿ��� ���� ==> %d \n", r1);
	printf("�� ��° ���ڿ��� ���� ==> %d \n", r2);

	if(strcmp)

}*/

/* {
	int aa[3][4];
	aa[0][0] = 1; aa[0][1] = 2; aa[0][2] = 3; aa[0][3] = 4;
	aa[1][0] = 5; aa[1][1] = 6; aa[1][2] = 7; aa[1][3] = 8;
	aa[2][0] = 9; aa[2][1] = 10; aa[2][2] = 11; aa[2][3] = 12;

	printf("aa[0][0]���� aa[2][3]���� ���\n");

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
	printf("aa[0][0]���� aa[2][3]���� ��� \n");

	for(i= 0 ; i < 3; i++)
	{
		for (k = 0; k < 4; k++)
		{
			printf("%3d", aa[i][k]);
		}
		printf("\n");
	}

}*/
//���ڿ� �Ųٷ� ����ϴ� ���α׷� �ۼ�
//1. ���ڿ� �Է�
//2. �Է¹��� ������ \0������ ��ġ�� ã�´�.
//3. \0���� ���� �������� �ݺ��Ͽ� ����Ѵ�.

/* {
	char aa[10];
	int i, count=0;
	printf("���ڿ��� �Է��ϼ��� :");
	scanf("%s", aa);

	for (i = 0; i < 10; i++)
	{
		if (aa[i] == '\0')
		{
			count = i;
				break;
		}
	}
	printf("������ �Ųٷ� ��� ==> ");
	for (i = count; i >= 0; i--)
	printf("%c", aa[i]);
}*/

/*{
	char str[100];//�迭�ϰ� �������� ���� �� �� ����?
	char ch1, ch2;
	int i;

	printf("���� ���ڸ� �Է�: ");
	scanf(str);

	printf("���� ���ڿ� ���ο� ���� : ");
	scanf("%c %c", &ch1, &ch2);

	for(i=0; i < strlen(str); i++)//�� ���� �ϳ��ϳ��� �˻��ϱ� i�� �ϳ��ϳ� ���ƴٴϴ� ������ ��
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
