# Práctica 1: Resolución de sistemas de ecuaciones lineales

## 1) Sistema de ecuaciones no homogéneos

Resolver los siguientes sistemas de ecuaciones lineales no homogéneos y los sistemas homogéneos asociados en $\mathbb{R}$ o en $\mathbb{C}$. Si la solución es única, puede verificarse el resultado en Python utilizando el comando ```np. linalg . solve```.

$$(a)
\begin{cases}
x_1 + x_2 - 2x_3 + x_4 = -2 \\
3x_1 - 2x_2 + x_3 + 5x_4 = 3 \\
x_1 - x_2 + x_3 + 2x_4 = 2
\end{cases}$$

> 1. Lo escribimos en forma de matriz: 
>
> $$ \begin{bmatrix}
       1 & 1 & -2 & 1 & | & -2\\
       3 & -2 & 1 & 5 & | & 3\\
       1 & -1 & 1 & 2 & | & 2
     \end{bmatrix}$$
>
> 2. Triangulamos la matriz: 
> - La fila 2 le restamos 3 veces la fila 1, y la fila 3 le restamos la fila 1.
>
> $$ \begin{bmatrix}
       1 & 1 & -2 & 1 & | & -2\\
       0 & -5 & 7 & 2 & | & 9\\
       0 & -2 & 3 & 1 & | & 4
     \end{bmatrix}$$
>
> - Hacemos 0 el segundo coeficiente de la fila 3 con la fila 2. A la fila 3 le restamos la fila 2 por $\frac{2}{5}$
>
> $$ \begin{bmatrix}
       1 & 1 & -2 & 1 & | & -2\\
       0 & -5 & 7 & 2 & | & 9\\
       0 & 0 & \frac{1}{5} & \frac{1}{5} & | & \frac{2}{5}
     \end{bmatrix}$$
>
> - Multiplicamos la última fila por 5 para simplificar
>
> $$ \begin{bmatrix}
       1 & 1 & -2 & 1 & | & -2\\
       0 & -5 & 7 & 2 & | & 9\\
       0 & 0 & 1 & 1 & | & 2
     \end{bmatrix}$$
>
> De la última ecuación sale que:
>
> $$x_3 + x_4 = 2 \Rightarrow x_3 = 2 - x_4$$
>
> Reemplazamos en la segunda ecuación:
>
> $$-5x_2 + 7(2-x_4) + 2x_4 = 9$$
>
> $$-5x_2 + 14 - 5x_4 = 9$$
>
> $$x_2 = \frac{-5 + 5x_4}{-5} \Rightarrow x_2 = 1 - x_4$$
>
> Reemplazando en la primera ecuación:
>
> $$x_1 + ( -1 + x_4) - 2( 2 - x_4) + x_4 = -2 $$
>
> $$x_1 +4x_4 - 5 = -2 \Rightarrow x_1 = 3-4x_4$$
>
> Entonces el sistema de solución nos queda que:
>
>$$\begin{cases}
x_1 = 3- 4t \\
x_2 = 1 - t \\
x_3 = 2 - t \\
x_4 = t
\end{cases}$$
>
> Donde $t \in \mathbb{R}$ es im parámetro libre, eso significa que el conjunto de soluciones es una recta en el espacio de 4 dimensiones.

$$(b)
\begin{cases}
x_1 + x_2 + x_3 − 2x_4 + x_5 = 1 \\
x_1 − 3x_2 + x_3 + x_4 + x_5 = 0 \\
3x_1 − 5x_2 + 3x_3 + 3x_5 = 0 
\end{cases}
$$

> 1. Lo escribimos en forma de matriz:
>
> $$ \begin{bmatrix}
       1 & 1 & 1 & -2 & 1 & | & 1\\
       1 & -3 & 1 & 1 & 1 & | & 0\\
       3 & -5 & 3 & 0 & 3 &| & 0
     \end{bmatrix}
> $$
>
> 2. Triangulamos la matriz:
>
> - La fila 2 le restamos la fila 1 y a la fila 3 le restamos tres veces la fila 1
>
> $$ \begin{bmatrix}
       1 & 1 & 1 & -2 & 1 & | & 1\\
       0 & -4 & 0 & 3 & 0 & | & -1\\
       0 & -8 & 0 & 6 & 0 &| & -3
     \end{bmatrix}
