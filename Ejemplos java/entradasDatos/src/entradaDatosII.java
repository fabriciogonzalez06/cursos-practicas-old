import javax.swing.*;/*Esta clase contiene varios m�todos y el que utilizaremos es statico por ende 
no ocuparemos crear un objeto de esa clase pero si usar la clase.metodo a utilizar */

public class entradaDatosII {

	public static void main(String[] args) {
		//Utilizar la clase  JOptionPane y el m�todo  showInputDialog 
		String nombre=JOptionPane.showInputDialog("Introduce tu nombre por favor ");//Este m�todo recibe String
		String edad=JOptionPane.showInputDialog("Introduce tu edad, por  favor ");
		int edad2=Integer.parseInt(edad);
		
		//Mostrar mensaje Final 
		System.out.println("Hola " + nombre + " el a�o siguiente tendr�s " + (edad2+1) + " a�os ");
		
		
		

	}

}
