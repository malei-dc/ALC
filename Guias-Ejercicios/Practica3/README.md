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