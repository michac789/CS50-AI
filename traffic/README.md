# Traffic

## Experimentation Process

In my first experiment, I tried only using one single layer for the convulational (32 filters, 3x3 kernel) and pooling layer (with 2,2 pool size), added with one single hidden layer and a dropout of 50% just by default (referring to the source code in handwriting.py). However, the result was bad as after 10 epoch, it was only 5.35% accurate which is extremely bad. As a result, I tried adding some more layers for both the convulational and pooling layer with the same default value as before. When there are two convulational layers and two pooling layer, the accuracy was preety good for about 90.57% after 10 epoch. However, adding more layers does not necessary makes it better, as when I added another convulational and pooling layer, the accuracy dropped to 85.68%. It seems that 2 layers work preety fine, so I stick with 2 convulational and 2 pooling layers for the rest of the experiment.

Next, I exprimented with the number of dropouts (continuing using 2 layers from my previous 90.57% result). When I increase the number of dropouts to 70%, the accuracy dropped down to 84.79%, which was what I expected. I then tried to decrease the number of dropouts down to 30%, and the result was better (as expected) with 95.73% accuracy. Adding more sample by further dropping down the dropout rate down to 10% only did make the accuracy a little bit better of 95.8%, and since it was taking way more time, I decided to settle with just 30% dropout rate.


90.57%
85.68%
95.73%
