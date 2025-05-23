# Práctica 3: Sistemas lineales y factorización

## 1) Propiedades matrices cuadradas

Sean $A$ y $B \in \mathbb{K}^{n \times n}$. Probar que.

- Si $A$ y $B$ son triangulares superiores, $AB$ es triangular superior.

    > Una matriz $T = [t_{ij}] \in K^{n\times n}$ es triangula superior si $t{\scriptsize ij} = 0$ para todo $i>j$ 
    > 
    > Sean $A$ y $B$ triangulares superiores, el producto $C = AB = [c_{ij}]$ donde queremos ver que 
    >
    > $$c {\scriptsize ij} = \sum_{k=1}^n a{\scriptsize ik}b{\scriptsize kj}$$
    >
    > $c_{ij} = 0$ si $i>j$
    >
    > Sabemos que $a{\scriptsize ik} = 0$ si $i>k$ y $b{\scriptsize kj} = 0$ si $k>j$. Entonces par que $c{\scriptsize ij} \neq 0$ se necesita que:
    >
    > - $i \leq k$ por triangularidad de $A$
    > - $k \leq j$ por triangularidad de $B$
    >
    > $\Rightarrow i\leq k \leq j \Rightarrow i \leq j$
    >
    > Pero si $i>j$ no existe ningún $k$ tal que $i\leq k \leq j$. Entonces en esos indices $c_{ij} = 0$. Luego $C$ es diagonal superior. 

- Si $A$ y $B$ son diagonales, $AB$ es diagonal.

    > Una matriz $T = [t_{ij}] \in K^{n\times n}$ es diagonal si $t{\scriptsize ij} = 0$ para todo $i \neq j$ 
    > 
    > Sean $A$ y $B$ diagonales, el producto $C = AB = [c_{ij}]$ donde queremos ver que 
    >
    > $$c {\scriptsize ij} = \sum_{k=1}^n a{\scriptsize ik}b{\scriptsize kj}$$
    >
    > $c_{ij} \neq 0$ para todo $i = j$
    >
    > Sabemos que $a{\scriptsize ik} = 0$ si $i \neq k$ y $b{\scriptsize kj} = 0$ si $k\neq j$. Entonces par que $c{\scriptsize ii} \neq 0$ se necesita que:
    >
    > - $i = k$ por diagonalidad de $A$
    > - $k = j$ por diagonalidad de $B$
    >
    > $\Rightarrow i = k = j \Rightarrow i = j$
    >
    > Pero si $i \neq j$ no existe ningún $k$ tal que $i = k = j$. Entonces en esos indices $c_{ij} = 0$. Luego $C$ es diagonal. 

- Si $A$ es estrictamente triangular superior (es decir, $a_{ij} = 0$ si $i ≥ j$), $A^n = 0$.

    > Cada vez que se multiplica matrices estrictamente triangulares superiores, los elementos "suben" más arriba de la diagonal, dejando más ceros en la parte superior de la matriz resultante. Luego de $n$ veces, queda la matriz de ceros.
    >
    > Podría salir con inducción en $n$

## 2) Descomposición LU

Sea 

$$A = \begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
2 & -1 & 0 & -2\\
-3 & 3 & 0 & -1\end{pmatrix} \in \mathbb{R}^{4 \times 4}$$

1. Escalonar la matriz $A$ multiplicándola a izquierda por matrices elementales $T^{ij}(a), a \in \mathbb{R}, 1 \leq i, j \leq 4$, con $i \neq j$

    $$T^{ij}(a) = I_n + aE^{ij}$$

    con $E^{ij}$ la matriz  con un 1 en posición (i,j)

