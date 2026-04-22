# p5.js Sketches

---

## Set 1 — Image Pixel Manipulation (Channel & Filter Operations)

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/TXnxZxUDw)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)

---

## 1. Image Pixel Manipulation — Blue Channel Boost

**Live sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/full/Ps-mMXEmk)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/Ps-mMXEmk"></iframe>
```

**Description:**  
Loads an image via `preload()` and iterates over every pixel using nested `x/y` loops. For each pixel, the red and green channels are clamped to their original values while the blue channel is offset by a passed-in `someValue`. The result is a blue-tinted version of the source image. Demonstrates `img.get()`, `img.set()`, `img.loadPixels()`, and `img.updatePixels()` — the core p5.js pixel manipulation API.

**Key concepts:** `loadImage`, `preload`, pixel loops, `get/set`, color channels, `loadPixels/updatePixels`

---

## 2. Image Pixel Manipulation — Red Channel Isolation

**Live sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/full/Y9JfoMzNA)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/Y9JfoMzNA"></iframe>
```

**Description:**  
Loads a forest/nature image and isolates the red channel by aggressively clamping green to a max of `20` and forcing blue to `0` entirely. The result is a high-contrast, infrared-like red tint over the scene. Builds on the same `get/set` pixel loop pattern as sketch #1 but demonstrates how channel suppression (rather than boosting) transforms an image's mood.

**Key concepts:** `loadImage`, `preload`, pixel loops, channel clamping, color isolation, `loadPixels/updatePixels`

---

## 3. Image Pixel Manipulation — Brightness Overexposure

**Live sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/full/5YovTn-mo)  
**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/5YovTn-mo)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/5YovTn-mo"></iframe>
```

**Description:**  
Loads the Happy Coding mascot cat photo (Stanley) and applies a uniform `+200` offset to all three color channels (R, G, B). Because every channel is pushed toward 255 equally, no color tint is introduced — instead the image is massively overexposed, washing out toward white. Demonstrates how symmetric channel manipulation affects brightness rather than hue, contrasting nicely with sketches #1 (blue tint) and #2 (red isolation).

**Key concepts:** `loadImage`, `preload`, pixel loops, uniform channel offset, brightness vs. hue, `loadPixels/updatePixels`

---

## 4. Image Pixel Manipulation — 3×3 Mean Filter (Box Blur)

**Live sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/full/2JqQlzvAM)  
**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/2JqQlzvAM)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/2JqQlzvAM"></iframe>
```

**Description:**  
Implements a 3×3 mean (box blur) convolution filter on Stanley the cat. For each pixel, all 8 neighbors and the center are sampled, and the R, G, B values are summed and divided by 9 to produce the blurred output. The image is loaded twice — once to apply the filter (`img`) and once to keep as the original (`imgCopy`) — and the canvas is doubled in width so both versions render side by side for direct comparison. First sketch in the series to introduce a spatial/neighborhood operation rather than per-pixel channel math.

**Key concepts:** `loadImage`, `preload`, 3×3 convolution, mean/box blur, neighbor sampling, `img.get()`, side-by-side canvas layout, `loadPixels/updatePixels`

---

---

## Set 2 — Binary, Inversion & Morphological Operations

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/EG_GlwuUO)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)

---

## 5. Image Processing — Luminance Threshold (Binarization)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/2RG-eG8Ac)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/2RG-eG8Ac"></iframe>
```

**Description:**  
Converts a coin image to a binary (black & white) output using the ITU-R luminance formula (`0.2126·R + 0.7152·G + 0.0722·B`) to compute each pixel's perceived brightness. Pixels below 128 are set to black, above to white. A 3×3 filter matrix is defined (used in sketch #8) but the core operation here is purely threshold-based. Canvas is doubled to show processed vs. original side by side. First sketch in the set to introduce binary image processing.

**Key concepts:** luminance formula, binarization, threshold operator, grayscale perception, side-by-side canvas, `img.get/set`

---

## 6. Image Processing — Color Inversion

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/rzRNTkjDa)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/rzRNTkjDa"></iframe>
```

**Description:**  
Inverts every pixel of the Stanley cat photo by subtracting each channel from 255 (`R = 255 - r`, `G = 255 - g`, `B = 255 - b`). Produces a photographic negative effect. The simplest possible per-pixel transformation — each channel is independently flipped around the midpoint. Includes pseudocode comments in the source showing the algorithm before implementation, making it a good teaching sketch.

**Key concepts:** color inversion, photographic negative, per-pixel subtraction, `255 - channel`

---

## 7. Image Processing — Mid-Tone Clamping (Contrast Reduction)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/mn0zdi0zM)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/mn0zdi0zM"></iframe>
```

**Description:**  
Clamps all three channels to a tight mid-tone range of 50–150, with an additional `someValue` offset on the blue channel. By cutting off both the darks (below 50) and lights (above 150), the image loses all contrast and flattens into a dull, gray-blue mid-range. Demonstrates how `min/max` clamping can destroy tonal range rather than just tinting — a contrast-crushing effect distinct from the channel boosts in Set 1.

**Key concepts:** channel clamping, contrast reduction, mid-tone range, `min/max` bounds, tonal compression

---

## 8. Image Processing — Morphological Dilation

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/2K6xeHnS_)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/2K6xeHnS_"></iframe>
```

