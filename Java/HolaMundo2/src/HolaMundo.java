
import java.util.Scanner;

//Nuestro primer programa Hola mundo(para comentar una linea)
/*
para comentar varias lines o extensivos
 */
 /*
public class HolaMundo {
    public static void main(String args[]) {
        System.out.println("Hola mi nombre es Javy");
        System.out.println("Hola Mundo desde Java");
    }
}
 */
public class HolaMundo {

    public static void main(String args[]) {
        /* System.out.println("Hola Mundo desde Java");
        //tipo entero
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //tipo string
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
         */
        //Var - inferencia e tipos en Java
        /*
       var miVariableEntera2 = 10;
       var miVariableCadena2 = "Seguimos Estudiando";
        System.out.println("miVariableEntera2=" + miVariableEntera2);
        System.out.println("miVariableCadena= " + miVariableCadena2);
        //soutv + tab (autocompleta para mandar a imprimir)
        //shift + f6 para ejecutar
        /*Reglas para definir una variable en Java
        1° utilizar preferentemete el metodo/tipo de escritura/entrada CAMELCASE, no utilizar mayuscula en la primer leta, empezar con minuscula y terminar con minuscula
        2° no utilizar numeros como primer letra de una variable
        3° no utilizar caracter especial como primer letra de una variable
        4° si puede utilizar guion bajo: _ 
        5° se puede usar elsigno: $
        6° No es recomendable utilizar acentos, para evitar conflictos 
        7° es ilegal utilizar el simbolo numeral: #
         *//*
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        //cuando imprime el resultado, sigue en primer contexto de izquierda a derecha, exeptuado si utilizamos los parentesis (), que se toman como prioridad ante todo
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
         *//*
        //Ejercicio: Caracteres especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre); // "\n" (diagonal inversa y letra n minuscula)
        System.out.println("Tabulador: \t" + nombre); // tabulador, espacio para centrar
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroseso: \b\b"+ nombre); // Caracter de retroseso
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");
         *//*
         //Ejercicio libro
         Scanner scanner = new Scanner(System.in);
        //
        System.out.println("Proporciona el titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el autor: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + "fue escrito por " + autor);
         *//*
        //Clase scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el Titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado = " + titulo2+" "+usuario2);
         *//*
        //Tipos numéricos Enteros
        byte numEnteroByte = 10; //se puede forzar a ingresarlo en byte con: "(byte)" antes del numero: (byte)127. Pero se pierde precicion
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: " + Byte.MAX_VALUE);

        short numEnteroShort = 10;//se puede forzar a ingresarlo en short con: "(short)" antes del numero: (shor)32768. Pero se pierde precicion
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del short: " + Short.MAX_VALUE);

        int numEnteroInt = 10;//se puede forzar a ingresarlo en short con: "(short)" antes del numero y "L" despues de la lietal: (shor)32768L. Pero se pierde precicion
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: " + Integer.MAX_VALUE);

        long numEnterolong = 10;
        System.out.println("numEnterolong = " + numEnterolong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valot maximo del Long: " + Long.MAX_VALUE);
         *//*
        //Tipos numéricos con coma/punto Decimal
        float numFloat = 10.0F;//toma el dato como "double",se puede colocar "F" o (float), para convertirlo en float letras mayusculas para mejor comprenciond el codigo. 
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de Float: "+ Float.MIN_VALUE);
        System.out.println("El valor maximo de Float: "+ Float.MAX_VALUE);
        
        double numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo de Double: "+ Double.MIN_VALUE);
        System.out.println("Valor maximo de Double: "+ Double.MAX_VALUE);
         *//*
        // Inferencia de tipos car y tipós primitivos
        var numEntero =20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto se trasnforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
         *//*
        //Tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36;//Valor decimal en el juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; //Indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36;//Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);
         *//*
        //Tipos primitivos booleano
        var varBool = false;
        System.out.println("varBool = " + varBool);

        if (varBool) {
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja ");
        }*//*
        // Algoritmo: ¿Es mayor de edad?
        var edad = 18;//Literal, tener presente la inferencia de tipos
        //var adulto = edad >= 18;//Esta es la expresion booleana
        if (edad >=18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
         *//*
        //convercion de tipos primitivos
        var edad = Integer.parseInt("20");//de string a entero
        System.out.println("edad = " + (edad + 1));

        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
         */
        //Pedir un valor
        //var entrada = new Scanner(System.in);
        //System.out.println("Digite su edad:");
        //edad = Integer.parseInt(entrada.nextLine());
        //System.out.println("edad = " + edad);
        /*
        //Conversion de tipos primitivos
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);

        var fraseChar = "programadores".charAt(3);//mostrar el indice/letra dentro de la palabra asignada en este caso "programacion"
        System.out.println("fraseChar = " + fraseChar);

        System.out.println("Digite un caracter:");
        fraseChar = entrada.nextLine().charAt(0);//Tener el scaner activo para poder utilizarlo
        System.out.println("fraseChar = " + fraseChar);
         *//*
        //Operadores aritmeticos
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("Resultado de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("Resultado de la resta = " +solucion);
        
        solucion = num1 * num2;
        System.out.println("Resultado de la multiplicacion = " +solucion);
        
        solucion = num1 / num2;
        System.out.println("Resultado de la division = " +solucion);
        
        var solucion2 = 3.4/num2;
        System.out.println("Resultado de la solucion2 = " + solucion2);
        
        solucion = num1 % num2;//Guarda el residuo entero de la division
        System.out.println("solucion2 = " + solucion2);//5/4
        
        if (num1 % 2== 0)
            System.out.println("El numero es par");
        else
            System.out.println("El numero es inpar");
         *//*
        //Operadores de asignacion
        int varNum1 = 1, varNum2 =4;
        var varNum3 = varNum1 + 6 -varNum2; //Una operacion
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 +=1;//
        System.out.println("varNum1 = " + varNum1);
        
        // -= += /= %=
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);
         *//*
        //Operadores unarios
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);//El resultado sera un numero negativo
        
        //Operadores de negacion
        var varC = true;//Esta literal en java es de tipo booleano
        var varD = !varC;//Aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //operadores de incremento:Preincremento
        var varE = 9;//Se va modificar su valor 
        var varF = ++varE;//Simbolo antes de la variable
        //Primero se incrementa la variable y despues se utiliza el valor
        System.out.println("varE = " + varE);//Se incrementa en la unidad
        System.out.println("varF = " + varF);//va a sumar uno
        
        //postincrecimiento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //operadores unarios de decremento: predecremento 
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//la variable ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK);//aqui va a decrementar en uno
        System.out.println("varL = " + varL);
         *//*
         //Valores de ingualdad o relacionales
         var aNum =5;
         var bNum =4;
         var cNum =(aNum == bNum);
         System.out.println("cNum = " + cNum);
         
         var dNum = aNum != bNum;
         
         var cadenaA = "Helo";
         var cadenaB = "bye bye";
         var cVar = cadenaA == cadenaB;
         System.out.println("cVar = " + cVar);
         
         var fVar = cadenaA.equals(cadenaB);
         System.out.println("fVar = " + fVar);
         
         var gVar = aNum == bNum;// > >= < <= == !=
         System.out.println("gVar = " + gVar);
         
         if (bNum % 2 == 0){
             System.out.println("El numero es par");
         } else {
             System.out.println("El numero es impar");    
         }
         var edad = 30;
         //var adulto = 18;//Literal, tener presente la inferencia de tipos
         var adulto = edad >= 18;//Esta es la expresion booleana
         if (edad >=18){ //Puede ser Tambien: if (edad >=adulto){
            System.out.println("Eres mayor de edad");
        }else{
            System.out.println("Eres menor de edad");
        }
         *//*
        //Operador condicional and
        var valorA = 7;
        var valorMinimo = 0;//Rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <=10;
        
        if (respuesta)
            System.out.println("Esta dentro del rango establecido");
        else
            System.out.println("Esta fuera del rango establecido");
         *//*
        var vacaciones = false;
        var diaLibre = true;
        if (vacaciones || diaLibre);
        System.out.println("Papa puede asistir al juego de su hijo");
        else;
        System.out.println("papa no puede asistir al juego de su hijo");
        *//*
         //Operador ternario
         var resultadoT = (5 > 8) ? "Veradadero" : "Falso";
         System.out.println("resultadoT = " + resultadoT);
         
         var numeroT = 4;
         resultadoT = (2 % numeroT == 0) ? "Es par" : "Es inpar";
         System.out.println("numeroT = " + numeroT);
         *//*
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucioneAritmetica = 4 + 5 * 6 / 3;//4+((5*6)/3)=30/3=10+4=14
        System.out.println("solucioneAritmetica = " + solucioneAritmetica);
        
        solucioneAritmetica = (4+5)*6/3;//4+5=9*6=54/3=18
        System.out.println("solucioneAritmetica = " + solucioneAritmetica);
        */
         

    }
}
