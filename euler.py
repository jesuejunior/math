# _*_ coding: utf-8 _*_

def euler(xi, xf):
    x = xi
    y = 1
    dx = 0.5
    nc = (xf - xi)/dx

    print [x, y]

    for i in range(int(nc)):
        dydx = f1(x);
        y = y + dydx * dx;
        x = x + dx;
        print [x,y]
		
#f'(x)
def f1(x):
	return ((-2 * x**3) + (12* x**2) - (20 * x )+ 8.5);

def main():
	print 'Euler'
	euler(0, 4)
  
if __name__ == "__main__":
    main()