**Description:**  
Implements morphological dilation using a 3×3 structuring element (filter matrix). For each pixel with luminance ≥ 128 (i.e. "on"), the algorithm spreads white (`color(255)`) to all neighboring positions where the filter value is `1`. Reads from a separate `imgOrg` copy to avoid contaminating the source during iteration. Applied to a binary dilation test image and displayed side by side with the original. Most algorithmically complex sketch in the set — introduces morphological operations used in computer vision for shape expansion and noise removal.

**Key concepts:** morphological dilation, structuring element, 3×3 kernel, binary image, neighbor spreading, `imgOrg` read buffer, side-by-side canvas

---

---

## Set 3 — Advanced Filters, Edge Detection & Image Geometry

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/PjnR2xw0C)  
**Tutorial reference:** [Happy Coding — p5.js Images](https://happycoding.io/tutorials/p5js/images)

---

## 9. Image Processing — Median Filter (Noise Reduction)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/uIZzKCUYi)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/uIZzKCUYi"></iframe>
```

**Description:**  
Applies a variable-size median filter (odd sizes: 3, 5, 7…) to the Stanley cat photo. For each pixel, all neighbors within the kernel window are collected into separate R, G, B arrays, sorted, and the middle (median) value is picked for each channel. Writes to a separate `filteredImg` buffer to avoid read/write contamination. Unlike the mean filter in sketch #4, the median filter preserves edges while removing noise — it's non-linear and cannot be expressed as a weighted sum.

**Key concepts:** median filter, noise reduction, variable kernel size, sorted neighbor arrays, non-linear filter, `createImage`, read/write buffer separation

---

## 10. Image Processing — Gaussian Blur

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/E1fi7DWrN)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/E1fi7DWrN"></iframe>
```

**Description:**  
Implements Gaussian blur using hardcoded 3×3 (divisor 16) and 5×5 (divisor 256) kernel weights derived from Pascal's triangle. For each pixel, neighboring values are multiplied by their kernel weight, summed per channel, and divided by the total kernel weight. Produces a smooth, natural-looking blur that mimics optical defocus — more perceptually accurate than the box blur in sketch #4 because center pixels are weighted more heavily than edges.

**Key concepts:** Gaussian kernel, weighted convolution, Pascal's triangle weights, blur vs. box blur, `createImage`, `constrain`

---

## 11. Image Processing — Laplacian Edge Detection

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/qfBx244cj)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/qfBx244cj"></iframe>
```

**Description:**  
Two-stage pipeline: first converts the image to grayscale using the ITU-R luminance formula, then applies the Laplacian kernel `[0,1,0],[1,-4,1],[0,1,0]` to detect regions of rapid intensity change (edges). Raw convolution values are stored in an array, normalized to 0–255 using min/max scaling, and rendered as a grayscale edge map. The most algorithmically sophisticated sketch so far — introduces second-order derivative edge detection and output normalization.

**Key concepts:** Laplacian kernel, edge detection, second-order derivative, grayscale conversion, min/max normalization, two-pass pipeline, `createImage`

---

## 12. Programmatic Image Generation — Circle

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/5kw4EcuwI)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/5kw4EcuwI"></iframe>
```

**Description:**  
Generates a binary circle image entirely from math — no `loadImage` at all. Creates a blank `2r × 2r` canvas, then for each pixel computes its distance from the center using `dist()`. Pixels inside the radius are set black, outside are set white. Simple but important: demonstrates that p5.js pixel operations can generate images from scratch, not just manipulate loaded ones. Good conceptual bridge to computer vision shape primitives.

**Key concepts:** `createImage`, `dist()`, programmatic shape generation, binary image, no `loadImage`, pixel math from scratch

---

## 13. Image Geometry — Nearest-Neighbor Downscaling (÷3)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/ZHx6JvFtc)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/ZHx6JvFtc"></iframe>
```

**Description:**  
Scales the Stanley cat image down to one-third its size by sampling every 3rd pixel (`X = x*3, Y = y*3`). Each output pixel maps directly to a single source pixel — no blending or interpolation. This is nearest-neighbor downsampling, the fastest but lowest-quality scaling method. Introduces image geometry operations (spatial remapping) as a new category distinct from per-pixel color operations or convolution filters.

**Key concepts:** nearest-neighbor interpolation, downscaling, spatial remapping, `createImage`, pixel sampling, image geometry

---

---

## Set 4 — WEBGL, 3D Camera & Lighting

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/ded0kGdQi)

---

## 14. WEBGL — Camera Controls & Flyover (Slider-Driven)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/M_NVJ103k)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/M_NVJ103k"></iframe>
```

**Description:**  
First sketch to use WEBGL mode. Six sliders control the first 6 parameters of `camera()` — eye position (X, Y, Z) and look-at center (centerX, centerY, centerZ). The `flyOver()` function offsets the slider-defined eye position by a fixed radius using `cos/sin` to simulate a circular orbit, though `theta` is reset each frame (not accumulated), so the arc is static until sliders are moved. Renders a single pink box as the scene subject. Good interactive intro to the p5.js camera model.