> $$
>
> - La fila 3 le restamos dos veces la fila 2, se nos anula los coeficientes de la ecuación pero no el término idependiente:
>
> $$ \begin{bmatrix}
       1 & 1 & 1 & -2 & 1 & | & 1\\
       0 & -4 & 0 & 3 & 0 & | & -1\\
       0 & 0 & 0 & 0 & 0 &| & -1
     \end{bmatrix}
> $$
>
> Este es un sistema incopatible, por lo tanto no tiene solución.

$$(c)
\begin{cases}
i x_1 − (1 + i)x_2 = −1 \\
x_1 − 2x_2 + x_3 = 0 \\
x_1 + 2i x_2 − x_3 = 2i
\end{cases}
$$

> 1. Lo escribimos en forma de matriz:
>
> $$ \begin{bmatrix}
  i & -1-i & 0 & | & -1 \\
  1 & -2 & 1 & | & 0 \\
  1 & 2i & -1 & | & 2i
  \end{bmatrix} $$
>
> 2. Triangulamos: 
>
> - La fila 2 le restamos la fila 1 multiplicado por $-i$, lo mismo para la fila 3
>
> $$ \begin{bmatrix}
  i & -1-i & 0 & | & -1 \\
  0 & -2 - (i + i^2) & 1 & | & -i \\
  0 & 2i - (i + i^2) & -1 & | & i
  \end{bmatrix} $$
>
> $$ \begin{bmatrix}
  i & -1-i & 0 & | & -1 \\
  0 & -1 -i & 1 & | & -i \\
  0 & i + 1 & -1 & | & i
  \end{bmatrix} $$
>
> - A la fila 3 le restamos la fila 2 multiplicado $-1$, podemos ve que la tercera ecuación se anula, lo que significa que aporta información redundante.
>
> $$ \begin{bmatrix}
  i & -1-i & 0 & | & -1 \\
  0 & -1 -i & 1 & | & -i \\
  0 & 0 & 0 & | & 0
  \end{bmatrix} $$
>
> De la segunda ecuación obtenemos que:
>
> $$ (-1-i) x_2 + x_3 = -i \Rightarrow (-1-i) x_2 = -i - x_3$$
>
> Si reemplazamos $(-1-i) x_2$ en la primera ecuación nos queda que:
>
> $$ix_1 -i-x_3 = -1 \Rightarrow x_1 = \frac{-1 + i + x_3}{i}$$
>
> El sistema de soluciones nos queda:
>
>$$\begin{cases}
x_1 = \frac{-1 + i + x_3}{i} \\
x_2 = \frac{-i - x_3}{-1-i} \\
x_3 = t
\end{cases}$$


$$(d)
\begin{cases}
2x_1 + (−1 + i)x_2 + x_4 = 2 \\
−x_1 + 3x_2 − 3ix_3 + 5x_4 = 1
\end{cases}
$$

## 2) Determinar valores de $k$

a. Determinar los valores de $k \in \mathbb{R}$ para que el siguiente sistema tenga solución única, infinitas soluciones, o no tenga solución: 

$$\begin{cases}
x_1 + kx_2 − x_3 = 1 \\
−x_1 + x_2 + k^2x_3 = −1 \\
x_1 + kx_2 + (k − 2)x_3 = 2
\end{cases}$$

> Lo escribimos en forma de matriz y triangulamos:
>
> $$ A = \begin{bmatrix}
  1 & k & -1 & | & 1 \\
  -1 & 1 & k^2 & | & -1 \\
  1 & k & k-2 & | & 2
  \end{bmatrix} $$
>
> Aplicamos $f_2 + f_1$ y $f_3 - f_1$:
>
> $$ A = \begin{bmatrix}
  1 & k & -1 & | & 1 \\
  0 & 1+k & k^2-1 & | & 0 \\
  0 & 0 & k-1 & | & 1
  \end{bmatrix} $$
>
> - De la última ecuación podemos sacar que si $k = 1$ el sistema no tendría solución pues quedaria una fila en $0$ igualado a algo distinto a $0$.
> 
> El determinante de la matriz nos da información, si $det(A) \neq 0$ entonces el sistema tiene solucion único.
>
> En nuestro caso tenemos:
>
> $$ A = \begin{bmatrix}
  1 & k & -1 \\
  0 & 1+k & k^2-1 \\
  0 & 0 & k-1 \\
  \end{bmatrix} $$
