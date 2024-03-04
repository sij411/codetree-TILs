import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < 2*n; i++) {
            arr.add(sc.nextInt());
        }

        arr.sort(Comparator.naturalOrder());
        
        int max = 0;
        for (int i = 0 ; i < n; i++) {
            if (max < arr.get(i) + arr.get((n*2-1)-i)){
                max = arr.get(i) + arr.get((n*2-1)-i);
            }
        }

        System.out.print(max);
    }
}