**Key concepts:** `WEBGL`, `camera()`, eye position, look-at target, `createSlider`, flyover orbit, `cos/sin` offset, 3D coordinate system

---

## 15. WEBGL — Directional Light, Ambient Light & Sine-Wave Spheres

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/U_-Kv3j1W)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/U_-Kv3j1W"></iframe>
```

**Description:**  
Sets up a WEBGL scene with `ambientLight` (dim red) and a `directionalLight` shining top-down (direction `0, -1, 0`). A small sphere tracks the mouse position. A row of 10 spheres oscillates vertically using `sin(frameCount * i * 0.01)`, creating a ripple wave effect. Demonstrates the interaction between ambient and directional lighting on 3D geometry, and how `frameCount` can drive per-object animations with phase offsets.

**Key concepts:** `WEBGL`, `directionalLight`, `ambientLight`, `sphere`, mouse tracking, `sin` wave animation, `frameCount`, phase offset, `push/pop`

---

## 16. WEBGL — Orbiting Point Light on a Sphere

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/CNIp_pW06)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/CNIp_pW06"></iframe>
```

**Description:**  
A small sphere orbits a large central sphere using `cos/sin` on `frameCount`. The orbiting sphere is rendered with `noLights()` so it always appears white (as a light source visual). A `pointLight` is placed at the same orbiting position, illuminating the large sphere dynamically as the light source moves. Uses helper functions `drawSphere`, `drawBox`, and `drawTorus` to encapsulate `push/translate/pop` patterns. Cleanly demonstrates the difference between a visual object and a light source occupying the same position.

**Key concepts:** `WEBGL`, `pointLight`, `noLights`, orbiting light, `cos/sin` animation, helper draw functions, `push/pop/translate`, light source vs. visual object

---

---

## Set 5 — Linear Algebra: Rotation Matrices, Projection & Ray Casting

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/LVH8z1UQL)

---

## 17. Math — 2D Rotation Matrix (Square Vertices)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/6Tc8SYoOz)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/6Tc8SYoOz"></iframe>
```

**Description:**  
Stores 4 vertices of a square in a `vertices[]` array and rotates each one around the canvas center using polar decomposition: converts (x, y) to (radius, angle) via `sqrt` and `atan2`, adds `rotationAngle`, then converts back with `cos/sin`. Press **Z** to increment the rotation angle. Each vertex is drawn as a circle. Introduces the core idea of rotation as angle accumulation in polar space before moving to full matrix form in sketch #19.

**Key concepts:** 2D rotation, polar coordinates, `atan2`, `cos/sin`, vertex array, keyboard input (`keyIsDown`), rotation around a pivot

---

## 18. Math — 2D Rotation Matrix (Single Orbiting Circle)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/M8rHmUH8G)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/M8rHmUH8G"></iframe>
```

**Description:**  
Simplified version of sketch #17 — a single point orbits the canvas center. Uses the same polar rotation approach (`dx/dy → r/theta → rotated x/y`) but with cleaner variable naming and a diamond shape drawn at center as a visual anchor. Press **Z** to rotate. The `rotateCube` step increment is `0.01` vs `0.07` in sketch #17, making the motion smoother. Good minimal example for isolating and understanding the rotation formula before scaling up to multiple vertices or 3D.

**Key concepts:** 2D rotation, polar form, `atan2`, single-point orbit, pivot rotation, incremental angle

---

## 19. Math — 3D Rotation Matrices + Perspective Projection (Wireframe Cube)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/X5puKfWdb)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/X5puKfWdb"></iframe>
```

**Description:**  
Builds a 3D wireframe cube from scratch without WEBGL — using explicit 3×3 rotation matrices for X, Y, and Z axes applied via `matmul()`. After rotation, a perspective projection matrix divides by `(distance - z)` to create depth foreshortening. 12 points define the cube + extra geometry; edges are drawn with `connect()`. Six keyboard controls handle roll, counter-roll, pitch, counter-pitch, yaw, and counter-yaw (**A/S, Z/X, Q/W**). A reference image of the rotation matrix formulas is overlaid on canvas. Most mathematically rich sketch in the collection.

**Key concepts:** 3×3 rotation matrices, `matmul`, X/Y/Z axis rotation, perspective projection, wireframe rendering, `createVector`, roll/pitch/yaw, 2D canvas 3D simulation

---

## 20. Math — Spaceship with Ray-Circle Intersection

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/5eBHRRjWH)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/5eBHRRjWH"></iframe>
```

**Description:**  
A spaceship (OOP `Spaceship` class) can thrust and turn with arrow keys + Z. A ray is cast from the ship's nose in the direction it's heading. `isInCircle()` implements ray-circle intersection using dot product projection: it finds the closest point on the ray to the circle center, then checks if that distance squared is within the circle's radius squared. The circle turns orange when the ray hits it. Introduces ray casting as a fundamental computer graphics and game dev concept — distinct from all previous pixel or geometry sketches.

