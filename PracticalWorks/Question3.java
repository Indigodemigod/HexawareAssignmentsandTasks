package Hexaware.ArraysPractice;

import java.util.Arrays;
import java.util.Scanner;
public class Question3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        int maxSum = 0;
        int start = 0;
        int end = n-1;
        for(int i = 0 ; i < n ; i++){
            int idx = i;
            int cs = 0;
            do{
                if(cs+arr[idx] < arr[idx]){
                    cs = arr[idx];
                    end = idx;
                }
                else{
                    cs += arr[idx];
                }
                if(maxSum < cs){
                    maxSum = cs;
                    start = i;
                }
                idx = (idx+1) % n;
            }while(idx!=i);
        }
        // System.out.println(start);
        // System.out.println(end);
        int idx = end;
        int[] ans = new int[(n-idx)+start];
        int sum = 0;
        for(int i = 0 ; i < ans.length; i++){
            ans[i] = arr[idx%n];
            sum += arr[idx%n];
            idx++;
        }
        System.out.println(Arrays.toString(ans));
        System.out.println(sum);
    }
}