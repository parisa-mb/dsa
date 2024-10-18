public class Five {
    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5};

        int max = max(arr, 0);
        System.out.println(max);
    }

    public static int max(int[] arr, int index) {

        if (index == arr.length -1) {
            return arr[index];
        }

        int maxInRest = max(arr, index + 1);

        return Math.max(arr[index], maxInRest);
    }

    }
