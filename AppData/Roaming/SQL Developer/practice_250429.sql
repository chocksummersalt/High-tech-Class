//대문자이거나 소문자로 시작하는 행
select *
from t_reg
where regexp_like(text, '[a-zA-Z]');

//소문자나 숫자로 시작하는 행
select *
from t_reg
where regexp_like(text, '[a-z] [0-9]');
// 공백이 있는 행
select *
from t_reg
where regexp_like(text, '[[:space:]]');
//숫자와 소문자가 연속적으로 3개가 붙어있는 행
select *
from t_reg
where regexp_like(text, '[0-9][a-z]{3}');
// 대문자가 있는 행
select *
from t_reg
where regexp_like(text, '[[:upper:]]');


//대문자 M으로 시작하고 이어서 o나 a로 시작하는 행
select name, id
from student
where regexp_like(id, '^M(a|o)');
//숫자로 시작하거나 소문자로 시작하는 행
select *
from t_reg
where regexp_like(text, '^[0-9]|^[a-z]');
//숫자나 소문자로 시작하는 행을 제거
select *
from t_reg
where regexp_like(text, '^[^0-9a-z]');

select *
from t_reg
where not regexp_like(text, '[a-z]');
//10으로 시작하는 아이피 추출
select *
from t_reg2 
where regexp_like(ip, '^[10]{2}');




//regexp_replace

//join grammar
select e.empno, e.ename, d.dname // emp, dept호출
from emp e, dept d // emp를 e 라고 부르겠다. dept를 d라고 부르겠다
where e.deptno = d.deptno;//e와 d의 deptno가 같은 것들 호출

select s.name "STU_NAME", d.dname  "DEPT_NAME"
from student s , department d
where s.deptno1 = d.deptno
order by d.dname desc;

select s.name "stu_name" , s.deptno "stud_no",  p.name "prof_name", p.profno "prof_no"
from student s , professor p
where s.profno = p.profno;

select s.name "STNAME", p.name "prof_name"
from student s , professor p
where s.profno = p.profno
and s.deptno1=101;

select c.gname "cust_name", to_char(c.point,'9,999,999') as "point", g.gname "gift name"
from customer c, gift g;

select s.name "stu_name", o.total " score", h.grade"credit"
from student s, score o, hakjum h
where s.studno = o.studno;
and o.total >=h.min_point
and o.total <=h.max_point;
//1번 예제
select s.name "stu_name", s.deptno1 "deptno1", d.dname "dept_name"
from student s, department d
where s.deptno1 = d.deptno;
//2번 예제
select e.name , e.position, e.pay, p.s_pay, p.e_pay
from emp2 e, p_grade p
where e.position = p.position;
//3번 예제


from emp2


select trunc((sysdate-birthday))
from emp2;


SELECT 
    E.NAME,
    TRUNC(MONTHS_BETWEEN(SYSDATE, TO_DATE(E.BIRTHDAY, 'RR/MM/DD')) / 12) AS AGE,
    E.POSITION AS CURR_POSITION,
    (SELECT P.POSITION
     FROM P_GRADE P
     WHERE TRUNC(MONTHS_BETWEEN(SYSDATE, TO_DATE(E.BIRTHDAY, 'RR/MM/DD')) / 12)
           BETWEEN P.S_AGE AND P.E_AGE
    ) AS BE_POSITION
FROM 
    EMP2 E
ORDER BY AGE;

//예제 4
select c.gname "cust_name", to_char(c.point,'9,999,999') "pont", g.gname "gift_name"
from customer c, gift g
where g.g_start <= c.point and g.gname = 'Notebook';

//예제 5
select * from professor;
select p1.profno, p1.name, p1.hiredate
from professor p1, professor p2
where p2.hiredate < p1.hiredate
group by p1.profno, p1.name, p1.hiredate;

//예제 6
// 1번 행부터 시작해서 대응하는 것 끼리 조인하게 되는데 입사일을 기준으로 오름차순 하기때문에
// smith가 제일 빠르니까 스미스를 기준으로 그 다음 입사일 쭉 내려가는. 사람 수를 세는 거니까
// 사람수를 카운트 해서 숫자를 세주는거야. 이해완료.
SELECT e1.empno, e1.ename, e1.hiredate, COUNT(e2.hiredate) "COUNT"
FROM emp e1, emp e2
WHERE e2.hiredate(+) < e1.hiredate
GROUP BY e1.empno, e1.ename, e1.hiredate
ORDER BY 4;




//ddl ctas create table as select 
//delete 는 도메인만 날라감 truncate는 자료 틀도 날라감 drop은 전부 날라감

create table new_table
(no Number(3), name varchar(10), birth date );

select * from temp01;
commit;

select temporary, duration
from user_tables
where table_name='temp01';

create table dept3
as
select * from dept2;

create table dept5
as select *from dept2
where 1 = 2 ;

alter table dept5
add(location varchar2(10));

select* from dept5;

create table new_emp
(no NUMBER(5), name varchar2(20), hiredate date); 

create table NEW_emp2
as
select * from new_emp;

create table NEW_emp3
as
select * from new_emp
where 1=2;

ALTER TABLE new_emp
ADD BIRTHDAY3 DATE DEFAULT SYSDATE;
select * from new_emp;

alter table new_emp2
modify(no number(7));
select * from new_emp2;

insert into new_emp2 values(1, 'hong', sysdate, sysdate);
select * from new_emp2;

drop new_emp2;

//update set 쓸때는 where 조건을 꼭 써줘야함. 안그러면 전부다 200이 되어버림.
update professor
set pay = pay * 1.15
where position = (select position from professor where name = 'sharon stone')
and pay <250;

//dml 연습
insert into dept2[("부서번호", "부서명")]
values (9000, "temp_1");

select *
from dept2;

INSERT INTO Dept2 (Dcode, DNAME, PDEPT, AREA)
    VALUES (9000, 'temp_1', 1006, 'nowhere');

alter session set nls_date_format='rrrr-mm-dd:hh24:mi:ss';
insert into professor (profno, name, id, position, pay, hiredate)
values(5001,'james bond', 'loveme','a full professor',500, '2014-10-23');

insert all
when profno between 1000 and 1999 then
into prof_3 values(profno,name)
select profno, name
from professor;

select * from prof_3;
CREATE TABLE prof_3 (
  profno NUMBER,
  name VARCHAR2(100)
);

INSERT ALL
  WHEN profno BETWEEN 1000 AND 1999 THEN
    INTO prof_3 (profno, name)
SELECT profno, name
FROM professor;

update professor
set bonus = 200
where position = 'assistant professor';

update professor
set pay = pay * 1.15
where position = (select position from professor where name='Sharon Stone')
and pay <250;


select * from professor;

 delete from dept2
 where dcode >= 9000 and dcode <= 9999;
 
 insert into dept2(dcode,dname)
 values(9020,'temp_20');
 select *
 from dept2;
 
 select * from professor;
 insert into professor4

    select profno, name, pay
    from professor
    where profno <= 3000;
 
 
 