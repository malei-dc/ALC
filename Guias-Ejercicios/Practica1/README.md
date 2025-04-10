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

## 8) Buscar k

Determinar todos los $k \in \mathbb{R}$ para los cuales:

1. $\langle(−2, 1, 6), (3, 0,−8)\rangle = \langle(1, k, 2k), (−1,−1, k^2 − 2), (1, 1, k)\rangle$

> Hay una igualdad de subespacios, lo que significa que la dimensión tienen que coincidir, en el subespacio de la derecha se ve que es LI, ya que si hacemos $2f_2 + 3f_1$ la segunda fila nos queda que $(0, 3, 2)$ confirmando mi afirmación. Entonces como es de dimensión 2 el otro subespacio también tiene que tener la misma dimensión. Ubicamos los vectores en fila y triangulo (se nos tiene que anular una fila):
>
> $$\begin{bmatrix} 
1 & k & 2k \\ 
-1 & -1 & k^2-2 \\
1 & 1 & k 
\end{bmatrix} \Rightarrow f_3+f_2
\begin{bmatrix} 
1 & k & 2k \\ 
-1 & -1 & k^2-2 \\
0 & 0 & k^2+k-2 
\end{bmatrix}$$
>
> Si factorizamos el polinomio que nos queda en la segunda fila:
>
> $$k^2+k-2 = (k+2)(k-1)$$
>
> Queda claro que el polinomio se anula en sus raices, en este caso son $k = 1 \land k = -2$. Nos queda que:
>
> $$\langle(−2, 1, 6), (3, 0,−8)\rangle =
\begin{cases}
\langle(1, 1, 2), (−1,−1, -1), (1, 1, 1)\rangle = \langle(1, 1, 2), (1, 1, 1)\rangle & \text { si } k = 1   \\
\langle(1, -2, -4), (−1,−1, 2), (1, 1, -2)\rangle = \langle(1, -2, -4), (1, 1, -2)\rangle & \text { si } k = -2
\end{cases}$$
>
> Que un subespacio sea igual que otra quiere decir que se puede escribir como combinación lineal de la otra. Entonces pongo cada vector como columnas de ambos subespacios y triangulo para ver que sucede:
>
> - Caso $k = 1:$
>
> $$\begin{bmatrix} 
-2 & 3 & | & 1 & 1\\ 
1 & 0 & | & 1 & 1 \\
6 & -8 & | & 2 & 1 
\end{bmatrix} \Rightarrow f_1 * \frac{1}{2} 
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
1 & 0 & | & 1 & 1 \\
6 & -8 & | & 2 & 1 
\end{bmatrix} \Rightarrow f_2 + f_1, f_3+6f_1
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
0 & 3/2 & | & 3/2 & 3/2 \\
0 & 1 & | & 5 & 4 
\end{bmatrix} \Rightarrow f_2 * \frac{2}{3}
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
0 & 1 & | & 1 & 1 \\
0 & 1 & | & 5 & 4 
\end{bmatrix}$$
>
>$$\Rightarrow f_3-f_2
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
0 & 1 & | & 1 & 1 \\
0 & 0 & | & 4 & 3 
\end{bmatrix}$$
> 
> La tercera fila representa la ecuacion $4x_1 + 3x_2 =0$, la triangulación me dio que es inconsistente, si hubiese $0 = 0$ tendriamos una dependencia lineal y los subespacio serían iguales, puedo concluir que no son iguales con esto? PREGUNTAR! Si, que no hayan dando que son dependiente linealmente es que existe una dirección que no está representado con los vectores de la igualdad, por lo tanto no son iguales.
>
> - Caso $k = -2$
>
> $$\begin{bmatrix} 
-2 & 3 & | & 1 & 1\\ 
1 & 0 & | & -2 & 1 \\
6 & -8 & | & -4 & -2 
\end{bmatrix} \Rightarrow f_1 * \frac{1}{2} 
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
1 & 0 & | & -2 & 1 \\
6 & -8 & | & -4 & -2 
\end{bmatrix} \Rightarrow f_2 + f_1, f_3+6f_1
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
0 & 3/2 & | & -3/2 & 3/2 \\
0 & 1 & | & -1 & 1 
\end{bmatrix} \Rightarrow f_2 * \frac{2}{3}
\begin{bmatrix} 
-1 & 3/2 & | & 1/2 & 1/2\\ 
0 & 1 & | & -1 & 1 \\
0 & 1 & | & -1 & 1 
\end{bmatrix}$$
>
> Observamos que las dos últimas filas son iguales, lo que indica que hay una fila redundante, sugiere que el sistema es compatible y dependiente. Esto confirma que los dos conjuntos de vectores generan subespacios de la misma dimensión y que los generadores del segundo conjunto pueden expresarse como combinaciones lineales de los del primero.
>
> Cumple para $k = -2$

