# Demo_wxPython
This Repository's programs used Python and wxPython

## mock_super_pi
As Demo application.  
This program's model is [superπ](http://ja.wikipedia.org/wiki/スーパーπ)  
→ ftp://pi.super-computing.org/

### Pi algorithm
```
def ppii(n) :
	a , b , i = 10 ** n , 10 ** n , n * 8 + 1
	while i >= 3 :
		a , i = (a + b + b ) * (i / 2) / i , i - 2
	return a - b
```
