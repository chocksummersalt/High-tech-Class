package pack;
import java.util.*;
public class IteratorEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		Vector<Integer> v = new Vector<Integer>();
		v.add(5);
		v.add(4);
		v.add(-1);
		v.add(2, 100);
		
		Iterator<Integer> it = v.iterator();
		while(it.hasNext()) {
			int n  = it.next();
			System.out.println(n);
			
			
		}
		
		int sum = 0;
		it = v.iterator();
		while(it.hasNext()) {//hasNext의 기능이 뭐지? 다음 값이 있냐 없냐
			int n = it.next(); // .next()의 기능이 뭐지?입력을 공백 단위로 구분해서 한단어 읽기
			sum = sum + n;
		}
		
		System.out.println("백터에 있는 정수 합:" + sum);
	}

}