2. $S \cap T = \langle(0, 1, 1)\rangle \text{ siendo } S = \{x \in \mathbb{R} : x_1 + x_2 − x_3 = 0 \} \text{ y } T = \langle(1, k, 2), (−1, 2, k)\rangle$

> Para que $(0, 1, 1) \in T$ tiene que tener solución, así que lo esctibimos como matriz y triangulamos:
>
> $$\begin{bmatrix} 
1 & -1 & | & 0\\ 
k & 2 & | & 1 \\
2 & k & | & 1 
\end{bmatrix} \Rightarrow f_2 - kf_1 \text{ con } k \neq 0, f_3 - 2f_1
\begin{bmatrix} 
1 & -1 & | & 0\\ 
0 & 2 +k & | & 1 \\
0 & k+2 & | & 1 
\end{bmatrix}$$
>
> La ultima fila se me anula, entonces el sistema queda compatible si $k \neq -2$, y para el caso de $k=0$ veamos:
>
> $$\begin{bmatrix} 
1 & -1 & | & 0\\ 
0 & 2 & | & 1 \\
2 & 0 & | & 1 
\end{bmatrix} \Rightarrow f_3 - 2f_2
\begin{bmatrix} 
1 & -1 & | & 0\\ 
0 & 2 & | & 1 \\
0 & 2 & | & 1 
\end{bmatrix}$$
>
> Tambien nos queda que es compatible, por lo tanto $(0, 1, 1) \in T$ si $k \neq -2$

## 9) La unión no genera un subespacio, pero...

Sean $S$ y $T$ subespacios de un $K$-espacio vectorial $V$ . Probar que $S \cup T$ es un subespacio de $V \Leftrightarrow  S \subseteq T$ o $T \subseteq S$.

> - $\Leftarrow)$ si $S \subseteq T$ o $T \subseteq S$, entonces $S \cup T$ es un subespacio:
>
>   - Si $S \subseteq T$ entonces $S \cup T = T$ ya que todos los elementos de $S$ están en $T$ y sabemos por hipótesis que $T$ es subespacio.
>   - Si $T \subseteq S$ entonces $S \cup T = S$ ya que todos los elementos de $T$ están en $S$ y sabemos por hipótesis que $S$ es subespacio.
>
>   En ambos casos la unión es igual a uno de los subespacios, por lo tanto se cumple.
>
> - $\Rightarrow)$ Suponemos que $S \cup T$ es un subespacio de $V$ y queremos probar que entonces $S \subseteq T$ o $T \subseteq S$.
>
>   Lo vamos a probar por el absurdo: supongamos que ninguno está contenido dentro del otro. Entonces existen 
>
>   - $s \in S - T$
>   - $t \in T - S$
>
>   Como $S \cup T$ es un subespacio debe ser cerrado bajo la suma y el producto por escalar, pero centremonos en la suma, por eso tenemos que $s+t \in S \cup T$, lo que no da dos posible casos:
>
>   1. Caso 1: $s+t \in S$:
>
>       Entonces $s+t \in S$, como tambien sabemos que $s \in S$ podemos restarlo $(s+t)-s = t \in S$, **ABS!** pues $t \notin S$
>
>   2. Caso 2: $s+t \in T$:
>
>       Entonces $s+t \in T$, como tambien sabemos que $t \in T$ podemos restarlo $(s+t)-t = s \in T$, **ABS!** pues $s \notin T$
>
> Ambos casos nos llevaron al absurdo por lo tanto se debe cumplir que $S \subseteq T$ o $T \subseteq S$. La idea que nos da esto es que para que una unión de dos subespacios resulte en subespacio del mismo $V$ es necesario que uno de los dos subespacio esté contenido en otra.

## 10) Indepedencia lineal

Decidir si los siguientes conjuntos son linealmente independientes sobre $K$. Cuando no lo sean, escribir a uno de ellos como combinación lineal de los otros.

1. {(1, 4,−1, 3) , (2, 1,−3,−1) , (0, 2, 1,−5)} en $\mathbb{R}^4$, para $K = \mathbb{R}$.

