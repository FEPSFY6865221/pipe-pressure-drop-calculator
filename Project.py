# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:31:58 2026

@author: Habib
"""
import math
from scipy.optimize import brentq
def area (r):
    return math.pi * r**2

def velocity(Q, A):
    return Q / A

def reynolds(rho, v, D, mu):
    return(rho * v * D / mu)

def colebrook(Re, eps, D):
    def g(f):
        return 1/f**0.5 + 2*math.log10(eps/D/3.7 + 2.51/(Re*f**0.5))
    return brentq(g, 0.005, 0.1)

def friction(Re, eps, D):
    if Re < 2300:
        return 64 / Re
    else:
        return colebrook(Re, eps, D)
        
def pressure_drop(f, L, D, rho, v):
    return f * (L/D) * (rho * v**2 / 2)

# --- get pipe and fluid details from the user ---
Q   = float(input("Flow rate (m³/s): "))
D   = float(input("Pipe diameter (m): "))
L   = float(input("Pipe length (m): "))
rho = float(input("Fluid density (kg/m³): "))
mu  = float(input("Fluid viscosity (Pa·s): "))
eps = float(input("Pipe roughness (m): "))

# --- run the calculator ---
A  = area(D/2)
v  = velocity(Q, A)
Re = reynolds(rho, v, D, mu)
f  = friction(Re, eps, D)
dP = pressure_drop(f, L, D, rho, v)

print("Reynolds number:", Re)
print("Friction factor:", f)
print("Pressure drop (Pa):", dP)
       
