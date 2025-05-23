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

### 7) Experimento en [practica2.ipynb](/Guias-Ejercicios/Practica2/practica2.ipynb)

Realizar las siguientes operaciones en Python. En todos los casos, pensar: ¿cuál es el resultado esperado? ¿coincide con el obtenido? ¿a qué se debe el problema (si lo hay)? (Notamos $\epsilon$ al épsilon de la máquina. Puede obtenerse importando la librería ```numpy``` como ```np``` y ejecutando el comando ```np. finfo (np.float32) .eps```).

1. Tomando $p =1e34, q = 1$, calcular $p + q − p$.
2. Tomando $p = 100, q =1e−15$, calcular $(p + q) + q$ y $((p + q) + q) + q$. Comparar con $p + 2q$ y con $p + 3q$ respectivamente.
3. $0.1+0.2 == 0.3$
4. $0.1+0.3 == 0.4$
5. $1e−323$
6. $1e−324$
7. $\frac{\epsilon}{2}$
8. $(1+\frac{\epsilon}{2})+ \frac{\epsilon}{2}$
9. $1+ (\frac{\epsilon}{2}+\frac{\epsilon}{2})$
10. $((1+\frac{\epsilon}{2})+\frac{\epsilon}{2})-1$
11. $(1+(\frac{\epsilon}{2}+\frac{\epsilon}{2}))-1$
12. $sen(10^j \pi)$ para $1\leq j \leq 25$
13. $sen(\frac{\pi}{2}+10^j \pi)$ para $1\leq j \leq 25$

### 8) Convergencia de sumatorias

Mostrar que una serie divergente de términos que tienden a 0 (e.g $\sum \frac{1}{n}$) podría resultar convergente en aritmética de punto flotante. ¿Qué debería ocurrir para que
el resultado numérico sea Inf? ¿Cuál es la mejor estrategia para realizar numéricamente una sumatoria de términos positivos?

> Cuando tenemos una serie armónica que matemáticamente diverge, es decir crece hasta el $\infty$ aunque sus términos tienden a $0$.
>
> El problema es que en punto flotante (```float64```) los valores dejan de contrubuir una vez que:
>
> $$\frac{1}{n}<\epsilon \ast S$$
>
> Donde $S$ es el valor acumulado de la suma. Entonces llega un punto en el que ```S + 1/n == S``` y deja de cambiar el valor acumulado como se ve en el ejercicio enterior con los experimentos. Así la serie parece "converger", pero solo los terminos se vuelven muy chicos para afectar la suma
>
```python
import numpy as np

S = 0.0
n = 1
while True:
    term = 1/n
    if S + term == S:
        break
    S += term
    n += 1

print(f"Resultado de la suma: {S}")
print(f"Número de términos usados: {n}")
```
## Normas vectoriales y sucesiones

### 11) Constantes de equivalencia entre las normas

Si $x \in \mathbb{R}^n$, probar que las constantes de equivalencia entre las normas $∥ · ∥_1$ y $∥ · ∥_2$ y entre las normas $∥ · ∥_2$ y $∥ · ∥_{\infty}$ vienen dadas por:

$$\|x\|_{\infty} \leq \|x\|{\scriptsize 2} \leq \sqrt{n}\|x\|{\scriptsize \infty}$$

