package Hexaware.ArraysPractice;

import java.util.Arrays;
import java.util.Scanner;

public class Question4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        int ans = Integer.MIN_VALUE;
        for(int i = 0 ; i < n ; i++){
            for(int j = i+1; j < n ; j++){
                int temp = Math.abs(arr[i] - arr[j]);
                if(temp > ans && arr[i] < arr[j]){
                    ans = temp;
                }
            }
        }
        System.out.println(ans);
    }
}