> Tenemos que ver indepedencia linea, ponemos los vectores en linea y triangulamos.
>
> $$\begin{bmatrix} 
1 & 4 & -1 & 3\\ 
2 & 1 & -3 & -1 \\
0 & 2 & 1 & -5 
\end{bmatrix} \Rightarrow f_2 - 2f_1
\begin{bmatrix} 
1 & 4 & -1 & 3\\ 
0 & -7 & -1 & -7 \\
0 & 2 & 1 & -5 
\end{bmatrix} \Rightarrow \frac{1}{7}f_2
\begin{bmatrix} 
1 & 4 & -1 & 3\\ 
0 & -1 & -1/7 & -1 \\
0 & 2 & 1 & -5 
\end{bmatrix}$$
>
> $$\Rightarrow f_3+2f_2 \begin{bmatrix} 
1 & 4 & -1 & 3\\ 
0 & -1 & -1/7 & -1 \\
0 & 0 & 5/7 & -7 
\end{bmatrix}$$
>
> Quedó triangulado, no se anuló ninguna fila, es LI

2. {(1 − i, i) , (2,−1 + i)} en $\mathbb{C}^2$, para $K = \mathbb{C}$.

> Hacemos lo mismo:
>
> $$\begin{bmatrix} 
1 -i & i \\ 
2 & -1 + i 
\end{bmatrix} \Rightarrow f_2 - (1+i)f_1
\begin{bmatrix} 
1 -i & i \\ 
0 & 0 
\end{bmatrix}$$
>
> Calculos Aux: 
>
> - Necesito que $f_2 - \alpha f_1 \rightarrow f_2$ para que se anule la fila 2, propongo $\alpha = \frac{2}{1-i}$ y racionalizo
>
> $$\alpha = \frac{2}{1-i}. \frac{1+i}{1+i} = \frac{2(1+i)}{2} = 1+i$$
>
> Se nos anula una fila, por lo tanto son linealmente dependientes, la segunda fila se escribe como combinación lineal con respecto a la primera de la forma:
>
> $$(2, -1+i) = (1+i) * (1-i, i)$$

## 11) Extracción de bases

Extraer una base de $S$ de cada uno de los siguientes sistemas de generadores y hallar la dimensión de $S$. Extender la base de $S$ a una base del espacio vectorial correspondiente.

1. $S = \langle(1, 1, 2), (1, 3, 5), (1, 1, 4), (5, 1, 1)\rangle \subseteq \mathbb{R}^3, K = \mathbb{R}$

> Para que un sistema de generadores sea una base necesita cumplir dos cosas:
>
> - Que los vectores sean LI
> - Que generen todo el espacio vectorial al que pertenece. (en este caso $\mathbb{R}^3$)
>
> A simple vista vemos que tenemos 4 vectores para generar $\mathbb{R}^3$ donde sabemos que alcanza con 3, entonces intuyo que sobra un vector. Vemos la indepedencia lineal poniendo los vectores en filas y triangulando:
>
>$$\begin{bmatrix} 
1 & 1 & 2 \\
1 & 3 & 5 \\
1 & 1 & 4 \\
5 & 1 & 1
\end{bmatrix} \Rightarrow f_2-f_1, f_3-f_1, f_4-5f_1 
\begin{bmatrix} 
1 & 1 & 2 \\
0 & 2 & 3 \\
0 & 0 & 2 \\
0 & -4 & -9
\end{bmatrix} \Rightarrow f_4+2f_2
\begin{bmatrix} 
1 & 1 & 2 \\
0 & 2 & 3 \\
0 & 0 & 2 \\
0 & 0 & -3
\end{bmatrix} \Rightarrow f_4 * 2$$
>
> $$\begin{bmatrix} 
1 & 1 & 2 \\
0 & 2 & 3 \\
0 & 0 & 2 \\
0 & 0 & -6
\end{bmatrix} \Rightarrow f_4 + 3f_3
\begin{bmatrix} 
1 & 1 & 2 \\
0 & 2 & 3 \\
0 & 0 & 2 \\
0 & 0 & 0
\end{bmatrix}$$
>
> Se nos anuló la cuarta fila, lo que significa que se puede escribir como combinación lineal con respecto a las primeras 3. Así que para formar una base elegimos los 3 primeros.
>
> $$S = \langle (1, 1, 2), (1, 3, 5), (1, 1, 4) \rangle$$ 
>
> En este caso no es necesario extender la base ya que estamos en $\mathbb{R}^3$ y tenemos 3 vectores LI que son base.

