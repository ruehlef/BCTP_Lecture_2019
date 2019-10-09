# Examples of the Tuesday afternoon coding session

In this coding session we implemented a simple CNN that learns to classify galaxies using PyTorch. As a training set we use the labeled galaxies provided by the [Galaxy Zoo](https://data.galaxyzoo.org) project. See [http://adsabs.harvard.edu/abs/2008MNRAS.389.1179L](http://adsabs.harvard.edu/abs/2008MNRAS.389.1179L) for more details. The pictures of the galaxies themselves are provided by the [Sloane Digital Sky Survey](https://www.sdss.org) and look like this (Image source: [https://www.sdss.org](https://www.sdss.org))
:

<img src="./galaxy.png" width="300px"/> 

We use the galaxy zoo data release 1 data, which can be downloaded from [https://data.galaxyzoo.org](https://data.galaxyzoo.org). The corresponding images are provided by the data release 7 of [SDSS](http://skyserver.sdss.org/dr7/en/tools/chart/list.asp). I provide a script to download the images and create a file that can be used for training afterwards. To run thi example:

1. Go to website https://data.galaxyzoo.org and download full catalog into a directory named `GalaxyZoo`.
2. Run the **get\_get_images.py** script to download the images into the `GalaxyZoo` directory via `python get_images.py`.
3. Start training the CNN via `python CNN_Classifier.py`.