> $$ T^{32}(-1)(T^{41}(3) T^{31}(-2)). A=$$
>
> $$ \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
0 & -1 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
*(\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0\\
3 & 0 & 0 & 1
\end{pmatrix} * 
\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
-2 & 0 & 1 & 0\\
0 & 0 & 0 & 1\end{pmatrix}) * 
\begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
2 & -1 & 0 & -2\\
-3 & 3 & 0 & -1\end{pmatrix} = $$
>
> $$ \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
0 & -1 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
*\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
-2 & 0 & 1 & 0\\
3 & 0 & 0 & 1
\end{pmatrix} *
\begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
2 & -1 & 0 & -2\\
-3 & 3 & 0 & -1\end{pmatrix} = $$
>
> $$ \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
0 & -1 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
*\begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
0 & 1 & 0 & -4\\
0 & 0 & 0 & 2\end{pmatrix} = 
\begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
0 & 0 & -4 & -4\\
0 & 0 & 0 & 2\end{pmatrix}$$

2. Hallar la descomposición $LU$ de $A$.

> Con el inciso anterior ya lo tenemos casi resuelto. La $U$ es la matriz $A$ triangulado y $L = [T^{32}(-1).(T^{41}(3).T^{31}(-2))]^{-1}$
>
> Como ya tenemos $U$, calculamos $L$, multiplicamos todos los $T$ y luego vemos de invertirlo, de la cuenta anterior tengo que:
>
> $$T^{32}(-1).(T^{41}(3).T^{31}(-2))=\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
0 & -1 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
*\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
-2 & 0 & 1 & 0\\
3 & 0 & 0 & 1
\end{pmatrix}=$$
>
> $$=\begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
-2 & -1 & 1 & 0\\
3 & 0 & 0 & 1
\end{pmatrix}$$
>
> $$\Rightarrow L = \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
-2 & -1 & 1 & 0\\
3 & 0 & 0 & 1
\end{pmatrix}^{-1}$$
>
> Invertir esto es sencillo ya que es invertir el signo de los valores que estan por debajo de la diagonal en cada columna.
>
> $$\Rightarrow L = \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
2 & 1 & 1 & 0\\
-3 & 0 & 0 & 1
\end{pmatrix}$$
>
> Luego si hacemos:
>
> $$L*U = \begin{pmatrix}1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 \\
2 & 1 & 1 & 0\\
-3 & 0 & 0 & 1
\end{pmatrix} . \begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
0 & 0 & -4 & -4\\
0 & 0 & 0 & 2\end{pmatrix} = \begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
2 & -1 & 0 & -2\\
-3 & 3 & 0 & -1\end{pmatrix}=A$$

3. Usando la descomposición del ítem anterior resolver el sistema $Ax = b$, para

$$b = \begin{pmatrix}1  \\ 
-7 \\
-5 \\
1 \end{pmatrix}$$

> Queremos resolver $Ax=b$ donde nos dan $b$, como tenemos la descomposición $LU = A$ podemos reemplazar, $L(Ux)=b$. Si llamamos $y = Ux$ podemos resolver $Ly=b$ y esto es sencillo pues $L$ es triangular inferior
>
> $Ly=b$
>
> $$\begin{pmatrix}1 & 0 & 0 & 0 & | & 1\\ 
0 & 1 & 0 & 0 & | & -7\\
2 & 1 & 1 & 0 & | & -5\\
-3 & 0 & 0 & 1 & | & 1
\end{pmatrix}$$
>
> - $y_1 = 1$
> - $y_2 = -7$
> - $2.1+1.(-7)+y_3 = -5 \Rightarrow y_3 = 0$
> - $1.(-3)+y_4=1 \Rightarrow y_4 = 4$
>
> $$y = \begin{pmatrix}1\\ 
-7\\
0\\
4
\end{pmatrix}$$
>
> Ahora que tengo $y$ puedo resolver $Ux=y$ y despejar $x$
>
> $Ux=y$
>
> $$\begin{pmatrix}1 & -1 & 0 & 1 & | & 1\\ 
0 & 1 & 4 & 0 & | & -7\\
0 & 0 & -4 & -4 & | & 0\\
0 & 0 & 0 & 2 & | & 4
\end{pmatrix}$$
>
> - $x_4 = 2$
> - $-4x_3 + (-4).2 = 0 \Rightarrow x_3 = -2$
> - $x_2 + 4.(-2) = -7 \Rightarrow x_2 = 1$
> - $x_1 - 1+2 = 1 \Rightarrow x_1 = 0$
>
> $$x = \begin{pmatrix}0\\ 
1\\
-2\\
2
\end{pmatrix}$$
>
> $Ax = b$ (chequeamos la consigna)
>
> $$\begin{pmatrix}1 & -1 & 0 & 1\\ 
0 & 1 & 4 & 0 \\
2 & -1 & 0 & -2\\
-3 & 3 & 0 & -1\end{pmatrix}. \begin{pmatrix}0\\ 
1\\
-2\\
2
\end{pmatrix} = 
\begin{pmatrix}1\\ 
-7\\
-5\\
1
\end{pmatrix} = b$$

