__author__ = 'Ivan'

import  math
import numpy as np


class AbsFinder:
    pass



class GoldenRatio (AbsFinder):

    def findMin(self,a,b,f,e=10E-6):
        k = (math.sqrt(5)-1)/2
        c = b - k * (b - a)
        d = a + k * (b - a)
        fc = f(c)
        fd = f(d)
        while((b - a) > e):
            if(fc < fd):
                b = d
                d = c
                c = b - k * (b - a)
                fd = fc
                fc = f(c)

            else:
                a = c
                c = d
                d = a + k * (b - a)
                fc = fd
                fd = f(d)
        return (a + b)/2


class Simpleks (AbsFinder):

    def findMin(self,F,X0,alfa,beat,gama,epsilon):
        X=self.calculatePoints()
        while():#neki uvjet
            h,l=self.calculateIndex(X)
            Xc=self.calculateCentroid()
            Xr = self.refleksija()
            if( F(Xr)<F(X[l])):
                Xe = self.ekspanzija();
                if(F(Xe)<F(X[l])):
                    X[h] = Xe
                else:
                    X[h] = Xr

            else:
                if( F(Xr)>F(X[j])):
                    za svaki (j=0..n, j!=h ):
                        if(F(Xr)<F(X[h])):
                            X[h] = Xr
                        Xk = self.kontrakcija();
                        if (F(Xk)<F(X[h])):
                            X[h] = Xk
                        else:
                            #pomakni sve tocke prema X[l];

                else:
                    X[h] = Xr

    def calculateIndex(X):
        h=0
        l=0
        max=X[0]
        min=X[0]
        for i in range(1,len(X)):
            if(max<X[i]):
                max=X[i]
                h=i
            if(min>X[i]):
                min=X[i]
                l=i
        return h,l

    def ekspanzija():
        pass

    def kontrakcija():
        pass

    def refleksija():
        pass

    def calculatePoints(self):
        return np.array()



class HookeJeeves (AbsFinder):

    def findMin(self,x0,F,Dx=1):
        xP = x0
        xB = x0
        while(): ##TODO: uvjet zaustavljanja?!
            xN = self.search(xP,Dx,F)  # definiran je potprogram
            if (F(xN)<F(xB)):    # prihvaæamo baznu toèku
                xP = 2*xN-xB  # definiramo novu tocku pretrazivanja
                xB = xN

            else:
                Dx=Dx/2
                xP = xB        # vracamo se na zadnju baznu tocku

        return xB
    def search(self,xP,Dx,F):
        x = xP
        for i in range(0,len(x)):
            P = F(x)
            x[i] = x[i] + Dx       # povecamo za Dx
            N = F(x)
            if( N>P):             # ne valja pozitivni pomak
                x[i] = x[i] - 2*Dx  # smanjimo za Dx
                N = F(x)
            if( N>P):          # ne valja ni negativni
                x[i] = x[i] + Dx;  # vratimo na staro


        return x

def unimodalni( h, tocka, l, r,f):

    l = tocka - h
    r = tocka + h
    m = tocka

    step = 1

    fm = f(tocka)
    fl = f(l)
    fr = f(r)

    if(fm < fr and fm < fl):
        return(l,r)
    elif(fm > fr):
        while(fm>fr):
            l = m
            m = r
            fm = fr
            step*=2
            r = tocka + h * step
            fr = f(r)

    else :
        while(fm>fl):
            r = m;
            m = l;
            fm = fl;
            step*=2
            l = tocka - h * step
            fl = f(l);
    return(l,r)