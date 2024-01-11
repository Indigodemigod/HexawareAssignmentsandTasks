package Hexaware.ArraysPractice;

import java.util.Arrays;
import java.util.Scanner;
//534268
public class Question2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        int[] ans = new int[n];
        for(int i = 0 ; i < n ; i++){
            int product = 1;
            for(int j = 0 ; j < n ; j++){
                if(i==j){
                    continue;
                }
                product *= arr[j];
            }
            ans[i] = product;
        }
        System.out.println(Arrays.toString(ans));
    }
}
