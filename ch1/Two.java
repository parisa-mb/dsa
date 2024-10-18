import java.util.Scanner;

public class Two {

    public static void main(String[] args) {

        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {6, 7, 8, 9};
        float result = average(arr1, 0);
        System.out.print(result/arr1.length);

    }
    public static float average(int[] arr, int index) {

        int leng = arr.length;
        if (index == leng) {
            return 0;
        }

        return (arr[index] + average(arr, index + 1));
    }


    }

