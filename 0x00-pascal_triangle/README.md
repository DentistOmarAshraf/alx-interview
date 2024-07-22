### Pascal Triangle

![Pascal Image](https://www.mathsisfun.com/numbers/images/pascals-triangle-add.svg)

![Pascal Triangle](https://www.mathsisfun.com/numbers/images/pascals-triangle-doubles.svg)

### output should be:

```bash
vagrant@ubuntu-focal:~/0x00-pascal_triangle$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
 
vagrant@ubuntu-focal:~/0x00-pascal_triangle$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
