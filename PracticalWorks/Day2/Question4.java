package Hexaware.Day2;

import java.util.Scanner;

public class Question4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String ans = "1";
        for(int i = 1 ; i < n ; i++){
            String temp = "";
            char ch = ans.charAt(0);
            int cnt = 1;
            for(int j = 1 ; j < ans.length() ; j++){
                if(ans.charAt(j) == ch){
                    cnt++;
                }
                else{
                    temp = temp + cnt + "" + ch;
                    ch = ans.charAt(j);
                    cnt = 1;
                }
            }
            ans = temp + cnt + "" + ch;
        }
        System.out.println(ans);
    }
}
