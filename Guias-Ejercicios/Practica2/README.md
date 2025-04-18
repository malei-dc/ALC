# Práctica 2: Aritmética de punto flotante. Número de condición.

## Transformaciones lineales

### 1) Aplicación lineal

Determinar cuáles de las siguientes aplicaciones son lineales.

1. $f: \mathbb{R}^3 \rightarrow \mathbb{R}^2, f(x1, x2, x3) = (x_2 − 3x_1 + \sqrt{2}x_3 , x_1 − \frac{1}{2}x_2) \longrightarrow \boxed{SI}$

    > Para que $f$ sea una T.L tiene que cumplir:
    >
    > - $f(\overset{\rightarrow}{0}) = \overset{\rightarrow}{0}$
    > - $f(u+v) = f(u) + f(v)$
    > - $f(\alpha u) = \alpha f(u)$
    
    > - A ojo veo que en $f(0,0,0) = (0,0)$
    > - Sean $(a,b,c)$ y $(x,y,z)$
    >   - $f((a,b,c)+ (x,y,z)) = f(a+x,b+y,c+z) = ((b+y)-3(a+x)+\sqrt{2}(c+z), (a+x)-\frac{1}{2}(b+y))$
    >   - $f(a,b,c) + f(x,y,z) = (b-3a+\sqrt{2}c, a-\frac{1}{2}b)+(y-3x+\sqrt{2}z, x-\frac{1}{2}y) = ((b+y)-3(a+x)+\sqrt{2}(c+z), (a+x)-\frac{1}{2}(b+y))$
    > - Sea $\alpha \in \mathbb{R}$ y $(x,y,z) \in \mathbb{R}^3$
    >   - $\alpha f(x,y,z) = \alpha (y-3x+\sqrt{2}z, x-\frac{1}{2}y) =  (\alpha(y-3x+\sqrt{2}z), \alpha(x-\frac{1}{2}y)) = f(\alpha(x,y,z))$
    >
    > Luego $f$ es una T.L.

2. $f: \mathbb{R}^2 \rightarrow \mathbb{R}^2, f(x1, x2) = (x_1 + x_2, |x_1|) \longrightarrow \boxed{NO}$

    >- En el $(0,0)$ la función se anula
    >- Sean $(a,b)$ y $(x,y)$
    >    - $f((a,b)+(x,y)) = f(a+x, b+y) = (a+x+b+y,|a+x|)$
    >    - $f(a,b) + f(x,y) = (a+b, |a|) + (x+y, |x|) = (a+b+x+y, |a|+|x|)$
    >
    > No es una transfomación lineal ya que si tomo $a = -1$ y $x = 3$:
    >
    > $$|a| + |x| = 1 + 3 = 4 \neq 2 = |-1+3| = |a+x| $$

3. $f: R^{2\times 2} → R, f(a_{11}, a_{12}, a_{21}, a_{22}) = a_{11}.a_{22}-a_{12}.a_{21} \longrightarrow \boxed{NO}$ (Es la determinante)

    > ---
    >
    > Nota: voy a escribir la matriz en fila por comodidad nomas.
    >
    > ---
    >
    > - En el $(0,0,0,0)$ la función se anula.
    > - Sean $(a_{11}, a_{12}, a_{21}, a_{22})$ y $(b_{11}, b_{12}, b_{21}, b_{22})$ vemos si se cumple la suma:
    >   - $f((a_{11}, a_{12}, a_{21}, a_{22}) + (b_{11}, b_{12}, b_{21}, b_{22})) = f(a_{11} + b_{11}, a_{12} + b_{12}, a_{21} +b_{21}, a_{22} + b_{22}) = (a_{11}+b_{11}).(a_{22}+b_{22}) - (a_{12}+b_{12}).(a_{21}+b_{21})$
    >   - $f(a_{11}, a_{12}, a_{21}, a_{22}) + f(b_{11}, b_{12}, b_{21}, b_{22}) = (a_{11}.a_{22}-a_{12}.a_{21}) + (b_{11}.b_{22}-b_{12}.b_{21})$
    >   
    >   No tiene pinta que sean lo mismo, buscamos un ejemplo: tomo $A = (1, 2, 3, 4)$ y $B = (5, 6, 7, 8)$ haciendo $A+B = (6,8,10,12)$
    >
    >   $$f(A) = 1 \ast 4 - 2 \ast 3 = -2, f(B)= 5 \ast 8-6 \ast 7=-2 \Rightarrow f(A) + f(B) = -4$$
    >
    >   $$f(A+B) = 6\ast 12-8\ast10 =-8$$
    >
    > Concluimos que el determinante no es una transformación lineal.