> - Primero veamos que $\|x\|_{\infty} \leq \|x\|{\scriptsize 2}$ para todo $x \in \mathbb{R}^n$. Si tomo ambas normas al cuadrado se deduce que: 
>
>   $$\|x\|^2{\scriptsize 2} = (\sum_{i=1}^n |x{\scriptsize i}|^2) \geq |x{\scriptsize max}|^2 = \|x\|_\infty^2 $$
>
>   pues al ser todos los términos de la suma no negativos, el máximo de los términos debe ser menor o igual que la suma completa.
>
> - Para la parte de $\|x\|{\scriptsize 2} \leq \sqrt{n}\|x\|_{\infty}$ vamos a ver un $M = \|x\|{\scriptsize \infty} = max{\scriptsize i}|x{\scriptsize i}|$ entonces:
>
>   $$\sum_{i=1}^n |x{\scriptsize i}|^2 \leq \sum_{i=1}^n M^2 = nM^2 \Rightarrow \|x\|{\scriptsize 2} = (\sum_{i=1}^n |x{\scriptsize i}|^2)^\frac{1}{2} \leq (nM^2)^\frac{1}{2} = \sqrt{n}M = \sqrt{n}\|x\|_\infty$$
>
> $$\square$$

$$\frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2 \leq \|x\|_1$$

> - Primero veamos que $\|x\|{\scriptsize 2} \leq \|x\|{\scriptsize 1}$ para todo $x \in \mathbb{R}^n$. Si tomo ambas normas al cuadrado se deduce que: 
>
>   $$\|x\|^2{\scriptsize 2} = (\sum_{i=1}^n |x{\scriptsize i}|^2) \leq (\sum_{i=1}^n |x{\scriptsize i}|)^2 = \|x\|^2{\scriptsize 1} $$
>
>   Esta desigualdad se cumple por la desigualdad cuadrática $(a+b)^2 = a^2 +2ab + b^2 \geq a^2 + b^2$ siendo $a,b$ numeros positivos como es en nuestro caso.
>
> - Ahora veamos que $\frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2$
>
>   Para esta parte usamos la desigualdad de Cauchy-Schwarz: $\langle x,y \rangle \leq \|x\|_2 \ast \|y\|_2$
>
>   Tomamos:
>
>   - $x = (x_1, ...,x_n) \in \mathbb{R}^n$
>   - $y = (sgn(x_1), ...,sgn(x_n))$ donde sgn es -1 si $x_i$ es negativo o 1 si es positivo y 0 si es 0
>
>   Con esos sabemos que $\langle x,y \rangle = \|x\|_1$ y que $\|y\|_2 = \sqrt{cantNoCeros} \leq \sqrt{n}$. Reemplazando nos queda que:
>
>   $$\langle x,y \rangle =\|x\|_1 \leq \|x\|_2 \ast \|y\|_2 \leq \|x\|_2 \ast \sqrt{n}$$
>
>   $$\Rightarrow \frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2$$
>
>   $\square$

### 12) Sucesiones

Para cada una de las siguientes sucesiones $[x_n]{\scriptsize n\in N}$, determinar si existe $lim_{n\rightarrow \infty} x{\scriptsize n}$ y en caso afirmativo hallarlo.

1. $x_n = \frac{1}{n}$

> $lim_{n\rightarrow \infty} \frac{1}{n} = 0$

2. $x_n = \frac{n^2+1}{n^2-1}$

> Cuando $n\rightarrow \infty$ los $\pm 1$ se vuelven despreciable, por lo que los términos dominates de esta sucesión son los $n^2$ en el numerador y denominador que se cancelan, por lo que el $lim_{n\rightarrow \infty} \frac{n^2+1}{n^2-1} = 1$

3. $x_n = (-1)^n$

> Esta sucesión no tiene límite ya que oscila entre $1$ y $-1$ dependiendo si $n$ es par o impar.
 
4. $x_n = (-1)^n e^{-n}$ 

> Esta sucesión tiene dos partes:
>
> - $(-1)^n$: oscila entre $1$ y $-1$
> - $e^{-n}$: tiende a $0$ cuando $n \rightarrow \infty$ ya que es una función exponencial decreciente.
>
> Por lo tanto el $lim_{n\rightarrow \infty} (-1)^n e^{-n} = 0$ 

### 13) Sucesiones en $R^2$

