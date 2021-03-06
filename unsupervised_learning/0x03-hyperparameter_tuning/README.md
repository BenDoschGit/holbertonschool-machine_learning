# Hyperparameter_Tuning

1. [Learning Objectives](#learning-objectives)
2. [References](#references)
3. [Tasks](#tasks)
	1. [Initialize Gaussian Process](#0-initialize-gaussian-process)
	2. [Gaussian Process Prediction](#1-gaussian-process-prediction)
	3. [Update Gaussian Process](#2-update-gaussian-process)
	4. [Initialize Bayesian Optimization](#3-initialize-bayesian-optimization)
	5. [Bayesian Optimization - Acquisition](#4-bayesian-optimization---acquisition)
	6. [Bayesian Optimization](#5-bayesian-optimization)
	7. [Bayesian Optimization with GPyOpt](#6-bayesian-optimization-with-gpyopt)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* What is Hyperparameter Tuning?
* What is random search? grid search?
* What is a Gaussian Process?
* What is a mean function?
* What is a Kernel function?
* What is Gaussian Process Regression/Kriging?
* What is Bayesian Optimization?
* What is an Acquisition function?
* What is Expected Improvement?
* What is Knowledge Gradient?
* What is Entropy Search/Predictive Entropy Search?
* What is GPy?
* What is GPyOpt?

## Refrences

* [Structuring Machine Learning Projects (Course 3 of the Deep Learning Specialization)](https://www.youtube.com/playlist?list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b "Structuring Machine Learning Projects (Course 3 of the Deep Learning Specialization)")
* [mathematicalmonk](https://www.youtube.com/watch?v=vU6AiEYED9E "(ML 19.1) Gaussian processes - definition and first examples")
* [Machine learning - Introduction to Gaussian processes](https://www.youtube.com/watch?v=4vGiHC35j9s "Machine learning - Introduction to Gaussian processes")
* [What is the fastest way to compute an RBF kernel in python?](https://stackoverflow.com/questions/47271662/what-is-the-fastest-way-to-compute-an-rbf-kernel-in-python "What is the fastest way to compute an RBF kernel in python?")
* [Radial Basis Function (RBF) Kernel: The Go-To Kernel](https://towardsdatascience.com/radial-basis-function-rbf-kernel-the-go-to-kernel-acf0d22c798a "Radial Basis Function (RBF) Kernel: The Go-To Kernel")
* [Machine learning - Introduction to Gaussian processes](https://www.youtube.com/watch?v=4vGiHC35j9s "Machine learning - Introduction to Gaussian processes")
* [Machine learning - Bayesian optimization and multi-armed bandits](https://www.youtube.com/watch?v=vz3D36VXefI "Machine learning - Bayesian optimization and multi-armed bandits")
* [Martin Krasser - Bayesian optimization](http://krasserm.github.io/2018/03/21/bayesian-optimization/ "Martin Krasser - Bayesian optimization")
* [Martin Krasser - Gaussian processes](http://krasserm.github.io/2018/03/19/gaussian-processes/ "Martin Krasser - Gaussian processes")
* [Bayesian Optimization](https://www.cse.wustl.edu/~garnett/cse515t/spring_2015/files/lecture_notes/12.pdf "Bayesian Optimization")

## Tasks
Create the class GaussianProcess that represents a noiseless 1D Gaussian process:

* Class constructor: def __init__(self, X_init, Y_init, l=1, sigma_f=1):

	* X_init is a numpy.ndarray of shape (t, 1) representing the inputs already sampled with the black-box function
	* Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of the black-box function for each input in X_init
	* t is the number of initial samples
	* l is the length parameter for the kernel
	* sigma_f is the standard deviation given to the output of the black-box function
	* Sets the public instance attributes X, Y, l, and sigma_f corresponding to the respective constructor inputs
	* Sets the public instance attribute K, representing the current covariance kernel matrix for the Gaussian process
*  Public instance method def kernel(self, X1, X2): that calculates the covariance kernel matrix between two matrices:

	* X1 is a numpy.ndarray of shape (m, 1)
	* X2 is a numpy.ndarray of shape (n, 1)
	* the kernel should use the Radial Basis Function (RBF)
	* Returns: the covariance kernel matrix as a numpy.ndarray of shape (m, n)

### [0. Initialize Gaussian Process](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/0-gp.py "0. Initialize Gaussian Process")

Based on 0-gp.py, update the class GaussianProcess:

* Public instance method def predict(self, X_s): that predicts the mean and standard deviation of points in a Gaussian process:
	* X_s is a numpy.ndarray of shape (s, 1) containing all of the points whose mean and standard deviation should be calculated
	* s is the number of sample points
	* Returns: mu, sigma
	* mu is a numpy.ndarray of shape (s,) containing the mean for each point in X_s, respectively
	* sigma is a numpy.ndarray of shape (s,) containing the variance for each point in X_s, respectively

---

### [1. Gaussian Process Prediction](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/1-gp.py "1. Gaussian Process Prediction")

Based on 0-gp.py, update the class GaussianProcess:

* Public instance method def predict(self, X_s): that predicts the mean and standard deviation of points in a Gaussian process:
	* X_s is a numpy.ndarray of shape (s, 1) containing all of the points whose mean and standard deviation should be calculated
		* s is the number of sample points
	* Returns: mu, sigma
		* mu is a numpy.ndarray of shape (s,) containing the mean for each point in X_s, respectively
		* sigma is a numpy.ndarray of shape (s,) containing the variance for each point in X_s, respectively

---

### [2. Update Gaussian Process](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/2-gp.py "2. Update Gaussian Process")

Based on 1-gp.py, update the class GaussianProcess:

* Public instance method def update(self, X_new, Y_new): that updates a Gaussian Process:
	* X_new is a numpy.ndarray of shape (1,) that represents the new sample point
	* Y_new is a numpy.ndarray of shape (1,) that represents the new sample function value
	* Updates the public instance attributes X, Y, and K

---

### [3. Initialize Bayesian Optimization](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/3-bayes_opt.py "3. Initialize Bayesian Optimization")

Create the class BayesianOptimization that performs Bayesian optimization on a noiseless 1D Gaussian process:

* Class constructor def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1, xsi=0.01, minimize=True):
	* f is the black-box function to be optimized
	* X_init is a numpy.ndarray of shape (t, 1) representing the inputs already sampled with the black-box function
	* Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of the black-box function for each input in X_init
	* t is the number of initial samples
	* bounds is a tuple of (min, max) representing the bounds of the space in which to look for the optimal point
	* ac_samples is the number of samples that should be analyzed during acquisition
	* l is the length parameter for the kernel
	* sigma_f is the standard deviation given to the output of the black-box function
	* xsi is the exploration-exploitation factor for acquisition
	* minimize is a bool determining whether optimization should be performed for minimization (True) or maximization (False)
	* Sets the following public instance attributes:
		* f: the black-box function
		* gp: an instance of the class GaussianProcess
		* X_s: a numpy.ndarray of shape (ac_samples, 1) containing all acquisition sample points, evenly spaced between min and max
		* xsi: the exploration-exploitation factor
		* minimize: a bool for minimization versus maximization
* You may use GP = __import__('2-gp').GaussianProcess

---

### [4. Bayesian Optimization - Acquisition](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/4-bayes_opt.py "4. Bayesian Optimization - Acquisition")

Based on 3-bayes_opt.py, update the class BayesianOptimization:

* Public instance method def acquisition(self): that calculates the next best sample location:
	* Uses the Expected Improvement acquisition function
	* Returns: X_next, EI
		* X_next is a numpy.ndarray of shape (1,) representing the next best sample point
		* EI is a numpy.ndarray of shape (ac_samples,) containing the expected improvement of each potential sample
* You may use from scipy.stats import norm

---

### [5. Bayesian Optimization](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/5-bayes_opt.py "5. Bayesian Optimization")

Based on 4-bayes_opt.py, update the class BayesianOptimization:

* Public instance method def optimize(self, iterations=100): that optimizes the black-box function:
	* iterations is the maximum number of iterations to perform
	* If the next proposed point is one that has already been sampled, optimization should be stopped early
	* Returns: X_opt, Y_opt
		* X_opt is a numpy.ndarray of shape (1,) representing the optimal point
		* Y_opt is a numpy.ndarray of shape (1,) representing the optimal function value

---

### [6. Bayesian Optimization with GPyOpt](https://github.com/BenDoschGit/holbertonschool-machine_learning/blob/main/unsupervised_learning/0x03-hyperparameter_tuning/6-bayes_opt.py "6. Bayesian Optimization with GPyOpt")

Write a python script that optimizes a machine learning model of your choice using GPyOpt:

* Your script should optimize at least 5 different hyperparameters. E.g. learning rate, number of units in a layer, dropout rate, L2 regularization weight, batch size
* Your model should be optimized on a single satisficing metric
* Your model should save a checkpoint of its best iteration during each training session
	* The filename of the checkpoint should specify the values of the hyperparameters being tuned
* Your model should perform early stopping
* Bayesian optimization should run for a maximum of 30 iterations
* Once optimization has been performed, your script should plot the convergence
* Your script should save a report of the optimization to the file 'bayes_opt.txt'
* There are no restrictions on imports

Once you have finished your script, write a blog post describing your approach to this task. Your blog post should include:

* A description of what a Gaussian Process is
* A description of Bayesian Optimization
* The particular model that you chose to optimize
* The reasons you chose to focus on your specific hyperparameters
* The reason you chose your satisficing matric
* Your reasoning behind any other approach choices
* Any conclusions you made from performing this optimization
* Final thoughts

---

## Author

[Benjamin Dosch](https://github.com/BenDoschGit)
