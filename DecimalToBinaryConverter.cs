using System;
using System.Collections.Generic;

class Solution {
    static void Main(string[] args) {
		Console.ForegroundColor = ConsoleColor.Green;
		Console.Write("Please input an integer: ");
        int input = Convert.ToInt32(Console.ReadLine());
        ConvertToBinary(input);
    }

    static void ConvertToBinary(int input){
		var original = input;
        //CB 2020-08-23 Create list for 0s and 1s
        var binary = new List<int>();
       
        do{
            double copyInput = input;
            //CB 2020-08-23 Half input
            input = input/2;
            copyInput = copyInput/2;
            
            //CB 2020-08-23 If there is a remainder, add 1 to list
            if (copyInput % 2 == 0.5){
                binary.Add(1);
            }
            
            //CB 2020-08-23 Else, add 0 to the list
            else{
                binary.Add(0);
            }
        }
        while(input > 0);

        binary.Reverse();       
		Console.WriteLine();
		
		Console.ForegroundColor = ConsoleColor.DarkGreen;
		Console.WriteLine("Base 10 = {0}", original);
		
		Console.Write("Base 2 = ");
		
		for(var i = 0; i < binary.Count; i++)
		{
			Console.Write(binary[i]);
		}
		
		Console.WriteLine();
		Console.WriteLine();
		
		Console.ForegroundColor = ConsoleColor.Green;
		Console.Write("Press a key to exit: ");
		Console.ReadKey();
    }
}