4.  $f: R^{2\times 2} → R^{2\times 3}, f(a_{11}, a_{12}, a_{21}, a_{22}) = (a_{22}, 0, a_{12}+a_{21}, 0, a_{11}, a_{22}- a_{11}) \longrightarrow \boxed{SI}$ 

    > - En el $\overset{\rightarrow}{0}$ la función se anula.
    > - La multiplicación por escalar tambien se cumple ya que lo puedo "sacar" afuera $\alpha f(A) = f(\alpha A)$ 
    > - Sea $A=(a_{ij})$, $B=(b_{ij})$ entonces:

$$f(A+B)= \begin{bmatrix}
a_{22}+b_{22} & 0 & (a_{12}+b_{12})+(a_{21}+b_{21}) \\
0 & a_{11}+b_{11} & (a_{22}+b_{22})+(a_{11}+b_{11})
\end{bmatrix}$$

$$f(A) + f(B)= \begin{bmatrix}
a_{22} & 0 & a_{12}+a_{21} \\
0 & a_{11} & a_{22} + a_{11}
\end{bmatrix} + 
\begin{bmatrix}
b_{22} & 0 & b_{12}+b_{21} \\
0 & b_{11} & b_{22} + b_{11}
\end{bmatrix} = 
\begin{bmatrix}
a_{22}+b_{22} & 0 & (a_{12}+b_{12})+(a_{21}+b_{21}) \\
0 & a_{11}+b_{11} & (a_{22}+b_{22})+(a_{11}+b_{11})
\end{bmatrix}$$

### 2) Transformación canónica

Escribir la matriz de las siguientes transformaciones lineales en base canónica. Interpretar geométricamente cada transformación.

1. $f(x, y) = (x, 0)$

> Para la base canónica aplicamos: $f(1,0) = (1, 0), f(0,1)=(0,0)$. Entonces la matriz asociada es:
>
> $$M=\begin{bmatrix} 
1 & 0 \\
0 & 0 
\end{bmatrix}$$
>
> Representación geométrica:  proyecta cualquier vector del plano sobre el eje $x$. En otras palabras, "aplana" el plano sobre el eje $x$ eliminando la componente vertical.
>
> ![](/Guias-Ejercicios/Practica2/graficos/02a-tl.png)


2. $f(x, y) = (x,−y)$

> Para la base canónica aplicamos: $f(1,0) = (1, 0), f(0,1)=(0,-1)$. Entonces la matriz asociada es:
>
> $$M=\begin{bmatrix} 
1 & 0 \\
0 & -1 
\end{bmatrix}$$
>
> Representación geométrica: Esta transformación refleja los puntos respecto del eje $x$. Es decir, cualquier punto queda igual en su componente $x$, pero la componente $y$ se invierte.
>
> ![](/Guias-Ejercicios/Practica2/graficos/02b-tl.png)

3. $f(x, y) = ( \frac{1}{2} (x + y), \frac{1}{2} (x + y))$

> Para la base canónica aplicamos: $f(1,0) = (\frac{1}{2}, 0), f(0,1)=(0,\frac{1}{2})$. Entonces la matriz asociada es:
>
> $$M=\begin{bmatrix} 
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} 
\end{bmatrix}$$
>
> Esta matriz proyecta cualquier vector sobre la recta $y=x$, porque el resultado de la transformación siempre es un múltiplo del vector $(1,1)$.
>
> ![](/Guias-Ejercicios/Practica2/graficos/02c-tl.png)

