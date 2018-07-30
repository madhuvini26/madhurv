import java.util.*;
import java.math.*;
 
class NextPrimeTest
{
    // Function to get nextPrimeNumber
    static long nextPrime(long n)
    {
        BigInteger b = new BigInteger(String.valueOf(n));
        return Long.parseLong(b.nextProbablePrime().toString());
    }
 
    // Driver method
    public static void main (String[] args)
                    throws java.lang.Exception
    {
        long n = 14;
        System.out.println(nextPrime(n));
    }
}