**Key concepts:** ray casting, ray-circle intersection, dot product, projection, `Spaceship` class, OOP, heading vector, `cos/sin` direction, `keyIsDown`, wrap edges

---

---

## Set 6 — Creative Animation & Interactivity

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/0RxPLTNz6)

---

## 21. Animation — 30 Bouncing Discs (Wall Collision)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/8pNdS2F6R)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/8pNdS2F6R"></iframe>
```

**Description:**  
Spawns 30 yellow discs at random positions, each with the same velocity vector `(2, 3)`. `moveDisc(idx)` checks boundary collisions per disc, flipping the corresponding delta component when the disc edge touches a wall (accounting for radius `r = 12.5`). Positions and deltas are stored in parallel `createVector` arrays indexed by disc ID. First sketch in the collection to simulate multiple independent moving objects with physics-style boundary reflection.

**Key concepts:** `createVector`, parallel arrays, boundary collision, velocity reflection, `random()`, multi-object simulation, wall bounce

---

## 22. Creative — Interactive Alien Face (Slider Controls)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/c-4Fwfi5b)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/c-4Fwfi5b"></iframe>
```

**Description:**  
Draws a large pink alien/robot face with layered ellipses for face, eyes, pupils, cheeks, nose, mouth, and antennae. Three sliders independently control mouth openness, eye size, and blush intensity. Mouse Y position drives antenna shake via `map()` and `random()`. Pupil color shifts with blush value. A purely creative sketch — no physics or math algorithms — demonstrating how `map()`, sliders, and layered shape drawing can build an expressive interactive character.

**Key concepts:** `createSlider`, `map()`, `random()` shake, layered shape drawing, character design, `stroke/fill`, interactive parameters

---

## 23. Animation — Keyframe Linear Interpolation with Speed Toggle

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/ZQkoYH3kx)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/ZQkoYH3kx"></iframe>
```

**Description:**  
Animates a ball between two x positions using manual linear interpolation: `x = x1*(1-t) + x2*t`, where `t` is mapped from elapsed `millis()` within an interval. The ball's y offset uses `abs(x-250)` to create a natural arc. When `t` reaches 1, `x1` becomes the previous `x2` and a new random `x2` is chosen — chaining keyframes. Click toggles between fast (3.5s) and slow (16s) interval modes. Introduces keyframe animation and easing fundamentals.

**Key concepts:** linear interpolation (`lerp`), `millis()`, keyframe chaining, `map()`, `constrain()`, arc via `abs()`, speed toggle, `mouseClicked`

---

## 24. Creative — Bouncing Face with Dynamic Scaling

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/NczoFYpQv)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/NczoFYpQv"></iframe>
```

**Description:**  
A blue face bounces around the full window, reversing direction at edges. Its radius is driven by x position via `map()` — growing larger on the right, shrinking on the left — making size feel like a consequence of motion. The face also rotates continuously. `drawFace()` encapsulates all drawing logic using `push/translate/rotate/pop`, with every feature (eyes, pupils, brows, mouth) independently scaled relative to `radius` via `map()`. A strong example of modular, parameter-driven character drawing.

**Key concepts:** `map()` scaling, `push/pop/translate/rotate`, `drawFace()` helper, bouncing physics, `windowWidth/Height`, `angleMode(DEGREES)`, proportional feature scaling

---

---

## Set 7 — Physics Simulation: Gravity, Collision Detection & Energy

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/kYjgY888h)

---

## 25. Physics — 30 Discs with Gravity, Velocity Integration & Collision Impulses

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/LM_hYC5p3)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/LM_hYC5p3"></iframe>
```

**Description:**  
The most physically complete disc simulation in the collection. Separates `positions`, `velocities`, `deltas`, and `forces` into parallel arrays. Each frame: collision impulses are resolved via normalized direction vectors scaled by `forcestrength` and `collisionDist`; gravity is added to `vy` each step (`gravity * timestep`); positions update via `velocity * timestep` (Euler integration); velocities are damped by `0.99` per frame for energy loss. Wall bounce uses `ALPHA` to attenuate velocity on impact. The `timestep` and `forcestrength` constants make the simulation tunable.

**Key concepts:** Euler integration, `timestep`, velocity impulse collision, gravity accumulation, energy damping (`0.99`), `ALPHA` wall restitution, `forcestrength`, normalized collision normal

---

## 26. Physics — Position-Based Collision Resolution (Elastic, ALPHA=1.0)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/Q1G-cpxot)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/Q1G-cpxot"></iframe>
```

**Description:**  
30 discs with wall boundary clamping and disc-disc collision resolution via **position correction** rather than velocity impulses. When two discs overlap, each is pushed apart by `collisionDist/2` along the collision axis. With `ALPHA=1.0`, wall bounces are fully elastic — no energy lost. No gravity. Simpler than sketch #25 but introduces the concept of positional constraint solving, a technique used in modern physics engines (e.g. Position Based Dynamics).

**Key concepts:** position-based collision, overlap correction, `collisionDist/2`, elastic bounce (`ALPHA=1.0`), constraint solving, no gravity

---

