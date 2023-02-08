package program;

import java.io.IOException;


import model.Endereco;
import service.ViaCepService;


public class Teste {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner ler = new Scanner(System.in);
		
		ViaCepService viacepservice = new ViaCepService();


        try {
            Endereco endereco = viacepservice.getEndereco("11085680");
           
            String ddd = endereco.getDdd();
            String uf = endereco.getUf();
            System.out.printf("Me informe o CEP: \n");
            
            System.out.println(endereco + "\n");
            System.out.println(ddd + "\n");
            System.out.println(uf  + "\n");
           
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }  

	}

}
