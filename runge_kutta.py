# _*_ coding: utf-8 _*_

#f'(x)
def f1(x):
	return ((-2 * x**3) + (12 * x**2) - (20 * x ) + 8.5)
		
def runge_kutta(xi, xf):
    x = xi
    y = 1
    dx = 0.5
    nc = (xf - xi) / dx
    h = (xf - xi) / nc
    print [x, y]

    for i in range(int(nc)):
        k1 = f1(x)
        k2 = f1(x + (0.5 * h))
        k3 = f1(x + h)

        y = y + ((1./6. * (k1 + (4 * k2) + k3)) * h)
        x = x + dx
        print [x, y]

def main():
	print 'Runge-Kutta'
	runge_kutta(0, 4)
  
if __name__ == "__main__":
    main()