## 27. Physics — Collision Resolution Scaffold (Inelastic, ALPHA=0.8, TODO stub)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/oISgHb8r5)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/oISgHb8r5"></iframe>
```

**Description:**  
Same structure as sketch #26 but `ALPHA=0.8` (inelastic wall bounce — 20% energy lost per collision) and `resolveCollision()` is intentionally left as a commented-out TODO stub. Serves as a starting template or exercise: the boundary clamping works, discs move and fall, but disc-disc collisions pass through each other until `resolveCollision` is implemented. Pairs directly with sketch #26 as a before/after teaching pair.

**Key concepts:** inelastic collision (`ALPHA=0.8`), energy loss, TODO scaffold, exercise template, contrast with sketch #26

---

## 28. Physics — Single Ball Gravity with Energy-Absorbing Bounce

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/mdj1l50o9)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/mdj1l50o9"></iframe>
```

**Description:**  
The simplest gravity sketch in the set — a single ball with initial velocity `(vx=20, vy=3)`. Each frame, `vy` is incremented by `a * dt` (gravity = 9.8, dt = 0.05), simulating free fall. On floor/ceiling hit, `vy` is negated and multiplied by `0.8` (losing 20% energy per bounce), causing the ball to settle. `vx` reflects off side walls elastically. A minimal, readable intro to Euler integration and restitution coefficients — the conceptual foundation for the more complex multi-disc simulations above.

**Key concepts:** gravity (`a = 9.8`), Euler integration, `dt`, restitution coefficient (`0.8`), single-body physics, `vx/vy`, wall reflection

---

---

## Set 8 — Agent Systems & Advanced Particle Physics

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/TZp5GSBii)

---

## 29. Agent Sim — Social Force Avoidance (Vanilla JS / Canvas 2D)

**Live sketch:** [jsFiddle](https://jsfiddle.net/Leug1mGraph/9t2jehwn/2/)

**Description:**  
The only non-p5.js sketch in the collection — written in raw Canvas 2D API. Spawns `w/5` agents, each with random velocity and an `aggro` flag (red = aggressive, black = passive). Each frame, every agent computes a social avoidance force from all neighbors within radius `d_h`: the force magnitude scales with proximity (`k = max(d_h - d_ab, 0)`) and is normalized then integrated with `TIME_STEP`. Agents wrap around canvas edges. A genuine agent-based model (ABM) with emergent crowd behavior — closest in spirit to simulation research of any sketch in the collection.

**Key concepts:** Canvas 2D API (no p5.js), agent-based model, social force model, avoidance force normalization, `aggro` flag, wrap-around, emergent behavior, `setInterval` animation loop

---

## 30. Physics — 30 Discs with Wrap-Around & Normalized Collision

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/HeOUoyi0L)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/HeOUoyi0L"></iframe>
```

**Description:**  
30 discs with randomized velocities wrap horizontally (left↔right teleport) and bounce vertically. `resolveAgentCollision()` correctly normalizes the collision direction vector before applying `collisionDist/2` position correction to each disc — fixing the unnormalized bug present in sketch #26. Random initial velocities create varied trajectories. The mix of wrap-around and bounce boundaries in a single sketch is a new combination not seen in previous sets.

**Key concepts:** wrap-around boundary, directional bounce, normalized collision vector, position-based resolution, random velocity init, mixed boundary types

---

## 31. Physics — 512 Particles, Verlet Integration, Gravity + Wind (Left Click)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/Zx72lIgpm)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/Zx72lIgpm"></iframe>
```

**Description:**  
Scales up to 512 particles using a Verlet-inspired integration loop: positions are updated first, collisions are accumulated into `deltas[]` with a `deltaCtrs[]` counter, then the averaged delta is applied. Velocities are derived from `(new_pos - old_pos) / timeStep` each frame (implicit Verlet). Gravity pulls downward; holding the mouse applies rightward wind force. Collision corrections are scaled by `1.2` to add slight over-separation. The `0.9999` velocity damping keeps energy slowly dissipating. First sketch to separate the physics and collision passes.

**Key concepts:** Verlet-style integration, `oldPositions`, delta accumulation, `deltaCtrs` averaging, 512 particles, gravity + wind, `mouseIsPressed`, two-pass update, implicit velocity derivation

---

## 32. Physics — 512 Particles, Bidirectional Wind (Left/Right Click)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/9fh3XE3bC)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/9fh3XE3bC"></iframe>
```

**Description:**  
Direct variant of sketch #31 with one key change: left click applies positive wind (`+5.0`) and right click applies negative wind (`-5.0`), enabling bidirectional horizontal force. Same Verlet integration structure, `deltaCtrs` collision averaging, and 512 particle count. Note: in this version gravity and wind are applied to both x and y in the position update (a likely experimental variation), producing diagonal drift behavior distinct from sketch #31.

**Key concepts:** bidirectional wind, `mouseButton === LEFT/RIGHT`, Verlet integration, variant comparison with sketch #31, force application axis difference

---

## 33. Physics — 70 Variable-Radius Discs, Gravity, Damping & Two-Pass Loop

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/0bk6hdX3g)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/0bk6hdX3g"></iframe>
```

