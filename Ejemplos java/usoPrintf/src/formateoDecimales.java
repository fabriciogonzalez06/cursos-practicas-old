import javax.swing.*;
public class formateoDecimales {

	public static void main(String[] args) {
		
		//Pedir un numero 
		String numero=JOptionPane.showInputDialog("Ingrese un n�mero par sacar ra�z cuadrada");
		//Convertir el n�mero a double
		
		double num=Double.parseDouble(numero);
		
		//Mostrar el resultado con la cadena de formato especificado 
		System.out.print("La raiz de " + num + " es: ");
		/*aqu� utilizamos el "%1.4f" para decir que despues de el punto decimal muestre solo 4 cifras y asi 
		 * se utiliza el printf y siempre requiere dos parametros */
		System.out.printf("%1.4f", Math.sqrt(num));
	}

}
