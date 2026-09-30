# Pipe Pressure Drop Calculator

A Python tool that calculates the pressure drop of a fluid flowing through a pipe, given the pipe dimensions and fluid properties.

## About

I built this while going into my second year of Chemical Engineering, as a way to learn Python and apply it to something from my own field rather than abstract exercises. Pipe pressure drop is a core chemical engineering calculation — it comes up in pump sizing, pipe design and process work — so it made a good first project: familiar physics, but real code to make it work. It's also practice, a starting point I intend to keep improving as I get better at Python.

## What it does

The user enters the pipe and fluid details, and the program calculates:

- the **Reynolds number** (whether the flow is laminar or turbulent)
- the **friction factor**
- the **pressure drop** across the pipe

## The engineering behind it

The calculation is a chain, where each result feeds the next:

**1. Cross-sectional area** of the pipe:

    A = π r²

**2. Fluid velocity**, from the volumetric flow rate and area:

    v = Q / A

**3. Reynolds number**, which decides the flow type:

    Re = ρ v D / μ

- Re < 2300 → laminar (smooth, orderly flow)
- Re > 4000 → turbulent (chaotic, mixing flow)

**4. Friction factor**, which depends on the flow type:

- **Laminar:** a direct formula, `f = 64 / Re`
- **Turbulent:** the **Colebrook equation**, which is *implicit* (the friction factor appears on both sides and can't be rearranged out). It's solved numerically using SciPy's `brentq` root-finder.

**5. Pressure drop**, using the Darcy–Weisbach equation:

    ΔP = f (L/D) (ρ v² / 2)

## How to run it

Requires Python with the `math` and `scipy` libraries (both included with the Anaconda distribution).

1. Run `Project.py`.
2. Enter each value when prompted (flow rate, diameter, length, density, viscosity, roughness), all in SI units.
3. The program prints the Reynolds number, friction factor and pressure drop.

## Example

For water in a commercial steel pipe:

| Input | Value |
|---|---|
| Flow rate | 0.05 m³/s |
| Diameter | 0.2 m |
| Length | 100 m |
| Density | 1000 kg/m³ |
| Viscosity | 0.001 Pa·s |
| Roughness | 0.000045 m |

**Output:**

    Reynolds number: 318309.9   (turbulent)
    Friction factor: 0.01633
    Pressure drop (Pa): 10345.6

## Possible improvements

Things I'd like to add as I keep learning:

- handle the transition zone (Re between 2300 and 4000), which the current version doesn't cover
- input validation (catch negative or non-numeric entries)
- plot pressure drop against flow rate
- support for different units (e.g. bar, litres/min)
