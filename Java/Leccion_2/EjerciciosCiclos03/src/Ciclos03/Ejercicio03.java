/*
Ejercicio 03: leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar
primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un Número: "));
        while (numero != 0){
            if (numero % 2== 0){
                JOptionPane.showMessageDialog(null,"El Número ingresado " +numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"El Número ingresado " +numero+" es INPAR");
             }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un Número: "));
        }
        JOptionPane.showMessageDialog(null,"El Número ingresado es " +numero+ " finaliza el programa");
        
    }
    
}
