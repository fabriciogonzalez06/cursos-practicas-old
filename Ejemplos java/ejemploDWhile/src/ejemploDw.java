import javax.swing.*;
public class ejemploDw {

	public static void main(String[] args) {
		// TODO Apéndice de método generado automáticamente
		String genero="";
		
		do {
			//Pedir genero
			genero=JOptionPane.showInputDialog("Introduce tu genero  (M/F)");
			
		}while(genero.equalsIgnoreCase("H")==false && genero.equalsIgnoreCase("M")==false );

		//Pedir altura 
		int altura=Integer.parseInt(JOptionPane.showInputDialog("Ingresa tu altura en cm "));
		
		int pesoIdeal=0;
		
		//Ver si es hombre o mujer y calcular el peso ideal
		if(genero.equalsIgnoreCase("m")) 
		{
			pesoIdeal=altura-110;
			
		}else if(genero.equalsIgnoreCase("m")); 
		{
			pesoIdeal=altura-120;
		}
		
		//Mostrar peso ideal 
		System.out.println("Tu peso ideal es " + pesoIdeal + " kg");
	}
	
	

}