2. $S = \langle(1, 1, 1, 1), (0, i, 1, 1), (0, i, 0, 0), (1, 1, 0, 0)\rangle \subseteq \mathbb{C}^{2 \times 2}, K = \mathbb{C}$

> No escribí los vectores en forma de matriz $2\times 2$ pero es análogo, me facilita para triangular y checkear independencia lineal.
>
> Hacemos lo mismo:
>
> $$\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & i & 1 & 1 \\
0 & i & 0 & 0 \\
1 & 1 & 0 & 0
\end{bmatrix} \Rightarrow f_4 - f_1 
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & i & 1 & 1 \\
0 & i & 0 & 0 \\
0 & 0 & -1 & -1
\end{bmatrix} \Rightarrow f_3 - f_2 
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & i & 1 & 1 \\
0 & 0 & -1 & -1 \\
0 & 0 & -1 & -1
\end{bmatrix}$$ 
>
> $$\Rightarrow
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & i & 1 & 1 \\
0 & 0 & -1 & -1 \\
0 & 0 & 0 & 0
\end{bmatrix}$$
>
> Nos quedó 3 vectores LI, pero para generar todo el espacio vectorial de $2 \times 2$ necesito 4 vectores, agrego uno que sea LI con los anteriores, por ejemplo uso $(0,0,0,1)$ para extender la base.
>
>  $$S = \langle (1, 1, 1, 1), (0, i, 1, 1), (0, i, 0, 0), (0, 0, 0, 1) \rangle$$ 

## 12) Independencia lineal en distintos cuerpos

Sean $v_1, . . . , v_k \in \mathbb{R}^n$. Probar que { $v_1, . . . , v_k$ } es L.I. sobre $\mathbb{R} \Leftrightarrow$  { $v_1, . . . , v_k$ } es L.I. sobre $\mathbb{C}$.

> - $\Rightarrow )$ Si son L.I. en $\mathbb{R}$, entonces son L.I. en $\mathbb{C}$
>
>   Que sea Linealmente independientes quiere decir que:
>
>   $$\sum_{i=1}^k \alpha_i v_i = 0 \Rightarrow v_1,...,v_k = 0$$
>
>   Supongamos que tenemos $z_1 v_1+...+z_k v_z = 0$ con $z_i \in \mathbb{C}$. Escribimos cada $z_i = a_i + b_i i$ con $a_i, b_i \in \mathbb{R}$. Entonces:
>
>   $$\sum_{i=1}^k (a_i + b_i i) v_i = 0$$
>
>   Separando parte real e imaginario nos queda:
>
>   $$(\sum_{i=1}^k a_i v_i)  +  i(\sum_{i=1}^k b_i v_i)= 0$$
>
>   Esto implica que:
>
>   $$\sum_{i=1}^k a_i v_i = 0  \text{ y que }  \sum_{i=1}^k b_i v_i= 0$$
>
>   Pero como los $v_i$ son L.I. en $\mathbb{R}$, eso significa que $a_i = b_i = 0 \Rightarrow z_i = a_i + b_i i = 0$. Nos queda que la única combinación lineal compleja que da 0 es la trivial, por lo tanto es L.I. tambien en $\mathbb{C}$
>
> - $\Leftarrow )$ Si son L.I. en $\mathbb{C}$, entonces son L.I. en $\mathbb{R}$
>
>   si hay una combinación lineal real que los anula, entonces es también una combinación compleja que los anula. Pero como supusimos que son L.I. en $\mathbb{C}$, eso sólo pasa si todos los coeficientes son 0 que tambien son reales. Por lo tanto son también L.I. en $\mathbb{R}$

## 13) Propiedades sobre matriz

Sean $m, n \text{ y } r \in \mathbb{N}$.

1. Probar que si $A \in K^{m \times n}$ satisface que $Ax = 0 \forall x \in K^n$ entonces $A = 0$. Deducir que si $A, B \in K^{m\times n}$ satisfacen que $Ax = Bx \forall x \in K^n$ entonces $A = B$.

    > La idea de esto es que si $A$ anula todos los vectores $x$, incluso los canónicos, entonces todos los productos fila por columna tienen que dar 0 y eso implica que $A = 0$.
    >
    > d/ tenemos que $A \in K^{m \times n}$ satisface que $Ax = 0 \forall x \in K^n$. Vamos a probar con los vectores canónicos ya que tiene la propiedad de que son una base de $K^n$ y permite "observar" una columna a la vez. Sea $e_j \in K^n$ el vector canónico con un 1 en posición $j$ y ceros el resto. Entonces $A_{e_j}$ es la j-esima columna de $A$.
    >
    > Pero por hipótesis $A_{e_j} = 0$ para todo $j = 1,..., n$. Entonces todas las columnas son 0 y por lo tanto $A = 0$.
    >
    > Conclusiones:
    >
    > - Si $Ax=0$ para todo $x$, entonces la única posibilidad es que la matriz sea nula.
    > - Si dos matrices actúan igual sobre todos los vectores, entonces son iguales pues:
    > $$Ax - Bx = 0, \forall x \in K^n \Rightarrow (A-B)x = 0, \forall x \in K^n \Rightarrow \text{ (aplicando lo anterior) } A-B=0 \Rightarrow A = B$$

