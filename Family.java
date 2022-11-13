
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
public class Family
{
   public static void main (String args[]) throws IOException {
    //variables defined
    int numGB = 0;
    int numBG = 0;
    int numGG = 0;
    int numBB = 0;
    int totalNum = 0;
    
   
    String token ="";
    int spaceDeleter = 0;
    int token2Sub = 0;
    
    File fileName = new File ("test1.txt"); 
    
    Scanner in = new Scanner(fileName); //scans file
    String character = in.nextLine();
    System.out.println("Composition statistics for families with two children");
    while(in.hasNextLine())
    {
        token = in.nextLine( ); //recives token from scanner
        System.out.print(token);
        if(token.equals("GB"))
        {
        numGB = numGB + 1;
        }
        else if(token.equals("BG"))
        {
        numBG = numBG + 1;
        }
        else if(token.equals("GG"))
        {
        numGG = numGG + 1;
        }
        else if(token.equals("BB"))
        {
        numBB = numBB + 1;
        }
        else if(token.equals(""))
        {
        spaceDeleter =+ 1; //tried to delete space to no avial
        }
        else 
        {
        System.out.println("Something went wrong. Please try again.");
        }
    }//end while
    
    
    
   

    
   } //end of main method
} //end of class
