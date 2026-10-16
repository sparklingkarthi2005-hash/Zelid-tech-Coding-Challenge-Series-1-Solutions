import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
 public static void main(String[] args) {
 Scanner s=new Scanner(System.in);
 int n=s.nextInt();
 int a[]=new int[n];
 for(int i=0; i<n; i++)
 {
 a[i]=s.nextInt();
 }
 int k=s.nextInt();
 for(int i=0; i<n; i++)
 {
 if(a[i]==k) {
 System.out.println("Element found at index " +i);
 return;
 }}
 System.out.println("Element not found");
 }}

