COL name FOR a20
COL LPAD (id,10,'*') FOR a20

SELECT ename, RPAD(ename, 9, SUBSTR('23456789', LENGTHB(ename))) as namenumber
from emp
where deptno=10 ;

//LTRIM, RTRIM (칼럼명, 제거할 문자)
SELECT ename,    REPLACE (ename, substr(ename,2,2),'--')"REPLACE"
from emp
where deptno=20;

SELECT name ,jumin, replace(jumin, substr(jumin,7,7),'-/-/-/-/') "replace"
from student
where deptno1 = 101;

SELECT name, tel, replace(tel, substr(tel,5,3),'***')
from student
where deptno1 = 102;

SELECT name, tel, replace(tel, substr(tel,9,4),'** **')
from student
where deptno1 = 101;

select trunc(months_between(sysdate,'14/08/31')) from dual;

//숫자처럼 생긴 문자만 변환 가능

select sysdate, to_char(sysdate, 'yyyy') "yyyy",
                to_char(sysdate, 'rrrr') "rrrr"
from dual;
//to_char 문자변환 연습
select studno, name, to_char(birthday, 'dd')||'-'||to_char(birthday,'mm')||'-'||to_char(birthday,'yy')
from student
where to_char(birthday, 'mm') = 01;

select empno, ename, hiredate
from emp
where to_char(hiredate,'mm') in(01,02,03);

// is null 연습
select empno, ename, hiredate, to_char((sal*12)+comm, '$999,999') "sal",
to_char(((sal*12)+comm)*1.15, '$999,999') "15%up"
from emp
where comm is not null;

//NVL 예제
select profno, name, pay, NVL(bonus,0)"BONUS", (pay*12+nvl(bonus,0)) "TOTAL"
from Professor
where deptno = 201;

select empno, ename, NVL(comm,0), nvl2(comm, 'Exist', 'Null') "NVL2"
from emp
where deptno = 30;


//decode 예제
SELECT  name,   jumin,  DECODE(SUBSTR(jumin, 7, 1), '1', 'man', 'woman') AS "GENDER"
FROM student
WHERE deptno1 = 101;

select name, tel, decode(substr(tel,1,instr(tel,')')-1), '02', 'seoul','031','gyeongy','051','busan','gyeongnam') "loc"
from student
where deptno1 = 101;

//case pract

select empno, ename, sal, 
case when sal between '1' and '1000' then 'Level 1'
    when sal between '1001' and '2000' then 'level 2'
    when sal between '2001' and '3000' then 'level 3'
    else 'level 4' 
end "LV"

from emp
