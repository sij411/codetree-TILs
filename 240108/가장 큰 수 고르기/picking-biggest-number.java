import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int INT_MIN = Integer.MIN_VALUE;

        ArrayList<Integer> arr = new ArrayList();
        Scanner sc = new Scanner(System.in);
        
        for(int i = 0; i < 10; i++) {
            int num = sc.nextInt();
            arr.add(num);
        }
        // System.out.print(arr);
        int maxVal = INT_MIN;
        for (int num : arr) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        System.out.print(maxVal);
        sc.close();
    }
}