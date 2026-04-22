# IT-360: Computer Graphics for Visual Effects

**Miguel Garcia** — Course Repository

A semester-long collection of simulations, experiments, and research built in Python (OpenGL / PyOpenGL) and p5.js, covering foundational 2D graphics through advanced physics-based rendering techniques.

---

## Table of Contents

- [Course Overview](#course-overview)
- [HW1 — OpenGL Fundamentals](#hw1--opengl-fundamentals)
- [Midterm — Physics-Based Simulations](#midterm--physics-based-simulations)
- [Midterm Presentation — Hair & Fur Paper Breakdown](#midterm-presentation--hair--fur-paper-breakdown)
- [Final Project — Smoke Simulation](#final-project--smoke-simulation)
- [Other Experiments](#other-experiments)
- [Setup & Running](#setup--running)

---

## Course Overview

IT-360 covers modern techniques and core algorithms in computer graphics, progressing from 2D rendering fundamentals to physically-based simulation:

| Topic | Tools |
|---|---|
| 2D Graphics & Color | OpenGL, PyOpenGL |
| Animation & Interaction | GLFW, mouse/keyboard events |
| Crowd & Particle Systems | Python, OpenGL |
| Physics Simulation (Rope, Smoke) | PBD, Stable Fluids |
| Hair & Fur Rendering | Research paper analysis |

---

## HW1 — OpenGL Fundamentals

**`HW1/`** — Progressive exercises building up to an interactive animated scene.

| File | Description |
|---|---|
| `circles.py` | Draw filled and outlined circles using `GL_TRIANGLE_FAN` |
| `mouse.py` | Mouse-driven circle interaction — click and drag |
| `anim.py` | Two circles bouncing and wrapping across the viewport |
| `crowd.py` | 50 circles with random velocities, collision detection, and drag |
| `spawn.py` | Dynamic circle spawning on mouse click |

**Key techniques:** `GL_TRIANGLE_FAN`, GLFW window/input handling, coordinate space mapping, real-time animation loops.

**Dependencies:** `glfw`, `PyOpenGL`

```bash
cd HW1
pip install -r requirements.txt
python crowd.py
```

---

## Midterm — Physics-Based Simulations

**`Project /`** — Three interconnected simulations implementing Position-Based Dynamics (PBD).

| File | Description |
|---|---|
| `point.py` | Single particle under gravity and boundary constraints |
| `rope.py` | Multi-segment rope with distance constraints and damping |
| `particle_smoke.py` | Particle smoke system driven by buoyancy and turbulence |

**Core algorithm — Position-Based Dynamics:**

```
Predict:  x* = x + v·Δt
Project:  apply constraints to x* (distance, boundary, density)
Update:   v = (x* − x) / Δt
```

This approach guarantees stability at any timestep by operating directly on positions rather than forces.

### Rope Simulation

| | |
|---|---|
| ![Rope curving under gravity](images/pbd-simulations/rope_screenshot.png) | ![Rope in motion](images/pbd-simulations/rope_frame1.png) |

*Left: Rope under gravity with distance constraints. Right: Rope mid-swing dragged by mouse.*

### Particle Smoke

| | | |
|---|---|---|
| ![Smoke rising](images/pbd-simulations/particle_smoke1.png) | ![Two smoke columns](images/pbd-simulations/particle_smoke2.png) | ![Dense smoke column](images/pbd-simulations/particle_smoke3.png) |

*Particle smoke driven by buoyancy, turbulence, and PBD density constraints. Parameters adjustable at runtime.*

A demo recording is included: `Project /Project Recording.mov`

---

## Midterm Presentation — Hair & Fur Paper Breakdown

**`Midterm Presentation/`** — Analysis of the 2012 paper:

> **"Fast Simulation of Inextensible Hair and Fur"**  
> Müller, Kim, and Chentanez (2012)

Blog write-up: [Fast Simulation of Inextensible Hair and Fur – Paper Breakdown](https://miguelgarcia3.wordpress.com/2025/11/18/fast-simulation-of-inextensible-hair-and-fur-paper-breakdown/)

### Paper Results

![Hair simulation results — straight, wavy, and curly at 25–47k strands](images/hair-fur/hair_results_fig1.png)

*Figure 1: Every hair strand simulated in real time. Left to right: 47k hairs at 25 FPS, long hair at 1.9M particles at 8 FPS, curly hair with visualization post-processing.*

| Curly Hair Render | FTL vs PBD vs Euler |
|---|---|
| ![Curly hair 3D render](images/hair-fur/curly_hair_render.png) | ![Method comparison — FTL (blue), PBD (green), Euler (red)](images/hair-fur/ftl_pbd_euler_comparison.png) |

*Left: Curly hair rendered in real time using the paper's method. Right (Figure 6): FTL (blue), PBD (green), and symplectic Euler (red) compared under the same per-frame budget.*

| Algorithm Diagrams | Fur with Repulsion |
|---|---|
| ![FTL correction and curly hair generation diagrams](images/hair-fur/ftl_algorithm_diagrams.png) | ![Fur hair-character repulsion](images/hair-fur/fur_repulsion_fig7.png) |

*Left: FTL mass-correction steps and curly hair vertex generation. Right (Figure 7): Fur simulation — hair-character repulsion prevents clipping without disturbing artifacts.*

### Paper Summary

The paper unifies three techniques into a single real-time solver:

1. **Position-Based Dynamics (PBD)** — stable, position-first constraint projection
2. **Follow-the-Leader (FTL)** — propagates strand shape from root to tip in one pass
3. **Grid-based repulsion** — prevents strand interpenetration at scale

**Key innovation:** A corrected mass distribution in the FTL algorithm enables zero-stretch behavior in a single iteration, even for thousands of strands.

### Performance Results

| Scene | FPS |
|---|---|
| 47,000 hair strands | 25 FPS |
| 1.9 million particles | 8 FPS |

### Strengths & Limitations

**Strengths:** Single-iteration stability · Scales to tens of thousands of strands · Works for straight, curly, and dense fur · Supports friction and volume preservation

**Limitations:** Introduces numerical damping · Simplified collision handling · Limited torsion/bending stiffness control

Files included:
- `FTLHairFur.pdf` — original paper
- `Midterm Presentation on Hair and Fur..pdf` — slide deck

---

## Final Project — Smoke Simulation

**`Final project /`** — A hybrid Eulerian/Lagrangian smoke simulator combining Stable Fluids and PBD.

**[Full write-up →](Final%20project%20/smoke_simulation_summary.md)**

### Simulation Frames

| | | |
|---|---|---|
| ![Smoke rising — early](images/final-smoke/smoke1.png) | ![Smoke column growing](images/final-smoke/smoke2.png) | ![Two smoke plumes](images/final-smoke/smoke3.png) |
| ![Smoke spreading](images/final-smoke/smoke4.png) | ![Full smoke simulation](images/final-smoke/smoke5.png) | |

*Frames captured from the final simulation. Stable Fluids drives global swirling; PBD particles add weight and controlled drift.*

### Architecture

```
Layer 1 — Eulerian Velocity Grid (Stable Fluids)
  └── Semi-Lagrangian advection
  └── Implicit diffusion (viscosity)
  └── Pressure projection (∇·u = 0)

Layer 2 — Lagrangian Particle System (PBD)
  └── Particles ride the velocity field
  └── Distance & density constraints
  └── Buoyancy forces
```

### Why Both?

| Stable Fluids | PBD Particles |
|---|---|
| Global swirling motion | Per-particle weight & drift |
| Unconditionally stable | Prevents clustering / jitter |
| Smooth vortex structures | Produces heavy, slow feel |

### Results

- Heavy, slow-drifting smoke with natural vortices
- Numerically stable at any timestep — no blow-up
- Visually rich swirling from the pressure projection step

```bash
cd "Final project"
python Smoke.py
```

---

## Other Experiments

| File / Folder | Description |
|---|---|
| `collision.py` | Standalone collision detection experiment |
| `p5js.edits/` | p5.js sketch notes and experiments (`sketches.md`) |
| `images/` | Organized screenshots and captured frames from all simulations |

---

## Setup & Running

**Requirements:** Python 3.8+, `glfw`, `PyOpenGL`, `numpy`

```bash
pip install glfw PyOpenGL PyOpenGL_accelerate numpy
```

Each subdirectory is self-contained. Run any `.py` file directly:

```bash
python HW1/crowd.py
python "Project /rope.py"
python "Final project /Smoke.py"
python collision.py
```

---

## Course Progression

```
HW1: 2D OpenGL basics
  └─> Project: Physics (PBD) — rope, particles
        └─> Final: Fluid sim (Stable Fluids + PBD)

Midterm Presentation: Research — FTL Hair/Fur paper
```

---

*IT-360 Computer Graphics for Visual Effects — Miguel Garcia*
