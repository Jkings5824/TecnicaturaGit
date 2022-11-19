
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada =  new Scanner(System.in);
        int horasSemanales;
        float salarioHora, salarioTotal;
        
        System.out.println("Ingrese las horas semanales trabajadas: ");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el salario por hora: ");
        salarioHora = Float.parseFloat(entrada.nextLine());
        
        salarioTotal= horasSemanales*salarioHora;
        System.out.println(salarioTotal+"\nEl salario semanal es: "+ salarioTotal);
                        
    }
}
