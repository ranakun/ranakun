<!-- github.com/ranakun — profile README. Image paths are repo-relative, not file-viewer URLs. -->

<p align="center">
  <img src="hero.svg" alt="Live threshold-signing ceremony — of five key shares two are offline; the remaining three send partial signatures that combine, at a 3-of-5 quorum, into one signature that is then verified." width="100%">
</p>

<h2 align="center">Rana Singh Shashwat</h2>
<p align="center"><strong>Applied cryptography &amp; MPC</strong> — threshold signing &amp; HSM-backed custody infrastructure</p>

<!-- DRAFT one-liner — confirm wording -->
<p align="center">I build the signing layer for institutional digital-asset custody:<br>
threshold signature schemes, secure multiparty computation, and air-gapped HSM key management.</p>

---

#### The primitive I build around

$$
f(0) = \sum_{i \in Q} \lambda_i f(i) \qquad \lambda_i = \prod_{j \in Q, j \neq i} \frac{j}{j - i}
$$

<sub>Lagrange interpolation at 0 reconstructs one secret from any <i>t</i> of <i>n</i> shares (|Q| = t) — the common core of every threshold scheme, independent of the underlying group: threshold ECDSA, EdDSA, BLS. No single party ever holds the key. (Shamir, <a href="https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf"><i>How to Share a Secret</i></a>, 1979.)</sub>

---

#### An elliptic-curve group, rendered — drag to rotate