Para cada una de las siguientes sucesiones de vectores $[x{\scriptsize n}]_{n\in \mathbb{N}}$ en $\mathbb{R}^2$, determinar si existe $lim{\scriptsize n\rightarrow \infty} x{\scriptsize n}$, y en caso afirmativo hallarlo.

1. $x_n = (1+\frac{1}{n},3)$

> $lim_{n\rightarrow \infty}(1+\frac{1}{n},3) = (1,3)$

2. $x_n = ((-1)^n,e^{-n})$

> Para que una sucesión en $\mathbb{R}^2$ exista, ambas coordenadas deben converger, en este caso en la primer coordenada oscila entre 1 y -1, por lo que no existe el límite. Por lo que el vector completo tampoco.

3. 

$$x_n = \begin{cases}(\frac{1}{n}, 0) & \text{si n es par} \\
(0,\frac{-1}{n}) & \text{si n es impar}\end{cases}$$

> Acá necesitamos analizar ambos casos:
>
> - Si $n$ es par: $(\frac{1}{n}, 0) \rightarrow (0,0)$ cuando $n \rightarrow \infty$
> - Si $n$ es impar: $(0,\frac{-1}{n}) \rightarrow (0,0)$ cuando $n \rightarrow \infty$
>
> Por lo tanto se concluye que $x_n \rightarrow (0,0)$ cuando $n \rightarrow \infty$

4. $x_n = (\frac{1}{2^n}, 4, sen(\pi n))$

> - La primera coordenada $\rightarrow 0$ cuando $n \rightarrow \infty$
> - La segunda es una cte, y la tercera siempre da 0 ya que $sen(k\pi) = 0$
>
> Por lo tanto $(\frac{1}{2^n}, 4, sen(\pi n)) \rightarrow (0,4,0)$ cuando $n \rightarrow \infty$

### 14) Sucesiones con normas

Dada una sucesión de vectores $[x{\scriptsize n}]_{n\in \mathbb{N}} \subset \mathbb{R}^k$ y dos normas $∥ · ∥{\scriptsize a}$ y $∥ · ∥{\scriptsize b}$ de
$\mathbb{R}^k$, usando la equivalencia de normas, probar

$$∥ x{\scriptsize n} ∥{\scriptsize a} \longrightarrow 0 \Longleftrightarrow ∥ x{\scriptsize n} ∥{\scriptsize b}\longrightarrow 0 \text{ cuando } n \rightarrow \infty$$

## Normas matriciales

### 16) Constantes de equivalencia entre normas

Si $A \in \mathbb{R}^{n\times n}$, probar que las constantes de equivalencia entre las normas $\| . \|{\scriptsize 1}$ y $\| . \|{\scriptsize 2}$ y entre las normas $\| . \|{\scriptsize 2}$ y $\| . \|_\infty$ dadas por:

Calcular los coeficientes para la equivalencia vectorial y matricial entre las normas $\|.\|{\scriptsize 1}$ y $\|.\|_\infty$

> ---
>
> Si una norma matricial está inducida por una norma vectorial $\|.\|$, entonces:
>
> $$\|A\| = \underset{x\neq0}{sup} \frac{\|Ax\|}{\|x\|} = \underset{\|x\|=1}{sup} \|Ax\|$$
>
> Por eso vamos a usar relaciones conocidas entre las normas vectoriales para deducir relaciones entre normas matriciales.
>
>---

$$\frac{1}{\sqrt{n}}\| A \|{\scriptsize \infty} \leq \| A \|{\scriptsize 2} \leq \sqrt{n} \| A \|_\infty$$