4. $f(x, y) = (x\ast cos(t) − y\ast sen(t) , x\ast sen (t) + y\ast cos (t))$

> Para la base canónica aplicamos: $f(1,0) = (cos(t), sen(t)), f(0,1)=(-sen(t),cos(t))$. Entonces la matriz asociada es:
>
> $$M=\begin{bmatrix} 
cos(t) & -sen(t) \\
sen(t) & cos(t)
\end{bmatrix}$$
>
> Esa función es una rotación del plano en sentido antihorario un ángulo $t$ (en radianes).
>
> ![](/Guias-Ejercicios/Practica2/graficos/02d-tl.png)

### 3) Unicidad de t.l

1. Probar que existe una única transformación lineal $f : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ tal que $f(1, 1) = (−5, 3)$ y $f(−1, 1) = (5, 2)$. Para dicha $f$, determinar $f(5, 3)$ y $f(−1, 2)$.

> Para probar que existe una única t.l hay que ver que los vectores de entrada forman una base, en este caso son $(1,1), (-1,1)$. Esto es importante ya que si son base, cualquier vector en $\mathbb{R}^2$ puede escribirse como combinación lineal de esos dos, y por lo tanto la t.l queda determinada por alguna combinación lineal sobre la base.
>
> A ojo se nota que son base, al ponerlos en fila y triangular, ninguna se anula, por lo que son L.I. Los vectores resultantes de esta triangulación a ojo son: $(1,1), (0, 2)$.
>
> - $f(5,3)$: tengo que buscar una combinación lineal, es decir buscamos $a,b$ tal que:
>
>   $$a(1,1) + b(-1,1) = (5,3) \Rightarrow (a-b, a+b) = (5,3)$$
>
>   Despejando nos queda que $a = 5+b$ y en la segunda ecuación es $5+b +b = 3 \Rightarrow b = -1 \Rightarrow a= 4$
>
>   Entonces:
>
>   $$f(5,3) = 4f(1,1) + -1f(-1,1) = 4(-5,3) + -1(5,2) = (-25,10)$$
>
> - $f(-1,2)$: hacemos lo mismo
>
>   $$a(1,1) + b(-1,1) = (-1,2) \Rightarrow (a-b, a+b) = (-1,2)$$
>
>   Despejando la primera ecuación $a = -1+b$ y en la segunda $-1+b+b=2 \Rightarrow b = \frac{3}{2} \Rightarrow a = \frac{1}{2}$
>
>   $$f(5,3) = \frac{1}{2}f(1,1) + \frac{3}{2}f(-1,1) = \frac{1}{2}(-5,3) + \frac{3}{2}(5,2) = (5,\frac{9}{2})$$

2. ¿Existiría una transformación lineal  $f : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ tal que $f(1, 1) = (2, 6)$, $f(−1, 1) = (2, 1)$ y $f(2, 7) = (5, 3)$?

>   $f(2,7)$: hacemos lo mismo, solo con la diferencia que ahora tengo que verificar que dé $(5,3)$
>
>   $$a(1,1) + b(-1,1) = (2,7) \Rightarrow (a-b, a+b) = (2,7)$$
>
>   Despejando la primera ecuación $a = 2+b$ y en la segunda $2+b+b=7 \Rightarrow b = \frac{9}{2} \Rightarrow a = \frac{13}{2}$
>
>   $$f(5,3) = \frac{13}{2}f(1,1) + \frac{9}{2}f(-1,1) = \frac{13}{2}(-5,3) + \frac{9}{2}(5,2) = (-10,\frac{57}{2})$$
>
>   Obtenemos que  $f(2, 7)= (-10,\frac{57}{2}) \neq (5, 3)$ no existe una transformación lineal que cumpla las tres condiciones.

3. Sean $f,g : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ t.l. tales que:

    $$f(1, 0, 1) = (1, 2, 1), f(2, 1, 0) = (2, 1, 0), f(−1, 0, 0) = (1, 2, 1), $$

    $$g(1, 1, 1) = (1, 1, 0), g(3, 2, 1) = (0, 0, 1), g(2, 2,−1) = (3,−1, 2). $$

    Determinar si $f=g$.

