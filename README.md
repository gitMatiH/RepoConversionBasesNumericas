<h1>Conversor de bases numéricas</h1>
<p>
  Convierte un número de entrada expresado en cierta base al mismo expresado en otra base.
  Contiene implementaciones explícitas e implementaciones nativas de python. 
</p>
<p>
  Aplicación en progreso.
  GUI en Qt en progreso.
</p>
<p>
https://www.udemy.com/course/design-patterns-python <br>
https://www.udemy.com/course/programming-effectively-in-python/ <br>
https://www.udemy.com/course/writing-clean-code/ <br>
https://www.udemy.com/course/python-3-deep-dive-part-1 <br>
https://www.udemy.com/course/python-3-deep-dive-part-2 <br>
https://www.udemy.com/course/python-3-deep-dive-part-3 <br>
https://www.udemy.com/course/python-3-deep-dive-part-4 <br>
https://www.udemy.com/course/python-rest-apis-with-flask-docker-mongodb-and-aws-devops <br>
https://www.udemy.com/course/desktop-gui-python-tkinter/ <br>
https://www.udemy.com/course/automated-software-testing-with-python/ <br>
</p>

<h2>Varios</h2>
<p>
How To Design Large Software Systems <br>
https://www.youtube.com/watch?v=u3YoNpSnmis <br>
Data Collection Project Ideas & Demos <br>
https://www.youtube.com/watch?v=Wx-gL-Dt5rI <br>
How to Convert any Python File to .EXE <br>
https://www.youtube.com/watch?v=CvcSpNm7PzU <br>
¿Cómo PASAR de .PY a .EXE? (Crear EJECUTABLE con Python) <br>
https://www.youtube.com/watch?v=CvcSpNm7PzU <br>
Convert Python To Exe Files <br>
https://www.youtube.com/watch?v=bYLU02QhlUM <br>
</p>
<h2>Artículos</h2>
<p>
Convert binary, octal, decimal, and hexadecimal in Python <br>
https://note.nkmk.me/en/python-bin-oct-hex-int-format/ <br>
Python Program to Convert Decimal to Binary, Octal and Hexadecimal <br>
https://www.datacamp.com/tutorial/python-data-type-conversion <br>
Convert a string of binary, octal, and hexadecimal notation to int <br>
https://note.nkmk.me/en/python-str-num-conversion/ <br>
</p>

'''python
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 255
>>> print(bin(i))
0b11111111
>>> print(oct(i))
0o377
>>> print(hex(i))
0xff
>>> i=16
>>> print(hex(i))
0x10
>>> print(bin(i)[2:])
10000
>>> format(i, 'b')
'10000'
>>> i
16
>>> format(i, 'd')
'16'
>>> int(format(i, 'd'))
16
'''