> Demo:
>
> Sabemos que para cualquier vector $x \in \mathbb{R}^n$:
>
> $$\frac{1}{\sqrt{n}}\| x \|{\scriptsize \infty} \leq \| x \|{\scriptsize 2} \leq \sqrt{n} \| x \|_\infty$$
>
> Ahora usamos esto para comparar normas matriciales. Como la norma de $A$ está inducida por la norma del vector, tenemos:
>
> - Cota superior: 
>
>   $$\|A\|_2 =  \underset{\|x\|_2 = 1}{sup} \|Ax\|{\scriptsize 2} \leq \underset{\|x\|_2 = 1}{sup} \sqrt{n} \|Ax\| {\scriptsize \infty} =  \sqrt{n} \underset{\|x\|_2 = 1}{sup} \|Ax\| {\scriptsize \infty} $$
>
>   Pero
>
>   $$\underset{\|x\|{\scriptsize 2} = 1}{sup} \|Ax\| {\scriptsize \infty} \leq \underset{\|x\|_\infty = 1}{sup} \|Ax\| {\scriptsize \infty} = \|Ax\| {\scriptsize \infty}$$ 
>
>   por lo tanto:
>
>   $$\|A\|_2 \leq \sqrt{n}\|A\|{\scriptsize \infty}$$
>
> - Cota inferior:
>
> $$\|A\|{\scriptsize \infty} = \underset{\|x\|_\infty = 1}{sup}\|Ax\|{\scriptsize \infty} \leq \underset{\|x\|_2 = \sqrt{n}}{sup}\|Ax\|{\scriptsize \infty} = \underset{\|x\|_2 = 1}{sup}\|A\sqrt{n}x\|{\scriptsize \infty} = \sqrt{n}\underset{\|x\|_2 = 1}{sup}\|Ax\|{\scriptsize \infty}$$
>
> Y de ahi:
>
> $$\|A\|{\scriptsize \infty} \leq \sqrt{n} \|A\|{\scriptsize 2} \Rightarrow \frac{1}{\sqrt{n}}\|A\|_\infty \leq \|A\|{\scriptsize 2}$$
>
> $$\square$$

$$\frac{1}{\sqrt{n}}\| A \|_1 \leq \| A \|_2 \leq \sqrt{n} \| A \|_1$$

> De forma analoga se calcula esto, te lo debo

### 17) Definición de norma 1 e inf matricial

Probar que para toda $A \in \mathbb{R}^{n \times n}$

$$\|A\|{\scriptsize \infty} = \underset{1\leq i \leq n}{max} \sum_{j=1}^n |a{\scriptsize ij}|$$

Es decir que la norma infinita de una matriz $A$ es max de las normas por fila

> Demo: 
>
> Llamemos $k$ a la fila que maximiza, es decir:
>
> $$\underset{1\leq i \leq n}{max}(\sum_{j=i}^n |a{\scriptsize ij}|) = \sum_{j=i}^n |a{\scriptsize kj}|)$$
>
> Si hay mas de un maximo tomamos cualquiera. Podemos suponer que $\sum_{j=1}^n |a{\scriptsize kj}| > 0$ de otro modo el resultado es inmediato. Llamemos $z$ al vertor de los signos de los elementos de esa fila $z=(sg(a_{k,1}),...,sg(a_{k,n}))$. Si algún $a{\scriptsize ki} = 0$ tomamos $sg(a{\scriptsize k1}) = 0$. Como la fila no es nula, $z\neq 0$. Luego $\|z\|{\scriptsize \infty} = 1$ ya que es tomar el max de $z$.
>
> $$\|A\|{\scriptsize \infty} = \underset{\|x\| {\scriptsize \infty} = 1}{max} \|Ax\|{\scriptsize \infty} \geq \|Az\|{\scriptsize \infty} \geq \sum_{j=1}^n a {\scriptsize ij} sg(a{\scriptsize ij}) = \sum_{j=1}^n |a{\scriptsize ij}| = \underset{1\leq i \leq n}{max} \sum_{j=1}^n |a{\scriptsize ij}|$$
>
> Esto prueba un lado de la desigualdad.
>
> Para la otra desigualdad, sea $x \in \mathbb{R}^n$ tal que $\|x\|{\scriptsize \infty}=1$, luego para todo $1\leq j \leq n, |x{\scriptsize j}| \leq \|x\|_{\infty} = 1$ y entonces, para cualquier elemento $i$ del vector $Ax$
>
> $$|[Ax]{\scriptsize i}| = |\sum_{j=1}^n a{\scriptsize ij} x {\scriptsize j}| \leq  |\sum_{j=1}^n a{\scriptsize ij}| \leq \underset{1\leq i \leq n}{max} (\sum_{j=1}^n |a{\scriptsize ij}|)$$
>
> Vimos que:
>
> $$1 )\|A\|{\scriptsize \infty} \geq \underset{1\leq i \leq n}{max} (\sum_{j=1}^n |a{\scriptsize ij}|)$$
> 
> $$2)\|A\|{\scriptsize \infty} \leq \underset{1\leq i \leq n}{max} (\sum_{j=1}^n |a{\scriptsize ij}|)$$
>
> Por ende tienen que ser iguales. $\square$