## 3) Descomposición LU en Python

Escribir funciones de Python que calculen la solución de un sistema:

1. $Ly = b$, siendo $L$ triangular inferior.
2. $Ux = y$, siendo $U$ triangular superior.

> Ya hechas en labo de $LU$.

## 4) Código de resolución de sistemas 

Escribir funciones de Python que realicen las siguientes tareas:

1. Calcular la descomposición $LU$ de una matriz dada $A$, asumiendo que no es necesario realizar pivoteos.
2. Resolver un sistema $Ax = b$, utilizando la función del ítem anterior y las del ejercicio 3 aplicar esta función para resolver el ítem c. del ejercicio 2

> Resuelto en el tp :)

## 5) Matrices sin descomposición LU

Considerar la matriz 

$$A = \begin{pmatrix}0 & 1 & 2\\ 
1 & 1 & 0\\
1 & 0 & 3
\end{pmatrix}$$

1. Probar que $A$ no admite descomposición $LU$.

> En la descomposición $LU$ donde nos queda que $L$ es la inversa de una matriz resultado de productos de varios $T$, en realidad está dividiendo por el valor de la diagonal de esa columna, si es $0$... No se puede hacer. 

2. Hallar la descomposición $LU$ de $PA$ para alguna matriz de permutación $P$ adecuada.

> Basicamente puedo permutar la fila 1 con fila 2, haciendo eso y luego la descomposición $LU$ 
>
> $$PA = LU$$
>
> $$\Rightarrow \begin{pmatrix}0 & 1 & 0\\ 
1 & 0 & 0\\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}0 & 1 & 2\\ 
1 & 1 & 0\\
1 & 0 & 3
\end{pmatrix} = 
\begin{pmatrix}1 & 0 & 0\\ 
0 & 1 & 0\\
-1 & 1 & 1
\end{pmatrix}
\begin{pmatrix}1 & 1 & 0\\ 
0 & 1 & 2\\
0 & 0 & 5
\end{pmatrix}$$

## 6) Relación entre inversibilidad y existencia de descomposición

Para cada una de las siguientes matrices analizar existencia y unicidad de la descomposición $LU$ (sin pivoteo). ¿Qué relación existe entre la inversibilidad de una matriz y la existencia de dicha descomposición?

$$A=\begin{pmatrix}0 & 1 & 0\\ 
1 & 0 & 0\\
0 & 0 & 1
\end{pmatrix}, B = \begin{pmatrix}0 & 1 & 0\\ 
1 & 0 & 0\\
0 & 0 & 0
\end{pmatrix}, C = \begin{pmatrix}0 & 1 & 1\\ 
0 & 0 & 1\\
0 & 1 & 0
\end{pmatrix}, D = \begin{pmatrix}1 & 0 & 0\\ 
0 & 1 & 0\\
0 & 0 & 0
\end{pmatrix}$$

