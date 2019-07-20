using System;

namespace C_
{
    class People{
        private string fname;
        private string lname;
        private int age;

        public People(string fn, string ln, int a){
            fname = fn;
            lname = ln;
            age = a;
        }

        public void showInfo(){
            Console.WriteLine("Full name: " + fname + " " + lname);
            Console.WriteLine("age: " + age);
        }
    }

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

            //ตัวอย่างการรับค่า input
            Console.Write("Enter the color: ");
            string myColor = Console.ReadLine();
            Console.WriteLine("Your input color: " + myColor);

            //ตัวอย่างการสร้าง Arrays
            int[] myNumArray = {2,3,4,5,6};
            string[] myNameList = new string[5];
            myNameList[0]="Fill";

            Console.WriteLine(myNumArray[0]);
            Console.WriteLine(myNameList[0]);

            //ตัวอย่างการใช้ method ที่สร้างขึ้นมาเอง
            SayHello();
            int myExponent = exponentNumber(2,3);

            //if else statement
            if (myExponent == 8){
                Console.WriteLine("The number is eight");
            }
            else{
                Console.WriteLine("The number is not eight");
            }

            //&& || != == คือตัวอย่าง operator

            //ตัวอย่าง loop
            Boolean loop = true;
            while(loop){
                Console.Write("Stop loop? (y|n): ");
                string ans = Console.ReadLine();
                if (ans == "n") loop = false;
            }

            //try catch
            try{
                //ทำอะไรสักอย่าง
                People people1 = new People("Tharathep","Klinla-or",20);
                people1.showInfo();
            }
            catch{
                //ถ้าเกิดโปรแกรมพังให้ทำอะไร
                Console.WriteLine("Error has occurred");
            }
        }

        //ตัวอย่างการสร้าง method ขึ้นมาเอง
        static void SayHello(){
            Console.WriteLine("Hello guys");
        }
        static int exponentNumber(int x, int y){
            int temp = x;
            for(int i = 0; i < y-1; i++){
                x *= temp;
            }
            Console.WriteLine("Value of x = " + x);
            return x;
        }
    }
}
