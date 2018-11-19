import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class PlusMinus {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        int positives = 0;
        int negatives = 0;
        int zeros = 0;
        for(int i : arr){
            if(i > 0){
                positives++;
            } else if(i < 0){
                negatives++;
            } else{
                zeros++;
            }
        }
        int total = positives + negatives + zeros;
        Double[] result = new Double[]{(double) positives / total, (double) negatives/total, (double) zeros/total};
        Arrays.stream(result).forEach(d -> System.out.printf("%.6f\n", d));
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
