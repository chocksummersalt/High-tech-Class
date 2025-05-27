package sec02.ex01;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/calc")
public class CarcServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();

        // Get parameters from the request
        String wonStr = request.getParameter("won");
        String operator = request.getParameter("operator");
        String command = request.getParameter("command"); // This parameter will be "calculate" when the form is submitted

        out.print("<html><body>");
        out.print("<h2>환율 계산기</h2>");

        // Check if a calculation request was made
        if (wonStr != null && !wonStr.isEmpty() && operator != null && command != null && command.equals("calculate")) {
            float won = 0;
            float result = 0;
            String resultStr = "";

            try {
                won = Float.parseFloat(wonStr);
                result = calculate(won, operator);
                resultStr = String.format("%.2f", result); // Format to 2 decimal places

                // Display the conversion result
                out.print("<p><b>변환 결과:</b></p>");
                out.print("<p>" + wonStr + "원은 ");
                
                // Add currency unit based on operator
                switch (operator) {
                    case "dollar":
                        out.print(resultStr + " 달러입니다.</p>");
                        break;
                    case "yen":
                        out.print(resultStr + " 엔입니다.</p>");
                        break;
                    case "yuan":
                        out.print(resultStr + " 위안입니다.</p>");
                        break;
                    case "pound":
                        out.print(resultStr + " 파운드입니다.</p>");
                        break;
                    case "euro":
                        out.print(resultStr + " 유로입니다.</p>");
                        break;
                    default:
                        out.print("잘못된 통화 단위입니다.</p>");
                        break;
                }
            } catch (NumberFormatException e) {
                out.print("<p style='color:red;'><b>오류:</b> 숫자를 정확히 입력하세요.</p>");
            }
        }

        // Always display the input form
        out.print("<form name='frmCalc' method='get' action='/pro06/calc'>"); // Ensure action points to your servlet URL
        out.print("금액(원): <input type='text' name='won' value='" + (wonStr != null ? wonStr : "") + "'><br>"); // Pre-fill won value if available
        out.print("<select name='operator'>");
        out.print("<option value='dollar'" + ("dollar".equals(operator) ? " selected" : "") + ">달러</option>");
        out.print("<option value='yen'" + ("yen".equals(operator) ? " selected" : "") + ">엔</option>");
        out.print("<option value='yuan'" + ("yuan".equals(operator) ? " selected" : "") + ">위안</option>");
        out.print("<option value='pound'" + ("pound".equals(operator) ? " selected" : "") + ">파운드</option>");
        out.print("<option value='euro'" + ("euro".equals(operator) ? " selected" : "") + ">유로</option>");
        out.print("</select>");
        out.print("<input type='hidden' name='command' value='calculate'>"); // Hidden field to trigger calculation
        out.print("<input type='submit' value='변환'>");
        out.print("</form>");

        out.print("</body></html>");
    }

    // This method remains the same as it handles the core calculation logic
    private float calculate(float won, String operator) {
        float result = 0;
        switch (operator) {
            case "dollar":
                result = won / 1320; // Example rate
                break;
            case "yen":
                result = won / 9.5f; // Example rate (often 100 JPY to KRW, so 1 JPY is less than 1 KRW)
                break;
            case "yuan":
                result = won / 180; // Example rate
                break;
            case "pound":
                result = won / 1600; // Example rate
                break;
            case "euro":
                result = won / 1400; // Example rate
                break;
            default:
                result = 0;
        }
        return result;
    }
}