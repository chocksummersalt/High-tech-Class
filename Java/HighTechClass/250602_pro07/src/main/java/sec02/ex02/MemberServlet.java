// Add necessary imports:
// import java.util.List;
// Assuming this path
package sec02.ex02;


import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/member3")
public class MemberServlet extends HttpServlet { // Added {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        doHandle(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        doHandle(request, response);
    }

    private void doHandle(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();
        MemberDAO dao = new MemberDAO();
        String command = request.getParameter("command");

        // Handle commands like adding a member
        if (command != null && command.equals("addMember")) {
            // ... your addMember logic ...
            // dao.addMember(vo);
        } else if (command != null && command.equals("delMember")) {
            // ... your delMember logic ...
        }

        // Always list members (or based on other logic)
        List<MemberVO> membersList = dao.listMembers(); // Fetch the list here

        out.print("<html><body>");
        out.print("<table border='1'><tr align='center' bgcolor='lightgreen'>");
        out.print("<td>아이디</td><td>비밀번호</td><td>이름</td><td>이메일</td><td>가입일</td><td>삭제</td></tr>");

        if (membersList != null) {
            for (MemberVO memberVO : membersList) { // Use enhanced for-loop
                // ... get details from memberVO ...
                out.print("<tr><td>" + memberVO.getId() + "</td><td>" + memberVO.getPwd() +
                          "</td><td>" + memberVO.getName() + "</td><td>" + memberVO.getEmail() +
                          "</td><td>" + memberVO.getJoinDate() + "</td>" +
                          "<td><a href='/pro07/member3?command=delMember&id=" + memberVO.getId() + "'>삭제</a></td></tr>"); // Corrected delete link
            }
        }
        out.print("</table>");
        out.print("<br><a href='/pro07/memberForm.html'>새 회원 등록하기</a>");
        out.print("</body></html>");
        out.close(); // Good practice
    }
} // Added } for the class

