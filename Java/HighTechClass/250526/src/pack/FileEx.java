package pack;
import java.io.*;
import java.io.FileWriter;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FileEx {
    public static void main(String[] args) {
 /*       File f1 = new File("c:\\windows\\system.ini");

        System.out.println(f1.getPath() + ", " + f1.getParent() + ", " + f1.getName());

        String res = "";
        if (f1.isFile()) res = "파일";
        else if (f1.isDirectory()) res = "디렉토리";

        System.out.println(f1.getPath() + "은 " + res + "입니다.");

        // 디렉토리 생성 예시
        File f2 = new File("c:\\Temp\\java_sample");
        if (!f2.exists()) {
            f2.mkdirs();
        }

        // 디렉토리 내 파일 목록 출력
        File dir = new File("c:\\windows");
        System.out.println("------ " + dir.getPath() + "의 서브리스트입니다. ------");

        File[] subFiles = dir.listFiles();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm");

        for (int i = 0; i < subFiles.length; i++) {
            File f = subFiles[i];
            String date = sdf.format(new Date(f.lastModified()));
            System.out.print(date + "\t");

            if (f.isDirectory()) {
                System.out.print("<DIR>\t\t" + f.getName());
            } else {
                System.out.print("\t" + f.length() + "\t" + f.getName());
            }
            System.out.println();*/
    	
    /*	File src - new File("c:\\windows\\system.ini");
    	File dest = new File("c:\\Temp\\stsrem.txt");
    	int c;
    	try {
    		FileReader fr = new FileReader(src);
    		FileWriter fw = new FileWriter(dest);
    		while((c = fr.read()) !=-1) {
    			fw.write((char)c));
    		}
    		fr.close((); fw.close();
    		System.out.)*/
    	

    	        File src = new File("C:\\Windows\\Web\\4K\\Wallpaper\\Windows\\img0_1920x1200.jpg");
    	        File dest = new File("C:\\Temp\\copyimg.jpg");

    	        try {
    	            FileInputStream fi = new FileInputStream(src);
    	            FileOutputStream fo = new FileOutputStream(dest);
    	            byte[] buf = new byte[1024 * 10]; // 10KB 버퍼

    	            while (true) {
    	                int n = fi.read(buf);
    	                if (n == -1) break; // EOF
    	                fo.write(buf, 0, n);
    	            }

    	            fi.close();
    	            fo.close();

    	            System.out.println(src.getPath() + " 를 " + dest.getPath() + "로 복사하였습니다.");

    	        } catch (IOException e) {
    	            System.out.println("파일 복사 중 오류 발생: " + e.getMessage());
    	        }
    	    }
    	

    }

