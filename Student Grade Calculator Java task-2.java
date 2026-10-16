import java.util.Scanner;
class Main {
 public static void main(String[] args) {
 Scanner s=new Scanner(System.in);
 System.out.println("Enter the no.of subjects:");
 int n=s.nextInt();
 int a[]=new int[n];
 System.out.println("Enter marks for "+n+" subjects:");
 for(int i=0; i<n; i++)
 {
 a[i]=s.nextInt();
 }
 int total=0;
 for(int i=0; i<n; i++)
 {
 total=total+a[i];
 }
 double average=(double)total/n;
char grade;
 if(average>=90)
 {
 grade='A';
 }
 else if(average>=75)
 {
 grade='B';
 }
 else if(average>=60)
 {
 grade='C';
 }
 else if(average>=50)
 {
 grade='D';
 }
 else
 {
 grade='F';
 }
 System.out.println("Total Marks="+total);
 System.out.println("Average="+average);
 System.out.println("Grade:"+grade);
 }
}
