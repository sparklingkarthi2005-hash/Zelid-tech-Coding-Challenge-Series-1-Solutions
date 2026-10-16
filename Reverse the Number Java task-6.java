import.java.util.Scanner;
public class Main
{
public static void main(String[] args)
{
Scanner s=new Scanner(System.in);
int n=s.nextInt(),rev=0;
while(n>0)
{
int r=n%10;
rev=rev*10+r;
n=n/10;
}
System.out.println(rev);
}}