**Description:**  
Introduces variable disc sizes via `radiusArr[]` — each disc gets a random radius between 11 and 21. Collision threshold uses the **sum of both radii** (`radiusArr[idxA] + radiusArr[idxB]`), making collision detection correctly size-aware. The draw loop is split into three explicit passes: (1) physics update + gravity, (2) collision resolution, (3) rendering. Velocity is damped by `0.92` per frame — stronger than previous sketches — causing discs to settle quickly into a pile. First sketch in the collection with heterogeneous body sizes.

**Key concepts:** variable radius, `radiusArr`, size-aware collision threshold, three-pass loop structure, velocity damping (`0.92`), gravity settling, heterogeneous bodies

---

---

## Set 9 — Boids & Goal-Seeking Agents

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/0Z7zAqHKz)

> This set implements the classic Boids model (Craig Reynolds, 1986) across three progressive versions, plus two goal-seeking agent variants and a standalone velocity planner. All sketches share the same agent scaffold: `positions`, `velocities`, `radiusArr`, `prefMovementVector`, `resolveCollision`, `constrainToBoudary`, and mouse drag interaction.

---

## 34. Boids — Avoidance Only

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/TVlUmW-dt)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/TVlUmW-dt"></iframe>
```

**Description:**  
The simplest Boids variant — implements only the **separation** (avoidance) rule. In `addBoidsForces()`, the avoidance vector points directly from neighbor to agent (`positions[idx] - positions[i]`), normalized and scaled by the avoidance slider. No cohesion or alignment. Each agent also has a `prefMovementVector` blended into velocity via `velocityPlanner_wo_goal`. Agents wrap horizontally, bounce vertically. Hovering an agent reveals its neighborhood radius as a faint circle. Draggable agents.

**Key concepts:** Boids separation rule, avoidance force, `BOIDS_NEIGHBOUR_THRESHOLD`, `velocityPlanner_wo_goal`, `C_VEL_INTERPOLATION`, mouse hover neighborhood visualization, drag interaction

---

## 35. Boids — Alignment (Working) + Avoidance (TODO)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/YyrVW8uIw)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/YyrVW8uIw"></iframe>
```

**Description:**  
Adds the **alignment** rule to the Boids model — `avgDirX/Y` accumulates neighbor velocities, then divides by `neighbourCtr` to get the average, which is applied as a force. Avoidance force is still a zero-placeholder TODO. The alignment slider controls how strongly agents match their neighbors' heading. Agents begin to form loose flocks moving in the same direction. First sketch in the set to produce emergent collective motion.

**Key concepts:** Boids alignment rule, average neighbor velocity, `alignmentSlider`, emergent flocking, `neighbourCtr`, velocity averaging

---

## 36. Boids — Full Scaffold (Cohesion + Alignment + Avoidance, TODO Stubs)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/hEjgfENsp)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/hEjgfENsp"></iframe>
```

**Description:**  
The complete three-rule Boids scaffold with all three behaviors wired to sliders (alignment, cohesion, avoidance), but cohesion and alignment are left as TODO stubs (`avgX/Y += 0.0`, `avgDirX/Y = 0.0`). `dirToCenterY = 0.0` explicitly zeroes the cohesion y-component. Serves as the exercise template — the structure is correct and sliders are functional, but students must fill in the neighbor averaging logic. Pairing with sketches #34 and #35 shows the before/after for each behavior.

**Key concepts:** Boids three-rule scaffold, `cohesionSlider`, `alignmentSlider`, `avoidanceSlider`, `dirToCenter` cohesion vector, exercise template, labeled TODO stubs

---

## 37. Agent Navigation — Goal-Seeking with Velocity Interpolation

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/U3y96JP-D)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/U3y96JP-D"></iframe>
```

**Description:**  
Shifts from flocking to **goal-directed navigation**. 15 agents are initialized on the left edge with shuffled goal positions on the right. `velocityPlanner_with_goal()` computes a normalized direction to each agent's goal and interpolates velocity toward it using `C_VEL_INTERPOLATION`. Velocity is lightly damped (`0.99`). Green dots mark goal positions. Both agents and goals are draggable — dragging a goal in real-time redirects that agent. No obstacles. Introduces the goal-seeking velocity planner pattern used in crowd simulation.

**Key concepts:** goal-directed navigation, `velocityPlanner_with_goal`, velocity interpolation, `prefSpeed`, `shuffle()`, draggable goals, green goal markers

---

## 38. Agent Navigation — Velocity Planner Without Goal

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/CxJGXCDm5)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/CxJGXCDm5"></iframe>
```

**Description:**  
Standalone implementation of `velocityPlanner_wo_goal()` — blends current velocity with a fixed `prefMovementVector` using `C_VEL_INTERPOLATION = 0.1`, making agents gradually align to their preferred direction rather than snapping. Velocity is lightly damped (`0.99`). 15 variable-radius agents bounce off walls (reversing `prefMovementVector` on contact) and resolve collisions. Mouse dragging repositions agents. The conceptual counterpart to sketch #37 — same interpolation pattern, but driven by a preferred direction rather than a goal position.

**Key concepts:** `velocityPlanner_wo_goal`, `prefMovementVector`, velocity interpolation, `C_VEL_INTERPOLATION`, preferred direction, wall-reversing preferred vector, drag interaction

---

## 39. Agent Navigation — Goal-Seeking with Obstacles

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/9HagVyUHg)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/9HagVyUHg"></iframe>
```

