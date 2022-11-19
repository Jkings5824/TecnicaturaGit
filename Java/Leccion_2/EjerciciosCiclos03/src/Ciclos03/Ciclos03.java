/*
Ejercicio 03: leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar
primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Ingrese un Número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El Número ingresado " +numero+ " es par");
            }
            else{
                System.out.println("El Número ingresado " + numero + " es impar");
            }
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("El número ingresado:  " + numero+ " finaliza el programa");   
    }
}
