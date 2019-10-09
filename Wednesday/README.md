# Examples of the Wednesday afternoon coding session

We impolemented an A3C reinforcement agent using [ChainerRL](https://github.com/chainer/chainerrl) v0.7.0. We connect our environment using the OpenAI gym interface.

We demonstrate how the agent finds a good spin configuration for the simple problem of a [1D Ising model](https://en.wikipedia.org/wiki/Ising_model) with no external magnetic field and nearest-neighbor interactions in either the ferromagnetic or anti-ferromagnetic phase.

A typical output would look like this:

```
I found an optimal configuration!
↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ 
I started from
↑ ↑ ↓ ↓ ↑ ↑ ↑ ↑ ↑ ↓ ↓ ↑ ↓ ↑ ↑ 
and took the actions
[10, 2, 3, 9, 12]
```

To run the code
1. Install chainerrl: `pip install chainerrl`
2. Download the files into some directory
3. Run with ` python train_a3c_gym.py 8 --env=1DIsing-A3C-v0`. The file train\_a3c\_gym.py is provided by chainerrl v0.7.0 and only contains minor changes to the policy and vlaue function NN.