**Description:**  
Extends sketch #37 with randomly placed circular obstacles. `resolveObstacleCollision()` pushes agents fully away from obstacle surfaces (agent bears all correction weight — `w_idxA=0.001`). Between 1 and 3 obstacles of random size spawn in the middle third of the canvas, creating natural bottlenecks. Agents must navigate around them to reach their goals. Also introduces `distanceConstraint()` — a generalized weighted distance constraint function not seen in other sketches. Dragging works for both agents and goals.

**Key concepts:** obstacle avoidance, `resolveObstacleCollision`, `obstacleArr/obstacleRadii`, asymmetric constraint weights, `distanceConstraint`, bottleneck navigation, random obstacle count/size

---

---

## Set 10 — Constraints, Chains & Soft-Body Simulation

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/2PkWjczNI)

---

## 40. Physics — Heavy Ball Bulldozer (Asymmetric Collision Weights)

**Live sketch:** [p5.js Editor](https://editor.p5js.org/tomerwei/sketches/bRqrRfVvH) *(reference sketch by tomerwei)*

**Description:**  
70 small yellow discs + 1 large red disc (index 0, radius 37–47). The key innovation is **asymmetric collision weights**: when index 0 is involved in a collision, its weight is set to `1000` vs `1` for the other disc — meaning small discs absorb nearly all the displacement and the red ball barely moves. Drag the red ball to bulldoze through the pile. Gravity + `0.92` damping causes discs to settle. Background is drawn after physics so trails vanish each frame. Demonstrates how weight ratios in position-based constraints can simulate mass differences without true rigid-body dynamics.

**Key concepts:** asymmetric constraint weights, simulated mass, `w_idxA=1000`, bulldozer interaction, `mouseDragged` on index 0, gravity + damping, variable-radius discs

---

## 41. Physics — Rope/Chain with Distance Constraints

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/TkFhtGoJ8)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/TkFhtGoJ8"></iframe>
```

**Description:**  
10 beads initialized in a horizontal row at the top of the canvas, connected sequentially by `distanceConstraint(i-1, i, 45)`. Each constraint enforces a fixed 45px separation between consecutive bead pairs using asymmetric weights (`w_idxA=0.1, w_idxB=1`), making the anchor end stiffer. Lines are drawn between consecutive beads to visualize the rope. `resolveCollision` is a TODO stub — beads pass through each other. Drag any bead to manipulate the chain. First sketch in the collection to use distance constraints for structure rather than collision avoidance.

**Key concepts:** distance constraint, rope/chain simulation, sequential bead linking, `distanceConstraint`, asymmetric weights, structural constraints, `mouseDragged`, line rendering

---

## 42. Physics — Spring Cloth Simulation

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/pQoyTzZiR)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/pQoyTzZiR"></iframe>
```

**Description:**  
Full cloth simulation using a 286×80 grid of `Particle` objects connected by `Spring` objects (stiffness `k=0.5`, rest length = `spacing=3.5`). The top row is locked in place. Each frame: springs apply Hooke's law forces and are rendered; particles receive gravity (`0,0.1`), quadratic drag (`speed² × 0.02`), and Perlin noise wind. Click the mouse to cut springs — `collideLineCircle` detects mouse-spring intersection and splices the spring from the array. Falling particles/springs are garbage-collected when both endpoints drop below the canvas. Inspired by The Coding Train (Daniel Shiffman). Most visually and computationally impressive sketch in the collection.

**Key concepts:** Hooke's law, spring-mass system, cloth simulation, OOP `Particle/Spring`, locked particles, Perlin noise wind (`noise(xoff)`), quadratic drag, spring cutting, `collideLineCircle`, garbage collection, `windowWidth/Height`

---

---

## Set 11 — Position-Based Dynamics: Cloth Simulation Series