> Para determinar que $f=g$ necesito verificar que por ejemplo $g(1,1,1) = f(1,1,1) = (1,1,0)$
>
> Busco $a,b,c$ tales que:
>
> $$a(1,0,1)+ b(2,1,0)+c(−1,0,0) = (1,1,1)$$
>
> $$\begin{bmatrix} 
1 & 2 & -1 & | & 1 \\ 
0 & 1 & 0 & | & 1 \\
1 & 0 & 0 & | & 1 \\ 
\end{bmatrix} \Rightarrow a = 1, b = 1, c= 2$$
>
> Entonces nos queda que:
>
> $$f(1,1,1) = 1f(1,0,1)+ 1f(2,1,0)+2f(−1,0,0)$$
>
> $$f(1,1,1) = (1,2,1)+ (2,1,0)+2(1,2,1) = (4,7,3) \neq (1, 1, 0) = g(1, 1, 1)$$
>
> Con esto podemos concluir que $f \neq g$

### 4) Buscar a

Hallar todos los $a \in \mathbb{R}$ para los cuales exista una transformación lineal $f : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ que satisfaga que $f(1,−1, 1) = (2, a,−1), f(1,−1, 2) = (a^2,−1, 1), f(1,−1,−2) = (5,−1,−7).$

> Veamos si los vectores de entrada son linealmente dependientes:
>
> $$ \begin{bmatrix}
1 & -1 & 1 \\
1 & -1 & 2 \\
1 & -1 & -2
\end{bmatrix} \Rightarrow f_2+f_1, f_3+f_1
\begin{bmatrix}
1 & -1 & 1 \\
0 & 0 & 3 \\
0 & 0 & -1
\end{bmatrix}$$
>
> Claramente son L.D. Intentemos escribir unos terminos de otros: 
>
> $$(1,−1,2) = (1,-1,1) + (0,0,1)$$
>
> $$(1,−1,−2) = (1,-1,1) + (-3) (0,0,1)$$
>
> Usando la linealidad podemos aplicar la funcion:
>
> $$f(1,−1,2) = f((1,-1,1) + (0,0,1)) = f(1,-1,1) + f(0,0,1) \Rightarrow (a^2,−1,1) = (2,a,−1) + f(0,0,1)$$
>
> Despejando nos queda que:
>
> $$f(0,0,1) = (a^2,−1,1) -  (2,a,−1) = (a^2-2, -1-a, 2)$$
>
> Haciendo lo mismo con el otro:
>
> $$f(1,−1,−2) = f((1,-1,1) + (-3) (0,0,1)) = f(1,-1,1) + (-3) f(0,0,1)$$
>
> Reemplazando tenemos que:
>
> $$(5,−1,−7) = (2,a,−1) + (-3)  (a^2-2, -1-a, 2) = (-3a^2+8, 4a+3,-7)$$
>
> De este último paso podemos despejar: 
>
> $$\begin{cases} 5 = -3a^2+8 \Rightarrow a^2 = 1 \Rightarrow a= \pm 1\\
-1 =  4a+3 \Rightarrow a = -1
\end{cases}$$
>
> Entonces concluimos que $a = -1$ es la única opción.

### 5) Núcleo e imagen de T.L

Calcular bases del núcleo y de la imagen para cada tranformación lineal de los ejercicios 2 y 3. Decidir, en cada caso, si $f$ es epimorfismo,monomorfismo o isomorfismo. En el caso que sea isomorfismo, calcular $f^{−1}$.

1. $f(x, y) = (x, 0)$

