package pack;
import java.io.*;
import java.util.*;

public class FileWriterEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
/*		Scanner scanner = new Scanner(System.in);
				FileWriter fout = null;
		int c;
		
		try{
			fout = new FileWriter("c:\\temp\\test.txt");
			while(true) {
				String line = scanner.nextLine();
				if(line.length()== 0)
					break;
				fout.write(line, 0, line.length());
				fout.write("\r\n",0,2);
			}
			fout.close();
		}catch(IOException e) {
			System.out.println("입출력 오류");
		}*/
		
	/*	byte b [] = {7,51,3,4,-1,24};
		try {
			FileOutputStream fout = new FileOutputStream("c:\\Temp\\test.out");
			for(int i = 0; i<b.length; i++)
				fout.write(b[i]);
			fout.close();
			
		}catch(IOException e) {
			System.out.println("저장할 수 없음. 경로명 확인요망");
			return;
			
			
		}
		System.out.println("c:\\Temp\\test.out을 저장하였습니다."); */
		
		byte b[]  = new byte[6];
		try {
			FileInputStream fin = new FileInputStream("c:\\Temp\\test.out");
			int n = 0, c;
			while((c = fin.read())!=-1) {
				b[n]=(byte)c;
				n++;
			}
			System.out.println("파일에서 읽은 배열을 출력합니다.");
			for(int i = 0; i<b.length;i++)System.out.print(b[i] + " ");
			System.out.println();
			fin.close();
			
			}catch(IOException e) {
				System.out.println("경로명 확인 요망");
		}
	}

}