> Para la matriz:
>
> $$A=\begin{pmatrix}0 & 1 & 0\\ 
1 & 0 & 0\\
0 & 0 & 1
\end{pmatrix}$$
>
> Si intentamos hacer la descomposición $LU$ en el elemento $a_{11}$ tenemos un $0$, por lo tanto no se puede iniciar la eliminación gaussiana estándar sin intercambiar filas $\Rightarrow$ no admite descomposición $LU$ sin pivoteo.
>
> Veamos si se puede invertir intentando calcular el determinante:
>
>  $$det(A)=\begin{vmatrix}0 & 1 & 0\\ 
1 & 0 & 0\\
0 & 0 & 1
\end{vmatrix} = 0 . \begin{vmatrix}0 & 0\\ 
0 & 1\\
\end{vmatrix}-1. \begin{vmatrix}1 & 0\\ 
0 & 1\\
\end{vmatrix} + 0 . \begin{vmatrix}1 & 0\\ 
0 & 0\\
\end{vmatrix} = -1$$
>
> $$\Rightarrow det(A) = -1 \neq 0 \rightarrow A \text{ es inversible.}$$
>
> - Una matriz puede ser invertible y no admitir descomposición LU sin pivoteo (como en este caso).
> - Para que exista $LU$ sin pivoteo, es necesario que todos los pivotes parciales (elementos de la diagonal) sean distintos a $0$ sin reordenar filas.
>
> --- 
>
> Siguiendo la misma linea con $A$ vamos a analizar cada uno de las matrices restantes:
>
> - Matriz $B$
>   - No admite descomposición $LU$ por tener diagonal en $0$
>   - Como tiene la última fila nula, su determinante es $0$, NO es inversible.
> - Matriz $C$
>   - No admite descomposición $LU$ por tener diagonal en $0$
>   - Como tiene una columna nula, su determinante es $0$, NO es inversible.
> - Matriz $D$
>   - Es triangular superior con ceros bajo la diagonal, si admite descomposición $LU \Rightarrow L = I, U=D$
>   - Tiene una fila nula, asi que NO es inversible.
>
> Conclusiones: 
>
> - La existencia de una descomposición LU sin pivoteo no implica que la matriz sea invertible.
> - La inversibilidad tampoco garantiza la existencia de una descomposición $LU$ sin pivoteo (caso de la matriz $A$ anterior).

## 7) Propiedades sobre las matrices L y U

Sea $A \in \mathbb{R}^{n \times n}$ inversible tal que $A = TS$ donde $T \in \mathbb{R}^{n\times n}$ es triangular inferior y $S \in \mathbb{R}^{n\times n}$ es triangular superior. Probar:

1. $T$ y $S$ son inversibles.

> Probamos que las derminantes de estas matrices no son 0. Según la consigna sabemos que $A$ es inversible, por lo tanto $det(A) \neq 0$. Sabemos que podemos escribir a $A = TS \Rightarrow det(A) = det(TS) = det(T) . det(S) \neq 0$
> 
> Y como sabemos que si una matriz cuadrada tiene determinante distinto a $0$ es inversible. Entonces $S$ y $T$ son inversibles.

2. $A$ tiene factorización $LU$ (con unos en la diagonal de $L$).

> Como podemos escribir $A = TS$ es muy similar a la descomposición $LU$, solo que $T$ no tiene 1 en la diagonal. Lo que se puede hacer en este caso es:
>
> $$T = L.D$$
>
> Donde $D$ es la diagonal de $T$ y $L$ es la matriz con 1 en la diagonal y debajo de la diagonal en cada columna tiene los valores $L_{ij} = \frac{T_{ij}}{T_{ii}}$ (para $i>j$ y $L_{ii} = 1$). Con esto ya tenemos nuestro descomposición $LU$
>
> $$A= (LD)S = L(DS)$$

## 9) Descomposición de Cholesky

Considerar la matriz 

