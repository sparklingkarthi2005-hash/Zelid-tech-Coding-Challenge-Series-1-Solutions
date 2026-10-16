import java.util.Scanner;
public class Main
{
public static void main(String[] args)
{
scanner s=new Scanner(System.in);
int n=s.nextInt();
boolean prime=true;
if(n<=1)
{
prime=false;
}
for(int i=2; i<n; i++)
{
if(n%i==0)
{
prime=false;
break;
}}
if(prime){
System.out.println(“YES”);
}
else{
System.out.println(“NO”);
}
}}
