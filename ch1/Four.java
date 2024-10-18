import java.util.Scanner;
public class Four {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.print(baseTwo(num));


    }

    public static String baseTwo(int n){

        if (n == 0) {
            return "0";
        }
        if (n == 1) {
            return "1";
        }

        return baseTwo(n / 2) + (n % 2);
    }
}
