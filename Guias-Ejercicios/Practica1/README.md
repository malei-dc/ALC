# Práctica 1: Resolución de sistemas de ecuaciones lineales

## 1) Sistema de ecuaciones no homogéneos

Resolver los siguientes sistemas de ecuaciones lineales no homogéneos y los sistemas homogéneos asociados en $\mathbb{R}$ o en $\mathbb{C}$. Si la solución es única, puede verificarse el resultado en Python utilizando el comando ```np. linalg . solve1.```

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

b. Considerar el sistema homogéneo asociado y dar los valores de $k$ para los cuales admite solución no trivial. Para esos $k$, resolverlo.