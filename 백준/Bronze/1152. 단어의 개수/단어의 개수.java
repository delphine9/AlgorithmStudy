import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine().trim();

        if (str.isEmpty()) {
            System.out.println("0");
        } else {
            String[] result = str.split(" ");
            System.out.println(result.length);
        }
    }
}