# Smoke Simulation Using Stable Fluids + Position-Based Dynamics
**Miguel Garcia — Project Summary**

---

## Overview

This project builds a stable, heavy-feeling smoke simulation by combining two complementary techniques: Stable Fluids for grid-based fluid motion and Position-Based Dynamics (PBD) for particle-level control. The result is smooth, slow-motion smoke with natural swirling and unconditional numerical stability.

---

## System Architecture

Two-layer design:

- **Layer 1 — Eulerian Velocity Grid:** handles global fluid flow via advection and projection.
- **Layer 2 — PBD Particle System:** particles ride the velocity field with constraints applied each step.

---

## Part 1: Stable Fluids

### Core Idea

- **Semi-Lagrangian advection** — traces fluid backwards through the velocity field
- **Implicit diffusion** — spreads velocity smoothly without instability
- **Projection for incompressibility** — enforces ∇·u = 0 via a pressure solve
- **Unconditional stability** — remains valid at any timestep Δt

### Solver Steps

1. Add external forces (gravity, buoyancy)
2. Advect velocity field (semi-Lagrangian backtracing)
3. Diffuse velocity (implicit solve for viscosity)
4. Project to divergence-free field (pressure Poisson solve)

### What Stable Fluids Gives

- Natural swirling motion — vortex structures emerge organically
- Stable at any Δt — no blow-up even with large timesteps
- Smooth velocity evolution — no high-frequency noise artifacts

---

## Part 2: Position-Based Dynamics (PBD)

### Core Ideas

- **Position-first updates** — directly correct positions, then derive velocities
- **Constraint projection** — iteratively satisfy distance/density constraints
- **Stable even at large Δt** — complementary to Stable Fluids

### Update Loop

**Predict → Project → Update velocity**

- Predict: `x* = x + v·Δt`
- Project: apply constraints to `x*` (typically 1–3 iterations)
- Update velocity: `v = (x* − x) / Δt`

### How PBD Helps Smoke

- Smooths particle clustering — repulsion constraints prevent overlap
- Removes jitter — constraint solve damps erratic micro-motion
- Produces heavy motion — constrained particles fall slower and drift naturally

---

## Combined Method

Stable Fluids drives the global velocity field (Eulerian / grid-based), while PBD particles ride that field with constraints applied (Lagrangian / particle-based). The two layers are complementary: Stable Fluids provides smooth, swirling flow; PBD adds the heavy, controlled feel.

---

## Results & Takeaways

- **Heavy, slow smoke** — PBD constraints produce natural weight and drift
- **Unconditionally stable** — no numerical blow-up at any timestep
- **Visually rich** — swirling vortices and smooth evolution
