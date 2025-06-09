package Sec04_Ex02;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/xvii")
public class FirstServlet extends HttpServlet {  // HttpServlet 상속 추가!
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=utf-8");
        request.setAttribute("address","서울시 성북구");
        RequestDispatcher dispatch = request.getRequestDispatcher("xviii");
        dispatch.forward(request,  response);
        
        
    }
}
