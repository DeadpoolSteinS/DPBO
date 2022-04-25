import java.util.*;

public class MyParser {
    public static Boolean isDataOutputStream(MyDataStream m) {
        return (m == dataOutputStream);
    }

    public static MyDataInputStream convertDataOutputStreamToDataInputStream(MyDataOutputStream m) {
        return new MyDataInputStream(m.getDataStream());
    }

    public static MyDataOutputStream convertDataInputStreamToDataOutputStream(MyDataInputStream m) {
        return new MyDataOutputStream(m.getDataStream());
    }

    public static Boolean isOperator(Character c) {
        return (c == '+' || c == '-' || c == '*' || c == '/' || c == '%');
    }

    public static Boolean isDigit(Character c) {
        return (c >= '0' && c <= '9');
    }

    public static List<MyDataOutputStream> getDigitOutputStream(MyDataInputStream in) {
        String from = in.getDataStream();
        String to = "";
        List<MyDataOutputStream> data = new ArrayList<>();

        for (Integer i = 0; i < from.length(); i++) {
            if (isDigit(from.charAt(i))) {
                to += from.charAt(i);
            } else {
                if (to.length() > 0)
                    data.add(new MyDataOutputStream(to));
                to = "";
            }
        }
        return data;
    }

    public static List<MyDataOutputStream> getOperatorOutputStream(MyDataInputStream in) {
        String from = in.getDataStream();
        String to = "";
        List<MyDataOutputStream> data = new ArrayList<>();

        for (Integer i = 0; i < from.length(); i++) {
            if (isOperator(from.charAt(i))) {
                to += from.charAt(i);
            } else {
                if (to.length() > 0)
                    data.add(new MyDataOutputStream(to));
                to = "";
            }
        }
        return data;
    }

    public static Integer parseStringToInteger(String s) {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            throw e;
        }
    }

    public static Boolean isInputStreamValid(MyDataInputStream in) {
        Boolean boleh = false;
        String from = in.getDataStream();

        for (Integer i = 0; i < from.length(); i++) {
            if (isOperator(from.charAt(i))) {
                if (!boleh || i == from.length() - 1)
                    return false;
                else
                    boleh = false;
            } else if (isDigit(from.charAt(i)))
                boleh = true;
        }
        return true;
    }

    public static Integer calculate(MyDataInputStream in) {
        try {
            isInputStreamValid(in)
            List<MyDataOutputStream> digit = getDigitOutputStream(in);
            List<MyDataOutputStream> operator = getOperatorOutputStream(in);
            Integer result = parseStringToInteger(digit.get(0).getDataStream());

            for (Integer i = 0; i < operator.size(); i++) {
                switch (operator.get(i).getDataStream()) {
                    case "+":
                        result += parseStringToInteger(digit.get(i + 1).getDataStream());
                        break;
                    case "-":
                        result -= parseStringToInteger(digit.get(i + 1).getDataStream());
                        break;
                    case "*":
                        result *= parseStringToInteger(digit.get(i + 1).getDataStream());
                        break;
                    case "/":
                        result /= parseStringToInteger(digit.get(i + 1).getDataStream());
                        break;
                    case "%":
                        result %= parseStringToInteger(digit.get(i + 1).getDataStream());
                        break;
                    default:
                        break;
                }
            }
            return result;
        } catch (Exception e) {
            throw new MissingOperandException();
        }
    }
}
