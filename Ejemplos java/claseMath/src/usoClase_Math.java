
public class usoClase_Math {

	public static void main(String[] args) {
		// TODO Ap�ndice de m�todo generado autom�ticamente
		//Ra�z cuadrad
		double raiz=Math.sqrt(81);
		System.out.println("La ra�z cuadrada de 9 es " + raiz);
		
		double base,exponente,res;
		base=4;
		exponente=4;
		res=Math.pow(base, exponente);
		System.out.println("El resultado de " + base + " ^" + exponente + " = " + res );
		
		
		//Redondear y refundiciones 
		double num1=5.85;
		int resultado=(int)Math.round(num1);//Refundici� o volcamiento debido a que round cuando recibe un 
		//double lo que devuelve es un long hay que refundir a int 
		System.out.println("El redondeo de " + num1 + " es " + resultado);
				
		
	}

}
