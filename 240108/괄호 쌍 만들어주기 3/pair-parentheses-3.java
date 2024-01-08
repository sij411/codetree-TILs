import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // )를 만나면 +1하고 탈출
        Scanner sc = new Scanner(System.in);
        String brackets = sc.nextLine();
        sc.close();
        
        int cnt = 0;
        for (int i = 0; i < brackets.length(); i++) {
            char target = brackets.charAt(i);
            for (int j = i + 1; j < brackets.length(); j++) {
                char comp = brackets.charAt(j);
                if (target == '(' && comp == ')') {
                    cnt += 1;
                }
            }
        }
        System.out.print(cnt);
    }
}