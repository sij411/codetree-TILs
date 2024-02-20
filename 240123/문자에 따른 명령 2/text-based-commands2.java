import java.util.Scanner;

public class Main {
    public static String dirs;
    public static int x = 0, y = 0;
    public static int currDir = 3;

    public static int[] dx = new int[]{1,  0, -1, 0};
    public static int[] dy = new int[]{0, -1,  0, 1};

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        dirs = sc.next();

        for(int i = 0; i < dirs.length(); i++) {
            char cDir = dirs.charAt(i);

            if(cDir == 'L')
                currDir = (currDir -1 + 4)% 4;
            else if(cDir == 'R')    
                currDir = (currDir + 1) % 4;
            else {
                x += dx[currDir];
                y += dy[currDir];
            }
        }

        System.out.print(x + " " + y);
    }
}