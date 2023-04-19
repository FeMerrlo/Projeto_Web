package model;

import java.util.ArrayList;
import java.util.List;

public class Pedido {
    private String nomeCliente;
    private List<Produto> listaProdutos;

    public Pedido(String nomeCliente) {
        this.nomeCliente = nomeCliente;
        this.listaProdutos = new ArrayList<>();
    }

    public void adicionarProduto(Produto produto) {
        if (produto.getQuantidade() < 0 || produto.getPrecoUnitario() < 0) {
            throw new IllegalArgumentException("Quantidade e preço unitário devem ser positivos.");
        }
        listaProdutos.add(produto);
    }

    public void removerProduto(Produto produto) {
        listaProdutos.remove(produto);
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public List<Produto> getListaProdutos() {
        return listaProdutos;
    }

    public double calcularValorTotal() {
        double valorTotal = 0.0;
        for (Produto produto : listaProdutos) {
            valorTotal += produto.getQuantidade() * produto.getPrecoUnitario();
        }
        return valorTotal;
    }
}
