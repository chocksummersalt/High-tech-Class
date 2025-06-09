package Sec04_Ex03;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Date;
import java.util.List;

import javax.servlet.RequestDispatcher;
// 필수 임포트 추가
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/mem") // 어노테이션 수정
public class MemberServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException, ServletException {
    	doHandle(request,response);
    		}
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException{
    	doHandle(request,response);
    }
    private void doHandle(HttpServletRequest request,HttpServletResponse response)
    throws ServletException, IOException{
    	request.setCharacterEncoding("utf-8");
    
    	response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();
        MemberDAO dao = new MemberDAO();

        // MemberVO 타입으로 리스트를 받는다고 가정
        List<MemberVO> memberList = dao.listMembers();

        request.setAttribute("membersList",  memberList);
      
        RequestDispatcher dispatch = request.getRequestDispatcher("viewMembers");
        dispatch.forward(request, response);
    }
} 