$$\|A\|{\scriptsize 1} = \underset{1\leq j \leq n}{max} \sum_{i=1}^n |a{\scriptsize ij}|$$

Es decir que la norma-1 de una matriz $A$ es max de las normas por columna

> Lo debo, pero calculo que es similar a arriba

### 18) Estimación Estocástica de la Norma-2 de una Matriz Mediante Muestreo Aleatorio en la Bola Unitaria

Se quiere estimar la norma-2 de una matriz $A \in \mathbb{R}^{n \times n}$ como el máximo del valor $∥Ax∥{\scriptsize 2}/∥x∥{\scriptsize 2}$ entre varios vectores $x \in \mathbb{R}^3$ no nulos generados al azar. Hacer un programa que
reciba una matriz $A$ y luego

- genere los primeros 100 términos de la siguiente sucesión:

    $$s{\scriptsize 1}=0, s{\scriptsize k+1} = max[s_k, \frac{\|Ax{\scriptsize k}\|{\scriptsize 2}}{\|x{\scriptsize k}\|{\scriptsize 2}}] $$

    donde los $x_k \in \mathbb{R}^3$ son vectores no nulos generados al azar en la bola unitaria: $B = [x :∥x∥_2 ≤ 1]$.

- grafique la sucesión calculada, junto con el valor exacto de la norma de la matriz.

Recordar que tanto la norma-2 puede calcularse con el comando ```np.linalg.norm```. Tener en cuenta que los vectores generados al azar (comando ```np.random.random```) tienen coordenadas en el intervalo [0, 1].

> En el archivo [practica2.ipynb](/Guias-Ejercicios/Practica2/practica2.ipynb) el codigo.
>
> ![](/Guias-Ejercicios/Practica2/graficos/18.png)
>
     A =  [[0.37454012 0.95071431 0.73199394]
           [0.59865848 0.15601864 0.15599452]
           [0.05808361 0.86617615 0.60111501]]
    iteracion 1 de la estimacion: 0
    iteracion 2 de la estimacion: 1.5473778966512244
    iteracion 3 de la estimacion: 1.5634298026819895
    iteracion 4 de la estimacion: 1.6457297869764551
    ...
    iteracion 99 de la estimacion: 1.6457297869764551
    norma exacta: 1.666728164305919

> - Como estoy generando vectores al azar en la bola unitaria de $\mathbb{R}^3$, es poco probable que alguno sea exactamente el vector que maximiza ese cociente. 
> - Con más iteraciones (por ejemplo, 10,000 en lugar de 100), es posible que la estimación se acerque más a la norma exacta, pero nunca garantiza que la iguale, porque es un método estocástico.
>
> ---
> 
> Un método estocástico es un procedimiento que implica aleatoriedad o probabilidad para obtener una solución aproximada a un problema. A diferencia de un método determinista (que siempre produce el mismo resultado para la misma entrada), un método estocástico puede dar resultados ligeramente diferentes cada vez que se ejecuta, porque usa números aleatorios como parte del proceso.
>
> ---

