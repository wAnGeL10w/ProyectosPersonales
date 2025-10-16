#include <iostream>

using namespace std;
int main(){
    int n=0;
    cout<<"Ingresa un numero entero positivo: ";cin>>n;
    //Valido que el numero sea positivo
    while (n<0){
        cout<<"Error, ingresa un numero entero positivo: ";cin>>n;
    }
    //Genero la tabla de multiplicar
    cout<<"\nTabla de multiplicar del "<<n<<endl;
    cout<<"-------------------------"<<endl;
    for(int i=1; i<=10; i++){
        cout<<n<<" x "<<i<<" = "<<n*i<<endl;
    }
    cout<<endl;
    return 0;
}