$$\begin{pmatrix}4 & 2 & -2\\ 
2 & 5 & 5\\
-2 & 5 & 11
\end{pmatrix}$$

Mostrar que es definida positiva y calcular su descomposición de Cholesky.

> Hacemos la eliminación gaussiana:
>
> $$\begin{pmatrix}4 & 2 & -2\\ 
2 & 5 & 5\\
-2 & 5 & 11
\end{pmatrix} \underset{F2-\frac{1}{2}F1, F3 + \frac{1}{2}F1}{\rightarrow} \begin{pmatrix}4 & 2 & -2\\ 
0 & 4 & 6\\
0 & 6 & 10
\end{pmatrix} \underset{F3-\frac{3}{2}F2}{\rightarrow} \begin{pmatrix}4 & 2 & -2\\ 
0 & 4 & 6\\
0 & 0 & 1
\end{pmatrix} = U$$
>
> Entonces tenemos que la matriz diagonal es:
>
> $$D = \begin{pmatrix}4 & 0 & 0\\ 
0 & 4 & 0\\
0 & 0 & 1
\end{pmatrix}$$
>
> que es definida positiva y por tanto también lo es el original.
>
> También podemos sacar que
>
> $$\overset{\sim}{L} = \begin{pmatrix}1 & 0 & 0\\ 
\frac{1}{2} & 1 & 0\\
-\frac{1}{2} & \frac{3}{2} & 1
\end{pmatrix}$$
>
> Por lo tanto para sacar $L$ tenemos que hacer $L = \overset{\sim}{L}\sqrt{D}$
>
> $$L = \begin{pmatrix}1 & 0 & 0\\ 
\frac{1}{2} & 1 & 0\\
-\frac{1}{2} & \frac{3}{2} & 1
\end{pmatrix} . \begin{pmatrix}2 & 0 & 0\\ 
0 & 2 & 0\\
0 & 0 & 1
\end{pmatrix} = \begin{pmatrix}2 & 0 & 0\\ 
1 & 2 & 0\\
-1 & 3 & 1
\end{pmatrix}$$
>
> Entonces se puede verificar que $M=LL^t$ (lo hacemos)
>
> $$ M = \begin{pmatrix}2 & 0 & 0\\ 
1 & 2 & 0\\
-1 & 3 & 1
\end{pmatrix} . \begin{pmatrix}2 & 1 & -1\\ 
0 & 2 & 3\\
0 & 0 & 1
\end{pmatrix} = \begin{pmatrix}4 & 2 & -2\\ 
1 & 5 & 5\\
-2 & 5 & 11
\end{pmatrix}$$
>
> :)

## 10) Caracterización de matrices definidas positivas mediante productos internos

Sea $A \in \mathbb{R}^{n\times n}$ una matriz simétrica. Probar que $A$ es definida positiva si y sólo si existe un conjunto de vectores linealmente independientes $[x_1, ..., x_n] \subseteq \mathbb{R}^n$ tal que $a_{ij}=x_i^t x_j$

> $\Rightarrow)$ Si tenemos que $A$ es definida positiva y simétrica, entonces existe la descomposición de Cholesky
>
> $$A = LL^t$$
>
> donde $L$ es una matriz triangular inferior con entradas reales y diagonal estrictamente positiva.
>
> Entonces podemos tomar las filas de $L$ como los vectores $x_i^t$ y nos queda que:
>
> $$a_{ij} = L_i L_j^t = x_i^t x_j$$
>
> Además como sé que $L$ tiene el rango completo por ser definida positiva (su determinante no es 0), las filas son LI 
>
> $\Leftarrow)$  si existe un conjunto de vectores linealmente independientes $[x_1, ..., x_n] \subseteq \mathbb{R}^n$ tal que $a_{ij}=x_i^t x_j$ quiero ver que $A$ es definida positiva.
>
> Construimos un $X \in \mathbb{R}^{n \times n}$ cuyas filas son vectores $x_i^t$.
>
> COMPLETAR

