# Development Task 1
# Lowest Common Ancestor


## Brief:
>To provide a program solution to the [Lowest Common Ancestor](https://en.wikipedia.org/wiki/Lowest_common_ancestor) problem. You are to implement a solution to the basic problem.
>
>+You may assume that the graph is structured as a "binary tree" (as you explore the problem, you may find that this simplification helps you reach a solution). You will find a great deal of sample code on how to solve this problem.
>
>+It is not enough simply to find and hack together a solution and submit it to me. My interest (and grading approach) is in how you build and validate your solution. This is now your opportunity to follow this model.
>
>
>**You will be graded based on your adherence to the following procedure:**
>
>-Choose a unit testing framework. A comprehensive by language list is available [here](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks).
>
>-Create a repository on a git service such as GitHub. Your work will be implemented in this repository.
>
>-Define a set of initial unit tests that capture the basic expected behaviour. This will require you to create sample data and also to identify the basic API for your solution.
>
>-Build your initial solution, testing it against your test code until it is working.
>
>-Refine the solution, expanding your test cases to deal with awkward parameters and edge cases that push the limits of your solution, enhancing your solution to deal with these.
>
>An obvious question will probably arise for you in reading this: how do I know that I have written sufficient test code? Well, that's for you to decide. You are done, when you believe no parameter set passed to your code could break it in a way that your test code does not already capture. You will be assessed based on a concept known as [code coverage](https://en.wikipedia.org/wiki/Code_coverage).
>
>
>**Submission:**
>You **must** commit regularly to your repository. If we do not see evidence of stepwise development progress, then we will withhold marks.
>Expect 0 for a repository with a single commit, no matter how excellent the implementation.
>You might thus perform a series of commits over a development session.
>A commit point does not necessitate the pushing of the commit to the online repository at that moment in time.
>
>
>**Deadline:** _Tuesday 2nd October_


***

## My Approach
I plan to write this code and its unit tests in Python. I have never used Python before.
1. I will read about unit testing in Python
2. I will sketch a few binary trees with nodes selected and their LCA marked. I will try to include as many edge cases as I can, such as cases where:
   1. one of the selected nodes is the LCA
   2. the selected nodes are the same
   3. one of the selected nodes is not in the graph
3. I will construct tests for each of the sample graphs I have drawn
4. I will construct a `Node` class and a `BinaryTree` class and the necessary functionality to pass the tests
5. I will run the tests and correct the classes as needed.

## Design Decisions
1. A node can be its own Lowest Common Ancestor if the other node(s) is/are a) itself b) a descendent of the node
2. If one of the nodes is not in the graph, the function will return an error
