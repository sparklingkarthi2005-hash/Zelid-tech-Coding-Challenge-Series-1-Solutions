import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
 public static void main(String[] args) {
 /* Enter your code here. Read input from STDIN. Print output
to STDOUT. Your class should be named Solution. */
 Scanner s=new Scanner(System.in);
 for(int i=0; i<2; i++)
 {
 int number=s.nextInt();
 s.nextLine();
 String Name=s.nextLine();
 String dept=s.nextLine();
 System.out.println("Roll No: " +number);
 System.out.println("Name: " +Name);
 System.out.println("Department: " +dept);
 }
 }
}
