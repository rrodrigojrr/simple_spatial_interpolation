# Scripts de interpolação espacial com IDW e RBF
by: Rodrigo Lins da Rocha Júnior

Esse repositório conta com dois scripts simples de interpolação espacial que podem ser usados para qualquer tipo de dado georeferenciado.

## Métodos:

* IDW - Inverse Distance Weighting: IDW é um método clássico de geoestatística. Estima o valor de ponto no espaço fazendo a média dos valores próximos ponderada pelo inverso da distância.
* RBF - Radial Basis Function: RBF tem a premissa semelhante ao IDW. Ou seja, o método estima pontos no espaço utilizando a média dos valores próximos ponderada pela distância. Porém, diferente do IDW, os parâmetros ponderadores não são calculados pelo inverso da distância e sim pela resolução de um sistema de esqueções lineares.

## Funções úteis:

* **reshape_grid**: Converte o array 1D gerado no momento da interpolação para um array 2D que é usado para plots.
* **coordsTransform**: Gera dois arrays (X e Y) de combinações possíveis de coordenadas a partir de dois arrays de sequência de grade.


## Melhorias e contribuição
Como mencionado, esse repositório é bem simples. Novas features serão adicionadas com o tempo.

Se você deseja contribuir com o projeto, por favor, não hesite em mandar um pull request ou me enviar um [email](rodrigo.lins.jr@gmail.com).




