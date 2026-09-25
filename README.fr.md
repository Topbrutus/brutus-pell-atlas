# Brutus–Pell Atlas

Auteur : **Gabriel St-Pierre**

Ce dépôt regroupe les structures Pell–Brutus dans une seule carte reproductible.

La coordonnée centrale est le rang de Pell :

$$z_P(n)=\min\{k\ge1:n\mid P_k\},$$

avec

$$P_0=0,\quad P_1=1,\quad P_{k+2}=2P_{k+1}+P_k.$$

Pour un entier $C$, une fibre Square-Rank est définie par

$$\mathcal F_C=\{n:z_P(n)=C^2\}.$$

L'atlas relie ensuite les entrées par fibres, collisions de rang, structures miroir, lifts et extensions qui conservent un rang vérifié.

Les rangs inscrits dans le jeu de données de référence sont recalculés par récurrence modulaire exacte.

Le projet ne revendique pas comme nouvelles les propriétés standards des suites de Pell; il organise des constructions, classifications et pistes de recherche sous le namespace Brutus–Pell.
