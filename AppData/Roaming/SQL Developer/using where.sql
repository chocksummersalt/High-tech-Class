--SELECT empno, ename
--FROM emp
--WHERE empno=7900;

--SELECT ename, sal
--FROM emp
--WHERE sal < 1000; --숫자는 그냥 사용 가능

--SELECT empno, ename, sal
--FROM emp
--WHERE ename = 'SMITH' ; ''없이 쓰면 인식 못함 ""쌍따옴표는 안됨, 대소문자 구문

--SELECT ename, hiredate
--FROM emp
--WHERE ename = 'SMITH' ;

--SELECT ename, hiredate
--FROM emp
--WHERE hiredate = '80/12/17' ;

--SELECT ename, sal + 100 * 1.1 #연산자 사용가능
--FROM emp
--WHERE deptno = 10;

--SELECT empno, ename, sal
--FROM emp
--WHERE sal >= 4000; #비교 연산자 사용가능

--SELECT empno, ename, sal
--FROM emp
--WHERE ename >= 'W' ; #알파벳에서도 사용가능

--SELECT ename, hiredate
--FROM emp
--WHERE hiredate >= '81/12/25'; #날짜에서도 사용 가능

--between 은 문자, 날짜, 숫자 다 가능 왼쪽이 적은 숫자, 오른쪽이 큰 숫자.

--SELECT empno, ename, deptno
--FROM emp
--WHERE deptno IN (10, 20); in은 괄호안에 해당하는 데이터가 왔을때 추출해주는 것.

--like 는 'P%' 의 경우는 값이 'P'로 시작하지만 'P'다음에는 무슨 값이 오든 상관없이 검색하라

--'%2' 의 경우는 값이 '2'로 끝나면서 '2' 이전에는 무슨 값이 오든 상관없이 검색하라

--'%PP%' 의 경우는 값이 'PP'를 포함하며 'PP' 앞뒤로 무슨 값이 오든 상관없이 검색하라

--where 에 붙는 IS NULL 과 IS NOT NULL은 빈거, 채워진거 찾는 것.

SELECT empno, ename, sal, comm
FROM emp
WHERE sal > 1000
AND (comm < 1000 OR comm IS NULL);

