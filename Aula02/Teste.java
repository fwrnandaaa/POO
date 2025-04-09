import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {
        // Criação de um objeto Scanner para ler entrada do usuário
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe seu nome: ");
        String nome = scanner.nextLine();  // Lê uma linha (incluindo espaços)

      
        System.out.print("Informe sua idade: ");
        int idade = scanner.nextInt(); 

        System.out.println("Olá " + nome + ", Você tem " + idade + " anos.");

        // Fechar o scanner 
        scanner.close();
    }
}
