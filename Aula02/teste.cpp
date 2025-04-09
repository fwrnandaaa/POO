
#include <iostream>
#include <string>

int main() {
    std::string nome;
    int idd;

    std::cout << "Informe seu nome: ";
    std::getline(std::cin, nome); //
    //getline: com ele eu consigo ler uma linha inteira incluindo espaços
    
    std::cout << "Informe sua idade: ";
    std::cin >> idd;

    // xibe a mensagem
    std::cout << "Olá " << nome << ", você tem " << idd << " anos." << std::endl;
    // endl = quebra de linha
    return 0;
}
