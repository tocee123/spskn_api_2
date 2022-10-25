# Variable names
When you name your variables, you can use different naming styles. In python the variable name
-  has to start with letter or `_`
- can contain only alphanumeric characters (A-z, 0-9) and _ 
- names are **case sensitive** (age, AGE and Age are 3 different variables)
- watch out for the space (`my variable` is not understood by the interpreter)
### Example for good variable names
```py
myvar = "John"  
my_var = "John"  
_my_var = "John"  
myVar = "John"  
MYVAR = "John"  
myvar2 = "John"
```
### Example for bad variable names/does not compile
```py
2myvar = "John"  
my-var = "John"  
my var = "John"
```
Good variabel name can be `myvariablename` or `outofmemoryexception`, however it is read very poorly, in the following part we will look at 3 different types of naming conventions
## PascalCase
This is used to name a function/method or a class, the first letter is **C**apital and every other word is capital too
- **O**ut**O**f**M**emory**E**xception
- **D**ate**F**ormat
- **D**atabase**C**onnection
- **L**inked**L**ist
- **E**vent**H**andler
## camelCase
In this case the first letter is **l**ower and the rest of the words are **c**apital, used to name local variables: 
- **j**enkins**S**erver
- **i**teration**C**ount
- **t**omcat**I**nstance
- **g**it**R**epository
- **m**icro**S**ervice
## snake_case
When you separate the words with **_**, the letters in the words are lower
- null_reference_exception
- date_of_birth_of_the_president_of_the_country
- number_of_earthworms_collected_after_rain
- the_last_number_of_pi_counted_by_chuck_norris
