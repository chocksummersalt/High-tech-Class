package sec02.ex01;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/first/test")
public class TestServlet1 extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // request.setCharacterEncoding("utf-8"); // GET 요청 시 이 부분은 의미 없음
        
        response.setContentType("text/html;charset=utf-8"); // 세미콜론으로 수정
        
        PrintWriter out = response.getWriter();
        
        String context = request.getContextPath();
        String url = request.getRequestURL().toString();
        String mapping = request.getServletPath();
        String uri = request.getRequestURI();
        
        out.println("<html>");
        out.println("<head>");
        out.println("<title>test servlet</title>");
        out.println("</head>");
        out.println("<body bgcolor='green'>");
        out.println("<b>test servlet입니다.</b><br>");
        response.getWriter().println("Servlet Path: " + mapping);
        response.getWriter().println("Servlet context: " + context);
        
        out.println("</body>");
        out.println("</html>");
    }
}
