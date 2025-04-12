# Práctica 2: Aritmética de punto flotante. Número de condición.

## Transformaciones lineales

### 1) Aplicación lineal

Determinar cuáles de las siguientes aplicaciones son lineales.

1. $f: \mathbb{R}^3 \rightarrow \mathbb{R}^2, f(x1, x2, x3) = (x_2 − 3x_1 + \sqrt{2}x_3 , x_1 − \frac{1}{2}x_2)$

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

2. $f: \mathbb{R}^2 \rightarrow \mathbb{R}^2, f(x1, x2) = (x_1 + x_2, |x_1|)$

    >- En el $(0,0)$ la función se anula
    >- Sean $(a,b)$ y $(x,y)$
    >    - $f((a,b)+(x,y)) = f(a+x, b+y) = (a+x+b+y,|a+x|)$
    >    - $f(a,b) + f(x,y) = (a+b, |a|) + (x+y, |x|) = (a+b+x+y, |a|+|x|)$
    >
    > No es una transfomación lineal ya que si tomo $a = -1$ y $x = 3$:
    >
    > $$|a| + |x| = 1 + 3 = 4 \neq 2 = |-1+3| = |a+x| $$

3. $f: R^{2\times 2} → R, f(a_{11}, a_{12}, a_{21}, a_{22}) = a_{11}.a_{22}-a_{12}.a_{21}$ (Es la determinante)

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
    >   $$f(A) = 1 * 4 - 2 * 3 = -2, f(B)= 5*8-6*7=-2 \Rightarrow f(A) + f(B) = -4$$
    >
    >   $$f(A+B) = 6*12-8*10 =-8$$
    >
    > Concluimos que el determinante no es una transformación lineal.

4.  $f: R^{2\times 2} → R^{2\times 3}, f(a_{11}, a_{12}, a_{21}, a_{22}) = (a_{22}, 0, a_{12}+a_{21}, 0, a_{11}, a_{22}- a_{11})$

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

>    
> Se concluye que $f$ es lineal