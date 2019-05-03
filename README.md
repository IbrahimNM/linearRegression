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
    
    X = [...]
    
    Y = [...]
  - Pass variables
  - Get function

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


