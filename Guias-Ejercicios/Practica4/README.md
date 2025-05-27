# Práctica 4: Autovalores y autovectores.

### 1) Polinomio característico de matrices

Calcular el polinomio característico, los autovalores y los autovectores de la matriz $A$ en cada uno de los siguientes casos (analizar por separado los casos $\mathbb{K} = \mathbb{R}$ y $\mathbb{K} = \mathbb{C}$):

$$A = \begin{pmatrix} 0 & a \\
-a & 0\end{pmatrix}, a \in \mathbb{R}$$


> El polinomio característico se calcula como: $\lambda I-A$ entonces nos queda que el polinomio característico es:
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
> 