package adivinarNumero;
import java.util.*;

public class adivinarNumeroRandom {

	public static void main(String[] args) 
	{
		
		//crear instancia para entrada de datos 
		Scanner entrada=new Scanner(System.in);
		
		//Crear n�mero aleatorio utilizando volcamiento
		int aleatoreo=(int)(Math.random()*100);
		
		int numero=0;
		
		int intentos=0;
		
		//Utilizar while para repetir 
		while(aleatoreo!=numero)
		{//Inicio while
			
			//Pedir numero 
			System.out.println("Ingrese un n�mero ");
			numero=entrada.nextInt();
			
			//Validar si es menor o mayor que el numero aleatoreo
			if(numero>aleatoreo) 
			{
				System.out.println("M�s bajo ");
			}else if(numero<aleatoreo)
			{
				System.out.println("M�s alto ");
			}
			
			//Incrementar intentos 
			intentos++;
		}//Final while
		
		//Se salio del ciclo porque el numero fue correcto y mostrar un mensaje que el numero fue encontrado 
		System.out.println("Correcto el n�mero es " + aleatoreo + " lo a logrado en " + intentos + " intentos" );
	}

}
