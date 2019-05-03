# Linear Regression

## What Is This?
This is an example of a **Simple Linear Regression** analysis. 

## How to use this
  1. **Create** a new instance and **Pass** your values:
      * Option 1:
      ```python
      instance = LinearRegression(x, y)
      ```
      * Option 2:
      ```python
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
  - Data: 
    
    **x = [1, 2, 3, 4, 5, 6, 7, 8]** 
    
    **y = [11, 22, 33, 44, 55, 66, 77, 88]**
  - Pass variables
      ```python
      instance = LinearRegression(x, y)
      ```
      
      **What is going to be calculated after you pass you values?**
 
      
      | x | y | (x - x̅)    | (y - ȳ) | (x - x̅) * (y - ȳ) | (x - x̅)<sup>2</sup> | (y - ȳ)<sup>2</sup> |
      | - | - | -----------| ------- | ----------------- | ------------------- | ------------------- |
      |1  |11 | -3.5       |-38.5    |  134.75           |                     |                     |
      |2  |2  | -2.5       |-27.5    |  68.75            |                     |                     |
      |3  |33 | -1.5       |-16.5    |  24.75            |                     |                     |
      |4  |44 | -0.5       |-5.5     |  2.75             |                     |                     |
      |5  |55 | 0.5        |5.5      |  2.75             |                     |                     |
      |6  |66 | 1.5        | 16.5    |  24.75            |                     |                     |
      |7  |77 | 2.5        |27.5     |  68.75            |                     |                     |
      |8  |88 | 3.5        |38.5     |  134.75           |                     |                     |
      
      
     <a href=""><img src="https://latex.codecogs.com/png.latex?\bar{x}&space;=&space;4.5&space;,&space;\bar{y}&space;=&space;49.5&space;,&space;\sum{x}&space;=&space;36.0&space;,&space;\sum{y}&space;=&space;396.0&space;,&space;\sigma{x}&space;=&space;2.45&space;,&space;\sigma{y}&space;=&space;26.94" title="\bar{x} = 4.5 , \bar{y} = 49.5 , \sum{x} = 36.0 , \sum{y} = 396.0 , \sigma{x} = 2.45 , \sigma{y} = 26.94" /></a>
      
  - Get function
      ```python
      myfunc = instance.getLinearRegressionFunction()
      ```
## Equations used
  * Linear Regression formula
  * Standard deviation 
  * Estimated random error formula
  
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


