# Linear Regression

## What Is This?
This is an example of a **Simple Linear Regression** analysis. 

## How to use this
  1. **Create** a new instance and **Pass** your values:
      * Option 1:
      ```python
      x = [...]
      y = [...]
      instance = LinearRegression(x, y)
      ```
      * Option 2:
      ```python
      x = [...]
      y = [...]
      instance = LinearRegression()
      instance.setX(x)
      instance.setY(y)
      ```
  2. **Get** the linear regression equation:
      * **getLinearRegressionFunction()** returns a lambda function. 
      ```python
      myLinearFun = instance.getLinearRegressionFunction()
      ```
      
## Example
  - **Data**: 
    
    <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?x&space;=&space;\begin{bmatrix}&space;1&&space;2&space;&3&space;&4&space;&5&space;&6&space;&7&space;&8&space;\end{bmatrix}" title="x = \begin{bmatrix} 1& 2 &3 &4 &5 &6 &7 &8 \end{bmatrix}" /></a>
    
    <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?y&space;=&space;\begin{bmatrix}&space;11&&space;22&space;&33&space;&44&space;&55&space;&66&space;&77&space;&88&space;\end{bmatrix}" title="y = \begin{bmatrix} 11& 22 &33 &44 &55 &66 &77 &88 \end{bmatrix}" /></a>
    
  - **Create** a new instance and **Pass** your data: 
      ```python
      instance = LinearRegression(x, y)
      ```
      
      **What is going to be calculated after you pass your values?**
       * The **average** of both x and y:
       
           <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bar{x}&space;=&space;4.5&space;,&space;\bar{y}&space;=&space;49.5&space;," title="\bar{x} = 4.5 , \bar{y} = 49.5 ," /></a>
       
       * The **sum** of each variable:
       
           <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?\sum{x}&space;=&space;36.0&space;,&space;\sum{y}&space;=&space;396.0&space;," title="\sum{x} = 36.0 , \sum{y} = 396.0 ," /></a>
       * Using the calculated values, the instance is going to calculate the following values: 
      
          | x | y | (x - x̅)    | (y - ȳ) | (x - x̅) * (y - ȳ) | (x - x̅)<sup>2</sup> | (y - ȳ)<sup>2</sup> |
          | - | - | -----------| ------- | ----------------- | ------------------- | ------------------- |
          |1  |11 | -3.5       |-38.5    |  134.75           |     12.25           |       1482.25       |
          |2  |2  | -2.5       |-27.5    |  68.75            |     6.25            |       756.25        |
          |3  |33 | -1.5       |-16.5    |  24.75            |     2.25            |       272.25        |
          |4  |44 | -0.5       |-5.5     |  2.75             |     0.25            |       30.25         |
          |5  |55 | 0.5        |5.5      |  2.75             |     0.25            |       30.25         |
          |6  |66 | 1.5        | 16.5    |  24.75            |     2.25            |       272.25        |
          |7  |77 | 2.5        |27.5     |  68.75            |     6.25            |       756.25        |
          |8  |88 | 3.5        |38.5     |  134.75           |     12.25           |       1482.25       |

       * The **standard deviation** of both x and y:
           
           <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?\sigma{x}&space;=&space;2.45&space;,&space;\sigma{y}&space;=&space;26.94" title="\sigma{x} = 2.45 , \sigma{y} = 26.94" /></a>
  
  - Get the **lambda** function
      ```python
      myfunc = instance.getLinearRegressionFunction()
      ```
## Equations used
  * Linear Regression formula:
      
      <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?y(x)&space;=&space;a&space;&plus;&space;bx" title="y(x) = a + bx" /></a>
  * Slope:
  
      <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?Slope&space;=&space;r&space;\frac{S_{y}}{S_{x}}" title="Slope = r \frac{S_{y}}{S_{x}}" /></a>
      
  * Standard deviation:
  
      <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?S_{x}&space;=&space;\sqrt{\frac{\sum&space;(x-\bar{x})^{2}}{n&space;-&space;1}}" title="S_{x} = \sqrt{\frac{\sum (x-\bar{x})^{2}}{n - 1}}" /></a>
      
      <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?S_{y}&space;=&space;\sqrt{\frac{\sum&space;(y-\bar{y})^{2}}{n&space;-&space;1}}" title="S_{y} = \sqrt{\frac{\sum (y-\bar{y})^{2}}{n - 1}}" /></a>
  
  * Pearson Correlation Coefficient:
  
    <a href="" target="_blank"><img src="https://latex.codecogs.com/png.latex?r&space;=&space;\frac{\sum((x&space;-&space;\bar{x})(y&space;-&space;\bar{y}))&space;}&space;{\sqrt{\sum&space;(x&space;-&space;\bar{x})^{2}&space;\sum(y&space;-&space;\bar{y})^{2}&space;}}" title="r = \frac{\sum((x - \bar{x})(y - \bar{y})) } {\sqrt{\sum (x - \bar{x})^{2} \sum(y - \bar{y})^{2} }}" /></a>
  
## Note
  * The **getLinearRegressionFunction()** returns a lambda function.
## Built With
* [Python](https://www.python.org/) - Python

## Versioning

We use [Github](https://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/IbrahimNM/BudgetOrganizer/tags).

## Authors

* **Ibrahim Almohaimeed** - [Github account](https://github.com/IbrahimNM)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.