2. Probar que si $A \in K^{m\times n}, B ∈ Kn×r$ con $B = (b_{ij})$ y, para $1 \leq j \leq r$, $B_j = (b_{1j}, ...,b_{nj})$ 
es la columna $j$-ésima de $B$, entonces $AB = (AB_1 | · · · | AB_r)$ (es decir, $AB_j$ es la columna $j$-ésima de $AB$).

## 15) Calcular bases

Dadas las bases de $\mathbb{R}^3$, $B =$ {(1, 1, 0), (0, 1, 1), (1, 0, 1)} y $B´=$ {(−1, 1, 1), (2, 0, 1), (1,−1, 3)}

1. Calcular $[(1, 1, 0)]_{B}$ y $[(1, 1, 0)]_{B´}$

> - $[(1, 1, 0)]_B$: lo tenemos que calcular teniendo la base $B$, lo que significa que tenemos que buscar una combinación linea de la base que sea igual a $(1, 1, 0)$. (o sea, las coordenadas)
> 
>   Queremos encontrar $a,b,c \in \mathbb{R}$ tales que: $a(1,1,0)+b(0,1,1)+c(1,0,1) = (1,1,0)$, desarrollamos:
>
>     $$(a,a,0)+(0,b,b)+(c,0,c) = (1,1,0)$$
>
>     $$(a+c,a+b,b+c) = (1,1,0)$$
>
>     - De la tercera ecuación tenemos: $b = -c$
>     - Sustituimos en la primera: $a-b=1$
>     - Y en la segunda: $a+b =1$
>     - Si ahora sumamos la primera con la segunda tenemos que: 
>
>         $$a+b+a-b = 1+1$$
>
>         $$2a = 2 \Rightarrow a = 1$$
>
>     - De la segunda ecuación reemplazamos a: $b = 0$
>     - De la primera obtenemos $b = -c = 0$
>
>     El resultado nos queda: $[(1, 1, 0)]_B = (1,0,0)$

> - $[(1, 1, 0)]_{B´}$: hacemos lo mismo, queremos encontrar $a,b,c \in \mathbb{R}$ tales que:
>
>     $$a(−1, 1, 1)+b(2, 0, 1)+c(1,−1, 3)=(1,1,0)$$
>
>     $$(−a, a, a)+(2b, 0, b)+(c,−c, 3c)=(1,1,0)$$
>
>     $$(-a+2b+c,a-c,a+b+3c)=(1,1,0)$$ 
>
>   Lo representamos como matriz y triangulamos:
>
> $$\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
1 & 0 & -1 & | & 1 \\
1 & 1 & 3 & | & 0
\end{bmatrix} \Rightarrow f_2 + f_1, f_3 + f_1
\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
0 & 2 & 0 & | & 2 \\
0 & 3 & 4 & | & 1
\end{bmatrix}$$
>
>   $$ \Rightarrow f_3 - \frac{3}{2}f_2
\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
0 & 2 & 0 & | & 2 \\
0 & 0 & 4 & | & -2
\end{bmatrix}$$
>
>   - De la tercera ecuación nos queda que $c = -\frac{1}{2}$
>   - De la segunda $b = 1$ 
>   - De la primera $-a + 2b + c = 1 \Rightarrow -a + 2 + \frac{-1}{2} = 1 \Rightarrow a = \frac{1}{2}$
>
>  El resultado nos queda: $[(1, 1, 0)]_{B´} = (\frac{1}{2},1,-\frac{1}{2})$