## Condición de matrices

### 19) Estabilidad y sensibilidad de sistemas lineales

Se tiene el sistema $Ax = b$

1. Sea $x$ la solución exacta y $\overset{\sim}{x}$ la solución obtenida numéricamente. Se llama residuo al vector $r := b − A \overset{\sim}{x}$ (residuo). Si notamos $e = x − \overset{\sim}{x}$ (error), mostrar que:

    $$\frac{1}{cond(A)} \frac{\|r\|}{\|b\|} \leq \frac{\|e\|}{\|x\|} \leq cond (A) \frac{\|r\|}{\|b\|} $$

> Demo:
>
> 1. Veamos algunas relaciones 
>
>       Sabemos que: 
>
>       $$Ae = A(x-\overset{\sim}{x}) = Ax - A\overset{\sim}{x} = b - A\overset{\sim}{x} = r \Rightarrow Ae = r$$
>
>       Entonces como $A$ invertible:
>
>       $$e = A^{-1}r \Rightarrow \|e\| = \|A^{-1}r\| \leq \|A^{-1}\| \|r\| $$
>
>       Ahora como también pasa que $Ax = b$
>
>       $$\|x\| = \|A^{-1}b\| \leq \|A^{-1}\|.\|b\| \Rightarrow \frac{1}{\|x\|} \geq \frac{1}{\|A^{-1}\|.\|b\|}$$
>
> 2. Cota superior:
>
>       $$\frac{\|e\|}{\|x\|} = \frac{\|A^{-1}r\|}{\|x\|} \leq \frac{\|A^{-1}\| \|r\|}{\|x\|} \overset{multiplico \text{ y } divido \text{ } A}{=} \|A^{-1}\| \|A\| \frac{\|r\|}{\|A\| .\|x\|} \leq cond(A)\frac{\|r\|}{\|b\|}$$
>
> 3. Cota inferior
>
> $$\frac{\|e\|}{\|x\|} = \frac{\|e\|}{\|A^{-1}b\|} \geq \frac{\|e\|}{\|A^{-1}\| \|b\|} = \frac{\|A^{-1}r\|}{\|A^{-1}\| \|b\|}$$
>
> NOTA: si vale que $\|A^{-1}r\| \geq \frac{1}{\|A\|}\|r\|$ gané, PREGUNTAR.

¿Cómo se puede interpretar este resultado?

> - $\frac{\|e\|}{\|x\|}$: el error relativo de la solución.
> - $\frac{\|r\|}{\|b\|}$: el erro relativo de la medición.
> - $cond(A) = \|A\|.\|A^{-1}\|$: número de condición representa cuán sensible es la solución a pretubaciones.
>
> Interpretación:
>
> 1. El error relativo está acotado por el error de la medición relativo, escalado por el número de condición.
> 2. No basta con que el residuo sea pequeño para asegurar que el error lo sea también.
> 3. Si $cond(A) \approx 1$ entonces error y residuo relativos son similares.

2. En lugar del dato exacto $b$ se conoce una aproximación $\overset{\sim}{b}$. $\overset{\sim}{x}$ es tal que $A\overset{\sim}{x} = \overset{\sim}{b}$. Probar
que:

    $$\frac{1}{cond(A)} \frac{\|b-\overset{\sim}{b}\|}{\|b\|} \leq \frac{\|x-\overset{\sim}{x}\|}{\|x\|} \leq cond (A) \frac{\|b-\overset{\sim}{b}\|}{\|b\|} $$

> La demo es análogo al anterior.

¿Cómo se puede interpretar este resultado?

> Este resultado te dice:
>
> - El error relativo en la solución $x$ depende directamente del error relativo en los datos $b$, y está amplificado por el número de condición.
> - Si $cond(A)≫1$, un pequeño error en los datos puede generar un gran error en la solución.
> - En cambio, si $cond(A)≈1$, entonces el error en $x$ es proporcional al error en $b$.

