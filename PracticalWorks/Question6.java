package Hexaware.ArraysPractice;

import java.util.Arrays;
import java.util.Scanner;

public class Question6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        Arrays.sort(arr);
        int ans = arr[n-1] - arr[0];
        for(int i = 0 ; i < n-1 ; i++){
            int min = Math.min(arr[0] + k , arr[i+1] - k);
            int max = Math.max(arr[i] + k , arr[n-1] - k);
            ans = Math.min(ans,max-min);
        }
        System.out.println(ans);
    }
}
