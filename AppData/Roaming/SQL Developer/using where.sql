--SELECT empno, ename
--FROM emp
--WHERE empno=7900;

--SELECT ename, sal
--FROM emp
--WHERE sal < 1000; --���ڴ� �׳� ��� ����

--SELECT empno, ename, sal
--FROM emp
--WHERE ename = 'SMITH' ; ''���� ���� �ν� ���� ""�ֵ���ǥ�� �ȵ�, ��ҹ��� ����

--SELECT ename, hiredate
--FROM emp
--WHERE ename = 'SMITH' ;

--SELECT ename, hiredate
--FROM emp
--WHERE hiredate = '80/12/17' ;

--SELECT ename, sal + 100 * 1.1 #������ ��밡��
--FROM emp
--WHERE deptno = 10;

--SELECT empno, ename, sal
--FROM emp
--WHERE sal >= 4000; #�� ������ ��밡��

--SELECT empno, ename, sal
--FROM emp
--WHERE ename >= 'W' ; #���ĺ������� ��밡��

--SELECT ename, hiredate
--FROM emp
--WHERE hiredate >= '81/12/25'; #��¥������ ��� ����

--between �� ����, ��¥, ���� �� ���� ������ ���� ����, �������� ū ����.

--SELECT empno, ename, deptno
--FROM emp
--WHERE deptno IN (10, 20); in�� ��ȣ�ȿ� �ش��ϴ� �����Ͱ� ������ �������ִ� ��.

--like �� 'P%' �� ���� ���� 'P'�� ���������� 'P'�������� ���� ���� ���� ������� �˻��϶�

--'%2' �� ���� ���� '2'�� �����鼭 '2' �������� ���� ���� ���� ������� �˻��϶�

--'%PP%' �� ���� ���� 'PP'�� �����ϸ� 'PP' �յڷ� ���� ���� ���� ������� �˻��϶�

--where �� �ٴ� IS NULL �� IS NOT NULL�� ���, ä������ ã�� ��.

SELECT empno, ename, sal, comm
FROM emp
WHERE sal > 1000
AND (comm < 1000 OR comm IS NULL);

