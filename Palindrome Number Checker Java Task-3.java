import java.util.Scanner;
public class Main
{
public static void main(String[] args)
{
System.out.println(“Enter the number:”);
Scanner s=new Scanner(System.in);
int n=s.nextInt(),rev=0,m=n;
while(n>0)
{
int r=n%10;
rev=rev*10+r;
n=n/10;
}
if(m==rev)
{
System.out.println(“Palindrome Number”);
}
else
{
System.out.println(“Not Palindrome Number”);
}
}}