> $Nu(f):$ buscamos los vectores  $(x,y)$ tales que:
>
> $$f(x, y) = (x, 0) = (0,0) \Rightarrow x = 0 \Rightarrow Nu(f) = [(0,y) \in \mathbb{R}^2]$$
>
> Base del núcleo:
>
> $$Nu(f)=[(0,1)]$$
>
> $Im(f):$ todos los vectores que se pueden escribir como $f(x,y) = (x,0)$ es decir:
>
> $$Im(f) = [(x,0) \in \mathbb{R}^2] $$
>
> Base de la imagen:
>
> $$Im(f)=[(1,0)]$$
>
> - Monomorfismo $\Leftrightarrow Nu(f) = [0] \rightarrow$ No cumple, ya que tiene núcleo no trivial.
> - Epimorfismo $\Leftrightarrow Im(f) = \mathbb{R}^2 \rightarrow$ No cumple, la imagen es solo una recta.
> - Isomorfismo $\Leftrightarrow$ mono + epi $\rightarrow$ No es epi ni mono. 

2. $f(x,y)=(x,−y)$

> $Nu(f):$ buscamos los vectores  $(x,y)$ tales que:
>
> $$f(x, y) = (x, -y) = (0,0) \Rightarrow x = 0, -y=0 \Rightarrow Nu(f) = [(0,0)]$$
>
> Base del núcleo: $\emptyset$
>
> $Im(f):$ todos los vectores que se pueden escribir como $f(x,y) = (x,-y)$ es decir:
>
> $$Im(f) = \mathbb{R}^2 \Rightarrow \text{Base: } [(1,0),(0,-1)] $$
>
> - Monomorfismo $\Leftrightarrow Nu(f) = [0] \rightarrow$ Si cumple.
> - Epimorfismo $\Leftrightarrow Im(f) = \mathbb{R}^2 \rightarrow$ Si
> - Isomorfismo $\Leftrightarrow$ mono + epi $\rightarrow$ Si 
>
> $f^{-1}$: para una t.l. $f: \mathbb{R}^n \rightarrow \mathbb{R}^n$, la función inversa $f^{-1}$ es la que deshace lo que hace $f$
>
> $$f^{−1}(f(v))=v \text{ y } f(f^{−1}(v))=v$$
>
> En nuestro caso de $f(x,y)=(x,−y)$ si aplicamos $f$ dos veces:
>
> $$f(f(x,y)) = f(x,-y) = (x,y) \Rightarrow f o f = id \Rightarrow f = f^{-1}$$

3. $f(x, y) = ( \frac{1}{2} (x + y), \frac{1}{2} (x + y))$

> $Nu(f):$ buscamos los vectores  $(x,y)$ tales que:
>
> $$f(x, y) = ( \frac{1}{2} (x + y), \frac{1}{2} (x + y)) \Rightarrow x + y = 0 \Rightarrow y = -x \Rightarrow x(1,-1)$$
>
> Base del núcleo: $Nu(f) = [(1,-1)]$
>
> $Im(f):$ todos los vectores que se pueden escribir como $f(x, y) = ( \frac{1}{2} (x + y), \frac{1}{2} (x + y))$ si tomo $s = \frac{1}{2} (x + y)$ obtengo que $f(x,y) = (s, s) = s(1,1)$ es decir:
>
> $$Im(f) = [(1,1)] $$
>
> - Monomorfismo $\Leftrightarrow Nu(f) = [0] \rightarrow$ No cumple, ya que tiene núcleo no trivial.
> - Epimorfismo $\Leftrightarrow Im(f) = \mathbb{R}^2 \rightarrow$ No cumple, la imagen es solo una recta.
> - Isomorfismo $\Leftrightarrow$ mono + epi $\rightarrow$ No es epi ni mono. 

4. $f(x, y) = (x\ast cos(t) − y\ast sen(t) , x\ast sen (t) + y\ast cos (t))$

> La matriz asociada es:
>
> $$A = \begin{bmatrix}
cos(t) & - sen(t) \\
sen(t) & cos(t)
\end{bmatrix}$$
>
> - Es mono pues el núcleo es $(0,0)$
> - Es epi ya que la transformacion lineal es una rotación en el plano con angulo $t$, la imagen puede tener la base canónica y genera todo $\mathbb{R}^2$
> - Como es mono y epi, entonces es iso
>
> La matriz inversa es:
>
> $$A^{-1} = \begin{bmatrix}
cos(t) & sen(t) \\
-sen(t) & cos(t)
\end{bmatrix}$$
>
>  Interpretación: Es una rotación en sentido horario (ángulo $−t$).

