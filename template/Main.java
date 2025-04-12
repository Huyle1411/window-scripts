import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    FastScanner fs = new FastScanner();
    PrintWriter out = new PrintWriter(System.out);
    int T = 1;
    T = fs.nextInt();
    for (int tt = 0; tt < T; tt++) {

    }
    out.close();
  }

  static final Random random = new Random();

  static void ruffleSort(int[] a) {
    int n = a.length;// shuffle, then sort
    for (int i = 0; i < n; i++) {
      int oi = random.nextInt(n), temp = a[oi];
      a[oi] = a[i];
      a[i] = temp;
    }
    Arrays.sort(a);
  }

  static void sort(int[] a) {
    ArrayList<Integer> l = new ArrayList<>();
    for (int i : a)
      l.add(i);
    Collections.sort(l);
    for (int i = 0; i < a.length; i++)
      a[i] = l.get(i);
  }

  static class FastScanner {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer("");

    String next() {
      while (!st.hasMoreTokens())
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException e) {
          e.printStackTrace();
        }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }

    int[] readArray(int n) {
      int[] a = new int[n];
      for (int i = 0; i < n; i++)
        a[i] = nextInt();
      return a;
    }

    long nextLong() {
      return Long.parseLong(next());
    }
  }
}