```stl
solid curve_torus
  facet normal 8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 3.718542e-17 1.000000e+00
    outer loop
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 3.718542e-17 1.000000e+00
    outer loop
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 -3.718542e-17 -1.000000e+00
    outer loop
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 -3.718542e-17 -1.000000e+00
    outer loop
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 1.015925e-16 1.000000e+00
    outer loop
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 1.015925e-16 1.000000e+00
    outer loop
      vertex 1.039230e+00 6.000000e-01 3.464102e-01
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex 6.928203e-01 4.000000e-01 3.464102e-01
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex 5.196152e-01 3.000000e-01 4.898587e-17
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 -1.015925e-16 -1.000000e+00
    outer loop
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 -1.015925e-16 -1.000000e+00
    outer loop
      vertex 6.928203e-01 4.000000e-01 -3.464102e-01
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex 1.039230e+00 6.000000e-01 -3.464102e-01
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
      vertex 1.212436e+00 7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 1.387779e-16 1.000000e+00
    outer loop
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 1.387779e-16 1.000000e+00
    outer loop
      vertex 6.000000e-01 1.039230e+00 3.464102e-01
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex 4.000000e-01 6.928203e-01 3.464102e-01
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex 3.000000e-01 5.196152e-01 4.898587e-17
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 -1.387779e-16 -1.000000e+00
    outer loop
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 -1.387779e-16 -1.000000e+00
    outer loop
      vertex 4.000000e-01 6.928203e-01 -3.464102e-01
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 1.039230e+00 -3.464102e-01
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
      vertex 7.000000e-01 1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 1.387779e-16 1.000000e+00
    outer loop
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 1.387779e-16 1.000000e+00
    outer loop
      vertex 7.347881e-17 1.200000e+00 3.464102e-01
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex 4.898587e-17 8.000000e-01 3.464102e-01
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex 3.673940e-17 6.000000e-01 4.898587e-17
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 -1.387779e-16 -1.000000e+00
    outer loop
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 -1.387779e-16 -1.000000e+00
    outer loop
      vertex 4.898587e-17 8.000000e-01 -3.464102e-01
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex 7.347881e-17 1.200000e+00 -3.464102e-01
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
      vertex 8.572528e-17 1.400000e+00 0.000000e+00
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 1.015925e-16 1.000000e+00
    outer loop
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 1.015925e-16 1.000000e+00
    outer loop
      vertex -6.000000e-01 1.039230e+00 3.464102e-01
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex -4.000000e-01 6.928203e-01 3.464102e-01
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex -3.000000e-01 5.196152e-01 4.898587e-17
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 -1.015925e-16 -1.000000e+00
    outer loop
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 -1.015925e-16 -1.000000e+00
    outer loop
      vertex -4.000000e-01 6.928203e-01 -3.464102e-01
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 1.039230e+00 -3.464102e-01
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
      vertex -7.000000e-01 1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 3.718542e-17 1.000000e+00
    outer loop
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 3.718542e-17 1.000000e+00
    outer loop
      vertex -1.039230e+00 6.000000e-01 3.464102e-01
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex -6.928203e-01 4.000000e-01 3.464102e-01
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex -5.196152e-01 3.000000e-01 4.898587e-17
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 -3.718542e-17 -1.000000e+00
    outer loop
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 -3.718542e-17 -1.000000e+00
    outer loop
      vertex -6.928203e-01 4.000000e-01 -3.464102e-01
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex -1.039230e+00 6.000000e-01 -3.464102e-01
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
      vertex -1.212436e+00 7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 -3.718542e-17 1.000000e+00
    outer loop
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 -3.718542e-17 1.000000e+00
    outer loop
      vertex -1.200000e+00 1.469576e-16 3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex -8.000000e-01 9.797174e-17 3.464102e-01
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 7.347881e-17 4.898587e-17
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 3.718542e-17 -1.000000e+00
    outer loop
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 3.718542e-17 -1.000000e+00
    outer loop
      vertex -8.000000e-01 9.797174e-17 -3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal -8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex -1.200000e+00 1.469576e-16 -3.464102e-01
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
      vertex -1.400000e+00 1.714506e-16 0.000000e+00
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 -1.015925e-16 1.000000e+00
    outer loop
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 -1.015925e-16 1.000000e+00
    outer loop
      vertex -1.039230e+00 -6.000000e-01 3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex -6.928203e-01 -4.000000e-01 3.464102e-01
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex -5.196152e-01 -3.000000e-01 4.898587e-17
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 1.015925e-16 -1.000000e+00
    outer loop
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 1.015925e-16 -1.000000e+00
    outer loop
      vertex -6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal -6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex -1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
      vertex -1.212436e+00 -7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 -1.387779e-16 1.000000e+00
    outer loop
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 -1.387779e-16 1.000000e+00
    outer loop
      vertex -6.000000e-01 -1.039230e+00 3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex -4.000000e-01 -6.928203e-01 3.464102e-01
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex -3.000000e-01 -5.196152e-01 4.898587e-17
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 1.387779e-16 -1.000000e+00
    outer loop
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 1.387779e-16 -1.000000e+00
    outer loop
      vertex -4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
    endloop
  endfacet
  facet normal -2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex -6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
      vertex -7.000000e-01 -1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 4.870585e-01
    outer loop
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 -1.387779e-16 1.000000e+00
    outer loop
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal 3.718542e-17 -1.387779e-16 1.000000e+00
    outer loop
      vertex -2.204364e-16 -1.200000e+00 3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 4.870585e-01
    outer loop
      vertex -1.469576e-16 -8.000000e-01 3.464102e-01
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -2.260446e-01 8.436100e-01 -4.870585e-01
    outer loop
      vertex -1.102182e-16 -6.000000e-01 4.898587e-17
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 1.387779e-16 -1.000000e+00
    outer loop
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -3.718542e-17 1.387779e-16 -1.000000e+00
    outer loop
      vertex -1.469576e-16 -8.000000e-01 -3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal 2.260446e-01 -8.436100e-01 -4.870585e-01
    outer loop
      vertex -2.204364e-16 -1.200000e+00 -3.464102e-01
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
      vertex -2.571758e-16 -1.400000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 4.870585e-01
    outer loop
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 -1.015925e-16 1.000000e+00
    outer loop
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 1.015925e-16 -1.015925e-16 1.000000e+00
    outer loop
      vertex 6.000000e-01 -1.039230e+00 3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 4.870585e-01
    outer loop
      vertex 4.000000e-01 -6.928203e-01 3.464102e-01
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -6.175654e-01 6.175654e-01 -4.870585e-01
    outer loop
      vertex 3.000000e-01 -5.196152e-01 4.898587e-17
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 1.015925e-16 -1.000000e+00
    outer loop
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -1.015925e-16 1.015925e-16 -1.000000e+00
    outer loop
      vertex 4.000000e-01 -6.928203e-01 -3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
    endloop
  endfacet
  facet normal 6.175654e-01 -6.175654e-01 -4.870585e-01
    outer loop
      vertex 6.000000e-01 -1.039230e+00 -3.464102e-01
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
      vertex 7.000000e-01 -1.212436e+00 0.000000e+00
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 4.870585e-01
    outer loop
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 -3.718542e-17 1.000000e+00
    outer loop
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
      vertex 1.200000e+00 0.000000e+00 3.464102e-01
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
    endloop
  endfacet
  facet normal 1.387779e-16 -3.718542e-17 1.000000e+00
    outer loop
      vertex 1.039230e+00 -6.000000e-01 3.464102e-01
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
      vertex 8.000000e-01 0.000000e+00 3.464102e-01
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 4.870585e-01
    outer loop
      vertex 6.928203e-01 -4.000000e-01 3.464102e-01
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
      vertex 6.000000e-01 0.000000e+00 4.898587e-17
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -8.436100e-01 2.260446e-01 -4.870585e-01
    outer loop
      vertex 5.196152e-01 -3.000000e-01 4.898587e-17
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 3.718542e-17 -1.000000e+00
    outer loop
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex 8.000000e-01 0.000000e+00 -3.464102e-01
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
    endloop
  endfacet
  facet normal -1.387779e-16 3.718542e-17 -1.000000e+00
    outer loop
      vertex 6.928203e-01 -4.000000e-01 -3.464102e-01
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex 1.200000e+00 0.000000e+00 -3.464102e-01
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 8.436100e-01 -2.260446e-01 -4.870585e-01
    outer loop
      vertex 1.039230e+00 -6.000000e-01 -3.464102e-01
      vertex 1.400000e+00 0.000000e+00 0.000000e+00
      vertex 1.212436e+00 -7.000000e-01 0.000000e+00
    endloop
  endfacet
endsolid curve_torus
```

---

<!-- DRAFT optional proof anchor — enable/edit or delete -->
<!-- <p align="center"><sub>MPC signing architecture · audited to 0 Critical/High · threshold-BLS air-gapped signing presented at NBC-2025, NTU Singapore</sub></p> -->

<p align="center">
  <sub>📍 Bangalore · ✉️ <a href="mailto:rana.iiitb@gmail.com">rana.iiitb@gmail.com</a> · ✍️ writeups soon</sub>
</p>
