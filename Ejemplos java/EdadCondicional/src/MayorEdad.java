import javax.swing.JOptionPane;

public class MayorEdad {

	public static void main(String[] args) {
		// TODO Ap�ndice de m�todo generado autom�ticamente
		
		//Pedir edad 
	    String edad=JOptionPane.showInputDialog("Ingrese su edad ");
	    double edad1=Double.parseDouble(edad);
	    
	    if(edad1<18) {
	    	System.out.println("es menor de edad");
	    }else
	    {
	    	
	    System.out.println("Es mayor de edad");
	    }

	}

}
