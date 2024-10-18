import java.util.Scanner;

public class One {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        if ( b == 0){
            System.out.print("division by zero");
        }
        else{
            int c = quotient(a, b);
            System.out.println(c);
        }



    }


    public static int quotient(int a, int b) {
        if (a< b) {
            return 0;
        }
        return 1 + quotient(a - b, b);
    }
}


