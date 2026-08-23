import java.util.Scanner;

// Name: Kunjan

public class CalculatorMethod
{
    // Method to add two numbers
    public static int add(int firstNumber, int secondNumber)
    {
        return firstNumber + secondNumber;
    }

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int firstNumber = input.nextInt();

        System.out.print("Enter second number: ");
        int secondNumber = input.nextInt();

        int result = add(firstNumber, secondNumber);

        System.out.println("Sum = " + result);

        input.close();
    }
}