# PruebaGitHubInstruccional
Es una prueba para usar GitHub instruccional

[![](http://img.youtube.com/vi/YaGqOPxHFkc/0.jpg)](http://www.youtube.com/watch?v=YaGqOPxHFkc "Intro")

## Ejemplos de cosas interesantes

* Enlace: [MiGitHub](https://github.com/ProfCDuqueTec)
* Formula: <img src="http://www.sciweavers.org/tex2img.php?eq=%20%20%5Cprod_a%5Eb%20x%20%5Csqrt%7B%20%5Calpha%20%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="  \prod_a^b x \sqrt{ \alpha } " width="68" height="50" />

```python
import java.util.Scanner;
import java.util.Arrays;

class Main {
  public static void main(String[] args) {
    String mensaje;
    String user;

    user="Camilo";
    mensaje = "Hakim>>\n\tHaré algunos trucos con un arrelgo\n\t";
    System.out.printf(mensaje);

    mensaje = "Primero voy a generar un arreglo con todos sus elementos en 0\n\tDame un número entero positivo para el tamaño del arreglo ?\n" + user + ">>\n\t";

    Scanner teclado = new Scanner(System.in);
    int nElem;

    System.out.printf(mensaje);
    nElem = teclado.nextInt();

    int arreglo[];
    arreglo= new int[nElem];

    Arrays.fill(arreglo,0);
    mensaje = "Hakim>>\n\tEl  arreglo inicializado es " + Arrays.toString(arreglo) + "\n";
    System.out.printf(mensaje);

    mensaje = "Hakim>>\n\tAhora voy a pedirte los datos para crear otro arreglo";
    System.out.printf(mensaje);

    for(int i=0;i<arreglo.length;i++){
      mensaje = "Hakim>>\n\tDame el elemento de la posicion " + i + " del arreglo:\n" + user + ">>\n\t";
      System.out.printf(mensaje);
      arreglo[i] = teclado.nextInt();
    }

    mensaje = "Hakim>>\n\tEl  arreglo es con los datos que me diste es " + Arrays.toString(arreglo) +"\n";
    System.out.printf(mensaje);

    Arrays.sort(arreglo);
    mensaje = "\n\tEl  arreglo ordenado en forma ascendente es " + Arrays.toString(arreglo) + "\n";
    System.out.printf(mensaje);

    int [] CopiaArreglo = Arrays.copyOf(arreglo,nElem+5);
    mensaje = "\n\tAhora una copia del arreglo con 5 elementos más es " + Arrays.toString(CopiaArreglo) + "\n";
    System.out.printf(mensaje);

    int [] CopiaArreglo2 = Arrays.copyOfRange(arreglo,nElem-1,nElem+5);
    mensaje = "\n\tAhora otro arreglo con los 6 últimos elementos de la copia es " + Arrays.toString(CopiaArreglo2) + "\n";
    System.out.printf(mensaje);    

    double maximo= Double.NEGATIVE_INFINITY;
    int posmax=0;
    for(int i=0;i<arreglo.length;i++){
      if(arreglo[i]>maximo) {
        maximo = arreglo[i];
        posmax=i;
        }
    }

     mensaje = "\n\tEl mayor valor del arreglo es " + (int) (maximo) + " en la posición" + posmax + "\n";
    System.out.printf(mensaje);

    double minimo= Double.POSITIVE_INFINITY;
    int posmin=0;
    for(int i=0;i<arreglo.length;i++){
      if(arreglo[i]<minimo){
        minimo = arreglo[i];
        posmin=i;
      }
    }
    mensaje = "\n\tEl menor valor del arreglo es " + (int) (minimo) + " en la posición" + posmax + "\n";
    System.out.printf(mensaje);

    int suma=0;
    for(int i=0;i<arreglo.length;i++){
      suma = suma + arreglo[i];
    }

    mensaje = "\n\tLa suma de todos los elementos del arreglo es " + suma +"\n";
    System.out.printf(mensaje);

    mensaje = "\n\tEl promedio de todos los elementos del arreglo es " + suma/2 +"\n";
    System.out.printf(mensaje);

    int contaNeg=0;
    for(int i=0;i<arreglo.length;i++){
      if(arreglo[i]<0) contaNeg++;
    }

  }
}```
