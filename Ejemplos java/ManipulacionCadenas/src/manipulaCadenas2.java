
public class manipulaCadenas2 {

	public static void main(String[] args) {
		
		String frase="Hoy es un buen día para programar en Java";
		//Método substring sirve para sacar de una cadena una parte de ella 
		String frase_resumen=frase.substring(24,41);//Recoge la frase: programar en Java
		//ESte pide como parametro un indice inicial y un final que será la nueva cadena 
		
		System.out.println(frase_resumen);
		
		
		//Uso del equals y equalsIgnoreCase los dos devuelven valores booleanos 
		//En el caso de equals distingue entre mayusculas y minusculas y el equalsIgnoreCase no 
		String alumno1,alumno2,dia1,dia2;
		alumno1="Fabricio";
		alumno2="Fabricio";
		dia1="Lunes";
		dia2="lunes";
		
		//Usando equals
		System.out.println("Usando equals y alumnos " + alumno1.equals(alumno2) );
		//Usando equalsIngnoreCase 
		System.out.println("Usando equalsIngoreCase " + dia1.equalsIgnoreCase(dia2));
		
		

	}

}
