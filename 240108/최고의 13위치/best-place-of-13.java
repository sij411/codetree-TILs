import java.util.Scanner;

public class Main {
    public static int MAX_N = 20;
    public static final int[][] grid = new int[MAX_N][MAX_N];
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
       int n = sc.nextInt();

       for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
       }

        int maxCnt = 0;
        for (int i = 0; i < n; i++) {
            
            for (int j = 0; j < n - 2; j++) {
                    maxCnt = Math.max(maxCnt, grid[i][j] + grid[i][j+1] + grid[i][j+2]);
            }
       }
       System.out.print(maxCnt);
    }
}