2. Calcular la matriz de cambio de base $C(B, B')$

> ---
> Solo por curiosidad:
>
> Para hacer cambio de base $B \rightarrow B´$ armamos los matrices de cambio $P_B$ y $P_{B´}$ que es básicamente poner las bases en columnas:
>
> $$P_B = \begin{bmatrix}
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1 
\end{bmatrix}
P_{B´} = \begin{bmatrix}
-1 & 2 & 1 \\
1 & 0 & -1 \\
1 & 1 & 3 
\end{bmatrix}$$
>
> Para hacer el cambio de base es: 
>
> $$[x]_{B´} = P_{B´}^{-1} . P_B . [x]_B$$
>---
>
> Lo que queremos acá es la **matriz** de cambio de base $(P_{B´ \leftarrow B})$, que se obtiene haciendo:
>
> 1. Escribimos cada vector de la base $B$ como combinación lineal de la base $B´$
> 2. Las coordenadas obtenidas se usan como columnas.
>
> $B =$ {(1, 1, 0), (0, 1, 1), (1, 0, 1)} y $B´=$ {(−1, 1, 1), (2, 0, 1), (1,−1, 3)}
>
> Entonces basicamente necesito calcular la matriz:
>
> $$P_{B´ \leftarrow B} = [[(1, 1, 0)]_{B´}, [(0, 1, 1)]_{B´},[(1, 0, 1)]_{B´}]$$
>
> - Ya tenemos el primero calculado pues $(1, 1, 0)]_{B´} = (\frac{1}{2},1,-\frac{1}{2})$
> - $(0,1,1)_{B´}$: 
>
> $$\begin{bmatrix}
-1 & 2 & 1 & | & 0 \\
1 & 0 & -1 & | & 1 \\
1 & 1 & 3 & | & 1
\end{bmatrix} \Rightarrow f_2 + f_1, f_3 + f_1
\begin{bmatrix}
-1 & 2 & 1 & | & 0 \\
0 & 2 & 0 & | & 1 \\
0 & 3 & 4 & | & 1
\end{bmatrix}$$
>
> $$ \Rightarrow f_3 - \frac{3}{2}f_2
\begin{bmatrix}
-1 & 2 & 1 & | & 0 \\
0 & 2 & 0 & | & 1 \\
0 & 0 & 4 & | & -1/2
\end{bmatrix}$$
>
> De la tercela fila tenemos que $c = -\frac{1}{8}$, de la segunda fila $b = \frac{1}{2}$ y de la primera fila $-a + 2(\frac{1}{2}) + -\frac{1}{8} \Rightarrow a = \frac{7}{8}$
>
> $$(0,1,1)_{B´} = (\frac{7}{8}, \frac{1}{2}, -\frac{1}{8})$$
>
> - $(1,0,1)_{B´}$: 
>
> $$\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
1 & 0 & -1 & | & 0 \\
1 & 1 & 3 & | & 1
\end{bmatrix} \Rightarrow f_2 + f_1, f_3 + f_1
\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
0 & 2 & 0 & | & 1 \\
0 & 3 & 4 & | & 2
\end{bmatrix}$$
>
> $$ \Rightarrow f_3 - \frac{3}{2}f_2
\begin{bmatrix}
-1 & 2 & 1 & | & 1 \\
0 & 2 & 0 & | & 1 \\
0 & 0 & 4 & | & 1/2
\end{bmatrix}$$
>
> De la tercera fila sale que $c = \frac{1}{8}$ y de la segunda sale que $b = \frac{1}{2}$, de la primera tenemos que $-a + 1 + \frac{1}{8} \Rightarrow a = \frac{9}{8}$
>
> $$(1,0,1)_{B´} = (\frac{9}{8}, \frac{1}{2}, \frac{1}{8})$$
>
> $$P_{B´ \leftarrow B} = \begin{bmatrix}
\frac{1}{2} & \frac{7}{8} & \frac{9}{8} \\
1 & \frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & -\frac{1}{8} & \frac{1}{8}
\end{bmatrix}$$

3. Comprobar que $C(B,B')*(1, 1, 0)_{B} = (1, 1, 0)_{B'}$ .

> - $P_{B´ \leftarrow B} = C(B,B')$
> - $(1, 1, 0)_{B} = (1,0,0)$
> - $(1, 1, 0)_{B'} = (\frac{1}{2},1,-\frac{1}{2})$
>
> $$C(B,B')*(1, 1, 0)_{B} = \begin{bmatrix}
\frac{1}{2} & \frac{7}{8} & \frac{9}{8} \\
1 & \frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & -\frac{1}{8} & \frac{1}{8}
\end{bmatrix} *  \begin{bmatrix}
1 \\
0 \\
0 \end{bmatrix} = (\frac{1}{2},1,-\frac{1}{2}) = (1, 1, 0)_{B'} $$