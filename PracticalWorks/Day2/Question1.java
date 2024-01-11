package Hexaware.Day2;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Question1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] words = new String[n];
        for(int i = 0 ; i < n ; i++){
            words[i] = sc.next();
        }
        String sentence = sc.nextLine();

        boolean ans = false;
        HashSet<String> set = new HashSet<>(Arrays.asList(words));
        int start = 0;
        for(int i = 1 ; i <= sentence.length() ; i++){
            String temp = sentence.substring(start,i);
            if(set.contains(temp)){
                start = i;
            }
        }
        if(start == sentence.length()){
            ans = true;
        }
        System.out.println(ans);
    }
}
