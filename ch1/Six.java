public class Six {

    public static void main(String[] args) {
        int result = multiply(5, 3);
        System.out.println(result);
    }

    public static int multiply(int a, int b) {
        if (b == 0) {
            return 0;
        }
        return a + multiply(a, b - 1);
    }
}
