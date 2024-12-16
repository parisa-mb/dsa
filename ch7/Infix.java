import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.util.function.Function;
public class Infix {
    public static void main(String args[])
    {
        Infix converter = new Infix();
        String infix = "3+(-4)+6";
        String postfix = converter.postfix(infix);
        System.out.println("Postfix: " + postfix);
        Function<Double, Double> expression = x -> x + Math.pow(x, x) - x;

        int width = 800;
        int height = 600;
        double xMin = -5;
        double xMax = 8;
        double yMin = -100;
        double yMax = 100;

        //GraphingCalculator graph = new GraphingCalculator(expression, width, height, xMin, xMax, yMin, yMax);
        //graph.setPreferredSize(new Dimension(width, height));

//        JFrame frame = new JFrame("Graphing Calculator");
//        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        frame.add(graph);
//        frame.pack();
//        frame.setLocationRelativeTo(null);
//        frame.setVisible(true);
    }


    public boolean isOperator(char c) {
        return (!(c >= 'a' && c <= 'z') &&
                !(c >= '0' && c <= '9') &&
                !(c >= 'A' && c <= 'Z'));
    }
    public boolean pre(char op1, char op2) {
        if (op1 == op2) {
            return false;
        }
//        if (op2 == null) {
//            return true;}

        if (op1 == '(' && "*/+^-".indexOf(op2) != -1) {
            return true;
        }
        if ("+-*/^".indexOf(op1) != -1 && op2 == '(') {
            return true;
        }

        if ("+-".indexOf(op1) != -1 && "*/^".indexOf(op2) != -1) {
            return false;
        }
        if ("*/".indexOf(op1) != -1 &&  op2 == '^') {
            return false;
        }
        if ("*/".indexOf(op1) != -1 && "+-".indexOf(op2) != -1) {
            return true;
        }
        if (op1 == '^' && "*/+-".indexOf(op2) != -1) {
            return true;
        }
//        if (op1 == '^' && op2 != null && op2 == '^') {
//            return false;
//        }

        return false;
    }
    public String postfix(String infix) {
        Stack<Character> operators = new Stack<>();
        StringBuilder postfix = new StringBuilder();

        for (int i = 0; i < infix.length(); i++) {
            char current = infix.charAt(i);

            if (Character.isDigit(current) || (current == '-' && (i == 0 || infix.charAt(i - 1) == '('))) {
                StringBuilder number = new StringBuilder();
                if (current == '-') {
                    number.append('-');
                    i++;
                }

                while (i < infix.length() && (Character.isDigit(infix.charAt(i)) || infix.charAt(i) == '.')) {
                    number.append(infix.charAt(i));
                    i++;
                }
                i--;
                postfix.append(number).append(" ");
            } else if (current == '(') {
                operators.push(current);
            } else if (current == ')') {
                while (!operators.isEmpty() && operators.peek() != '(') {
                    postfix.append(operators.pop()).append(" ");
                }
                if (!operators.isEmpty() && operators.peek() == '(') {
                    operators.pop();
                }
            } else if (isOperator(current)) {
                while (!operators.isEmpty() && !pre(current, operators.peek()) && operators.peek() != '(') {
                    postfix.append(operators.pop()).append(" ");
                }
                operators.push(current);
            }
        }

        while (!operators.isEmpty()) {
            postfix.append(operators.pop()).append(" ");
        }

        return postfix.toString().trim();
    }

    public String prefix(String infix)
    {
        Stack<Character> operators = new Stack<Character>();
        Stack<String> operands = new Stack<String>();


        for (int i = 0; i < infix.length(); i++){
            char current = infix.charAt(i);


            if (current == '(') {
                operators.push(current);
            } else if (Character.isDigit(current) || (current == '-' && (i == 0 || infix.charAt(i - 1) == '('))) {
                StringBuilder number = new StringBuilder();
                if (current == '-') {
                    number.append('-');
                    i++;
                }

                while (i < infix.length() && (Character.isDigit(infix.charAt(i)) || infix.charAt(i) == '.')) {
                    number.append(infix.charAt(i));
                    i++;
                }
                i--;
                operands.push(number.toString());}
            else if (!isOperator(infix.charAt(i)))
            {
                operands.push(infix.charAt(i) + "");
            }

            else if (infix.charAt(i) == ')')
            {
                while (!operators.empty() &&
                        operators.peek() != '(')
                {
                    String op1 = operands.peek();
                    operands.pop();

                    String op2 = operands.peek();
                    operands.pop();

                    char op = operators.peek();
                    operators.pop();

                    String tmp = op + op2 + op1;
                    operands.push(tmp);
                }
                operators.pop();
            }
            else {
                while (!operators.empty() && !pre(infix.charAt(i), operators.peek())) {

                    String op1 = operands.peek();
                    operands.pop();

                    String op2 = operands.peek();
                    operands.pop();

                    char op = operators.peek();
                    operators.pop();

                    String tmp = op + op2 + op1;
                    operands.push(tmp);
                }
                operators.push(infix.charAt(i));
            }
            System.out.println("Processing: " + infix.charAt(i));
            System.out.println("Operators: " + operators);
            System.out.println("Operands: " + operands);
        }
        while (!operators.empty()) {
            String op1 = operands.peek();
            operands.pop();

            String op2 = operands.peek();
            operands.pop();

            char op = operators.peek();
            operators.pop();

            String tmp = op + op2 + op1;
            operands.push(tmp);
        }
        return operands.peek();
    }

    public class GraphingCalculator extends JPanel {

        private final Function<Double, Double> function; // Function to graph
        private final int width;
        private final int height;
        private final double xMin;
        private final double xMax;
        private final double yMin;
        private final double yMax;

        public GraphingCalculator(Function<Double, Double> function, int width, int height,
                                  double xMin, double xMax, double yMin, double yMax) {
            this.function = function;
            this.width = width;
            this.height = height;
            this.xMin = xMin;
            this.xMax = xMax;
            this.yMin = yMin;
            this.yMax = yMax;
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g;
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            int xAxis = mapYToScreen(0);
            int yAxis = mapXToScreen(0);
            g2.setColor(Color.GRAY);
            g2.drawLine(0, xAxis, width, xAxis);
            g2.drawLine(yAxis, 0, yAxis, height);

            g2.setColor(Color.PINK);
            for (int i = 0; i < width; i++) {
                double x1 = mapScreenToX(i);
                double x2 = mapScreenToX(i + 1);
                double y1 = function.apply(x1);
                double y2 = function.apply(x2);

                if (y1 >= yMin && y1 <= yMax && y2 >= yMin && y2 <= yMax) {
                    int screenX1 = i;
                    int screenX2 = i + 1;
                    int screenY1 = mapYToScreen(y1);
                    int screenY2 = mapYToScreen(y2);
                    g2.drawLine(screenX1, screenY1, screenX2, screenY2);
                }
            }
        }

        private int mapXToScreen(double x) {
            return (int) ((x - xMin) / (xMax - xMin) * width);
        }

        private int mapYToScreen(double y) {
            return (int) (height - (y - yMin) / (yMax - yMin) * height);
        }

        private double mapScreenToX(int screenX) {
            return xMin + screenX * (xMax - xMin) / width;
        }

       }}



