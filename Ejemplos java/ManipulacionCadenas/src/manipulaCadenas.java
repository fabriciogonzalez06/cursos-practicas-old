
public class manipulaCadenas {

	public static void main(String[] args) {
		// TODO Ap�ndice de m�todo generado autom�ticamente

		String miNombre="Fabricio";
		
		System.out.println("M� nombre es " + miNombre );
		
		//MOstrar el tama�o de la cadena
		System.out.println("M� nombre tiene " + miNombre.length() + " letras");
		
		//Mostrar la primera letra de la cadena 
		System.out.println("La primera letra de mi nombre es " + miNombre.charAt(0));
		
		//Mostrar ultima letra
		int ultimaLetra=miNombre.length();
		System.out.println("La ultima letra es " + miNombre.charAt(ultimaLetra-1));
		
	}

}
