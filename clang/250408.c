
/*//변수 선언
int i;
char bf[20];
FILE* wfp;
FILE* rfp;

// 파일 열기
rfp = fopen("C:\\Users\\AISW-006\\Desktop\\data.txt", "r");
wfp = fopen("C:\\Users\\AISW-006\\Desktop\\data2.txt", "w");
//파일 읽기
while (1)
{
	fgets(bf, sizeof(bf), rfp); //파일에서 한 줄 읽기
	if (feof(rfp)) break; //파일 끝에 도달하면 종료

	for (i = strlen(bf) - 2; i >= 0; i--) //문자열의 끝에서부터 거꾸로 읽기
	{
		fprintf(wfp, "%c", bf[i]); //거꾸로 읽은 문자 출력
	}
	fprintf(wfp, "\n");
	if (feof(rfp))
		break; //파일 끝에 도달하면 종료
	// 반대 순서로 파일에 쓰기
}
//파일 닫기
fclose(rfp);
fclose(wfp);
}*/

/* {
	//int aa[10000]; //메모리는 할당되었는데 안쓰면 낭비되는 것임.
	int* p;
	int i, hap = 0;
	int cnt;

	printf("몇 개의 숫자를 입력하시겠습니까? : ");
	scanf("%d", &cnt);


	p = (int*)malloc(sizeof(int) * cnt);
	printf(p);

		for (i = 0; i < cnt; i++) //cnt만큼 반복
	{
		printf(" %d번째 숫자 :", i + 1);
		scanf("%d", p + i);
		// scanf("%d", &aa[i]);
	}

	//p = aa;

	for (i = 0; i < cnt; i++) //cnt만큼 반복
	{
		hap = hap + *(p + i);
	}

	printf("합계 ==> %d\n", hap);

	free(p); //동적할당한 메모리 해제

}*/

/*int* p, * s;
int i, j;

printf("malloc() 함수 사용\n");
p = (int*)malloc(sizeof(int) * 3);

for(i=0; i<3; i++)
	printf("할당된 곳의 초깃값 p[%d] ==>%d\n", i, p[i]);

free(p); //동적할당한 메모리 해제

printf("\ncalloc()함수 사용\n");
s = (int*)calloc(sizeof(int),3);

for (j = 0; j < 3; j++)
	printf("할당된 곳의 초깃값 s[%d] ==> %d\n", j, s[j]);

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
		printf("%d 번째 문자열 :", i + 1);

		gets(data[i]);
	}

	printf("\n입력과 반대로 출력\n");

	for (i = 2; i >= 0; i--)
	{
		printf("%d 번째 문자열 : %s\n", i + 1, data[i]);
	}
}*/

/* {
	char* p[3];
	char imsi[100];
	int i, size;

	for (i = 0; i < 3; i++)
	{
		printf("%d 번째 문자열 : ", i + 1);
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

	printf("a에 저장된 값 = %d\n", a);
	printf("b에 저장된 값 = %d\n", b);
	printf("c에 저장된 값 = %d\n", c);

	printf("b가 가리키는 값 = %d\n", *b);
	printf("c가 가리키는 값 = %d\n", *c);
	printf("c가 최종적으로 가리키는 값 = %d\n", **c);
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

	strcpy(name[0], "홍길동");

	kor[0] = 90;
	eng[0] = 80;
	avg[0] = (kor[0] + eng[0]) / 2.0f;

	strcpy(name[1], "이명박");

	kor[1] = 50;
	eng[1] = 30;
	avg[1] = (kor[1] + eng[1]) / 2.0f;

	for(i=0; i<2; i++)
	{
		printf("이름 ==> %s\n", name[i]);
		printf("국어 ==> %d\n", kor[i]);
		printf("영어 ==> %d\n", eng[i]);
		printf("평균 ==> %.2f\n", avg[i]);
	}*/


	/*scanf("%s", name, 9);//최대 9자 제한 하는 법

	printf("국어 : ");
	scanf("%d", &kor);

	printf("영어 : ");
	scanf("%d", &eng);
	avg = (kor + eng) / 2.0f;

	printf("\n");
	printf("이름 ==> %s\n", name);
	printf("국어 ==> %d\n", kor);
	printf("영어 ==> %d\n", eng);
	printf("평균 ==> %.2f\n", avg);
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

	printf("이름 입력 :");
	scanf("%s",p->name);

	printf("국어 점수 입력 :");
	scanf("%d", &p->kor);
	printf("영어 점수 입력 :");
	scanf("%d", &p->eng);

	p->avg = (p->kor + p->eng) / 2.0f;
	printf("학생이름 ==> %s\n", p->name);
	printf("국어 점수 ==> %d\n", p->kor);
	printf("영어 점수 ==> %d\n", p->eng);
	printf("평균 점수 ==> %.2f\n", p->avg);
	*/

	/*union student {
		int tot;
		char grade;
	};

	union student u;

	u.tot = 300;
	u.grade = 'A';

	printf("총점 ==> %d\n", u.tot);
	printf("학점 ==> %c\n", u.grade);
	}*/

	enum week { sun, mon, tue, wed, thu, fri, sat };
	enum week ww;

	ww = sat;

	if (ww == sun)
		printf("일요일입니다.\n");
	else
		printf("일요일이 아닙니다.\n");
}