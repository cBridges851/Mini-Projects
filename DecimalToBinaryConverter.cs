using System;
using System.Collections.Generic;

class Solution {
    static void Main(string[] args) {
		Console.ForegroundColor = ConsoleColor.Green;
		Console.Write("Please input an integer: ");
        int input = Convert.ToInt32(Console.ReadLine());
        var binary = ConvertToBinary(input);
		
		Console.ForegroundColor = ConsoleColor.DarkGreen;
		Console.WriteLine("\nBase 10 = {0}", input);
		Console.Write("Base 2 = ");
		
		foreach(var bit in binary)
		{
			Console.Write(bit);
		}
		
		Console.ForegroundColor = ConsoleColor.Green;
		Console.Write("\n\nPress a key to exit: ");
		Console.ReadKey();
    }

    static List<int> ConvertToBinary(int denary)
    {
        //CB 2020-08-23 Create list for 0s and 1s
        var binary = new List<int>();
        
        do
        {
            double copyDenary = denary;
            //CB 2020-08-23 Half denary
            denary = denary/2;
            copyDenary = copyDenary/2;
            
            //CB 2020-08-23 If there is a remainder, add 1 to list
            if (copyDenary % 2 == 1)
            {
                binary.Add(0);
            }
            
            //CB 2020-08-23 Else, add 0 to the list
            else
            {
                binary.Add(1);
            }
        }
        while(denary > 0);

        binary.Reverse();
        return binary;
    }
}