## 14) Gram-Schmidt (con QR por mi)

Aplicar el algoritmo de Gram-Schmidt para calcular bases ortonormales de los subespacios generados por las siguientes bases:

1. $B = \langle (1, 0, 1), (0, 1, 1), (0, 0, 1)\rangle$

> Dado la base $B$ quiero construir un nuevo bon (base ortonormal) $\overset{\sim}{B} = \langle q_1, q_2, q_3 \rangle$
>
> Para cada vector de la base $B$ primero calculo $\overset{\sim}{q}$ y luego normalizo. Empecemos:
>
> Tomo $v_1: (1,0,1)$
>
> $$\overset{\sim}{q_1} = v_1 = (1,0,1)$$
>
> Tomo $v_2: (0,1,1)$
>
> $$\overset{\sim}{q_2} = v_2 - P_{\overset{\sim}{q_1}}(v_2) = \begin{pmatrix}0\\ 
1\\
1
\end{pmatrix} - \frac{(1,0,1)\begin{pmatrix}0\\ 
1\\
1
\end{pmatrix}}{(1,0,1)\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix}} 
\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} = \begin{pmatrix}0\\ 
1\\
1
\end{pmatrix} - \frac{1}{2} 
\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} = 
\begin{pmatrix}-\frac{1}{2}\\ 
1\\
\frac{1}{2}
\end{pmatrix} $$
>
> Tomo $v_3: (0,0,1)$
>
> $$\overset{\sim}{q_3} = v_3 - P_{\langle\overset{\sim}{q_1},\overset{\sim}{q_2}\rangle}(v_3) = v_3 - P_{\overset{\sim}{q_1}}(v_3) - P_{\overset{\sim}{q_2}}(v_3) =$$
>
> $$ = \begin{pmatrix}0\\ 
0\\
1
\end{pmatrix} - \frac{(1,0,1)\begin{pmatrix}0\\ 
0\\
1
\end{pmatrix}}{(1,0,1)\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix}} 
\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} - \frac{(-\frac{1}{2}, 
1,\frac{1}{2})\begin{pmatrix}0\\ 
0\\
1
\end{pmatrix}}{(-\frac{1}{2}, 
1,\frac{1}{2})\begin{pmatrix}-\frac{1}{2}\\ 
1\\
\frac{1}{2}
\end{pmatrix}} 
\begin{pmatrix}-\frac{1}{2}\\ 
1\\
\frac{1}{2}
\end{pmatrix} =$$
>
>$$ = \begin{pmatrix}0\\ 
0\\
1
\end{pmatrix} - \frac{1}{2} 
\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} - \frac{\frac{1}{2}}{\frac{3}{2}} 
\begin{pmatrix}-\frac{1}{2}\\ 
1\\
\frac{1}{2}
\end{pmatrix} = \begin{pmatrix}0\\ 
0\\
1
\end{pmatrix} - \frac{1}{2} 
\begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} - \frac{1}{3} 
\begin{pmatrix}-\frac{1}{2}\\ 
1\\
\frac{1}{2}
\end{pmatrix} = \begin{pmatrix}-\frac{1}{3}\\ 
-\frac{1}{3}\\
\frac{1}{3}
\end{pmatrix}$$
>
> Ya tengo todos los $\overset{\sim}{q}$. Ahora normalizo cada uno:
>
> $$q_1 = \frac{\overset{\sim}{q_1}}{\|\overset{\sim}{q_1}\|_2} = \overset{\sim}{q_1} \frac{1}{\sqrt{2}} = \begin{pmatrix}\frac{1}{\sqrt{2}}\\ 
0\\
\frac{1}{\sqrt{2}}
\end{pmatrix}$$
>
> $$q_2 = \frac{\overset{\sim}{q_2}}{\|\overset{\sim}{q_2}\|_2} = \overset{\sim}{q_2} \frac{\sqrt{3}}{\sqrt{2}} = \begin{pmatrix}-\frac{\sqrt{2}}{2\sqrt{3}}\\ 
\frac{\sqrt{2}}{\sqrt{3}}\\
\frac{\sqrt{2}}{2\sqrt{3}}
\end{pmatrix}$$
>
> $$q_3 = \frac{\overset{\sim}{q_3}}{\|\overset{\sim}{q_3}\|_2} = \overset{\sim}{q_3} \sqrt{3} = \begin{pmatrix}-\frac{\sqrt{3}}{3}\\ 
-\frac{\sqrt{3}}{3}\\
\frac{\sqrt{3}}{3}
\end{pmatrix}$$
>
> Obtuve mi base bon, vayamos más allá y busquemos la factorización $QR$.
>
> Sabemos que $\langle v_1 \rangle = \langle q_1 \rangle, \langle v_1,v_2 \rangle = \langle q_1, q_2 \rangle, \langle v_1,v_2,v_3 \rangle = \langle q_1, q_2,q_3 \rangle$
>
> $$v_1 = \begin{pmatrix}1\\ 
0\\
1
\end{pmatrix} = \sqrt{2} \begin{pmatrix}\frac{1}{\sqrt{2}}\\ 
0\\
\frac{1}{\sqrt{2}}
\end{pmatrix} = \sqrt{2} q_1$$
>
> $$v_2 = \begin{pmatrix}0\\ 
1\\
1
\end{pmatrix} =  \frac{\sqrt{2}}{2}\begin{pmatrix}\frac{1}{\sqrt{2}}\\ 
0\\
\frac{1}{\sqrt{2}}
\end{pmatrix} + \frac{\sqrt{3}}{\sqrt{2}} \begin{pmatrix}-\frac{\sqrt{2}}{2\sqrt{3}}\\ 
\frac{\sqrt{2}}{\sqrt{3}}\\
\frac{\sqrt{2}}{2\sqrt{3}}
\end{pmatrix} = \frac{\sqrt{2}}{2}q_1 + \frac{\sqrt{3}}{\sqrt{2}} q_2$$
>
> $$v_3 = \begin{pmatrix}0\\ 
0\\
1
\end{pmatrix} =  \frac{1}{\sqrt{2}} \begin{pmatrix}\frac{1}{\sqrt{2}}\\ 
0\\
\frac{1}{\sqrt{2}}
\end{pmatrix} + \frac{\sqrt{2}}{2\sqrt{3}} \begin{pmatrix}-\frac{\sqrt{2}}{2\sqrt{3}}\\ 
\frac{\sqrt{2}}{\sqrt{3}}\\
\frac{\sqrt{2}}{2\sqrt{3}}
\end{pmatrix} + \frac{1}{\sqrt{3}} \begin{pmatrix}-\frac{\sqrt{3}}{3}\\ 
-\frac{\sqrt{3}}{3}\\
\frac{\sqrt{3}}{3}
\end{pmatrix} = \frac{1}{\sqrt{2}} q_1 + \frac{\sqrt{2}}{2\sqrt{3}} q_2 + \frac{1}{\sqrt{3}} q_3$$
>
> Armamos la descomposición:
>
> $$\begin{pmatrix}v_1| & v_2| & v_3 \end{pmatrix} = 
\begin{pmatrix}1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 1 & 1 \end{pmatrix} = 
\begin{pmatrix}q_1| & q_2| & q_3 \end{pmatrix} 
\begin{pmatrix}
\sqrt{2} & \frac{\sqrt{2}}{2} & \frac{1}{\sqrt{2}} \\
0 & \frac{\sqrt{3}}{\sqrt{2}} & \frac{\sqrt{3}}{2\sqrt{2}} \\
0 & 0 & \frac{1}{\sqrt{3}} \end{pmatrix} = QR$$

