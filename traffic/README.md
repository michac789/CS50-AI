# Traffic

## Experimentation Process

In my first experiment, I tried only using one single layer for the convulational (32 filters, 3x3 kernel) and pooling layer (with 2,2 pool size), added with one single hidden layer and a dropout of 50% just by default (referring to the source code in handwriting.py). However, the result was bad as after 10 epoch, it was only 5.35% accurate which is extremely bad. As a result, I tried adding some more layers for both the convulational and pooling layer with the same default value as before. When there are two convulational layers and two pooling layer, the accuracy was preety good for about 


90.57%
