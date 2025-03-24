# Personal Notes from Attending Online Molssi Python Workshop 

(Check Out the Workshop!)[https://education.molssi.org/python_scripting_cms/]

## Format of Python for Data Processing
- Workshop is done on **Jupiter Notebook** but this notes used **Spyder**

For Anyone Who Never Used Spyder Before:
- can be opened from Anaconda once downloaded or from terminal `spyder`

<img width="262" alt="image" src="https://github.com/user-attachments/assets/b97b9cb2-0eac-45cb-8751-f4a3002133f8" />

(Reccommended Video)[https://www.youtube.com/watch?v=7FwXz1KqFBU]

----

# Lesson 0: Assigning Variables and Data Types

(Link to Lesson 0)[https://education.molssi.org/python_scripting_cms/01-introduction/index.html]

variable_name = variable_value

hashtags are used for comments

example:

<img width="305" alt="image" src="https://github.com/user-attachments/assets/a40cb17f-a1d8-44f4-bb55-f5b9b5b6f72f" />

to print values: `print(deltaG)`

Run script directly from Spyder terminal:

<img width="333" alt="Screenshot 2025-03-24 at 12 47 00 PM" src="https://github.com/user-attachments/assets/d068ce2b-cdc6-4c2f-8b2c-0591c6fa7c1c" />

### Assigning multiple variables

Example script:

`deltaH, deltaS, temp = -541.5, 10.4, 298`

`deltaG = deltaH - temp * deltaS`

`print(deltaG)`

Output should give: `-3640.7000000000003`

### Data Types

`type(deltaG` should give output `float`

Changing Data types:

`deltaG_string = str(deltaG)`

`type(deltaG_string)`

should give output of `str`
   - do `print(type(delta_string))` to actually see output of data type

### Lists

ex:

`energy_kcal = [-13.4, -2.7, 5.4, 42.1]`

Determining its length

`energy_length = len(energy_kcal)`

print list length

`print('The length of this list is', energy_length)`

# Lists

example list:

`energy_kcal = [-13.4, -2.7, 5.4, 42.1]`

Determining its length:

`energy_length = len(energy_kcal)`

`print('The length of this list is', energy_length)`

Printing first element on list 

`print(energy_kcal[0])`

Converting between units

`energy_kilojoules = energy_kcal[1] * 4.184`

`print(energy_kilojoules)`

Output should give: '-11.296800000000001`

### Slices

general syntax:

`new_list = list_name[start:end]`

example:

`short_list = energy_kcal[0:2]`

`print(short_list)`

output should give: `[-13.4, -2.7]`

### For loops

General syntax:

for variable in list:
   do things using variable

example:

<img width="190" alt="image" src="https://github.com/user-attachments/assets/a794d374-4f38-4334-90b0-9b321652089d" />

Appending without creating list to shows NameError:

before creating list:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/684ab4b8-48b2-4273-9cef-60adc2612a1d" />

After creating list:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/122b3855-dd00-4252-a3e1-dad5f393c7a5" />


Output should give: `[-56.0656, -12.1336, 22.593600000000002, 176.1464]`

### Logic Statements

Example: 

<img width="200" alt="image" src="https://github.com/user-attachments/assets/3abe2f57-f615-461b-bad2-6f644a1bd8b3" />

Output should give: `[-56.0656, -11.296800000000001]`

Logic Statements List:
- equal to: `==`
- not equal to: `!=`
- greater than, `<`
- less than, `<`
- greater than or equal to `>=`
- less than or equal to `<=`
- checking more than one condition: use `and`, `or`, and `not`

Example:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/5af68234-2247-4c2b-b7d6-38f096db960c" />

Output: `[-56.0656, -11.296800000000001]`













