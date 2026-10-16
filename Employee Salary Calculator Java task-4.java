import java.util.Scanner;
public class SalaryCalculator {
 public static void main(String[] args) {
 Scanner s = new Scanner(System.in);
 // Input Basic Salary
 System.out.print("Enter Employee's Basic Salary: ");
 double basicSalary = s.nextDouble();
 // Calculations based on criteria
 double hra = 0.20 * basicSalary;
 double da = 0.10 * basicSalary;
 double grossSalary = basicSalary + hra + da;
 double pf = 0.12 * basicSalary;
 double netSalary = grossSalary - pf;
 System.out.println("\n=== Salary Details ===");
 System.out.printf("Basic Salary : %.2f\n", basicSalary);
 System.out.printf("HRA (20%%) : %.2f\n", hra);
 System.out.printf("DA (10%%) : %.2f\n", da);
 System.out.println("----------------------");
 System.out.printf("Gross Salary : %.2f\n", grossSalary);
 System.out.printf("PF (12%%) : %.2f\n", pf);
 System.out.println("----------------------");
 System.out.printf("Net Salary : %.2f\n", netSalary);
 }
}