### 20) Calcular número condición y experimentos

sea

$$A= \begin{bmatrix}
3 & 0 & 0 \\
0 & \frac{5}{4} & \frac{3}{4} \\
0 & \frac{3}{4} & \frac{5}{4}
\end{bmatrix}$$

1. Calcular $cond_{\infty}(A)$

> Sabemos que $cond_{\infty}(A) = \|A\| * \|A^{-1}\|$
>
> Para calcular $\|A\|_{\infty}$ es el máximo de la suma de los modulos en la fila:
>
> - Fila 1: $|3| + 0 + 0 = 3$
> - Fila 2: $0 + |\frac{5}{4}| + |\frac{3}{4}| = 2$
> - Fila 2: $0 + |\frac{3}{4}| + |\frac{5}{4}| = 2$
>
> Entonces queda que $max(3,2,2) = 3 \Rightarrow \|A\|_{\infty} = 3$
>
> Ahora para invertir la matriz $A$ usamos la estructura especial que tiene la matriz
>
> $$A= \begin{bmatrix}
3 & 0  \\
0 & B
\end{bmatrix} \Rightarrow A^{-1} = \begin{bmatrix}
\frac{1}{3} & 0  \\
0 & B^{-1}
\end{bmatrix}$$
>
> Entonces para invertir $B$ tenemos que calcular la determinante y cambiar los signos de la siguiente forma:
>
> $$B^{-1} =\frac{1}{det(B)} \begin{bmatrix}
a & -b  \\
-b & a
\end{bmatrix}$$
>
> Donde $a = \frac{5}{4}$ y $b= \frac{3}{4}$ entonces para calcular la $det(A) = a . a - b . b = \frac{25}{16} - \frac{9}{16} = 1$
>
> Entonces queda que:
>
> $$ A^{-1} = \begin{bmatrix}
\frac{1}{3} & 0 & 0 \\
0 & \frac{5}{4} & -\frac{3}{4} \\
0 & -\frac{3}{4} & \frac{5}{4}
\end{bmatrix}$$
>
> Lo cual a vista sale que $\|A^{-1}\|_{\infty} = 2 \Rightarrow cond(A) = 3 .2 = 6$

2. ¿Cuán chico debe ser el error relativo en los datos $(\frac{\|b-\overset{\sim}{b}\|}{\|b\|})$, si se desea que el error relativo en la aproximación de la solución $(\frac{\|x-\overset{\sim}{x}\|}{\|x\|})$ sea menor que $10^{-4}$ en $\|.\|_{\infty}$?

> Por el ejercicio anterior sabemos que:
>
> $$\frac{\|x-\overset{\sim}{x}\|}{\|x\|} \leq cond (A) \frac{\|b-\overset{\sim}{b}\|}{\|b\|}$$
>
> Como ya calculamos que $cond(A)= 6$ y queremos que $\frac{\|x-\overset{\sim}{x}\|}{\|x\|}< 10^{-4}$ despejamos el error relativo:
>
> $$6.\frac{\|b-\overset{\sim}{b}\|}{\|b\|} < 10^{-4} \Rightarrow \frac{\|b-\overset{\sim}{b}\|}{\|b\|} < \frac{10^{-4}}{6} = 1.666*10^{-5}$$

3. Realizar experimentos numéricos para verificar las estimaciones del ítem anterior. Considerar $b = (3, 2, 2)^t$, que se corresponde con la solución exacta $x = (1, 1, 1)^t$. Generar vectores de error aleatorios, normalizarlos para que su norma sea tan chica como la estimada en el item anterior y perturbar $b$ obteniendo $\overset{\sim}{b}$. Finalmente, resolver $A\overset{\sim}{x} = \overset{\sim}{b}$ y verificar que $\|\overset{\sim}{x} − x\| < 10^{−4}$.