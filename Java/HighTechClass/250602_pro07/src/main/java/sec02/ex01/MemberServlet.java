package sec02.ex01;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Date;
import java.util.List;

// 필수 임포트 추가
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/member2") 
public class MemberServlet extends HttpServlet { 
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException { 
        response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();
        MemberDAO dao = new MemberDAO(); // 

      
        List list = dao.listMembers();

        out.print("<html><body>");

        out.print("<table border='1'><tr align='center' bgcolor='lightgreen'>");
        out.print("<td>아이디</td><td>비밀번호</td><td>이름</td><td>이메일</td><td>가입일</td></tr>");

        // 수정된 for 루프
        for (int i = 0; i < list.size(); i++) {
            MemberVO memberVO = (MemberVO) list.get(i); 
            String id = memberVO.getId();
            String pwd = memberVO.getPwd();
            String name = memberVO.getName();
            String email = memberVO.getEmail();
            Date joinDate = memberVO.getJoinDate();
            out.print("<tr><td>" + id + "</td><td>" + pwd + "</td><td>" + name + "</td><td>" + email + "</td><td>" + joinDate + "</td></tr>");
        } // for 루프 끝

        out.print("</table></body></html>");
    } // 
} 