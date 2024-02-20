import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;

public class Main {
    
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int a, b;
        String n;

        a = sc.nextInt(); 
        b = sc.nextInt();
        n = sc.next();

        int num = convertAToDecimal(a, n);
        // System.out.println(num);
        String bNumber = convertToB(b, num);
        System.out.println(bNumber);

    }

    static int convertAToDecimal (int a, String n) {
        int decimal_n = 0;
        for (int i = 0 ; i < n.length(); i++) {
            int num = n.charAt(n.length() - i - 1) - '0'; // 아스키 코드 0은 49

            decimal_n += Math.pow(a, i) * num;
            
        }
        return decimal_n;
    }

    static String convertToB (int b, int decimal) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> bNumber = new ArrayList<>();

        while (decimal != 0) {
            stack.push(decimal % b);
            decimal /= b;
        }

        while (!stack.isEmpty()) {
            bNumber.add(Integer.toString(stack.pop()));
        }

        return String.join("", bNumber);

    }
}