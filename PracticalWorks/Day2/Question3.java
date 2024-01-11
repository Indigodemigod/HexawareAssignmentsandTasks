package Hexaware.Day2;

import java.util.Scanner;

import static javax.swing.text.html.HTML.Attribute.N;

public class Question3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n > 7) {
            int rem = n - (n / 10) * 10;
            n = n / 10 - 2 * rem;
        }

        System.out.println(Math.abs(n) == 0 || Math.abs(n) == 7);
    }
}