>
> $$det(A) = (1+k)(k-1) - [(k^2-1)*0] = k^2-1$$
>
> Queremos que $k^2-1 \neq 0 \Rightarrow k \neq \pm 1$
>
> - Como vimos que si $k=1$ el sistema no tiene solución, si $k=-1$ la segunda fila se anula, pero como el otro lado del igual también es $0$, nos dice que sería una ecuación redundante, lo que nos quedaría un sistema de 2 ecuaciones con 3 incógnitas, es decir que tendría infinitas soluciones.
> - Y finalmente como solución única serían todos los $k \neq \pm 1$

b. Considerar el sistema homogéneo asociado y dar los valores de $k$ para los cuales admite solución no trivial. Para esos $k$, resolverlo.

> Como el sistema es homogéneo, todo lo que esta a la derecha del igual es 0.
>
> Si $k=1$:
>
> $$ A = \begin{bmatrix}
  1 & 1 & -1 & | & 0 \\
  0 & 2 & 0 & | & 0 \\
  0 & 0 & 0 & | & 0
  \end{bmatrix} $$
>
> - De la segunda ecuación sale que $x_2 = 0$
> - De la primera tenemos que $x_1 + 0 -x_3 = 0 \Rightarrow x_1 = x_3$
>
> $$(x_1,x_2,x_3)=t(1,0,1), t \in \mathbb{R}$$

> Si $k=-1$
>
> $$ A = \begin{bmatrix}
  1 & -1 & -1 & | & 0 \\
  0 & 0 & 0 & | & 0 \\
  0 & 0 & -2 & | & 0
  \end{bmatrix} $$
>
> - De la tercera ecuación sale que $x_3 = 0$
> - De la primera tenemos que $x_1 - x_2 + 0 = 0 \Rightarrow x_1 = x_2$
>
> $$(x_1,x_2,x_3)=t(1,1,0), t \in \mathbb{R}$$

## 4) Encontrar coeficientes

Encontrar los coeficientes de la parábola $y = ax^2 + bx + c$ que pasa por los puntos $(1, 1), (2, 2)$ y $(3, 0)$. Verificar el resultado obtenido usando Python. Graficar los puntos y la parábola aprovechando el siguiente código:

```python
import numpy as np
import matplotlib.pyplot as plt #libreria para graficar
# . . .
# Aca , crear la matriz y resolver el sistema para calcular a, b y c .
# . . .
xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])
x = np.linspace(0, 4, 100) #genera 100 puntos equiespaciados entre 0 y 4.
f = lambda t: a∗t∗∗2+b∗t+c #esto genera una funcion f de t .
plt.plot (xx, yy, ’∗’)
plt.plot (x , f(x))
plt.show ()
```
> Para encontrar los coeficientes de la parábola tenemos que evaluar en los puntos que nos dan, como nos dan 3 puntos, nos quedará un sistema de tres ecuaciones con tres incógnitas.
>
> - Para el punto $(1, 1)$: nos queda $1 = a + b + c$
> - Para el punto $(2, 2)$: nos queda $2 = 4a + 2b+c$
> - Para el punto $(3, 0)$: nos queda $0 = 9a + 3b + c$
>
> Lo escribimos como matriz y triangulamos:
>
> $$ \begin{bmatrix}
  1 & 1 & 1 & | & 1 \\
  4 & 2 & 1 & | & 2 \\
  9 & 3 & 1 & | & 0
  \end{bmatrix} $$
>
> Hacemos $f_2 - 4f_1$ y $f_3 - 9f_1$
>
> $$ \begin{bmatrix}
  1 & 1 & 1 & | & 1 \\
  0 & -2 & -3 & | & -2 \\
  0 & -6 & -8 & | & -9
  \end{bmatrix} $$
>
> Hacemos $f_3 - 3f_2$
>
> $$ \begin{bmatrix}
  1 & 1 & 1 & | & 1 \\
  0 & -2 & -3 & | & -2 \\
  0 & 0 & 1 & | & -3
  \end{bmatrix} $$
>
> - De la tercera ecuación obtenemos que $c = -3$
> - De la segunda tenemos que $-2b + 9 = -2 \Rightarrow b = \frac{11}{2}$
> - De la primera ecuación tenemos que $a + \frac{11}{2} - 3 = 1 \Rightarrow a = -\frac{5}{2}$

> En el archivo [practica1.ipynb](/Guias-Ejercicios/Practica1/practica1.ipynb) está verificado el resultado, me da lo mismo :)

