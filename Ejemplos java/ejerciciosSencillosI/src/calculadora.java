import java.util.*;
public class calculadora {

	public static void main(String[] args) {
		
		//Crear instancia para entradas 
		Scanner entrada =new Scanner(System.in);
		
		System.out.println("Ingrese su nombre, por favor ");
		 String nombre=entrada.nextLine();
		 
		 System.out.println("Ingrese el primer número ");
		 double num1=entrada.nextDouble();
		 
		 System.out.println("Ingrese el segundo número");
		 double num2=entrada.nextDouble();
		 
		 double suma=num1+num2;
		 double resta=num1-num2;
		 double multiplicacion=num1*num2;
		 double division=num1/num2;
		 
		 System.out.println("Su nombre es " + nombre);
		System.out.println("La suma de " + num1 + " + " + num2 + " = " + suma);
		System.out.println("La resta de " + num1 + " - " + num2 + " = " + resta);
		System.out.println("La multiplicacion de " + num1 + " * " + num2 + " = " + multiplicacion);
		System.out.println("La division de " + num1 + " / " + num2 + " = " + division);
	}

}
