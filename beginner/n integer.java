public static void printAverage
{
int num=0;
    double sum=0;
    double avg=0;
    int counter=0;
    while(num>=0){
   System.out.print("Type a number: ");
     num=console.nextInt();

        if(num>0){
     sum+=num;
     counter++;
    avg=sum/counter;
        }


    }
    System.out.println("Average was " +  avg);


}
