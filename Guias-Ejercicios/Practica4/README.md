# Práctica 4: Autovalores y autovectores.

### 1) Polinomio característico de matrices

Calcular el polinomio característico, los autovalores y los autovectores de la matriz $A$ en cada uno de los siguientes casos (analizar por separado los casos $\mathbb{K} = \mathbb{R}$ y $\mathbb{K} = \mathbb{C}$):

$$A = \begin{pmatrix} 0 & a \\
-a & 0\end{pmatrix}, a \in \mathbb{R}$$


> El polinomio característico se calcula como: $det(\lambda I-A)$ entonces nos queda que el polinomio característico es:
>
> $$det(\lambda \begin{pmatrix} 1 & 0 \\
0 & 1\end{pmatrix} - \begin{pmatrix} 0 & a \\
-a & 0\end{pmatrix}) = det\begin{pmatrix} \lambda & -a \\
a & \lambda \end{pmatrix}$$
>
> $$det\begin{pmatrix} \lambda & -a \\
a & \lambda \end{pmatrix} = \lambda^2 + a^2$$
>
> Los autovalores son las raíces del polinomio característico:
>
> $$\lambda^2 + a^2 = 0 \Rightarrow \lambda = \pm ai$$
>
> - En $\mathbb{K} = \mathbb{R}$ el polinomio no tiene raíces reales, así que no hay autovalores reales.
> - En $\mathbb{K} = \mathbb{C}$ las raices son $\lambda_1 = ai$ y $\lambda_2 = -ai$. Entonces hay dos autovalores complejos conjugados.
>
> Calculamos los autovectores para cada autovalor:
>
> - Caso $\lambda = ai$
> 
> $$(ai . \begin{pmatrix}1 & 0 \\ 
0 & 1\end{pmatrix} - \begin{pmatrix} 0 & a \\
-a & 0\end{pmatrix})v = 0 \Rightarrow \begin{pmatrix}ai & -a \\ 
a & ai\end{pmatrix} v = \begin{pmatrix} 0 \\
0\end{pmatrix}$$
>
> $$\begin{pmatrix}ai & -a & | & 0 \\ 
a & ai & | & 0\end{pmatrix} \overset{if_2-f_1}{\rightarrow} \begin{pmatrix}ai & -a & | & 0 \\ 
0 & 0 & | & 0\end{pmatrix}$$
>
> Tomamos la primera ecuanción: $aix -ay = 0 \Rightarrow y = ix$ entonces el primer autovalor es:
>
> $$S_{\lambda = ai} =  \langle (1, i) \rangle$$
>
> - Caso $\lambda = -ai$
> 
> $$(-ai . \begin{pmatrix}1 & 0 \\ 
0 & 1\end{pmatrix} - \begin{pmatrix} 0 & a \\
-a & 0\end{pmatrix})v = 0 \Rightarrow \begin{pmatrix}-ai & -a \\ 
a & -ai\end{pmatrix} v = \begin{pmatrix} 0 \\
0\end{pmatrix}$$
>
> $$\begin{pmatrix}-ai & -a & | & 0 \\ 
a & -ai & | & 0\end{pmatrix} \overset{if_2+f_1}{\rightarrow} \begin{pmatrix}-ai & -a & | & 0 \\ 
0 & 0 & | & 0\end{pmatrix}$$
>
> Tomamos la primera ecuanción: $-aix -ay = 0 \Rightarrow y = -ix$ entonces el primer autovalor es:
>
> $$S_{\lambda = -ai} =  \langle (1, -i) \rangle$$

$$B = \begin{pmatrix} 0 & 2 & 1 \\
-2 & 0 & 2 \\
-1 & -2 & 0\end{pmatrix}$$

> Calculamos el polinomio caracteristico $det(\lambda I - B)$:
>
> $$\lambda \begin{pmatrix} 1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1\end{pmatrix} - \begin{pmatrix} 0 & 2 & 1 \\
-2 & 0 & 2 \\
-1 & -2 & 0\end{pmatrix} = \begin{pmatrix} \lambda & -2 & -1 \\
2 & \lambda & -2 \\
1 & 2 & \lambda\end{pmatrix}$$
>
> $$det\begin{pmatrix} \lambda & -2 & -1 \\
2 & \lambda & -2 \\
1 & 2 & \lambda\end{pmatrix}= \lambda^3 + 4 + -4 -(-\lambda + -4\lambda+-4\lambda) = \lambda^3 +9\lambda = \lambda(\lambda^2+9)$$
>
> Los autovalores son las raices del polinomio característico, en este caso son:
>
> $$\lambda = 0 \text{ y } \lambda = \pm 3i$$
>
> Calculamos los autovectores para cada autovalor:
>
> - Caso $\lambda = 0$
> 
> $$(0 . \begin{pmatrix}1 & 0 & 0\\ 
0 & 1 & 0 \\
0 & 0 & 1\end{pmatrix} - \begin{pmatrix} 0 & 2 & 1 \\
-2 & 0 & 2 \\
-1 & -2 & 0\end{pmatrix})v = 0 \Rightarrow \begin{pmatrix} 0 & -2 & -1 \\
2 & 0 & -2 \\
1 & 2 & 0\end{pmatrix} v = \begin{pmatrix} 0 \\
0 \\
0 \end{pmatrix}$$
>
> 1. $-2y -z = 0 \Rightarrow z=-2y$
> 2. $2x-2z = 0 \Rightarrow 2x+4y = 0 \Rightarrow x = -2y$
> 3. $-x-2y = 0 \Rightarrow 2y-2y = 0$ OK
>
> $$S_{\lambda=0} = \langle(-2,1,-2) \rangle$$
>
> > - Caso $\lambda = 3i$
> 
> $$(3i . \begin{pmatrix}1 & 0 & 0\\ 
0 & 1 & 0 \\
0 & 0 & 1\end{pmatrix} - \begin{pmatrix} 0 & 2 & 1 \\
-2 & 0 & 2 \\
-1 & -2 & 0\end{pmatrix})v = 0 \Rightarrow \begin{pmatrix} 3i & -2 & -1 \\
2 & 3i & -2 \\
1 & 2 & 3i\end{pmatrix} v = \begin{pmatrix} 0 \\
0 \\
0 \end{pmatrix}$$
>
>
> $$S_{\lambda=3i} = meRindo$$

$$C = \begin{pmatrix} 3 & 1 & 0 \\
-4 & -1 & 0 \\
4 & -8 & -2\end{pmatrix}$$

> Calculamos el polinomio característico $(\lambda I - C)$
>
> $$\lambda \begin{pmatrix} 1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1\end{pmatrix} - \begin{pmatrix} 3 & 1 & 0 \\
-4 & -1 & 0 \\
4 & -8 & -2\end{pmatrix} = \begin{pmatrix} \lambda-3 & -1 & 0 \\
4 & \lambda+1 & 0 \\
-4 & 8 & \lambda+2\end{pmatrix}$$
>
> $$det\begin{pmatrix} \lambda-3 & -1 & 0 \\
4 & \lambda+1 & 0 \\
-4 & 8 & \lambda+2\end{pmatrix} = (\lambda +2) . [(\lambda -3)(\lambda +1)-(-1).4] = $$
>
> $$=(\lambda +2) . [(\lambda^2-2\lambda+1)] = (\lambda +2) . (\lambda -1)^2$$
>
> Los autovalores son:
>
> - $\lambda = 1$ (con multiplicidad algebraica 2)
> - $\lambda = -2$ 
>
> Calculamos los autovectores para cada autovalor: