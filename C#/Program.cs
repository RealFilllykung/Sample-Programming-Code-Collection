using System;

namespace C_
{
    class Program
    {
        static void Main(string[] args)
        {
            //เวลาเราจะสร้าง project file ใหม่ใน VS code ให้พิมพ์ dotnet new console
            Console.WriteLine("Hello World!"); //<-- วิธี print output
            Console.Write("Hello World but no new line");
            Console.Write(" na ja\n");

            //วิธีประกาศตัวแปล
            int myNumber = 3;
            string myString = "Hello";
            char myChar = 'A';
            Boolean mybool = false;

            Console.WriteLine(myString.ToLower()); //ทำให้ตัว myString เป็นตัวเล็กทั้งหมด
            Console.WriteLine(myString[0]);//print ค่าตัวแรกของ myString
            Console.WriteLine(myString.IndexOf('e')); //บอกตำแหน่งของตัว e ใน myString

        }
    }
}
