import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // i = n, j = n + 1, k = j + 1 ==> n + 2 
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int cnt = 0;

        ArrayList<Integer> arr = new ArrayList();
        for (int i = 0; i < n; i++) {
            arr.add(sc.nextInt());
        }

        for (int i = 0; i < n - 2; i++) {
            int a = arr.get(i);
            for (int j = i + 1; j < n - 1; j++) {
                int b = arr.get(j);
                for (int k = j + 1; k < n; k++) {
                    int c = arr.get(k);
                    if (a <= b && b <= c) {
                        cnt += 1;
                    }
                }
            }
        }
        System.out.print(cnt);
    } 
}