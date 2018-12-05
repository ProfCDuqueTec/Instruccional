package com.company;
import java.util.Scanner;

class Hakim {
    public static String Usuario;

    public Hakim(String mensaje){
        System.out.printf("Hakim>> " + mensaje);
    }

    public static String SetUsuario(String mensaje){
        System.out.printf("Hakim>> " + mensaje + "\n\t\tTu>> ");

        Scanner teclado = new Scanner(System.in);
        return teclado.nextLine();
    }

    public static void Habla(String mensaje){
        System.out.printf("Hakim>> " + mensaje);
    }

    public static int LeeEntero(String mensaje, int LimInf, int LimSup, String NomUsuario){
        int num;
        Scanner lectura = new Scanner(System.in);
        while (true){ //bucle infinito
            try{ //intentar el siguiente bloque {}
                Hakim.Habla(mensaje +"\n\t" + NomUsuario + ">> ");
                num = lectura.nextInt();
                if((num<LimInf) || (num>=LimSup) ){  //validación de rango
                    Hakim.Habla("Dame un número entero entre " + LimInf + " y " + LimSup + "\n\t" + NomUsuario);
                    continue; //repita el ciclo
                }else{
                    break; // finalice el ciclo
                } //todo bien entonces salir del while con el número correcto en el rango
            }catch(java.util.InputMismatchException e){ //ocurrió un error de tipo en la lectura
                System.out.printf("Ocurrió un error de tipo de dato!\n");
                System.out.printf("El sistema generó el siguiente mensaje: \n\t" + e + "\n");
                lectura = new Scanner(System.in); // crear un nuevo objeto teclado para no tener el error
                continue; //No coincide el tipo de dato ingresado con el esperado, seguir en el while
            }
        }
        return num;
    }

}

class Main {
    public static void main(String[] args) {
        Hakim Chatbot = new Hakim("Hola, mucho gusto, soy Hakim, El Sabio!\n");
        Hakim.Usuario = Hakim.SetUsuario("Cuál es tu nombre?");
        Hakim.Habla("Mucho gusto! " + Hakim.Usuario + "\n");
        int edad = Hakim.LeeEntero("Qué edad tienes?",1,100, Hakim.Usuario);
    }
}