
public class Thirteen {
        public static void main(String args[]){

            int N = 2;
            hanoi(N, 'S', 'A', 'D');}

    public static void hanoi(int n, char S,
                             char A, char D)
    {
        if (n == 0) {
            return;
        }
        hanoi(n - 1, S, D, A);
        System.out.println("Move disk " + n + " from rod "
                + S + " to rod "
                + D);
        hanoi(n - 1, A, S, D);
    }

}
