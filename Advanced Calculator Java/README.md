### Reference Image
![image](https://user-images.githubusercontent.com/54449603/197407828-44e264da-0b7c-4eff-89d0-927e8d027fec.png)

### Brief
The above image shows the calculator we are building in this project. We can perform various mathematical operations & calculations.

### Description
 - The screenshot attached at the end shows the calculator we have built in this project. We can perform various mathematical operations & calculations just by clicking the equivalent  buttons of the calculator in the GUI. I have tried to make it simple and easy to use in the [Calculator GUI](https://github.com/shounakbasu/Python-Games-and-Projects/blob/main/Advanced%20Calculator%20Java/calculator.java).

 - Previouly, before making the GUI, the user had to refer to the image as GUI and type in characters which in turn were interpreted by the calculator as various operators or operands and the results will be shown after calculation is performed. This is Still implemented by [AdvCalculator.java](https://github.com/shounakbasu/Python-Games-and-Projects/blob/main/Advanced%20Calculator%20Java/AdvCalculator.java).

- **Note** : 
    - The calculator at present can handle only one mathematical operation at a time. The results need to be cleared using `C` button before performing second operation,
    - for arithmetic function **Sqrt** or **Squareroot** first enter in the operand then the operator.
    - for arithmetic functions **1/x** or **Reciprocal** first enter in the operand then the operator.
    - for arithmetic function **x^2** or **Square** first enter in the operand then the operator.
    - The input is given by the user by pressing the buttons (which are internally taken in the form of String consisting of lowercase characters only)

 ### Improvisation 1
  - GUI added for the calculator to make the user experience more smooth

 ### Improvisations **to be** made
  - BODMAS rule is to be implemented to handle multiple operations in one go.
  
### Screenshot of GUI made
![image](https://user-images.githubusercontent.com/54449603/198872178-cfac9aed-882a-486d-a447-295e7d36f6dd.png)

#### Mapping of characters (used and implemented internally)
  ```
'a' --> 'R' or Square root
'b' --> '0'
'c' --> '.'
'd' --> '='
'e' --> '1'
'f' --> '2'
'g' --> '3'
'h' --> '+'
'i' --> '4'
'j' --> '5'
'l' --> '-'
'm' --> '7'
'n' --> '8'
'o' --> '9'
'p' --> '*'
'q' --> 'S' or Square
'r' --> 'F' or Fraction
's' --> 'C' or Clear/Restart
't' --> '/'
  ```

#### Credits:
I got this idea from an assigment given in a NPTEL course called [Programming in Java](https://onlinecourses.nptel.ac.in/noc20_cs08/course). It was a good course to learn about Java.
