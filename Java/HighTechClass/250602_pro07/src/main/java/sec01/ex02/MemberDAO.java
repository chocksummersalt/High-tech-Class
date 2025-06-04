package sec01.ex02;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class MemberDAO {
    private Connection con;
    private PreparedStatement Pstmt;
    
    
    private static final String driver = "oracle.jdbc.driver.OracleDriver";
    private static final String url = "jdbc:oracle:thin:@localhost:1521:testdb";
    private static final String user = "scott";
    private static final String pwd = "tiger";
    
    public List listMembers() {
        List list = new ArrayList();
        
        try {
            connDB();
            String query = "select * from t_member";
            System.out.println(query);
            ResultSet rs = Pstmt.executeQuery(query);
            
            while(rs.next()) {
            	System.out.println("--------");
                String id = rs.getString("id");
                String pwd = rs.getString("pwd");
                String name = rs.getString("name");
                String email = rs.getString("email");
                Date joinDate = rs.getDate("joinDate");
                
                MemberVO vo = new MemberVO();
                vo.setId(id);
                vo.setPwd(pwd);
                vo.setName(name);
                vo.setEmail(email);
                vo.setJoinDate(joinDate);
                list.add(vo);
            }
            rs.close();
            Pstmt.close();
            con.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
        return list;
    }
    
    private void connDB() {
        try {
            Class.forName(driver);
            System.out.println("oracle driver loaded");
            con = DriverManager.getConnection(url, user, pwd);
            System.out.println("connection established");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}