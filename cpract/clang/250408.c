
/*//���� ����
int i;
char bf[20];
FILE* wfp;
FILE* rfp;

// ���� ����
rfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "r");
wfp = fopen("C:\\Users\\AISW-006\\Desktop\\data2.txt", "w");
//���� �б�
while (1)
{
	fgets(bf, sizeof(bf), rfp); //���Ͽ��� �� �� �б�
	if (feof(rfp)) break; //���� ���� �����ϸ� ����

	for (i = strlen(bf) - 2; i >= 0; i--) //���ڿ��� ���������� �Ųٷ� �б�
	{
		fprintf(wfp, "%c", bf[i]); //�Ųٷ� ���� ���� ���
	}
	fprintf(wfp, "\n");
	if (feof(rfp))
		break; //���� ���� �����ϸ� ����
	// �ݴ� ������ ���Ͽ� ����
}
//���� �ݱ�
fclose(rfp);
fclose(wfp);
}*/

/* {
	//int aa[10000]; //�޸𸮴� �Ҵ�Ǿ��µ� �Ⱦ��� ����Ǵ� ����.
	int* p;
	int i, hap = 0;
	int cnt;

	printf("�� ���� ���ڸ� �Է��Ͻðڽ��ϱ�? : ");
	scanf("%d", &cnt);


	p = (int*)malloc(sizeof(int) * cnt);
	printf(p);

		for (i = 0; i < cnt; i++) //cnt��ŭ �ݺ�
	{
		printf(" %d��° ���� :", i + 1);
		scanf("%d", p + i);
		// scanf("%d", &aa[i]);
	}

	//p = aa;

	for (i = 0; i < cnt; i++) //cnt��ŭ �ݺ�
	{
		hap = hap + *(p + i);
	}

	printf("�հ� ==> %d\n", hap);

	free(p); //�����Ҵ��� �޸� ����

}*/

/*int* p, * s;
int i, j;

printf("malloc() �Լ� ���\n");
p = (int*)malloc(sizeof(int) * 3);

for(i=0; i<3; i++)
	printf("�Ҵ�� ���� �ʱ갪 p[%d] ==>%d\n", i, p[i]);

free(p); //�����Ҵ��� �޸� ����

printf("\ncalloc()�Լ� ���\n");
s = (int*)calloc(sizeof(int),3);

for (j = 0; j < 3; j++)
	printf("�Ҵ�� ���� �ʱ갪 s[%d] ==> %d\n", j, s[j]);

free(s);

}*/
#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<malloc.h>
#include<string.h>
void main()
/* {
	char data[3][100];
	int i;

	for (i = 0; i < 3; i++)
	{
		printf("%d ��° ���ڿ� :", i + 1);

		gets(data[i]);
	}

	printf("\n�Է°� �ݴ�� ���\n");

	for (i = 2; i >= 0; i--)
	{
		printf("%d ��° ���ڿ� : %s\n", i + 1, data[i]);
	}
}*/

/* {
	char* p[3];
	char imsi[100];
	int i, size;

	for (i = 0; i < 3; i++)
	{
		printf("%d ��° ���ڿ� : ", i + 1);
		gets(imsi);

		size = strlen(imsi);
		p[i] = (char*)malloc((sizeof(char) * size) + 1);

		strcpy(p[i], imsi);
	}
	for (i = 0; i < 3; i++)
		free(p[i]);
}*/

{

	/*int a = 3;
	int* b = &a;
	int** c = &b;

	printf("a�� ����� �� = %d\n", a);
	printf("b�� ����� �� = %d\n", b);
	printf("c�� ����� �� = %d\n", c);

	printf("b�� ����Ű�� �� = %d\n", *b);
	printf("c�� ����Ű�� �� = %d\n", *c);
	printf("c�� ���������� ����Ű�� �� = %d\n", **c);
	*/
	/*struct  bibim
	{
		int a;
		float b;
		char c;
		char d[5];
	};

	struct bibim b1;

	b1.a = 10;
	b1.b = 1.1f;
	b1.c = 'A';
	strcpy(b1.d, "ABCD");

	printf("b1.a ==> %d\n", b1.a);
	printf("b1.b ==> %f\n", b1.b);
	printf("b1.c ==> %c\n", b1.c);
	printf("b1.d ==> %s\n", b1.d);
	*/

	/*char name[3][20];
	int kor[3];
	int eng[3];
	float avg[3];

	int i;

	strcpy(name[0], "ȫ�浿");

	kor[0] = 90;
	eng[0] = 80;
	avg[0] = (kor[0] + eng[0]) / 2.0f;

	strcpy(name[1], "�̸��");

	kor[1] = 50;
	eng[1] = 30;
	avg[1] = (kor[1] + eng[1]) / 2.0f;

	for(i=0; i<2; i++)
	{
		printf("�̸� ==> %s\n", name[i]);
		printf("���� ==> %d\n", kor[i]);
		printf("���� ==> %d\n", eng[i]);
		printf("��� ==> %.2f\n", avg[i]);
	}*/


	/*scanf("%s", name, 9);//�ִ� 9�� ���� �ϴ� ��

	printf("���� : ");
	scanf("%d", &kor);

	printf("���� : ");
	scanf("%d", &eng);
	avg = (kor + eng) / 2.0f;

	printf("\n");
	printf("�̸� ==> %s\n", name);
	printf("���� ==> %d\n", kor);
	printf("���� ==> %d\n", eng);
	printf("��� ==> %.2f\n", avg);
	*/
	/*struct student {
		char name[10];
		int kor;
		int eng;
		float avg;
	};

	struct student s;
	struct student* p;

	p = &s;

	printf("�̸� �Է� :");
	scanf("%s",p->name);

	printf("���� ���� �Է� :");
	scanf("%d", &p->kor);
	printf("���� ���� �Է� :");
	scanf("%d", &p->eng);

	p->avg = (p->kor + p->eng) / 2.0f;
	printf("�л��̸� ==> %s\n", p->name);
	printf("���� ���� ==> %d\n", p->kor);
	printf("���� ���� ==> %d\n", p->eng);
	printf("��� ���� ==> %.2f\n", p->avg);
	*/

	/*union student {
		int tot;
		char grade;
	};

	union student u;

	u.tot = 300;
	u.grade = 'A';

	printf("���� ==> %d\n", u.tot);
	printf("���� ==> %c\n", u.grade);
	}*/

	enum week { sun, mon, tue, wed, thu, fri, sat };
	enum week ww;

	ww = sat;

	if (ww == sun)
		printf("�Ͽ����Դϴ�.\n");
	else
		printf("�Ͽ����� �ƴմϴ�.\n");
}