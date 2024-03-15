import java.util.Scanner;
class Human {
        public String name;
        public String streetNumber;
        public String region;

        public Human (String name, String streetNumber, String region) {
            this.name = name;
            this.streetNumber = streetNumber;
            this.region = region;
        }

        public void printInfo() {
            System.out.println("name " + this.name );
            System.out.println("addr " + this.streetNumber);
            System.out.println("city " + this.region );
        }
    }
    
public class Main {
    public static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int n = sc.nextInt();
        Human[] word = new Human[n];

        for (int i = 0; i < n; i++) {
            String name = sc.next();
            String streetNumber = sc.next();
            String region = sc.next();
            word[i] = new Human(name, streetNumber, region);
          

        }

        int min_val = 0;

        for(int i = 1; i<n; i++){
            if (word[i].name.compareTo(word[min_val].name)>0){
                min_val = i;
            }
        }

        word[min_val].printInfo();

    }
}