## 5) Encontrar sistema de generadores

Encontrar un sistema de generadores para los siguientes espacios vectoriales:

1. $\{ (x, y, z) \in \mathbb{R}^3: x+y-z=0; x-y=0 \} $  

> Intento despejar las ecuaciones que pueda:
>
> - De $x-y = 0 \Rightarrow x = y = \frac{z}{2}$
> - Reemplazamos en la primera: $y + y -z = 0 \Rightarrow y = \frac{z}{2}$
>
> De solución nos queda que: $(x, y, z) = (\frac{z}{2}, \frac{z}{2}, z) = z(\frac{1}{2}, \frac{1}{2}, 1) \Rightarrow S = \langle(\frac{1}{2}, \frac{1}{2}, 1)\rangle$ 

2. $\{ A \in \mathbb{C}^{3 \times 3}: A = -A^{t} \}$

>  Supongamos que tenemos la siguiente matriz:
>
> $$ A = \begin{bmatrix}
  a & b & c \\
  d & e & f \\
  g & h & i
  \end{bmatrix} $$
>
> La matriz traspuesta de $-A$ es poner su columna como filas
>
> $$-A^t = \begin{bmatrix} 
-a & -d & -g \\ 
-b & -e & -h \\  
-c & -f & -i  
\end{bmatrix}$$
>
> Luego la consigna nos pide que:
>
> $$A = -A^t \Rightarrow \begin{bmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i
\end{bmatrix} = 
\begin{bmatrix} 
-a & -d & -g \\ 
-b & -e & -h \\  
-c & -f & -i  
\end{bmatrix}$$
>
> - Notamos que en la diagonal nos queda que $a = -a \Rightarrow a = 0$, y así lo mismo para todos los elementos.
> - Si igualamos la parte de la diagonal inferior izquierda de la matriz nos queda los mismos elementos de la diagonal superior derecha pero opuestos.
>
> Nos queda algo como:
>
> $$ \begin{bmatrix} 
0 & b & c \\ 
-b & 0 & f \\  
-c & -f & 0  
\end{bmatrix} = b * 
\begin{bmatrix} 
0 & 1 & 0 \\ 
-1 & 0 & 0 \\  
0 & 0 & 0  
\end{bmatrix} + c * 
\begin{bmatrix} 
0 & 0 & 1 \\ 
0 & 0 & 0 \\  
-1 & 0 & 0  
\end{bmatrix} + f * 
\begin{bmatrix} 
0 & 0 & 0 \\ 
0 & 0 & 1 \\  
0 & -1 & 0  
\end{bmatrix}$$
>
> Entonces los generadores son las matrices que quedan multiplicando:
>
> $$Sol = \begin{bmatrix} 
0 & 1 & 0 \\ 
-1 & 0 & 0 \\  
0 & 0 & 0  
\end{bmatrix},  
\begin{bmatrix} 
0 & 0 & 1 \\ 
0 & 0 & 0 \\  
-1 & 0 & 0  
\end{bmatrix}, 
\begin{bmatrix} 
0 & 0 & 0 \\ 
0 & 0 & 1 \\  
0 & -1 & 0  
\end{bmatrix}$$

3. $\{ A \in \mathbb{C}^{3 \times 3}: tr(A) = 0 \}$

>  Supongamos que tenemos la siguiente matriz:
>
> $$ A = \begin{bmatrix}
  a & b & c \\
  d & e & f \\
  g & h & i
  \end{bmatrix} $$
>
> Emm solo sé que $a+e+i = 0$ ... Help

4. $\{ x \in \mathbb{C}^4: x_1 + x_2 - ix_4 = 0, ix_1+ (1+i)x_2-x_3=0 \} $
	
> Intento despejar las ecuaciones que pueda:
>
> - De la primera ecuación despejo: $x_1 + x_2 - ix_4 = 0 \Rightarrow x_1 = ix_4 - x_2$ 
> - Reemplazo en la otra ecuación: $i(ix_4 - x2)+ (1+i)x_2-x_3=0 \Rightarrow x_3 = -x_4 + x_2$
>
> De solución nos queda que $(x_1, x_2, x_3, x_4) = (ix_4 - x_2, x_2, -x_4 + x_2, x_4) = x_2(-1, 1, 1, 0) + x_4(i, 0, -1, 1) \Rightarrow S = \langle (-1, 1, 1, 0),(i, 0, -1, 1)\rangle$

## 6) Conversiones de generadores

Sea $S = \langle (1,−1, 2, 1), (3, 1, 0,−1), (1, 1,−1,−1)\rangle \subseteq \mathbb{R}^4$.

1. Determinar si $(2, 1, 3, 5) \in S$

> Para determinarlo podemos escribir $S$ pasandolo a ecuaciones y ver si el vector $(2, 1, 3, 5)$ satisface ese sistema de ecuaciones.
>
> Verificamos si existe una combinación lineal para $S$:
>
> $$(x_1, x_2, x_3, x_4) = \lambda_{1}(1,−1, 2, 1) + \lambda_{2}(3, 1, 0,−1) + \lambda_{3}(1, 1,−1,−1) = (2, 1, 3, 5)$$
>
> Nos queda el siguiente sistema de ecuaciones:
>
>$$S=\begin{cases} 
\lambda_1 + 3\lambda_2 + \lambda_3 = 2 \\ 
-\lambda_1 + \lambda_2 + \lambda_3 = 1 \\ 
2\lambda_1 - \lambda_3 = 3 \\ 
\lambda_1 - \lambda_2 - \lambda_3 = 5 
\end{cases}$$
>
> Ahora toca representarlo como matriz y resolver el sistema triangulando:
>
> $$ \begin{bmatrix} 
1 & 3 & 1 & | & 2 \\ 
-1 & 1 & 1 & | & 1 \\
2 & 0 & -1 & | & 3 \\ 
1 & -1 & -1 & | & 5
\end{bmatrix} $$
>
> - Hacemos: $f_2+f_1, f_3-2f_1, f_4-f_1 $
>
> $$ \begin{bmatrix} 
1 & 3 & 1 & | & 2 \\ 
0 & 4 & 2 & | & 3 \\
0 & -6 & -3 & | & -1 \\ 
0 & -4 & -2 & | & 3
\end{bmatrix} $$
>
> - Si hacemos $f_4 + f_2$ nos queda:
>
> $$ \begin{bmatrix} 
1 & 3 & 1 & | & 2 \\ 
0 & 4 & 2 & | & 3 \\
0 & -6 & -3 & | & -1 \\ 
0 & 0 & 0 & | & 6
\end{bmatrix} $$
>
> La última fila nos queda una inconsistencia, por lo tanto concluimos que $(2, 1, 3, 5) \notin S$

2. Determinar si $T = \{ x \in \mathbb{R}^4/x_1 − x_2 − x_3 = 0 \} \subseteq S$.

> Si $T \subseteq S$ quiere decir que cualquier vector que satisface $T$ debe poder expresarse como combinación lineal de los vectores de $S$. De la ecuación de $T$ sale que $x_1=x_2+x_3$ entonces tenemos que $(x_2 + x_3, x_2, x_3, x_4) = x_2(1, 1, 0, 0) + x_3(1, 0, 1, 0) + x_4(0, 0, 0, 1)$ donde forman un conjunto de vectores que es una base para $T$.
>
> Si queremos ver que el subespacio de $T \subseteq S$, los vectores de la base de $T$ tienen que escribirse como combinación lineal de $S$. Así que planteo el sistema de ecuaciones poniendo los vectores de $S$ como columna, asociando a la base de $T$ y los resuelvo para los tres vectores a la vez.
>
> $$ \begin{bmatrix} 
1 & 3 & 1 & | & 1 & 1 & 0\\ 
-1 & 1 & 1 & | & 1 & 0 & 0\\
2 & 0 & -1 & | & 0 & 1 & 0\\ 
1 & -1 & -1 & | & 0 & 0 & 1
\end{bmatrix}  \Rightarrow f_2+f_1, f_3-2f_1, f_4-f_1 
\begin{bmatrix} 
1 & 3 & 1 & | & 1 & 1 & 0\\ 
0 & 4 & 2 & | & 2 & 1 & 0\\
0 & -6 & -3 & | & -2 & -1 & 0\\ 
0 & -4 & -2 & | & -1 & -1 & 1
\end{bmatrix} $$
>
>$$\Rightarrow f_4 + f_2
\begin{bmatrix} 
1 & 3 & 1 & | & 1 & 1 & 0\\ 
0 & 4 & 2 & | & 2 & 1 & 0\\
0 & -6 & -3 & | & -2 & -1 & 0\\ 
0 & 0 & 0 & | & 1 & 1 & 1
\end{bmatrix}
$$ 
>
> Como la última ecuación da una inconsistencia, no tenemos solución para el sistema de ecuaciónes, por lo tanto no se puede expresar a $T$ como combinación lineal de $S$, luego $T \subsetneq S$

3. Determinar si $S \subseteq \{x \in \mathbb{R}^4/x_1 − x_2 − x_3 = 0 \}$.

> Acá es al revés del ejercicio anterior, si quiero ver que $S \subseteq T$ quiere decir que cualquier vector que satisface $S$ se puede escribir como combinación lineal de $T$. Aprovechando las cuentas anteriores planteo el matriz asociado al sistema de ecuaciones de $T$ junto a los vectores de $S$.
>
> $$ \begin{bmatrix} 
1 & 1 & 0 & | & 1 & 3 & 1 \\ 
1 & 0 & 0 & | & -1 & 1 & 1 \\
0 & 1 & 0 & | & 2 & 0 & -1 \\ 
0 & 0 & 1 & | & 1 & -1 & -1
\end{bmatrix} \Rightarrow f_2 - f_1 
\begin{bmatrix} 
1 & 1 & 0 & | & 1 & 3 & 1 \\ 
0 & -1 & 0 & | & -2 & -2 & 0 \\
0 & 1 & 0 & | & 2 & 0 & -1 \\ 
0 & 0 & 1 & | & 1 & -1 & -1
\end{bmatrix} \Rightarrow f_3+f_2
\begin{bmatrix} 
1 & 1 & 0 & | & 1 & 3 & 1 \\ 
0 & -1 & 0 & | & -2 & -2 & 0 \\
0 & 0 & 0 & | & 0 & -2 & -1 \\ 
0 & 0 & 1 & | & 1 & -1 & -1
\end{bmatrix}$$
>
> Como la terceraa ecuación da una inconsistencia, no tenemos solución para el sistema de ecuaciónes, por lo tanto no se puede expresar a $S$ como combinación lineal de $T$, luego $S \subsetneq T$

## 7) Cuentas con generadores

Hallar un sistema de generadores para $S \cap T$ y para $S + T$ como subespacios de $V$, y determinar si la suma es directa en cada uno de los siguientes casos:

1. $V = \mathbb{R}^3, S = \{(x, y, z) : 3x − 2y + z = 0\} \text{ y } T = \{(x, y, z) : x + z = 0 \}$

> - $S \cap T$: como están dado por ecuaciones, la intersección es que se cumplan ambas formulas. De la fórmula en $T$ obtenemos que $x = -z$. Reemplazando en la otra tenemos que $-3z-2y+z = 0 \Rightarrow y = -z$. Entonces nos queda que $(x, y, z) = z(-1,-1,1) \Rightarrow sol=\langle (-1,-1,1) \rangle$
> - $S+T$: los pasamos a generadores y los apilamos en la solución. En este caso es suma directa.
>
> $$S = (x, y, 2y-3x) = x(1, 0, -3) + y(0, 1, 2) = \langle (1,0,-3), (0,1,2) \rangle$$
>
> $$T = (-z, y, z) = y(0,1,0) + z(-1,0,1) = \langle (0,1,0), (-1,0,1) \rangle$$
>
> $$S+T = \langle (1,0,-3), (0,1,2), (0,1,0), (-1,0,1) \rangle$$
>

2. $V = \mathbb{R}^3, S = \{(x, y, z) : 3x − 2y + z = 0, x − y = 0\} \text{ y } T = \langle (1, 1, 0), (5, 7, 3)\rangle$

> - $S \cap T$: escribo los generadores como combinación lineal, en este caso tengo
>
> $$t \in T \Rightarrow t = \alpha(1,1,0) + \beta(5,7,3) = (\alpha + 5 \beta, \alpha + 7 \beta, 3 \beta)= (x, y ,z)$$
>
> $$\text{Despejando las ecuaciones de }S \text{ nos queda: } 3y-2y+z = 0 \Rightarrow y + z = 0$$
>
> $$\text{Le pido que } t \text{ esté en }S \Rightarrow y+z = 0 \Rightarrow \alpha+ 7 \beta + 3 \beta = 0 \Rightarrow \alpha = -10\beta$$
>
> $$\Rightarrow t = ( -10\beta + 5 \beta,  -10\beta + 7 \beta, 3 \beta) = (-5 \beta, -3\beta, 3 \beta) = \beta (-5,-3,3) \Rightarrow S \cap T = \langle (-5,-3,3) \rangle$$
>
> - $S + T$: paso $S$ a generadores, de la operaciónes anteriores sale que $x = y$ y luego que $z = -y$. La suma nos queda directo.
>
> $$S = \langle (1,1,-1) \rangle \Rightarrow S + T = \langle (1,1,-1), (1, 1, 0), (5, 7, 3)\rangle$$

3. $V = \mathbb{R}^3, S = \langle(1, 1, 3), (1, 3, 5), (6, 12, 24)\rangle, T = \langle(1, 1, 0), (3, 2, 1)\rangle$

> - $S+T$: aprovecho que están ambos con generadores, y que $(6,12,24)=6(1,2,4)$ así que son equivalentes. Puede que tenga info redundante, no importa, la suma es esa.
>
> $$S+T = \langle (1, 1, 3), (1, 3, 5), (1, 2, 4), (1, 1, 0), (3, 2, 1)\rangle$$
>
> - $S \cap T$: para calcular esto puedo escribirlo como combinación lineal de los generadores de ambas ecuaciones, por lo que debemos encontrar las solciones de
>
> $$\alpha_1 (1,1,3) + \alpha_2 (1,3,5) + \alpha_3 (1,2,4) = \beta_1 (1,1,0) + \beta_2 (3,2,1)$$
>
> $$\alpha_1 (1,1,3) + \alpha_2 (1,3,5) + \alpha_3 (1,2,4) - \beta_1 (1,1,0) - \beta_2 (3,2,1) = 0$$
>
> $$\begin{bmatrix} 
1 & 1 & 1 & -1 & -3 & | & 0 \\ 
1 & 3 & 2 & -1 & -2 & | & 0 \\
3 & 5 & 4 & 0 & -1 & | & 0 
\end{bmatrix} \Rightarrow f_2 - f_1, f_3 - 3f_1
\begin{bmatrix} 
1 & 1 & 1 & -1 & -3 & | & 0 \\ 
0 & 2 & 1 & 0 & 1 & | & 0 \\
0 & 2 & 4 & 1 & 8 & | & 0 
\end{bmatrix} \Rightarrow f_3-f_2
\begin{bmatrix} 
1 & 1 & 1 & -1 & -3 & | & 0 \\ 
0 & 2 & 1 & 0 & 1 & | & 0 \\
0 & 0 & 3 & 1 & 7 & | & 0 
\end{bmatrix}$$
>
> 1. De la tercera ecuación obtenemos que $3\alpha_3 + \beta_1 + 7\beta_2 = 0 \Rightarrow \beta_1 = -3\alpha_1-7\beta_2$
> 2. De la segunda ecuación obtenemos que $2\alpha_2 + \alpha_3 + \beta_2 = 0 \Rightarrow \alpha_3 = -\beta_2 - 2\alpha_2 \Rightarrow \alpha_3 = 5\beta_2 + 8\alpha_1$
> 3. Reemplazando en la primera ecuación tenemos que $\alpha_1 +\alpha_2 + (-\beta_2 - 2\alpha_2)-(-3\alpha_1-7\beta_2) -3\beta_2 = 4\alpha_1-\alpha_2 + 3\beta_2 = 0 \Rightarrow \alpha_2 = -4\alpha_1-3\beta_2$
>
>     Reemplazamos las expresiones obtenidas en:
>
> $$v =\alpha_1 (1,1,3) + \alpha_2 (1,3,5) + \alpha_3 (1,2,4) = \beta_1 (1,1,0) + \beta_2 (3,2,1)$$
>
> $$v = \alpha_1 (1,1,3) + (-4\alpha_1-3\beta_2) (1,3,5) + (5\beta_2 + 8\alpha_1) (1,2,4) = (-3\alpha_1-7\beta_2) (1,1,0) +  \beta_2 (3,2,1)$$
>
> Muchas cuentas uwu

4. $V = \mathbb{R}^{3 \times 3}, S = \{(x_{ij}) / x_{ij} = x_{ji} \forall i, j\}, T = \{(x_{ij}) / x_{11} + x_{12} + x_{13} = 0\}$
5. $V = \mathbb{C}^3, S = \langle (i, 1, 3 − i), (4, 1 − i, 0) \rangle, T = \{x ∈ \mathbb{C}^3 : (1 − i)x_1 − 4x_2 + x_3 = 0\}$