import java.util.Scanner;

public class JavaProgram
{
   public static void main(String args[])
   {
      String str;
      Scanner scan = new Scanner(System.in);
	  
      System.out.print("Enter Your First Name : ");
      str = scan.nextLine();
	  
      System.out.print("Hello, " + str);
   }
}
