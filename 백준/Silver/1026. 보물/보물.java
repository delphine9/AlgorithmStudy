import java.util.*;

public class  Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        ArrayList<Integer> B = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            B.add(sc.nextInt());
        }

        Arrays.sort(A);

        int result = 0;
        for (int i = 0; i < N; i++) {
            int maxB = Collections.max(B);
            B.remove(Integer.valueOf(maxB));
            result += A[i] * maxB;
        }

        System.out.println(result);
    }
}