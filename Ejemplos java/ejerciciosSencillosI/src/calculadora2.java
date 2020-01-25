import javax.swing.*;
public class calculadora2 {

	public static void main(String[] args) {
		
		String nombre=JOptionPane.showInputDialog("Ingrese su nombre, por favor");
		String  aux=JOptionPane.showInputDialog("Ingrese el número 1 ");
		double num1=Double.parseDouble(aux);
		 aux=JOptionPane.showInputDialog("Ingrese el número 2");
		 double num2=Double.parseDouble(aux);
		 
		 //Realizar operacions 
		 double suma=num1+num2;
		 double resta=num1-num2;
		 double multiplicacion=num1*num2;
		 double division=num1/num2;
		 
		 //Mostrar salidas
		 
		    System.out.println("Su nombre es " + nombre);
			System.out.println("La suma de " + num1 + " + " + num2 + " = " + suma);
			System.out.println("La resta de " + num1 + " - " + num2 + " = " + resta);
			System.out.println("La multiplicacion de " + num1 + " * " + num2 + " = " + multiplicacion);
			System.out.println("La division de " + num1 + " / " + num2 + " = " + division);
		

	}

}
