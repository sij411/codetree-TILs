import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int INT_MAX = Integer.MAX_VALUE;

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // the num of houses
        // input
        ArrayList<Integer> arr = new ArrayList();
        for (int i = 0; i < n; i++) {
            arr.add(sc.nextInt());
        }

        int minDist = INT_MAX;
        for (int i = 0; i < n; i++) {
            int totalDist = 0;
            for (int j = 0; j < n; j++) {
                totalDist = totalDist + ( Math.abs(i - j) * arr.get(j) );
            }
            if (totalDist < minDist) {
                minDist = totalDist;
            }
        }

        System.out.print(minDist);
    }
}