#!/usr/bin/env python3
"""Generate an ASCII STL of an "elliptic-curve group" torus for the profile's 3D beat.

A curve over the complex numbers is topologically a torus; we render that as a clean,
low-poly solid the viewer can drag-to-rotate inside the README (```stl fenced block).

Facets = MAJOR * MINOR * 2. Keep it modest: the STL text is inlined into README.md, so
more facets = a longer file. ~120-220 reads as intentionally "designed / low-poly".

    python tools/gen_torus_stl.py        # writes curve-torus.stl in the cwd

Per-facet normals are computed by cross product (always valid); winding is consistent
so the solid shades cleanly.
"""
import math

MAJOR = 12      # segments around the main ring
MINOR = 6       # segments around the tube cross-section
R     = 1.00    # main (ring) radius
r     = 0.40    # tube radius
NAME  = "curve_torus"
OUT   = "curve-torus.stl"


def pt(i, j):
    u = 2.0 * math.pi * (i % MAJOR) / MAJOR
    v = 2.0 * math.pi * (j % MINOR) / MINOR
    cu, su, cv, sv = math.cos(u), math.sin(u), math.cos(v), math.sin(v)
    return ((R + r * cv) * cu, (R + r * cv) * su, r * sv)


def sub(a, b):   return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def unit(a):
    m = math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]) or 1.0
    return (a[0]/m, a[1]/m, a[2]/m)


def facet(out, a, b, c):
    n = unit(cross(sub(b, a), sub(c, a)))
    out.append("  facet normal %.6e %.6e %.6e" % n)
    out.append("    outer loop")
    for vx in (a, b, c):
        out.append("      vertex %.6e %.6e %.6e" % vx)
    out.append("    endloop")
    out.append("  endfacet")


def main():
    out = ["solid %s" % NAME]
    for i in range(MAJOR):
        for j in range(MINOR):
            a, b, c, d = pt(i, j), pt(i+1, j), pt(i+1, j+1), pt(i, j+1)
            facet(out, a, b, c)
            facet(out, a, c, d)
    out.append("endsolid %s" % NAME)
    with open(OUT, "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("wrote %s: %d facets" % (OUT, MAJOR * MINOR * 2))


if __name__ == "__main__":
    main()
