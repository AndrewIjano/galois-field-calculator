# Galois Field Calculator

## Description
Implements a simple [Galois Field](https://en.wikipedia.org/wiki/Finite_field) calculator.

There is only the `GF(2^8)` and `GF(2^32)` calculator.

## Usage

```bash
$ python3 gf_calculator.py
```

## GF(2^8) Calculator

The `GF(2^8)` calculator is a postfix calculator with the addiction and multiplication operations.

The irreducible polynomial is `m(x) = x^8 + x^4 + x^3 + x + 1`. 

The values must be given in the hexadecimal form.

Example:

```
$ python3 gf_calculator.py
Choose the calculator:
1 - GF(2^8) calculator
2 - GF(2^32) calculator
> 1
Welcome to the GF(2^8) calculator!
Write 'help' to get help
>>> help
This is a Postfix caculator
Write number in GF(2^8) in the hexadecimal form. Ex: 2A
Write '+' to sum the previous two numbers
Write '*' to multiply the previous two numbers
Write 'print' or 'p' to print the stack
Write 'clear' to clear the stack
Write 'q' to exit the calculator
>>> 65
>>> 0e
>>> +
0x6B
>>> 02
>>> *
0xD6
>>> 
```
## GF(2^32) Calculator

The `GF(2^32)` calculator implements just the product of two polinomials `A(x)`, `B(x)` in the `GF(2^32)`, where
```
A(x) = a_3 * x^3 + a_2 * x^2 + a_1 * x + a_0

B(x) = b_3 * x^3 + b_2 * x^2 + b_1 * x + b_0
```
and the coefficients are in `GF(2^8)`.

The irreducible polynomial is `M(x) = x^4 + 1`. 

The coefficients must be given in the hexadecimal form. 

Example:

To calculate the following product:
```
A(x) * B(x) = ((B2)*x^3 +  (55)*x^2 + (87)*x + (3D)) * ((03)*x^3 + (01)*x^2 + (01)*x + (02)) 
```

```
$ python3 gf_calculator.py
Choose the calculator:
1 - GF(2^8) calculator
2 - GF(2^32) calculator
> 2
Welcome to the GF(2^32) calculator!
For a while, there is only the multiplication operation...

A(x) coefficients: b2 55 87 3d
B(x) coefficients: 03 01 01 02

0xEADD650F
```

## License
Released under the MIT License.  See the [LICENSE](LICENSE.txt) file for further details.
