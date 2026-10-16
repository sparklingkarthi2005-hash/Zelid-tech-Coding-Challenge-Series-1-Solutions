import java.util.Scanner;
public class Main {
 public static void main(String[] args) {
 Scanner s = new Scanner(System.in);
 System.out.println("Enter the number of elements: ");
 int n = s.nextInt();
 int[] a= new int[n];
 System.out.println("Enter " + n + " numbers:");
 for (int i = 0; i < n; i++) {
 a[i] = s.nextInt();
}
// Assume initial small values
 int largest = numbers[0];
 int secondLargest = -1;
 // Find the largest value first
 for (int i = 1; i < n; i++) {
 {
 largest = numbers[i];
 }
 }
 // Find the largest value that is not equal to 'largest'
 for (int i = 0; i < n; i++) {
 if (numbers[i] != largest) {
   if (secondLargest == -1 || numbers[i] > secondLargest) {
 secondLargest = numbers[i];
 }
 }
 }
 if (secondLargest == -1) {
 System.out.println("There is no distinct second largest
number.");
 } else {
 System.out.println("Second largest number is: " +
secondLargest);
 }
 }
}

 
