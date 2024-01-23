# Buffons needle problem for $k$ crossings
## Purpose and setup
This Python script allows the user to simulate the probability of getting exactly $k$ crossings when a needle of length $l$ is dropped onto a floor with parallel horizontal lines that are equidistant by $d$.  The purpose of this script is to provide us with an empirical estimate of the probability of getting $k$ crossings so that the mathematical derivations that have been derived can be upheld. To convince yourself, I highly recommend you read the mathematical derivations presented below, run the code for your choice of `d` and `l`, and lastly verify the mathematical expressions using the interactive file I created in Desmos under Additional resources.

The condition for this Python script is that $d\leq l$. In that case, the number of possible crossings $k$ is simply given by $0\leq k\leq \lfloor{l/d}\rfloor = m$.  The geometrical setup is presented in the following figure. 
![296607120-2b09023a-653f-4bee-9e22-083652ec2b3e-modified](https://github.com/Thidius/buffons-k-crossings/assets/121384892/a83a0f92-8148-457e-b946-9cdb8a7dfbc2)

## Prerequisites
Ensure you have the following Python libraries installed:

- `matplotlib`
- `numpy`

## Usage
Open the script in a Python environment.
Modify the `no_of_needles`, `l`, and `d` parameters as needed.
Run the script to visualize the needle dropping simulation and the resulting histogram of crossings.


## Parameters
`no_of_needles`: Number of needles to drop during the simulation.
`l`: Length of the needle.
`d`: Distance between parallel lines.

## Simulation Process
1. Parallel Lines Setup: Lines are drawn parallel at a distance `d` from each other.
2. Needle dropping loop: Random needles are dropped, and the script calculates the number of crossings for each needle.
3. Visualization: The script generates the calculated probabilities which are showcased with a plot, providing insights into the distribution.


## Mathematical derivation for the probabilities
The needle is dropped as in the figure above, with a distributed $\theta \in \mathcal{U}[0,\pi/2]$ and $y\in\mathcal{U}(0,d)$. These two ranges are sufficient to cover the sample space we are interested in because of symmetry reasons. Also, we will keep $y$ as an open set to ignore the special cases when the needle precisely crosses the line and accept it as null measure. 


### Case $k= 0$

To derive the probabilities of getting exactly $k$ crossings, we will firstly impose a condition on our $\theta$. Note that the result we will derive is simply for $0$ < $k$ < $m$. The case $k=0$ is covered by studying the common Buffons needle problem for a long needle. In https://en.wikipedia.org/wiki/Buffon%27s_needle_problem the probability of getting at least $1$ crossing is derived, which means the probability of getting $k=0$ crossings is simply given by

$$ P(0 \ \text{crossings}) = 1 - P(\text{at least one crossing})$$ 

### Case $0$ < $k$ < $m$

We initialize the problem by working with a simpler case, and hopefully it will become clearer on how we can extrapolate the result. Firstly study the figure below
![Skärmbild 2024-01-14 184905-modified](https://github.com/Thidius/buffons-k-crossings/assets/121384892/c62b2389-044e-46af-9926-88dde4d5fc55)

We are interested in finding out the probability of getting exactly $1$ crossing. Note that the minimum angle that suffices this condition is given by $\theta_\text{min} = \arcsin \frac{1\cdot d - y}{l}$ simply by using trigonometry. First subtracting the left dashed white distance $1\cdot d$ with the uniformly distributed $y$ gives us the displacement in the $y$ direction, which gives us the shorter green dashed distance, and the hypotenuse is then trivially given by $l$. 

Similarly we can deduce that the the maximum angle $\theta$ is given by $\theta_\text{max} = \arcsin \frac{2\cdot d - y}{l}$. Therefore we have the condition for getting $1$ crossing to be: 

$$ \arcsin \frac{1\cdot d - y}{l} \leq \theta < \arcsin \frac{2\cdot d - y}{l}$$

It's very easy to extend this argument for a total of $k$ crossings, then the condition simply becomes

$$ \arcsin \frac{k\cdot d - y}{l} \leq \theta < \arcsin \frac{(k+1)\cdot d - y}{l}$$

Note that we haven't included the right end in the range of $\theta$ since then we will have $k+1$ crossings, trivially then the left end is included. To find the probability of getting $k$ crossings we have to integrate our joint probability density function, but since the ingoing random variables are independent, they are simply multipled.

$$ P(k \ \text{crossings}) = \int_0^d \int_{\arcsin \frac{k\cdot d - y}{l}}^{\arcsin \frac{(k+1)\cdot d - y}{l}} \frac{1}{\pi/2 \cdot d} d\theta dy$$

### Case $k = m$

For calculating the probability of getting $m$ crossings, we utilize firstly that the probability of getting at least $1$ crossing is well documented previously, see for instance the derivation once again in the link https://en.wikipedia.org/wiki/Buffon%27s_needle_problem. This means that we can find the probability of getting $m$ crossings by

$$P(m \ \text{crossings}) = P(\text{at least one crossing}) -P(k=1,2,...,m-1)= $$

$$ = \frac{2l}{\pi d} \left(\frac{d}{l} \arccos\frac{d}{l} + 1 - \sqrt{1-\left(\frac{d}{l}\right)^2}\right) - \sum_{k=1}^{m-1} P(k \ \text{crossings})$$

Notice however that if we define 

$$I(k) = \int_0^d \int_{0}^{\arcsin \frac{k\cdot d - y}{l}} \frac{1}{\pi/2 \cdot d} d\theta$$

then $P(k \ \text{crossings}) = I(k+1) - I(k)$ which means that 

$$\sum_{k=1}^{m-1} P(k \ \text{crossings}) = \sum_{k=1}^{m-1} I(k+1)-I(k) = I(m) - I(1)$$ 

becomes a simply telescoping sum, meaning we end up with

$$P(m \ \text{crossings}) = \frac{2l}{\pi d} \left(\frac{d}{l} \arccos\frac{d}{l} + 1 - \sqrt{1-\left(\frac{d}{l}\right)^2}\right) - I(m) + I(1)$$

## Additional resources
I have also created a Desmos environment where I have tried to visualize the integrals for each $k$. It can also be used for verifying the results provided by the Python simulation. Sliders are included to play around with $l$ and $d$, and all the probabilities calculated above are collected in a folder. I hope you will enjoy it!

[Desmos Interactive](https://www.desmos.com/calculator/r2fjyw7jjb)