5. Tenemos $f: \mathbb{R}^2 \rightarrow \mathbb{R}^2$

$$\begin{cases} 
f(1,1) = (-5, 3) \\
f(-1,1) = (5, 2)
\end{cases}$$

> $Im(f):$ es lo que esta a la derecha del $=$
>
> $$Im(f) = [(-5,3), (5,2)]$$
>
> Si triangulo los dos vectores quedan $(-5,3),(0,5)$, es decir que son L.I. por lo tanto una base de la imagen es $Im(f) = \langle (-5,3),(0,5) \rangle$ 
>
> $Nu(f)$: busco $(x,y)/ f(x,y) = (0,0)$
>
> $$(x,y) = a(1,1) + b(-1,1) = (0,0)$$
>
> $$f(x,y) = f(a(1,1)) + f(b(-1,1)) = a\ast f(1,1) + b \ast f(-1,1) = a \ast (-5,3) + b \ast (5,2) = (-5a+5b, 3a+2b)=(0,0)$$
>
> $$\begin{bmatrix}
-1 & 1 & | & 0\\
3 & 2 & | & 0
\end{bmatrix} \Rightarrow f_2+3f_1 
\begin{bmatrix}
-1 & 1 & | & 0\\
0 & 5 & | & 0
\end{bmatrix} \Rightarrow b=0, a=0$$
>
> Entonces nos queda que el nucleo es la solución trivial $Nu(f) = (0,0)$
>
> - Epimorfismo: si, la imagen genera $\mathbb{R}^2$
> - Monomorfismo: si, el núcleo es $(0,0)$
> - Isomorfismo: si
>
> $f^{-1}$: los vectores (1,1) y (−1,1) son tu base inicial, y su imagen es la base transformada. Pero necesitamos la matriz de $f$ en la base canónica. Para eso necesitamos escribir a los vectores (1,0) y (0,1) como combinaciones lineales de (1,1) y (-1,1)
>
> - $(1,0) = a(1,1)+b(-1,1) \Rightarrow (a-b,a+b) = (1,0)$
>
> $$\begin{cases}
a-b = 1 \Rightarrow -b-b = 1 \Rightarrow b = -\frac{1}{2}\\
a+b = 0 \Rightarrow a = -b \Rightarrow a = \frac{1}{2}
\end{cases}$$
>
> Entonces aplicando la linealidad:
>
> $$f(1,0) = \frac{1}{2}f(1,1)  -\frac{1}{2}f(-1,1) = \frac{1}{2}(−5, 3)  -\frac{1}{2}(5, 2) = (-5, \frac{1}{2})$$ 
>
> - $(0,1) = a(1,1)+b(-1,1) \Rightarrow (a-b,a+b) = (0,1)$
>
> $$\begin{cases}
a-b = 0 \Rightarrow a = b\\
a+b = 1 \Rightarrow b = \frac{1}{2} = a
\end{cases}$$
>
> Entonces aplicando la linealidad:
>
> $$f(0,1) = \frac{1}{2}f(1,1)  +\frac{1}{2}f(-1,1) = \frac{1}{2}(−5, 3)  +\frac{1}{2}(5, 2) = (0, \frac{5}{2})$$
>
> La matriz en base canónica es:
>
> $$A= \begin{bmatrix}
-5 & 0 \\ 
\frac{1}{2} & \frac{5}{2}
\end{bmatrix}$$
>
> Entonces la inversa es:
>
> $$A^{-1}= \frac{1}{det(A)}\begin{bmatrix}
 \frac{5}{2} & 0 \\ 
-\frac{1}{2} & -5
\end{bmatrix}$$
>
> $$Det(A) = (-5)(\frac{5}{2}) - 0(-\frac{1}{2}) = -\frac{25}{2}$$
>
> $$A^{-1}= \frac{1}{-\frac{25}{2}}\begin{bmatrix}
 \frac{5}{2} & 0 \\ 
