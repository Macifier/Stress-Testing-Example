# Stress-Testing-Example
This repo shows example of testing your fine tuned algo with alteranate algo that always return right result
but takes more time computationally. 
# Algo Objective
Find the maximum product of two distinct num- bers in a sequence of non-negative integers.<br/>
Input: A sequence of non-negative integers.<br/>
Output: The maximum value that can be obtained by multiplying two different elements from the sequence.
Example Input - <br/>
Input - 3 <br/>
        1 2 3 <br/>
Output - 6         
# Process 
In this two algo are defined to achieve objective <b>mainSolution.py</b> is fine tuned algo <br/>
where as <b>alteranateSolution.py</b> algo is used to check algo provided in mainSolution.py<br/>
<b>test_generator.py</b> file generates tests to check both algo gives equal result<br/>
if output of both algo are not equal on certain input then find a bug then run tests again.<br/>
# Running 
You can run stress testing by running command<br/> 
<b>python3 main.py</b> 10 -<b> no of test to perform </b> 500 -<b> seed value for random generator 

