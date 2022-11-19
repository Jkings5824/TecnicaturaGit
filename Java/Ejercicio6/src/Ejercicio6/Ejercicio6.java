package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo = 0, luis, juan, total;
        System.out.println("Dijite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        

        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de Luis es: US$ " + luis);
        System.out.println("El dinero de juan es: US$ " + juan);
        System.out.println("El total de dinero entre los tres es: US$ " + total);
    }
}
