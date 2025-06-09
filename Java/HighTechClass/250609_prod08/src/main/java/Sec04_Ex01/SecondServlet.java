package Sec04_Ex01;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/xvi")
public class SecondServlet extends HttpServlet{
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
	throws ServletException, IOException{
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		String address=(String)request.getAttribute("address");
		out.println("<html><body>");
		out.println("주소"+address);
		out.println("<br>");
		out.println("redirect 바인딩 실습");
		out.println("</body></html>");
}

}
