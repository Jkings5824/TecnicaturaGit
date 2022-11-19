package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Debera ingresar dos numeros");
        System.out.println("Primer numero: ");
        int num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Segundo numero:");
        int num2 = Integer.parseInt(entrada.nextLine());
        System.out.println("El numero mayor es: ");
        System.out.println(num1 > num2 ? num1 : num2);

    }
}