2. $B = \langle(i, 1 − i, 0), (i, 1, 0)\rangle$

> Dado la base $B$ quiero construir un nuevo bon (base ortonormal) $\overset{\sim}{B} = \langle q_1, q_2 \rangle$
>
> Para cada vector de la base $B$ primero calculo $\overset{\sim}{q}$ y luego normalizo. Empecemos:
>
> Tomo $v_1: (i, 1 − i, 0)$
>
> $$\overset{\sim}{q}_1 = v_1 = (i, 1 − i, 0)$$
>
> Tomo $v_2: (i, 1, 0)$
>
> $$\overset{\sim}{q_2} = v_2 - P_{\overset{\sim}{q_1}}(v_2) = \begin{pmatrix}i\\ 
1\\
0
\end{pmatrix} - \frac{(i,1-i,0)\begin{pmatrix}i\\ 
1\\
0
\end{pmatrix}}{(i,1-i,0)\begin{pmatrix}i\\ 
1-i\\
0
\end{pmatrix}} 
\begin{pmatrix}i\\ 
1-i\\
0
\end{pmatrix} = \begin{pmatrix}i\\ 
1\\
0
\end{pmatrix} - \frac{-i}{-1-2i} 
\begin{pmatrix}i\\ 
1-i\\
0
\end{pmatrix} = ...$$

