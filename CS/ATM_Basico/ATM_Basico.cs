using System;

class Program
{
    static double saldo = 0.0;
    static void Main(string[] args)
    {
        while (true)
        {
            Console.Clear();
            Console.WriteLine("Bienvenido al Cajero Automático Básico");
            Console.WriteLine("Seleccione una opción:");
            Console.WriteLine("1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir");
            try
            {
                int opcion = Convert.ToInt32(Console.ReadLine());
                if (opcion < 1 || opcion > 4)
                {
                    Console.WriteLine("Error: Opción no válida\nPor favor, ingrese un número entre 1 y 4.\n");
                    Console.ReadKey();
                    continue;
                }
                else
                {
                    switch (opcion)
                    {
                        case 1:
                            ConsultarSaldo();
                            break;
                        case 2:
                            RetirarDinero();
                            break;
                        case 3:
                            DepositarDinero();
                            break;
                        case 4:
                            Console.WriteLine("Gracias por usar el Cajero Automático. ¡Hasta luego!");
                            break;
                    }
                    if (opcion == 4) break;
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Entrada no válida\nPor favor, ingrese un número entre 1 y 4.\n");
                Console.ReadKey();
                continue;
            }
        }
    }
    static void ConsultarSaldo()
    {
        Console.WriteLine($"\nSu saldo actual es: ${saldo:F2}\n");
        Console.ReadKey();
    }
    static void RetirarDinero()
    {
        if (saldo > 0)
        {
            while (true)
            {
                Console.Write("Ingrese la cantidad a retirar: ");
                double cantidad = 0.0;
                //Validar que se ingrese un número
                try
                {
                    cantidad = Convert.ToDouble(Console.ReadLine());
                    if (cantidad <= 0)
                    {
                        Console.WriteLine("Error: La cantidad a retirar debe ser positiva.\n");
                        Console.ReadKey();
                        continue;
                    }
                }
                //Atrapar error de formato
                catch (FormatException)
                {
                    Console.WriteLine("Error: Entrada no válida\nPor favor, ingrese una cantidad numérica.\n");
                    Console.ReadKey();
                    continue;
                }
                //Validar fondos suficientes
                if (cantidad > saldo)
                {
                    Console.WriteLine("Error: Fondos insuficientes.\n");
                    Console.ReadKey();
                    continue;
                }
                saldo -= cantidad;
                Console.WriteLine($"Ha retirado: ${cantidad:F2}\n");
                Console.ReadKey();
                break;
            }
        }
        else
        {
            Console.WriteLine("No tiene fondos suficientes para retirar dinero.\n");
            Console.ReadKey();
        }
    }
    static void DepositarDinero()
    {
        while (true)
        {
            Console.Write("Ingrese la cantidad a depositar: ");
            double cantidad = 0.0;
            //Validar que se ingrese un número
            try
            {
                cantidad = Convert.ToDouble(Console.ReadLine());
                if (cantidad <= 0)
                {
                    Console.WriteLine("Error: La cantidad a depositar debe ser positiva.\n");
                    Console.ReadKey();
                    continue;
                }
            }
            //Atrapar error de formato
            catch (FormatException)
            {
                Console.WriteLine("Error: Entrada no válida\nPor favor, ingrese una cantidad numérica.\n");
                Console.ReadKey();
                continue;
            }
            saldo += cantidad;
            Console.WriteLine($"Ha depositado: ${cantidad:F2}\n");
            Console.ReadKey();
            break;
        }
    }
}

