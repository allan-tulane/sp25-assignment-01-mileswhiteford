

# CMPS 2200 Assignment 1

**Name:**Miles Whiteford


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, $2^{n+1} \in O(2^n)$. This is beacuse 2^{n+1} is equal to 2*2^n which is a just a constant multiplied by 2^n, which in O notation would be 2^n
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, it is not. Using the limit method we see that the limit of $2^{2^n} / 2^n$ as n goes to infinity would be equal to infinity, since it can be rewritten as 2^{{2^n}-n}, which would grow exponentially as n grows. This means that $2^{2^n} is not \in O(2^n)$
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, similarly to the last problem, $n^{1.01}$ is going to grow much faster than $\mathrm{log}^2 n$, meaning that there limit approaching infinity would be infinity, meaning that this is fasle.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?
.  Yes, because their limit when approaching infinity is equal to infinty, $n^{1.01} \in \Omega(\mathrm{log}^2 n)$
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, intuitively we can see that $\sqrt{n}$ grows at a much faster rate than $(\mathrm{log} n)^3$, meaning that it is not $O((\mathrm{log} n)^3)$
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, as somewhat explained in the previous answer, $\sqrt{n}$ grows at a much faster rate than $(\mathrm{log} n)^3$ which means that their limit as n approaches infinity would be infinity, meaning that $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function recursively finds the xth number of the fibonacci sequence by recursively adding the previous two numbers in the sequence together (as is the defintion of the fibonacci sequence) until the base case is reached in which either foo(0) returns 0 (because the 0th element is 0), or foo(1) returns 1 (because the 1st element is 1). 
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
Both the work and the span of this function are O(n), since this function will always iterate over the list of length n exactly n times only once. 
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  longest_run_recursive's work is W(n) = 2W(n/2)+O(1) which means that the work is O(nlogn).
.  Each call recursively splits each side of the list again which makes the span S(n) = O(logn)
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm? 
  In this case, the work would be W(n) = W(n/2)+O(n) which makes the work O(nlogn)
  The span in this case would not change, remaining S(n) = O(logn)

.  
.  
.  
.  
.  
.  
.  
.  

