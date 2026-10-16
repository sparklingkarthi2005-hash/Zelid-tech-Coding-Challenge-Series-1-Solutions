import java.util.Scanner;
public class Main
{
public static void main(String[] args)
{
Scanner s=new Scanner(System.in);
String str=s.nextline();
Char c[]=str.toCharArray();
int count=0;
for(int i=0; i<c.length; i++)
{
if(c[i]==’A’ || c[i]==’E’ || c[i]==’I’ || c[i]==’O’ || c[i]==’U’ || c[i]==’a’ ||
c[i]==’e’ || c[i]==’I’ || c[i]==’o’ || c[i]==’u’)
{
count++;
}
}
System.out.println(count);
}}
