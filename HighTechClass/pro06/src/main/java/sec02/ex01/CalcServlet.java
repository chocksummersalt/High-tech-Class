package sec02.ex01;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/calc")
public class CarcServlet extends HttpServlet 
{
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
	throws ServletException, IOException
	{
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		String id = request.getParameter("won");
		String pw = request.getParameter("operator");
		
if (command != null && command.equals("calculate"))
{
	String result = calculate(Float.parseFloat(won),operator);
	pw.print("<html><font size=10>변환결과</font><br>");
	pw.print("<html><font size=10>"+result+"</font><br>");
	pw.print("<a href='/pro06/calc'> 환율 계산기</a>");
	return;
}	
pw.print("<html><title>환율 계산기</title>");
pw.print("<html><font size=5>환율 계산기</font><br>");
pw.print("<a href='/pro06/calc'> 환율 계산기</a>");
pw.print("<html><name='frmCalc' method = 'get' action = '/pro06/calc' />");
pw.print("<html><font size=10>"+result+"</font><br>");
pw.print("<a href='/pro06/calc'> 환율 계산기</a>");
pw.print("<html><font size=10>변환결과</font><br>");
pw.print("<html><font size=10>"+result+"</font><br>");
pw.print("<a href='/pro06/calc'> 환율 계산기</a>");
pw.print("<html><font size=10>변환결과</font><br>");
pw.print("<html><font size=10>"+result+"</font><br>");
pw.print("<a href='/pro06/calc'> 환율 계산기</a>");


	}
}

}