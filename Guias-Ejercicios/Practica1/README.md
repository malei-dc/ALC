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

2. $\{ A \in \mathbb{C}^{3 \times 3}: A = -A^{t} \} $
3. $\{ A \in \mathbb{C}^{3 \times 3}: tr(A) = 0 \} $
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
	> $$(x_1, x_2, x_3, x_4) = Z_{1}(1,−1, 2, 1) + Z_{2}(3, 1, 0,−1) + Z_{3}(1, 1,−1,−1) = (2, 1, 3, 5)$$
	>
	> Nos queda el siguiente sistema de ecuaciones:
	>
	>$$S=\begin{cases} 
	Z_{1} + 3Z_{2} + Z_{3} = 2 \\ 
	-Z_{1} + Z_{2} + Z_{3} = 1 \\ 
	2Z_{1} - Z_{3} = 3 \\ 
	Z_{1} - Z_{2} - Z_{3} = 5 
	\end{cases}$$
	>
	> Ahora toca representarlo como matriz y resolver el sistema triangulando:


2. Determinar si $\{ x \in \mathbb{R}^4/x1 − x2 − x3 = 0 \} \subseteq S$.
3. Determinar si $S \subseteq \{x \in \mathbb{R}^4/x_1 − x_2 − x_3 = 0 \}$.