import javax.swing.*;
public class formateoDecimales {

	public static void main(String[] args) {
		
		//Pedir un numero 
		String numero=JOptionPane.showInputDialog("Ingrese un número par sacar raíz cuadrada");
		//Convertir el número a double
		
		double num=Double.parseDouble(numero);
		
		//Mostrar el resultado con la cadena de formato especificado 
		System.out.print("La raiz de " + num + " es: ");
		/*aquí utilizamos el "%1.4f" para decir que despues de el punto decimal muestre solo 4 cifras y asi 
		 * se utiliza el printf y siempre requiere dos parametros */
		System.out.printf("%1.4f", Math.sqrt(num));
	}

}
