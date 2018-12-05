# PruebaGitHubInstruccional
Es una prueba para usar GitHub instruccional

[![](http://img.youtube.com/vi/YaGqOPxHFkc/0.jpg)](http://www.youtube.com/watch?v=YaGqOPxHFkc "Intro")

## Ejemplos de cosas interesantes

* Enlace: [MiGitHub](https://github.com/ProfCDuqueTec)
* Formula: <img src="http://www.sciweavers.org/tex2img.php?eq=%20%20%5Cprod_a%5Eb%20x%20%5Csqrt%7B%20%5Calpha%20%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="  \prod_a^b x \sqrt{ \alpha } " width="68" height="50" />

```java

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
}

```

ahora unos Ejemplos

<p><a id="examples" title="Examples" class="toc-item"></a></p>

<h2>Examples</h2>

<ul class="example-nav js-examples-nav">
  <li><a href="#" class="selected" data-container-id="example-text" data-proofer-ignore="">Text</a></li>
  <li><a href="#" data-container-id="example-lists" data-proofer-ignore="">Lists</a></li>
  <li><a href="#" data-container-id="example-images" data-proofer-ignore="">Images</a></li>
  <li><a href="#" data-container-id="example-headers" data-proofer-ignore="">Headers &amp; Quotes</a></li>
  <li><a href="#" data-container-id="example-code" data-proofer-ignore="">Code</a></li>
  <li><a href="#" data-container-id="example-extras" data-proofer-ignore="">Extras</a></li>
</ul>

<div class="markdown-example" id="example-text">
<pre class="source">
It's very easy to make some words **bold** and other words *italic* with Markdown. You can even <span style="white-space:nowrap">[link to Google!](http://google.com)</span>
</pre>
<div class="rendered">
It's very easy to make some words <strong>bold</strong> and other words <em>italic</em> with Markdown. You can even <a href="http://google.com">link to Google!</a>
</div>
</div>

<div class="markdown-example" id="example-lists" style="display:none">
<pre class="source">
Sometimes you want numbered lists:

1. One
2. Two
3. Three

Sometimes you want bullet points:

* Start a line with a star
* Profit!

Alternatively,

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this
</pre>
<div class="rendered">
  <p>Sometimes you want numbered lists:</p>
  <ol>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
  </ol>
  <p>Sometimes you want bullet points:</p>
  <ul>
  <li>Start a line with a star</li>
  <li>Profit!</li>
  </ul>
  <p>Alternatively,</p>
  <ul>
  <li>Dashes work just as well</li>
  <li>And if you have sub points, put two spaces before the dash or star:
  <ul>
  <li>Like this</li>
  <li>And this</li>
  </ul>
  </li>
  </ul>
</div>
</div>

<div class="markdown-example" id="example-images" style="display:none">
<pre class="source">
If you want to embed images, this is how you do it:

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
</pre>
<div class="rendered">
  <p>If you want to embed images, this is how you do it:</p>
  <p><img src="https://octodex.github.com/images/yaktocat.png" alt="Image of Yakotocat"></p>
</div>
</div>

<div class="markdown-example" id="example-headers" style="display:none">
<pre class="source">
# Structured documents

Sometimes it's useful to have different levels of headings to structure your documents. Start lines with a `#` to create headings. Multiple `##` in a row denote smaller heading sizes.

### This is a third-tier heading

You can use one `#` all the way up to `######` six for different heading sizes.

If you'd like to quote someone, use the &gt; character before the line:

&gt; Coffee. The finest organic suspension ever devised... I beat the Borg with it.
&gt; - Captain Janeway
</pre>
<div class="rendered">
  <h1>Structured documents</h1>

  <p>Sometimes it’s useful to have different levels of headings to structure your documents. Start lines with a <code>#</code> to create headings. Multiple <code>##</code> in a row denote smaller heading sizes.</p>

  <h3>This is a third-tier heading</h3>

  <p>You can use  one <code>#</code> all the way up to <code>######</code> six for different heading sizes.</p>

  <p>If you’d like to quote someone, use the &gt; character before the line:</p>

  <blockquote><p>Coffee. The finest organic suspension ever devised… I beat the Borg with it.
  - Captain Janeway</p></blockquote>
</div>
</div>

<div class="markdown-example" id="example-code" style="display:none">
<pre class="source">
There are many different ways to style code with GitHub's markdown. If you have inline code blocks, wrap them in backticks: `var example = true`.  If you've got a longer block of code, you can indent with four spaces:

    if (isAwesome){
      return true
    }

GitHub also supports something called code fencing, which allows for multiple lines without indentation:

```
if (isAwesome){
  return true
}
```

And if you'd like to use syntax highlighting, include the language:

```javascript
if (isAwesome){
  return true
}
```
</pre>
<div class="rendered">
  <p>There are many different ways to style code with GitHub’s markdown. If you have inline code blocks, wrap them in backticks: <code>var example = true</code>.  If you’ve got a longer block of code, you can indent with four spaces:</p>

<pre><code>if (isAwesome){
  return true
}
</code></pre>

  <p>GitHub also supports something called code fencing, which allows for multiple lines without indentation:</p>

<pre><code>if (isAwesome){
  return true
}
</code></pre>

  <p>And if you’d like to use syntax highlighting, include the language:</p>

<div class="highlight highlight-javascript"><pre><span class="k">if</span> <span class="p">(</span><span class="nx">isAwesome</span><span class="p">){</span>
  <span class="k">return</span> <span class="kc">true</span>
<span class="p">}</span>
</pre></div>

</div>
</div>

<div class="markdown-example" id="example-extras" style="display:none">
<pre class="source">
GitHub supports many extras in Markdown that help you reference and link to people. If you ever want to direct a comment at someone, you can prefix their name with an @ symbol: Hey @kneath — love your sweater!

But I have to admit, tasks lists are my favorite:

- [x] This is a complete item
- [ ] This is an incomplete item

When you include a task list in the first comment of an Issue, you will see a helpful progress bar in your list of issues. It works in Pull Requests, too!

And, of course emoji! :<span></span>sparkles: :<span></span>camel: :<span></span>boom:
</pre>
<div class="rendered">
  <p>GitHub supports many extras in Markdown that help you reference and link to people. If you ever want to direct a comment at someone, you can prefix their name with an @ symbol: Hey <a href="https://github.com/kneath" class="user-mention">@kneath</a> — love your sweater!</p>

  <p>But I have to admit, tasks lists are my favorite:</p>

  <ul class="task-list">
  <li class="task-list-item">
  <input type="checkbox" class="task-list-item-checkbox" checked disabled> This is a complete item</li>
  <li class="task-list-item">
  <input type="checkbox" class="task-list-item-checkbox" disabled> This is an incomplete item</li>
  </ul>
  <p>When you include a task list in the first comment of an Issue, you will see a helpful progress bar in your list of issues. It works in Pull Requests, too!</p>
  <p>And, of course emoji! <img class="emoji" title=":sparkles:" alt=":sparkles:" src="https://assets-cdn.github.com/images/icons/emoji/unicode/2728.png" height="20" width="20"> <img class="emoji" title=":camel:" alt=":camel:" src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f42b.png" height="20" width="20"> <img class="emoji" title=":boom:" alt=":boom:" src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f4a5.png" height="20" width="20"></p>

</div>
</div>
klklk
