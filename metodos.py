import numpy as np
import sympy as sp
from math import factorial

def FalsaPosicion(f, lim_inf, lim_sup, exactitud):
    func = lambda x: eval(f)
    lim_inf = eval(lim_inf)
    lim_sup = eval(lim_sup)
    exactitud = eval(exactitud)
    if(func(lim_inf)*func(lim_sup) > 0):
        print('La función no cumple el teorema en el intervalo')
    else:
        p_medio= lim_inf- (func(lim_inf)*func(lim_inf - lim_sup))/(func(lim_inf) - func(lim_sup))
        while(np.abs(func(p_medio)) > exactitud):
            p_medio= lim_inf- (func(lim_inf)*func(lim_inf - lim_sup))/(func(lim_inf) - func(lim_sup))
            if(func(lim_inf) * func(p_medio) < 0):
                lim_sup = p_medio
            else:
                lim_inf = p_medio
        print('La raiz de la funcion es ', p_medio)
    return p_medio

def Biseccion(func, lim_inf, lim_sup, exactitud):
    if(func(lim_inf)*func(lim_sup) > 0):
        print('La función no cumple el teorema en el intervalo')
    else:
        while(np.abs(lim_sup - lim_inf) > exactitud):
            p_medio = (lim_inf + lim_sup)/2
            if(func(lim_inf) * func(p_medio) < 0):
                lim_sup = p_medio
            else:
                lim_inf = p_medio
    return p_medio

#############################################################################
def cota_T(f, x_, x0, n):
    x = sp.symbols('x')
    df = sp.diff(f,x,n+1)
    df = sp.lambdify(x,df)
    u=np.linspace(min(x_,x0), max(x_,x0), 1000)
    M=np.max(np.abs(df(u)))
    cota = M*np.abs((x_-x0)**(n+1)/factorial(n+1))
    return cota #Factor de error

def s_taylor(f,x0,n):
    x = sp.symbols('x')
    p=0
    for k in range(n+1):
        df=sp.diff(f,x,k)
        dfx=df.evalf(subs={x:x0})
        f_s=dfx*(x-x0)**k/factorial(k)
        p+=f_s
    return p #Polinomio aproximado

############################################################################

def Euler(func,a,b,h,co):
    f = lambda t,y: eval(func)
    a = eval(a)
    b = eval(b)
    h = eval(h)
    co = eval(co)
    n = int((b-a)/h)
    t = np.linspace(a,b,n+1)
    eu = [co]
    for i in range(n):
        eu.append(eu[i]+h*f(t[i], eu[i]))
    return eu

def Runge(f,a,b,h,co):
    n = int((b-a)/h)
    t = np.linspace(a,b,n+1)
    rk = [co]
    for i in range(n):
        k1=h*f(t[i], rk[i])
        k2= h*f(t[i]+h/2, rk[i]+1/2*k1)
        k3= h*f(t[i]+h/2, rk[i]+1/2*k2)
        k4= h*f(t[i+1], rk[i]+k3)
        rk.append(rk[i]+1/6*(k1+2*k2+2*k3+k4))
        print(k1,k2,k3,k4)        
    return t,rk

##############################################################################

def NewtonR(f,x0,tol):
    x = sp.symbols('x')
    f = eval(f)
    x0 = eval(x0)
    tol = eval(tol)
    df = sp.diff(f, x)
    new = x - f/df
    new = sp.lambdify(x, new)
    x1 = new(x0)
    i= 1
    while (np.abs(x1-x0) > tol):
        x0 = x1
        x1 = new(x0)
        i += 1
    return x1,i

#################################################################################

def Secante(f, x0, x1, tol):
    x2= x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
    while np.abs(x2-x1) > tol:
        x0 = x1
        x1 = x2
        x2 = x1 -f(x1)*(x0-x1)/(f(x0)-f(x1))
    return x2

#################################################################################