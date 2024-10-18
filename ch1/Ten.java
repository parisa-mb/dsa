public class Ten {
    public static void main(String[] args) {

        int n = 5;
        int result = finale(n);
        System.out.println(result);
    }

    public static int factoriel(int n) {
        if (n == 0 || n== 1) {
            return 1;
        }
        return 1/(n * factoriel(n - 1));
    }

    public static int finale(int n) {
        if (n == 1) {
            return 1;
        }
        return (1/factoriel(n)) + finale(n - 1);
    }
}

