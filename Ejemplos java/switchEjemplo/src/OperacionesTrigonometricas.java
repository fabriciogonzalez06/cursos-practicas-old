//Importar paquetes para Clase Scanner y JOptionPane
import java.util.*;//Clase para utilizar Scanner 
import javax.swing.*;//Para utilizar JOptionPane
public class OperacionesTrigonometricas {

	public static void main(String[] args) {
		//Crear Instancia de tipo Scanner 
		Scanner entrada=new Scanner(System.in);
		
		System.out.println("Elige una opción: \n 1: Cuadrado \n 2: Rectangulo \n 3: Triangulo \n 4: Circulo");
		int opc=entrada.nextInt();
		
		//Usar switch 
		switch (opc)
		{
		case 1:
			//Pedir un lado 
			int lado=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la base "));
			//Mostrar resultado 
			System.out.println("El area del cuadrado es " + Math.pow(lado, 2));
			//Se ocupa un break
			break;
		case 2:
			int base=Integer.parseInt(JOptionPane.showInputDialog("Introduce la base "));
			int altura=Integer.parseInt(JOptionPane.showInputDialog("Introduce la altura "));
			//Mostrar resultado 
			System.out.println("El area del rectangulo es " + (base*altura));
			//Se ocupa un break
			break;
		case 3:
			
			base=Integer.parseInt(JOptionPane.showInputDialog("Introduce la base "));
			altura=Integer.parseInt(JOptionPane.showInputDialog("Introduce la altura "));
			//Mostrar resultado del area del triangulo 
			System.out.println("El area del triangulo es " + (base*altura)/2);
			//Break necesario 
			break;
		case 4:
			
			int radio=Integer.parseInt(JOptionPane.showInputDialog("Introduce el radio "));
			
			System.out.print("El area del radio es ");
			System.out.printf("%1.2f", Math.PI*(Math.pow(radio, 2)));
			break;
		default:
			System.out.println("Esta opción no es válida");			
		}

	}

}
