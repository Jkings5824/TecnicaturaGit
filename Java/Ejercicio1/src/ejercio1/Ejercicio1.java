//Ejercicio tienda de Libros
package ejercio1;

import java.util.Scanner;

public class Ejercicio1{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el ID del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("onfirme si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());

        System.out.println(nombreLibro + " #" + idLibro);
        System.out.println("precioLibro = $" + precioLibro);
        System.out.println("El envio del libro gratuito es: " + envioGratuito);

    }
}
