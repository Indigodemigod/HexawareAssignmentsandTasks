package Hexaware.ArraysPractice;

import java.util.Arrays;
import java.util.Scanner;

public class Question5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        int ans = 0;
        if(arr.length == 1){
            System.out.println(arr[0]);
            return;
        }
        for(int i = 0 ; i < n ; i++){
            int flag = 0;
            for(int j = i+1 ; j < n ; j++){
                if(arr[i] == arr[j]){
                    flag = 1;
                }
            }
            int idx = i;
            if(idx!=0){
                for(int j = idx-1 ; j>=0 ; j--){
                    if(arr[i] == arr[j]){
                        flag = 1;
                    }
                }
            }
            if(flag == 0){
                ans = arr[i];
                break;
            }
        }
        System.out.println(ans);
    }
}