-\frac{1}{2} & -5
\end{bmatrix} = 
-\frac{2}{25}\begin{bmatrix}
 \frac{5}{2} & 0 \\ 
-\frac{1}{2} & -5
\end{bmatrix} = 
\begin{bmatrix}
 -\frac{1}{5} & 0 \\ 
\frac{1}{25} & \frac{2}{5}
\end{bmatrix}$$

6. Mas de lo mismo
7. Tambien. Paso, next.

### 6) Más imagen, nucleo, mono, epi, iso

Sean $f : \mathbb{R}^3 \rightarrow \mathbb{R}^4, f(x_1, x_2, x_3) = (x_1 + x_2, x_1 + x_3, 0, 0)$ y $g: \mathbb{R}^4 \rightarrow \mathbb{R}^2,
g(x_1, x_2, x_3, x_4) = (x_1 − x_2, 2x_1 − x_2)$. Calcular el núcleo y la imagen de $f$, de $g$ y de $g ◦ f$. Decidir si son monomorfismos, epimorfismos o isomorfismos.

> - $f$
>   - $Nu(f)$: queremos buscar $(x,y,z)/ f(x,y,z)=(0,0,0,0)$, me queda que $x+y=0, x+z=0 \Rightarrow x = -y, z = y \Rightarrow Nu(f) = [y(-1,1,1) \in \mathbb{R}^3]$. La base del núcleo es $Nu(f) = \langle (-1,1,1) \rangle$ como no es la solución trivial, **NO** es mono.
>   - $Im(f)$: descomponemos $(x_1 + x_2, x_1 + x_3, 0, 0) = x_1(1,1,0,0) + x_2(1,0,0,0) + x_3(0,1,0,0)$. A ojo sé que es L.D ya que tenemos dos vectores canónicos, así que podemos sacar el vector $(1,1,0,0)$ para formar una base que queda: $Im(f) = \langle(1,0,0,0),(0,1,0,0)\rangle$ está claro que con 2 vectores no generamos todo $\mathbb{R}^4$, por lo tanto **NO** es epi.

> - $g$
>   - $Nu(g)$: queremos buscar $(x,y,z,w) = (0,0)$, me queda que $x-y =0, 2x-y=0 \Rightarrow x = 0, y=0 \Rightarrow Nu(g) = [z(0,0,1,0)+w(0,0,0,1) \in \mathbb{R}^4]$. La base del núcleo es $Nu(g) = \langle(0,0,1,0),(0,0,0,1)\rangle$ como no es el núcleo trivial **NO** es mono.
>   - $Im(g)$: descomponemos $(x_1 − x_2, 2x_1 − x_2) = x_1(1,2)+x_2(-1,-1)$ son L.I ya que si triangulamos nos queda $(1,2), (0,1)$ lo cual forman la base de la imagen $Im(g) = \langle(1,2), (0,1)\rangle$ que generan todo $\mathbb{R}^2$. **SI** es epi.

> - $gof$ notar que $\mathbb{R}^3 \rightarrow \mathbb{R}^2 $
>   - $Nu(gof)$: desarrollamos
>
>       $$f(x,y,z) = (x + y, x + z, 0, 0) $$
>
>       $$g(f(x,y,z)) = g(x + y, x + z, 0, 0) =  ((x + y) − (x + z), 2(x + y) − (x + z)) = (y-z, x+2y-z)$$
>
>       $$gof(x,y,z) = (y-z, x+2y-z)$$
>
>      Queremos que $gof(x,y,z) = (0,0)$ de la primera ecuación nos queda $y = z$ y de la segunda que $x = -z$. Nuevamente la base del núcleo es 
$Nu(gof)= \langle (-1,1,1)\rangle \Rightarrow$ **NO** es mono
>
>   - $Im(gof)$: la salida de $g$ ya vimos que generaba todo $\mathbb{R}^2$ y $f$ no anula los dos primeros valores de entrada para $g$, asi que **SI** es epi
>

 
## Aritmética de punto flotante