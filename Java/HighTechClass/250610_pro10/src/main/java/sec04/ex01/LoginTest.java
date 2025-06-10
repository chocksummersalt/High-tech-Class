package sec04.ex01;

import javax.servlet.http.HttpServletRequest;

@WevServlet("/login")

public class LoginTest extends HttpServlet {
	protected void doPost(HttpServletRequest request, HttpSercletResponse response)

	throws ServletException, IOException{
		request.setCharacterEncoding("utf-8"));
		PrintWriter out = response.getWriter();
		
	}
}
