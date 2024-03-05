import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        // currentLength = currentIndex + 1
        // mid = currentIndex / 2
        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            arr.add(sc.nextInt());
            
            if ((i + 1) % 2 == 1) {
                Collections.sort(arr);
                int num = arr.get(i / 2);
                System.out.print( num + " ");
          
                
            }
        }
    }
}