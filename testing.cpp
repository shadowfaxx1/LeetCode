#include<bits/stdc++.h>
using namespace std;

int main () 
{
     string x ="  -31 okf a ";
    try {
        int result = std::stoi(x);
        std::cout << result << std::endl;
    } 
    catch (const std::invalid_argument& e) {
        std::cout << "Invalid argument: " << e.what() << std::endl;
    } 
    catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << std::endl;
    }
}