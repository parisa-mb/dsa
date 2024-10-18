public class Seven {

    public static void main(String[] args) {
        int result = bmm(5, 3);
        System.out.println(result);
    }

    public static int bmm(int a, int b) {
        if (a%b==0) {
            return b;
        }
        return bmm(b, a%b);
    }
}

