
using System;
namespace Teste;
class Program
{
    static void Main()
    {
        // Solicitar o nome do usuário
        Console.Write("Informe seu nome: ");
        string nome = Console.ReadLine();  // ReadLine é o print

        // Solicitar a idade do usuário
        Console.Write("Informe sua idade: ");
        int idade = int.Parse(Console.ReadLine()); 

        // WriteLine
        Console.WriteLine("Olá " + nome + ", Você tem " + idade + " anos.");
    }
}

