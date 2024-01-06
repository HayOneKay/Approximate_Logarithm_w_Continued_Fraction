#Aendern Sie hier die werte für die Funktion

#-------------------------------#
#Basis entspricht somit 2/1, bitte nur Ganzzahlen
bruch_basis = (512, 1)
#-------------------------------#
#Argument Entspricht somit 5/1, bitte nur Ganzzahlen
bruch_argument = (4, 1)
#-------------------------------#
#Also Log[bruch_basis](bruch_argument)
#-------------------------------#

from math import floor
MAX_ITER = 20
seemsRational = False
saetze = ["ist ungefähr", "ist"]

#Nur für die Implementierung
class frac(object):

        def __init__(self, numerator, denominator):
            assert denominator != 0, "Null im Nenner"
            self.n = numerator 
            self.d = denominator
            self.st1 = bool(numerator < denominator)

        def simplify(self):
            a = self.n
            b = self.d
            while b:
                a, b = b, a % b
            self.n = floor(self.n / a)
            self.d = floor(self.d / a)
        
        def addInt(self, _val):
            num = _val * self.d
            self.n += num
            self.simplify()
        
        def addFrac(self, _val):
            self.n = self.n * _val.d + _val.n * self.d
            self.d = _val.d * self.d
            self.simplify()        
        
        def __add__(self, _val: object):
            if _val.__class__ == int :
                return self.addInt(_val)
            elif _val.__class__ == self.__class__:
                return self.addFrac(_val)
            return None
        
        def subInt(self, _val):
            num = _val * self.d
            self.n -= num
            self.simplify()
        
        def subFrac(self, _val):
            self.n = self.n * _val.d - _val.n * self.d
            self.d = _val.d * self.d
            self.simplify()	        
        
        def __sub__(self, _val: object):
            if _val.__class__ == int :
                return self.subInt(_val)
            elif _val.__class__ == self.__class__:
                return self.subFrac(_val)
            return None
            
        def mulInt(self, _val):
            self.n *= _val
            self.simplify()
        
        def mulFrac(self, _val):
            self.n *= _val.n
            self.d *= _val.d
            self.simplify()        
        
        def __mul__(self, _val: object):
            if _val.__class__ == int :
                return self.mulInt(_val)
            elif _val.__class__ == self.__class__:
                return self.mulFrac(_val)
            return None

        def divInt(self, _val):
            self.d *= _val
            self.simplify()
            
        def divFrac(self, _val):
            self.n *= _val.d
            self.d *= _val.n
            self.simplify()

        def __truediv__(self, _val: object):
            if _val.__class__ == int :
                return self.divInt(_val)
            elif _val.__class__ == self.__class__:
                return self.divFrac(_val)	
            return None		
        
        def __str__(self):
            if self.d == 1:
                return str(self.n)
            return f"{self.n}/{self.d}"
            
        def eqInt(self, _val):
            return (_val*self.d == self.n)

        def eqFrac(self, _val):
            return bool(self.n * _val.d == _val.n * self.d)
        
        def gtInt(self, _val):
            return bool(self.n > _val * self.d)

        def gtFrac(self, _val):
            return bool(self.n * _val.d > _val.n * self.d)

        def reciprocal(self):
            num1 = self.n
            num2 = self.d
            self.n = num2
            self.d = num1 

        def __eq__(self, _val):
            if (_val.__class__ == int):
                return self.eqInt(_val)
            elif (_val.__class__ == self.__class__):
                return self.eqFrac(_val)
            return None

        def __gt__(self, _val):
            if (_val.__class__ == int):
                return self.gtInt(_val)
            elif (_val.__class__ == self.__class__):
                return self.gtFrac(_val)
            return None	

        def __ge__(self, _val):
            return bool((self > _val) or (self == _val))
        
        def __lt__(self, _val):
            return not (self >= _val)

        def __le__(self, _val):
            return bool((self < _val) or (self == _val))

#Nur für die Implementierung
class continuedFrac(frac):
    def __init__(self, _val : list):
        l = len(_val)
        if (l == 1):
            self.n = 1
            self.d = _val[0]
            print(self.n, " ", self.d)
            return
    
        self.n = 1
        self.d = _val[-1]
        for i in range(-2, - (len(_val)), -1):
            self + _val[i]
            self.simplify()
            self.reciprocal()
        self + _val[0]
        self.simplify()
    
    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return str(f"{self.n}/{self.d}")

#Nur für die Implementierung
def check_log_conditions(arg, base):
    assert base > 0, "Unerlaubte Basis"
    assert arg > 0, "Unerlaubtes Argument"
    if (0 < arg < 1):
        if (base > 1):
            return True    
    elif (0 < base < 1):
        if (arg > 1):
            return True      
    elif (0 < arg < 1 and 0 < base < 1):
        return bool(base > arg)
    else:
        return False

#Nur für die Implementierung
def logarithmus(basis : frac, other : frac, genauigkeit : int):
        if other == 1:
            return {"AlsBruch": 0, "AlsListe": [0]}
        #Variablen Deklarieren/Eingabe
        base = frac(basis.n, basis.d)
        base.simplify()
        of = frac(other.n, other.d)
        of.simplify()
        cont_frac = []
        isNegative = check_log_conditions(of, base)

        if (((of > 1) == False)): of.reciprocal()
        if ((base > 1) == False): base.reciprocal()
        
        #Haupt-Aktion
        for iteration in range(0, genauigkeit if bool((genauigkeit <= 20) & (genauigkeit >= 1)) else MAX_ITER):
            exp = 0
            
            if (of == base):		
                print("Lucky Rational!\n") 
                cont_frac.append(exp + 1)
                istRational = True
                break
            
            while (of > base):		
                of / base 
                exp += 1
                if (of == base): 
                    istRational = True
                    break
            
            cont_frac.append(exp)
            base, of = of, base
        
        fraction = continuedFrac(cont_frac)
        
        #Noch das Vorzeichen Dranhängen
        if (isNegative):
            for num in range(0, len(cont_frac) - 1):
                if cont_frac[num] > 0:
                    cont_frac[num] = cont_frac[num] * - 1
                    fraction * - 1
                    break
        
        #Ergebnis Returnen
        return {"AlsBruch": fraction.__str__(), "AlsListe": cont_frac}

if __name__ == "__main__":
    basis = frac(bruch_basis[0], bruch_basis[1])
    von = frac(bruch_argument[0], bruch_argument[1])
    x = logarithmus(basis, von, MAX_ITER)
    print(f"Log{basis.__str__()}({von.__str__()}) {saetze[int(seemsRational)]}")
    print(f"Als Bruch: {x.__getitem__('AlsBruch')}")
    print(f"Als Liste: {x.__getitem__('AlsListe')}\n")