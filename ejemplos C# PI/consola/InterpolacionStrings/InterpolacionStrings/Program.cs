using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterpolacionStrings
{
    class Program
    {
        static void Main(string[] args)
        {
            //Cambiar el titulo de la consola 
            Console.Title = "INTERPOLACION";
            //Cambiar el color de fondo y color de letras de la consola 
            Console.BackgroundColor = ConsoleColor.DarkRed;
            Console.ForegroundColor = ConsoleColor.White;
            Console.Clear();
            
            //Mediante un ciclo while mostrar los pares del 1 al 10 
            int i = 1;
            while (i<=100)
            {

                if (i%2==0)
                {
                    Console.Write( " " + $" {i}");//Aquí se usa la interpolación que es en una cadena usar llaves y al inicio siempre el signo dolar
                }
                //Incrementar i
                i++;
            }
            
            //Pausar programa 
            Console.ReadKey();
        }
    }
}
