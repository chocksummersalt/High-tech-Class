package Sec04_Ex03;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class MemberDAO {
    private Connection con;
    private Statement stmt;
    
    private static final String driver = "oracle.jdbc.driver.OracleDriver";
    private static final String url = "jdbc:oracle:thin:@localhost:1521:testdb";
    private static final String user = "scott";
    private static final String pwd = "tiger";
    
    public List<MemberVO> listMembers() {
        List<MemberVO> list = new ArrayList<MemberVO>();
        
        try {
            connDB();
            String query = "select * from t_member";
            System.out.println(query);
            ResultSet rs = stmt.executeQuery(query);
            
            while(rs.next()) {
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
            stmt.close();
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
            stmt = con.createStatement();
            System.out.println("statement created");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}