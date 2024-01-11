package Hexaware.Day2;

import java.util.HashMap;
import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<Integer,Integer> visited = new HashMap<>();
        int ans = findNumberOfSquares(n,visited);
        System.out.println(ans);
    }
    private static int findNumberOfSquares(int n,HashMap<Integer,Integer> map){
        if(n <= 3){
            return n;
        }
        if(map.containsKey(n)){
            return map.get(n);
        }
        int ans = n;
        for(int i = 1; i*i <= n ; i++){
            ans = Math.min(ans,findNumberOfSquares(n-i*i,map));
        }
        map.put(n,ans);
        return ans;
    }
}
