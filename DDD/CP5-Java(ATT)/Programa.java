package program;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.InputMismatchException;
import model.Pedido;
import model.Produto;

public class Programa {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<Pedido> listaPedidos = new ArrayList<Pedido>();

        while (true) {
            System.out.print("Digite o nome do cliente: ");
            String nomeCliente = scanner.nextLine();

            int quantidadeProdutos = 0;
            int tentativas = 3;
            for (int i = 1; i <= tentativas; i++) {
                try {
                    System.out.print("Digite a quantidade de produtos que deseja comprar: ");
                    quantidadeProdutos = scanner.nextInt();
                    scanner.nextLine();
                    break;
                } catch (InputMismatchException e) {
                    System.out.println("Quantidade inválida! Digite um número inteiro.");
                    scanner.nextLine();
                }
            }

            Pedido novoPedido = new Pedido(nomeCliente);
            for (int i = 1; i <= quantidadeProdutos; i++) {
                System.out.println("Produto " + i + ":");
                System.out.print("Nome: ");
                String nomeProduto = scanner.nextLine();
                int quantidadeProduto = 0;
                boolean quantidadeProdutoValida = false;
                while (!quantidadeProdutoValida) {
                    try {
                        System.out.print("Quantidade: ");
                        quantidadeProduto = scanner.nextInt();
                        scanner.nextLine();
                        quantidadeProdutoValida = true;
                    } catch (InputMismatchException e) {
                        System.out.println("Quantidade inválida! Digite um número inteiro.");
                        scanner.nextLine();
                    }
                }
                double precoProduto = 0.0;
                while (true) {
                    try {
                        System.out.print("Preço: ");
                        precoProduto = scanner.nextDouble();
                        scanner.nextLine();
                        break;
                    } catch (InputMismatchException e) {
                        System.out.println("Preço inválido! Digite um número decimal.");
                        scanner.nextLine();
                    }
                }

                Produto produto = new Produto(nomeProduto, quantidadeProduto, precoProduto);
                novoPedido.adicionarProduto(produto);
            }

            listaPedidos.add(novoPedido);

            System.out.print("Deseja cadastrar um novo pedido? (s/n) ");
            String resposta = scanner.nextLine();
            if (!resposta.equalsIgnoreCase("s")) {
                break;
            }
        }


        try {
            File arquivoPedidos = new File("pedidos.txt");
            arquivoPedidos.createNewFile();
            
            FileWriter gravadorPedidos = new FileWriter(arquivoPedidos);
            BufferedWriter escritor = new BufferedWriter(gravadorPedidos);

            for (Pedido pedido : listaPedidos) {
                escritor.write(pedido.getNomeCliente());
                escritor.newLine();
                for (Produto produto : pedido.getListaProdutos()) {
                	escritor.write(String.format("%s,%d,%.2f%n", produto.getNome(), produto.getQuantidade(), produto.getPrecoUnitario()));
                }
                escritor.newLine();
                }
                            
                            escritor.close();

                            System.out.println("cadastrado com sucesso!");

                        } catch (IOException e) {
                            System.out.println("Erro ao gravar pedidos no arquivo.");
                        }
                    }
}