3. $B = \langle(1,−1, 0, 1), (0, 1, 1, 0), (−1, 0, 1, 1)\rangle$

## 15) Construcciones de proyectores

En cada uno de los siguientes casos construir un proyector $f : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ que cumpla:

1. $Im(f) = (x_1, x_2, x_3)/x_1 + x_2 + x_3 = 0$

> Hallamos una base de $Im(f)=\langle (-1,1,0)(-1,0,-1)\rangle$ y completamos a una base de $\mathbb{R}^3$ y luego definimos $f$ sobre esa base. $B = \langle (-1,1,0)(0,-1,-1)(0,0,1)\rangle$ es claro que $B$ es una base de $\mathbb{R}^3$ que contirne a una base de $Im(f)$.
>
> Ahora, si $y \in Im(f) \Rightarrow \exist x \in \mathbb{R}^3/ f(x) = y$ de modo que $f(x) = f(y)$ pero $f(x) = y$, así que $y=f(y)$.
>
> Por lo tanto, si $f$ es un proyector e $y \in Im(f)$, entonces $f(y) = y$. Definimos:
>
> $$\begin{cases}f(-1,1,0) = (-1,1,0) \\
f(0,-1,-1) = (0,-1,-1) \\
f(0,0,1) = (0,0,0)
\end{cases}$$
>
> Con esta definición tenemos que $Nu(f) \oplus Im(f) = \mathbb{R}^3$
>
> Una vez que tenemos definido $f$ sobre una base podemos hacer explicitamente la expresión $f(x,y,z)$:
>
> $$(x,y,z) = \lambda_1 (-1,1,0) + \lambda_2 (0,-1,-1) + \lambda_3 (0,0,1)$$
>
> $$\begin{cases}x = -\lambda_1 \\
y = \lambda_1 - \lambda_2 \\
z = -\lambda_2 + \lambda_3
\end{cases} \Rightarrow \begin{cases}-x = \lambda_1 \\
-y - x = \lambda_2 \\
z -y -x = \lambda_3
\end{cases} $$
>
> Por lo tanto 
>
> $$(x,y,z) = (-x) (-1,1,0) + (-y - x)  (0,-1,-1) + (z -y -x) (0,0,1)$$
>
> $$\Rightarrow f(x,y,z) = (-x) f(-1,1,0) + (-y - x) f(0,-1,-1) + (z -y -x) f(0,0,1)$$
>
> $$= (-x) (-1,1,0) + (-y - x) (0,-1,-1) + (z -y -x) (0,0,0) \Rightarrow $$
>
> $$ f(x,y,z) = (x, -y-2x,y+x) $$