**Collection:** [p5.js Editor Collection](https://editor.p5js.org/miguelagarcia-dev/collections/1TIMB1TmR)

> All four sketches share the same 10×10 particle grid scaffold: `getParticleIndex`, `indexInRange`, `distanceConstraint` with stiffness, `pointConstraint` pinning two corners, a `simulation()` loop with `iterNum=3` solver iterations, gravity + `0.92` damping, and a green mouse cursor circle. Differences are noted per sketch.

---

## 43. Cloth Sim — Base (Drag Any Vertex)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/RwlQoOrQ-)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/RwlQoOrQ-"></iframe>
```

**Description:**  
The foundational cloth sketch. A 10×10 grid of 100 particles is connected by horizontal and vertical distance constraints (`clothVertexDistance = 15px`, stiffness `0.5`). Two corner particles are pinned via `pointConstraint` at `(width/3, 0)` and `(2*width/3, 0)`. `mouseDragged` finds the nearest vertex and teleports it to the mouse — allowing any part of the cloth to be grabbed and pulled. Solver runs `iterNum=3` constraint iterations per frame. `gravity=5.5` causes the cloth to hang with visible drape.

**Key concepts:** Position-Based Dynamics, `distanceConstraint`, `pointConstraint`, `iterNum` solver iterations, cloth grid indexing, `getParticleIndex`, pinned vertices, `mouseDragged` nearest-vertex search

---

## 44. Cloth Sim — Click to Pull Corner

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/rduQtBxte)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/rduQtBxte"></iframe>
```

**Description:**  
Same cloth scaffold as sketch #43 but replaces `mouseDragged` with `mousePressed` — clicking teleports the **last particle** (`positions[positions.length-1]`, the bottom-right corner) to the mouse position. Rather than grabbing any vertex, you can only yank a specific corner on each click, creating a distinct interaction mode. Good for studying how a single-point disturbance propagates through the constraint network.

**Key concepts:** `mousePressed` vs `mouseDragged`, corner-specific interaction, constraint propagation, single-point disturbance

---

## 45. Cloth Sim — Tearable Cloth

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/4E-4Wm3ev)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/4E-4Wm3ev"></iframe>
```

**Description:**  
Adds tearing to the base cloth. Inside `distanceConstraint`, a check compares `dist > 6 * requiredDistance` — if a constraint is stretched beyond 6× its rest length, it is spliced from `distanceConstraintIndexPairs`, permanently removing that edge from the simulation. The cloth can be torn by dragging aggressively. Combines `mouseDragged` nearest-vertex interaction with the tearing mechanic. The tear condition uses `dist` rather than `constraintDistance`, so it fires on extreme separation rather than moderate overlap.

**Key concepts:** cloth tearing, constraint removal, `splice`, stretch threshold (`6× rest length`), permanent edge deletion, `mouseDragged` + tear combo

---

## 46. Cloth Sim — Diagonal Constraints (Shear Resistance)

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/_Y4hoFysC)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/_Y4hoFysC"></iframe>
```

**Description:**  
Upgrades the constraint topology by adding **diagonal springs** connecting `(row, col) → (row+1, col+1)` and `(row, col) → (row+1, col-1)` with rest length `clothVertexDistance * √2`. This adds shear resistance — the cloth resists diagonal deformation and holds its shape more rigidly. Gravity is reduced to `0.1` (vs `5.5`) for a more floating drape. Constraint pairs are stored as `[idxA, idxB, distance]` arrays (not `createVector`) to carry the per-edge rest length. `pointConstraint` is a TODO stub — corners are not pinned, so the cloth falls freely. `mousePressed` moves the last vertex.

**Key concepts:** diagonal spring constraints, shear resistance, `√2` rest length, per-edge distance storage, `[idxA, idxB, dist]` array format, low gravity, `pointConstraint` TODO, topology comparison with sketch #43

---

---

## Set 12 — Pathfinding Algorithms

*(No collection link provided)*

---

## 47. Pathfinding — A* Search Visualization

**Edit sketch:** [p5.js Editor](https://editor.p5js.org/miguelagarcia-dev/sketches/AsFsutM0x)  
**Embed:**
```html
<iframe src="https://editor.p5js.org/miguelagarcia-dev/full/AsFsutM0x"></iframe>
```

**Description:**  
Visualizes the A* algorithm running step-by-step on a 50×50 grid. Each frame advances one iteration: the open set node with the lowest `f = g + h` score is expanded, its neighbors checked, and the best path reconstructed by walking `previous` pointers back from `current` to `start`. Closed set cells are shown in red, open set in green, and the current best path as a pink polyline. Random walls block some cells. End is set to `grid[cols-1][0]` (top-right corner). The sketch pauses (`noLoop()`) when the goal is reached or no solution exists. Inspired by The Coding Train.

**Key concepts:** A* algorithm, `f = g + h`, heuristic (Euclidean distance), open/closed sets, `previous` pointer path reconstruction, wall obstacles, step-by-step visualization, `noLoop()`

---

## 48. Pathfinding — BFS Flow Field + Social Force Agents (Vanilla JS)

**Live sketch:** [jsFiddle](https://jsfiddle.net/Leug1mGraph/ayg794qu/2/)

**Description:**  
Combines two systems in vanilla Canvas 2D. The **Grid/BFS layer** builds a distance field from the canvas center using breadth-first search (`buildNodePath`), then generates a flow field (`createFlowField`) where each node's `flow` vector points toward its lowest-distance neighbor. The **agent layer** uses a Helbing-style social force model: a goal force drives agents toward their preferred velocity, an exponential repulsion force (`A * exp(r_ab / B)`) plus a hard contact repulsion (`k_repluse`) pushes them apart, and total force is clamped by `MAX_FORCE` with speed capped at `MAX_SPEED`. Even-indexed agents consult the flow field planner for velocity direction. FPS counter overlaid. The most algorithmically complete sketch in the collection — navigation + crowd simulation combined.

**Key concepts:** BFS distance field, flow field, `buildNodePath`, `createFlowField`, Helbing social force model, exponential repulsion, goal force, `MAX_FORCE/MAX_SPEED` clamping, flow field planner, FPS counter, vanilla Canvas 2D

---
