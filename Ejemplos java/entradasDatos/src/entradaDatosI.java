import java.util.*;

public class entradaDatosI {

	public static void main(String[] args) {
		
		//Crear el objeto Scanner para introducir información del exterior del programa 
		Scanner entrada=new Scanner(System.in);
		
		//Pedir nombre
		System.out.println("Introduce tu nombre por favor ");
		String nombre=entrada.nextLine();
		
		//Pedir edad 
		System.out.println("Introduce tu edad por favor ");
		int edad=entrada.nextInt();
		
		//Mostrar edad y nombre 
		System.out.println("Hola " + nombre + " Tu edad es " + edad);
		
		entrada.close();
		
	}

}
