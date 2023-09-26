using FiapHelloWord.Models;
using System;


namespace FiapHelloWord
{
    class Program
    {
        static void Main(System.String[] args)
        {
            aHelloModel hello = new HelloModel();
            hello.Mensagem = "Ola FIap, tudo ok ?";


            Console.WriteLine(hello.Mensagem);


            Console.Read();


        }
    }



}
