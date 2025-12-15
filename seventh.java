import java.util.Scanner;

public class ABWholeCube {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get input from the user
        System.out.println("Enter the value of a: ");
        // Use double for precision, or int if only whole numbers are needed
        double a = scanner.nextDouble(); 

        System.out.println("Enter the value of b: ");
        double b = scanner.nextDouble();

        // Calculate (a + b) whole cube using Math.pow()
        double resultPow = Math.pow(a + b, 3); // The Math.pow method takes two double arguments

        // Calculate (a + b) whole cube using direct multiplication
        double sum = a + b;
        double resultDirect = sum * sum * sum;

        // Print the results
        System.out.println("Result using Math.pow(): " + resultPow);
        System.out.println("Result using direct multiplication: " + resultDirect);

        scanner.close();
    }
}
