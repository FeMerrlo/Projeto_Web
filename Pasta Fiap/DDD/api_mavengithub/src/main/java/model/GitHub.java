package model;

public class GitHub {
	
	private String nome;
	private String qtdSeg;
	private String qtdRep;
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getQtdSeg() {
		return qtdSeg;
	}
	public void setQtdSeg(String qtdSeg) {
		this.qtdSeg = qtdSeg;
	}
	public String getQtdRep() {
		return qtdRep;
	}
	public void setQtdRep(String qtdRep) {
		this.qtdRep = qtdRep;
	} 
	
	   @Override
	    public String toString() {
	        return "nome=" + nome + ", qtdSeg=" + qtdSeg + ", qtdRep=" + qtdRep;
	    }

}
