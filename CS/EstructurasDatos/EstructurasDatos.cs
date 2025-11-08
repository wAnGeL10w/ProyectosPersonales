using System;
using System.Threading;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Primer Hola Mundo en C#");
        Console.Write("Escribe tu nombre: ");
        string? nombre = Console.ReadLine();

        Console.WriteLine($"Hola, {nombre}! Bienvenido al mundo de C#.");

        //Realizo una pausa de 2 segundos para despues limpiar la consola
        Thread.Sleep(2000);
        Console.Clear();

        //Creo un arreglo de tipo String con varios nombres
        string[] nombres = { "Ana", "Luis", "Carlos", "Marta", "Sofía" };
        Console.WriteLine("Lista de nombres:");
        /*Uso un ciclo que funciona de manera similar a for pero itera directamente 
        sobre los elementos del arreglo*/
        foreach (string n in nombres)
        {
            Console.WriteLine("Hola " + n + ", Bienvenido a C#");
        }

        Thread.Sleep(2000);
        Console.Clear();
        int[] numeros = {1, 2, 3, 4, 5};
        for (int i = 0; i < numeros.Length; i++)
        {
            Console.WriteLine("Número: " + numeros[i]);
            if(numeros[i] % 2 == 0){
                Console.WriteLine(numeros[i] + " es un número par.");
            }else{
                Console.WriteLine(numeros[i] + " es un número impar.");
            }
        }
        Salida();
    }
    static void Salida()
    {
        Console.WriteLine("Presiona cualquier tecla para salir...");
        Console.ReadKey();
    }
}

