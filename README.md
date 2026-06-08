<!-- github.com/ranakun -->

<p align="center">
  <img src="hero.svg" alt="Live threshold signing ceremony. Of five key shares two are offline; the remaining three send partial signatures that combine, at a 3 of 5 quorum, into one signature that is then verified." width="100%">
</p>

<h2 align="center">Rana Singh Shashwat</h2>
<p align="center"><strong>Applied cryptography &amp; MPC</strong> · threshold signing &amp; HSM-backed custody infrastructure</p>

<p align="center">I build the signing layer for institutional digital-asset custody:<br>
threshold signature schemes, secure multiparty computation, and air-gapped HSM key management.</p>

---

#### The primitive I build around

$$
f(0) = \sum_{i \in Q} \lambda_i f(i) \qquad \lambda_i = \prod_{j \in Q, j \neq i} \frac{j}{j - i}
$$

<sub>Lagrange interpolation at 0 reconstructs one secret from any <i>t</i> of <i>n</i> shares (|Q| = t): the common core of every threshold scheme, independent of the underlying group (threshold ECDSA, EdDSA, BLS). No single party ever holds the key. (Shamir, <a href="https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf"><i>How to Share a Secret</i></a>, 1979.)</sub>

---

#### Reconstruct the secret · find the angle

<sub>A cloud of shards. Exactly one camera angle resolves it. Drag, or hit the viewer's auto-rotation.</sub>

```stl
solid shards
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.976342e-01 5.560591e-01 3.169216e-02
      vertex -1.637375e-01 5.560591e-01 3.169216e-02
      vertex -1.637375e-01 6.840371e-01 3.169216e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.976342e-01 5.560591e-01 3.169216e-02
      vertex -1.637375e-01 6.840371e-01 3.169216e-02
      vertex -3.976342e-01 6.840371e-01 3.169216e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.026443e-01 5.630654e-01 -1.830784e-02
      vertex -1.658006e-01 6.926558e-01 -1.830784e-02
      vertex -1.658006e-01 5.630654e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.026443e-01 5.630654e-01 -1.830784e-02
      vertex -4.026443e-01 6.926558e-01 -1.830784e-02
      vertex -1.658006e-01 6.926558e-01 -1.830784e-02
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -3.976342e-01 5.560591e-01 3.169216e-02
      vertex -1.637375e-01 5.560591e-01 3.169216e-02
      vertex -1.658006e-01 5.630654e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -3.976342e-01 5.560591e-01 3.169216e-02
      vertex -1.658006e-01 5.630654e-01 -1.830784e-02
      vertex -4.026443e-01 5.630654e-01 -1.830784e-02
    endloop
  endfacet
  facet normal -9.991498e-01 0.000000e+00 4.122622e-02
    outer loop
      vertex -1.637375e-01 5.560591e-01 3.169216e-02
      vertex -1.637375e-01 6.840371e-01 3.169216e-02
      vertex -1.658006e-01 6.926558e-01 -1.830784e-02
    endloop
  endfacet
  facet normal -9.991498e-01 0.000000e+00 4.122622e-02
    outer loop
      vertex -1.637375e-01 5.560591e-01 3.169216e-02
      vertex -1.658006e-01 6.926558e-01 -1.830784e-02
      vertex -1.658006e-01 5.630654e-01 -1.830784e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex -1.637375e-01 6.840371e-01 3.169216e-02
      vertex -3.976342e-01 6.840371e-01 3.169216e-02
      vertex -4.026443e-01 6.926558e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex -1.637375e-01 6.840371e-01 3.169216e-02
      vertex -4.026443e-01 6.926558e-01 -1.830784e-02
      vertex -1.658006e-01 6.926558e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 9.950172e-01 0.000000e+00 -9.970318e-02
    outer loop
      vertex -3.976342e-01 6.840371e-01 3.169216e-02
      vertex -3.976342e-01 5.560591e-01 3.169216e-02
      vertex -4.026443e-01 5.630654e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 9.950172e-01 0.000000e+00 -9.970318e-02
    outer loop
      vertex -3.976342e-01 6.840371e-01 3.169216e-02
      vertex -4.026443e-01 5.630654e-01 -1.830784e-02
      vertex -4.026443e-01 6.926558e-01 -1.830784e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.290423e-01 6.153245e-01 -3.912539e-01
      vertex 2.527894e-01 6.153245e-01 -3.912539e-01
      vertex 2.527894e-01 7.569424e-01 -3.912539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.290423e-01 6.153245e-01 -3.912539e-01
      vertex 2.527894e-01 7.569424e-01 -3.912539e-01
      vertex -1.290423e-01 7.569424e-01 -3.912539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.305116e-01 6.223307e-01 -4.412539e-01
      vertex 2.556677e-01 7.655611e-01 -4.412539e-01
      vertex 2.556677e-01 6.223307e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.305116e-01 6.223307e-01 -4.412539e-01
      vertex -1.305116e-01 7.655611e-01 -4.412539e-01
      vertex 2.556677e-01 7.655611e-01 -4.412539e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -1.290423e-01 6.153245e-01 -3.912539e-01
      vertex 2.527894e-01 6.153245e-01 -3.912539e-01
      vertex 2.556677e-01 6.223307e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -1.290423e-01 6.153245e-01 -3.912539e-01
      vertex 2.556677e-01 6.223307e-01 -4.412539e-01
      vertex -1.305116e-01 6.223307e-01 -4.412539e-01
    endloop
  endfacet
  facet normal -9.983472e-01 0.000000e+00 -5.747141e-02
    outer loop
      vertex 2.527894e-01 6.153245e-01 -3.912539e-01
      vertex 2.527894e-01 7.569424e-01 -3.912539e-01
      vertex 2.556677e-01 7.655611e-01 -4.412539e-01
    endloop
  endfacet
  facet normal -9.983472e-01 0.000000e+00 -5.747141e-02
    outer loop
      vertex 2.527894e-01 6.153245e-01 -3.912539e-01
      vertex 2.556677e-01 7.655611e-01 -4.412539e-01
      vertex 2.556677e-01 6.223307e-01 -4.412539e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 2.527894e-01 7.569424e-01 -3.912539e-01
      vertex -1.290423e-01 7.569424e-01 -3.912539e-01
      vertex -1.305116e-01 7.655611e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 2.527894e-01 7.569424e-01 -3.912539e-01
      vertex -1.305116e-01 7.655611e-01 -4.412539e-01
      vertex 2.556677e-01 7.655611e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 9.995685e-01 0.000000e+00 -2.937353e-02
    outer loop
      vertex -1.290423e-01 7.569424e-01 -3.912539e-01
      vertex -1.290423e-01 6.153245e-01 -3.912539e-01
      vertex -1.305116e-01 6.223307e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 9.995685e-01 0.000000e+00 -2.937353e-02
    outer loop
      vertex -1.290423e-01 7.569424e-01 -3.912539e-01
      vertex -1.305116e-01 6.223307e-01 -4.412539e-01
      vertex -1.305116e-01 7.655611e-01 -4.412539e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.722185e-01 5.653650e-01 -3.471888e-02
      vertex 4.122478e-01 5.653650e-01 -3.471888e-02
      vertex 4.122478e-01 6.954847e-01 -3.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.722185e-01 5.653650e-01 -3.471888e-02
      vertex 4.122478e-01 6.954847e-01 -3.471888e-02
      vertex 2.722185e-01 6.954847e-01 -3.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.755920e-01 5.723712e-01 -8.471888e-02
      vertex 4.173565e-01 7.041034e-01 -8.471888e-02
      vertex 4.173565e-01 5.723712e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.755920e-01 5.723712e-01 -8.471888e-02
      vertex 2.755920e-01 7.041034e-01 -8.471888e-02
      vertex 4.173565e-01 7.041034e-01 -8.471888e-02
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex 2.722185e-01 5.653650e-01 -3.471888e-02
      vertex 4.122478e-01 5.653650e-01 -3.471888e-02
      vertex 4.173565e-01 5.723712e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex 2.722185e-01 5.653650e-01 -3.471888e-02
      vertex 4.173565e-01 5.723712e-01 -8.471888e-02
      vertex 2.755920e-01 5.723712e-01 -8.471888e-02
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.122478e-01 5.653650e-01 -3.471888e-02
      vertex 4.122478e-01 6.954847e-01 -3.471888e-02
      vertex 4.173565e-01 7.041034e-01 -8.471888e-02
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.122478e-01 5.653650e-01 -3.471888e-02
      vertex 4.173565e-01 7.041034e-01 -8.471888e-02
      vertex 4.173565e-01 5.723712e-01 -8.471888e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 4.122478e-01 6.954847e-01 -3.471888e-02
      vertex 2.722185e-01 6.954847e-01 -3.471888e-02
      vertex 2.755920e-01 7.041034e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 4.122478e-01 6.954847e-01 -3.471888e-02
      vertex 2.755920e-01 7.041034e-01 -8.471888e-02
      vertex 4.173565e-01 7.041034e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.722185e-01 6.954847e-01 -3.471888e-02
      vertex 2.722185e-01 5.653650e-01 -3.471888e-02
      vertex 2.755920e-01 5.723712e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.722185e-01 6.954847e-01 -3.471888e-02
      vertex 2.755920e-01 5.723712e-01 -8.471888e-02
      vertex 2.755920e-01 7.041034e-01 -8.471888e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -4.381760e-01 7.870541e-01 -3.621301e-01
      vertex -1.943329e-01 7.870541e-01 -3.621301e-01
      vertex -1.943329e-01 1.077996e+00 -3.621301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -4.381760e-01 7.870541e-01 -3.621301e-01
      vertex -1.943329e-01 1.077996e+00 -3.621301e-01
      vertex -4.381760e-01 1.077996e+00 -3.621301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.431985e-01 7.960756e-01 -4.121301e-01
      vertex -1.965604e-01 1.090353e+00 -4.121301e-01
      vertex -1.965604e-01 7.960756e-01 -4.121301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.431985e-01 7.960756e-01 -4.121301e-01
      vertex -4.431985e-01 1.090353e+00 -4.121301e-01
      vertex -1.965604e-01 1.090353e+00 -4.121301e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex -4.381760e-01 7.870541e-01 -3.621301e-01
      vertex -1.943329e-01 7.870541e-01 -3.621301e-01
      vertex -1.965604e-01 7.960756e-01 -4.121301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex -4.381760e-01 7.870541e-01 -3.621301e-01
      vertex -1.965604e-01 7.960756e-01 -4.121301e-01
      vertex -4.431985e-01 7.960756e-01 -4.121301e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -1.943329e-01 7.870541e-01 -3.621301e-01
      vertex -1.943329e-01 1.077996e+00 -3.621301e-01
      vertex -1.965604e-01 1.090353e+00 -4.121301e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -1.943329e-01 7.870541e-01 -3.621301e-01
      vertex -1.965604e-01 1.090353e+00 -4.121301e-01
      vertex -1.965604e-01 7.960756e-01 -4.121301e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex -1.943329e-01 1.077996e+00 -3.621301e-01
      vertex -4.381760e-01 1.077996e+00 -3.621301e-01
      vertex -4.431985e-01 1.090353e+00 -4.121301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex -1.943329e-01 1.077996e+00 -3.621301e-01
      vertex -4.431985e-01 1.090353e+00 -4.121301e-01
      vertex -1.965604e-01 1.090353e+00 -4.121301e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.381760e-01 1.077996e+00 -3.621301e-01
      vertex -4.381760e-01 7.870541e-01 -3.621301e-01
      vertex -4.431985e-01 7.960756e-01 -4.121301e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.381760e-01 1.077996e+00 -3.621301e-01
      vertex -4.431985e-01 7.960756e-01 -4.121301e-01
      vertex -4.431985e-01 1.090353e+00 -4.121301e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -1.934966e-01 1.107561e+00 -3.433583e-01
      vertex -1.934966e-01 1.238091e+00 -3.433583e-01
      vertex -4.362903e-01 1.238091e+00 -3.433583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.934966e-01 1.107561e+00 -3.433583e-01
      vertex -4.362903e-01 1.238091e+00 -3.433583e-01
      vertex -4.362903e-01 1.107561e+00 -3.433583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.957241e-01 1.120311e+00 -3.933583e-01
      vertex -4.413128e-01 1.252344e+00 -3.933583e-01
      vertex -1.957241e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.957241e-01 1.120311e+00 -3.933583e-01
      vertex -4.413128e-01 1.120311e+00 -3.933583e-01
      vertex -4.413128e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -1.934966e-01 1.107561e+00 -3.433583e-01
      vertex -1.934966e-01 1.238091e+00 -3.433583e-01
      vertex -1.957241e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -1.934966e-01 1.107561e+00 -3.433583e-01
      vertex -1.957241e-01 1.252344e+00 -3.933583e-01
      vertex -1.957241e-01 1.120311e+00 -3.933583e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex -1.934966e-01 1.238091e+00 -3.433583e-01
      vertex -4.362903e-01 1.238091e+00 -3.433583e-01
      vertex -4.413128e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex -1.934966e-01 1.238091e+00 -3.433583e-01
      vertex -4.413128e-01 1.252344e+00 -3.933583e-01
      vertex -1.957241e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.362903e-01 1.238091e+00 -3.433583e-01
      vertex -4.362903e-01 1.107561e+00 -3.433583e-01
      vertex -4.413128e-01 1.120311e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.362903e-01 1.238091e+00 -3.433583e-01
      vertex -4.413128e-01 1.120311e+00 -3.933583e-01
      vertex -4.413128e-01 1.252344e+00 -3.933583e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex -4.362903e-01 1.107561e+00 -3.433583e-01
      vertex -1.934966e-01 1.107561e+00 -3.433583e-01
      vertex -1.957241e-01 1.120311e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex -4.362903e-01 1.107561e+00 -3.433583e-01
      vertex -1.957241e-01 1.120311e+00 -3.933583e-01
      vertex -4.413128e-01 1.120311e+00 -3.933583e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.686917e-01 7.294617e-01 -4.293273e-02
      vertex 2.543774e-01 7.294617e-01 -4.293273e-02
      vertex 2.543774e-01 9.991143e-01 -4.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.686917e-01 7.294617e-01 -4.293273e-02
      vertex 2.543774e-01 9.991143e-01 -4.293273e-02
      vertex 1.686917e-01 9.991143e-01 -4.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.707780e-01 7.384831e-01 -9.293273e-02
      vertex 2.575233e-01 1.011471e+00 -9.293273e-02
      vertex 2.575233e-01 7.384831e-01 -9.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.707780e-01 7.384831e-01 -9.293273e-02
      vertex 1.707780e-01 1.011471e+00 -9.293273e-02
      vertex 2.575233e-01 1.011471e+00 -9.293273e-02
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 1.686917e-01 7.294617e-01 -4.293273e-02
      vertex 2.543774e-01 7.294617e-01 -4.293273e-02
      vertex 2.575233e-01 7.384831e-01 -9.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 1.686917e-01 7.294617e-01 -4.293273e-02
      vertex 2.575233e-01 7.384831e-01 -9.293273e-02
      vertex 1.707780e-01 7.384831e-01 -9.293273e-02
    endloop
  endfacet
  facet normal -9.980265e-01 -2.054554e-16 -6.279485e-02
    outer loop
      vertex 2.543774e-01 7.294617e-01 -4.293273e-02
      vertex 2.543774e-01 9.991143e-01 -4.293273e-02
      vertex 2.575233e-01 1.011471e+00 -9.293273e-02
    endloop
  endfacet
  facet normal -9.980265e-01 -2.041347e-16 -6.279485e-02
    outer loop
      vertex 2.543774e-01 7.294617e-01 -4.293273e-02
      vertex 2.575233e-01 1.011471e+00 -9.293273e-02
      vertex 2.575233e-01 7.384831e-01 -9.293273e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 2.543774e-01 9.991143e-01 -4.293273e-02
      vertex 1.686917e-01 9.991143e-01 -4.293273e-02
      vertex 1.707780e-01 1.011471e+00 -9.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 2.543774e-01 9.991143e-01 -4.293273e-02
      vertex 1.707780e-01 1.011471e+00 -9.293273e-02
      vertex 2.575233e-01 1.011471e+00 -9.293273e-02
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.686917e-01 9.991143e-01 -4.293273e-02
      vertex 1.686917e-01 7.294617e-01 -4.293273e-02
      vertex 1.707780e-01 7.384831e-01 -9.293273e-02
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.686917e-01 9.991143e-01 -4.293273e-02
      vertex 1.707780e-01 7.384831e-01 -9.293273e-02
      vertex 1.707780e-01 1.011471e+00 -9.293273e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 2.315944e-01 9.386166e-01 3.191669e-01
      vertex 2.315944e-01 1.049236e+00 3.191669e-01
      vertex 1.535831e-01 1.049236e+00 3.191669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.315944e-01 9.386166e-01 3.191669e-01
      vertex 1.535831e-01 1.049236e+00 3.191669e-01
      vertex 1.535831e-01 9.386166e-01 3.191669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.347404e-01 9.513666e-01 2.691669e-01
      vertex 1.556693e-01 1.063488e+00 2.691669e-01
      vertex 2.347404e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.347404e-01 9.513666e-01 2.691669e-01
      vertex 1.556693e-01 9.513666e-01 2.691669e-01
      vertex 1.556693e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal -9.980265e-01 0.000000e+00 -6.279485e-02
    outer loop
      vertex 2.315944e-01 9.386166e-01 3.191669e-01
      vertex 2.315944e-01 1.049236e+00 3.191669e-01
      vertex 2.347404e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal -9.980265e-01 0.000000e+00 -6.279485e-02
    outer loop
      vertex 2.315944e-01 9.386166e-01 3.191669e-01
      vertex 2.347404e-01 1.063488e+00 2.691669e-01
      vertex 2.347404e-01 9.513666e-01 2.691669e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 2.315944e-01 1.049236e+00 3.191669e-01
      vertex 1.535831e-01 1.049236e+00 3.191669e-01
      vertex 1.556693e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 2.315944e-01 1.049236e+00 3.191669e-01
      vertex 1.556693e-01 1.063488e+00 2.691669e-01
      vertex 2.347404e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.535831e-01 1.049236e+00 3.191669e-01
      vertex 1.535831e-01 9.386166e-01 3.191669e-01
      vertex 1.556693e-01 9.513666e-01 2.691669e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.535831e-01 1.049236e+00 3.191669e-01
      vertex 1.556693e-01 9.513666e-01 2.691669e-01
      vertex 1.556693e-01 1.063488e+00 2.691669e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 1.535831e-01 9.386166e-01 3.191669e-01
      vertex 2.315944e-01 9.386166e-01 3.191669e-01
      vertex 2.347404e-01 9.513666e-01 2.691669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 1.535831e-01 9.386166e-01 3.191669e-01
      vertex 2.347404e-01 9.513666e-01 2.691669e-01
      vertex 1.556693e-01 9.513666e-01 2.691669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.910329e-01 7.782940e-01 -3.135782e-01
      vertex 4.407402e-01 7.782940e-01 -3.135782e-01
      vertex 4.407402e-01 1.065998e+00 -3.135782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 2.910329e-01 7.782940e-01 -3.135782e-01
      vertex 4.407402e-01 1.065998e+00 -3.135782e-01
      vertex 2.910329e-01 1.065998e+00 -3.135782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.944063e-01 7.873154e-01 -3.635782e-01
      vertex 4.458490e-01 1.078354e+00 -3.635782e-01
      vertex 4.458490e-01 7.873154e-01 -3.635782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.944063e-01 7.873154e-01 -3.635782e-01
      vertex 2.944063e-01 1.078354e+00 -3.635782e-01
      vertex 4.458490e-01 1.078354e+00 -3.635782e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 2.910329e-01 7.782940e-01 -3.135782e-01
      vertex 4.407402e-01 7.782940e-01 -3.135782e-01
      vertex 4.458490e-01 7.873154e-01 -3.635782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 2.910329e-01 7.782940e-01 -3.135782e-01
      vertex 4.458490e-01 7.873154e-01 -3.635782e-01
      vertex 2.944063e-01 7.873154e-01 -3.635782e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.407402e-01 7.782940e-01 -3.135782e-01
      vertex 4.407402e-01 1.065998e+00 -3.135782e-01
      vertex 4.458490e-01 1.078354e+00 -3.635782e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.407402e-01 7.782940e-01 -3.135782e-01
      vertex 4.458490e-01 1.078354e+00 -3.635782e-01
      vertex 4.458490e-01 7.873154e-01 -3.635782e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 4.407402e-01 1.065998e+00 -3.135782e-01
      vertex 2.910329e-01 1.065998e+00 -3.135782e-01
      vertex 2.944063e-01 1.078354e+00 -3.635782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 4.407402e-01 1.065998e+00 -3.135782e-01
      vertex 2.944063e-01 1.078354e+00 -3.635782e-01
      vertex 4.458490e-01 1.078354e+00 -3.635782e-01
    endloop
  endfacet
  facet normal 9.977317e-01 1.925077e-16 6.731598e-02
    outer loop
      vertex 2.910329e-01 1.065998e+00 -3.135782e-01
      vertex 2.910329e-01 7.782940e-01 -3.135782e-01
      vertex 2.944063e-01 7.873154e-01 -3.635782e-01
    endloop
  endfacet
  facet normal 9.977317e-01 1.895585e-16 6.731598e-02
    outer loop
      vertex 2.910329e-01 1.065998e+00 -3.135782e-01
      vertex 2.944063e-01 7.873154e-01 -3.635782e-01
      vertex 2.944063e-01 1.078354e+00 -3.635782e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 4.315962e-01 1.077146e+00 -2.240849e-01
      vertex 4.315962e-01 1.204092e+00 -2.240849e-01
      vertex 2.849949e-01 1.204092e+00 -2.240849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 4.315962e-01 1.077146e+00 -2.240849e-01
      vertex 2.849949e-01 1.204092e+00 -2.240849e-01
      vertex 2.849949e-01 1.077146e+00 -2.240849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 4.367050e-01 1.089896e+00 -2.740849e-01
      vertex 2.883683e-01 1.218344e+00 -2.740849e-01
      vertex 4.367050e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 4.367050e-01 1.089896e+00 -2.740849e-01
      vertex 2.883683e-01 1.089896e+00 -2.740849e-01
      vertex 2.883683e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.315962e-01 1.077146e+00 -2.240849e-01
      vertex 4.315962e-01 1.204092e+00 -2.240849e-01
      vertex 4.367050e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.315962e-01 1.077146e+00 -2.240849e-01
      vertex 4.367050e-01 1.218344e+00 -2.740849e-01
      vertex 4.367050e-01 1.089896e+00 -2.740849e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 4.315962e-01 1.204092e+00 -2.240849e-01
      vertex 2.849949e-01 1.204092e+00 -2.240849e-01
      vertex 2.883683e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 4.315962e-01 1.204092e+00 -2.240849e-01
      vertex 2.883683e-01 1.218344e+00 -2.740849e-01
      vertex 4.367050e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.849949e-01 1.204092e+00 -2.240849e-01
      vertex 2.849949e-01 1.077146e+00 -2.240849e-01
      vertex 2.883683e-01 1.089896e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.849949e-01 1.204092e+00 -2.240849e-01
      vertex 2.883683e-01 1.089896e+00 -2.740849e-01
      vertex 2.883683e-01 1.218344e+00 -2.740849e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 2.849949e-01 1.077146e+00 -2.240849e-01
      vertex 4.315962e-01 1.077146e+00 -2.240849e-01
      vertex 4.367050e-01 1.089896e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 2.849949e-01 1.077146e+00 -2.240849e-01
      vertex 4.367050e-01 1.089896e+00 -2.740849e-01
      vertex 2.883683e-01 1.089896e+00 -2.740849e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.534568e-01 -7.958933e-01 1.396899e-01
      vertex -1.417170e-01 -7.958933e-01 1.396899e-01
      vertex -1.417170e-01 -4.958444e-01 1.396899e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.534568e-01 -7.958933e-01 1.396899e-01
      vertex -1.417170e-01 -4.958444e-01 1.396899e-01
      vertex -1.534568e-01 -4.958444e-01 1.396899e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.554445e-01 -8.062020e-01 8.968990e-02
      vertex -1.435526e-01 -5.022667e-01 8.968990e-02
      vertex -1.435526e-01 -8.062020e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.554445e-01 -8.062020e-01 8.968990e-02
      vertex -1.554445e-01 -5.022667e-01 8.968990e-02
      vertex -1.435526e-01 -5.022667e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.534568e-01 -7.958933e-01 1.396899e-01
      vertex -1.417170e-01 -7.958933e-01 1.396899e-01
      vertex -1.435526e-01 -8.062020e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.534568e-01 -7.958933e-01 1.396899e-01
      vertex -1.435526e-01 -8.062020e-01 8.968990e-02
      vertex -1.554445e-01 -8.062020e-01 8.968990e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.417170e-01 -7.958933e-01 1.396899e-01
      vertex -1.417170e-01 -4.958444e-01 1.396899e-01
      vertex -1.435526e-01 -5.022667e-01 8.968990e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.417170e-01 -7.958933e-01 1.396899e-01
      vertex -1.435526e-01 -5.022667e-01 8.968990e-02
      vertex -1.435526e-01 -8.062020e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex -1.417170e-01 -4.958444e-01 1.396899e-01
      vertex -1.534568e-01 -4.958444e-01 1.396899e-01
      vertex -1.554445e-01 -5.022667e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex -1.417170e-01 -4.958444e-01 1.396899e-01
      vertex -1.554445e-01 -5.022667e-01 8.968990e-02
      vertex -1.435526e-01 -5.022667e-01 8.968990e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.534568e-01 -4.958444e-01 1.396899e-01
      vertex -1.534568e-01 -7.958933e-01 1.396899e-01
      vertex -1.554445e-01 -8.062020e-01 8.968990e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.534568e-01 -4.958444e-01 1.396899e-01
      vertex -1.554445e-01 -8.062020e-01 8.968990e-02
      vertex -1.554445e-01 -5.022667e-01 8.968990e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -1.311350e-01 -4.023580e-01 4.279380e-01
      vertex -1.311350e-01 1.367177e-02 4.279380e-01
      vertex -1.419983e-01 1.367177e-02 4.279380e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.311350e-01 -4.023580e-01 4.279380e-01
      vertex -1.419983e-01 1.367177e-02 4.279380e-01
      vertex -1.419983e-01 -4.023580e-01 4.279380e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.329706e-01 -4.079900e-01 3.779380e-01
      vertex -1.439859e-01 1.386315e-02 3.779380e-01
      vertex -1.329706e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.329706e-01 -4.079900e-01 3.779380e-01
      vertex -1.439859e-01 -4.079900e-01 3.779380e-01
      vertex -1.439859e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal -9.993268e-01 6.667045e-17 3.668659e-02
    outer loop
      vertex -1.311350e-01 -4.023580e-01 4.279380e-01
      vertex -1.311350e-01 1.367177e-02 4.279380e-01
      vertex -1.329706e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal -9.993268e-01 6.613537e-17 3.668659e-02
    outer loop
      vertex -1.311350e-01 -4.023580e-01 4.279380e-01
      vertex -1.329706e-01 1.386315e-02 3.779380e-01
      vertex -1.329706e-01 -4.079900e-01 3.779380e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex -1.311350e-01 1.367177e-02 4.279380e-01
      vertex -1.419983e-01 1.367177e-02 4.279380e-01
      vertex -1.439859e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex -1.311350e-01 1.367177e-02 4.279380e-01
      vertex -1.439859e-01 1.386315e-02 3.779380e-01
      vertex -1.329706e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.419983e-01 1.367177e-02 4.279380e-01
      vertex -1.419983e-01 -4.023580e-01 4.279380e-01
      vertex -1.439859e-01 -4.079900e-01 3.779380e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.419983e-01 1.367177e-02 4.279380e-01
      vertex -1.439859e-01 -4.079900e-01 3.779380e-01
      vertex -1.439859e-01 1.386315e-02 3.779380e-01
    endloop
  endfacet
  facet normal 1.015579e-14 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.419983e-01 -4.023580e-01 4.279380e-01
      vertex -1.311350e-01 -4.023580e-01 4.279380e-01
      vertex -1.329706e-01 -4.079900e-01 3.779380e-01
    endloop
  endfacet
  facet normal 9.976471e-15 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.419983e-01 -4.023580e-01 4.279380e-01
      vertex -1.329706e-01 -4.079900e-01 3.779380e-01
      vertex -1.439859e-01 -4.079900e-01 3.779380e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -1.433799e-01 8.510041e-02 9.439265e-02
      vertex -1.433799e-01 4.920911e-01 9.439265e-02
      vertex -1.552575e-01 4.920911e-01 9.439265e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.433799e-01 8.510041e-02 9.439265e-02
      vertex -1.552575e-01 4.920911e-01 9.439265e-02
      vertex -1.552575e-01 8.510041e-02 9.439265e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.452155e-01 8.618988e-02 4.439265e-02
      vertex -1.572451e-01 4.983909e-01 4.439265e-02
      vertex -1.452155e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.452155e-01 8.618988e-02 4.439265e-02
      vertex -1.572451e-01 8.618988e-02 4.439265e-02
      vertex -1.572451e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.433799e-01 8.510041e-02 9.439265e-02
      vertex -1.433799e-01 4.920911e-01 9.439265e-02
      vertex -1.452155e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.433799e-01 8.510041e-02 9.439265e-02
      vertex -1.452155e-01 4.983909e-01 4.439265e-02
      vertex -1.452155e-01 8.618988e-02 4.439265e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex -1.433799e-01 4.920911e-01 9.439265e-02
      vertex -1.552575e-01 4.920911e-01 9.439265e-02
      vertex -1.572451e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex -1.433799e-01 4.920911e-01 9.439265e-02
      vertex -1.572451e-01 4.983909e-01 4.439265e-02
      vertex -1.452155e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.552575e-01 4.920911e-01 9.439265e-02
      vertex -1.552575e-01 8.510041e-02 9.439265e-02
      vertex -1.572451e-01 8.618988e-02 4.439265e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.552575e-01 4.920911e-01 9.439265e-02
      vertex -1.572451e-01 8.618988e-02 4.439265e-02
      vertex -1.572451e-01 4.983909e-01 4.439265e-02
    endloop
  endfacet
  facet normal -7.008741e-15 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.552575e-01 8.510041e-02 9.439265e-02
      vertex -1.433799e-01 8.510041e-02 9.439265e-02
      vertex -1.452155e-01 8.618988e-02 4.439265e-02
    endloop
  endfacet
  facet normal -6.915643e-15 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.552575e-01 8.510041e-02 9.439265e-02
      vertex -1.452155e-01 8.618988e-02 4.439265e-02
      vertex -1.572451e-01 8.618988e-02 4.439265e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.265604e-01 -8.387109e-01 -6.798757e-02
      vertex 1.409457e-01 -8.387109e-01 -6.798757e-02
      vertex 1.409457e-01 -5.225199e-01 -6.798757e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.265604e-01 -8.387109e-01 -6.798757e-02
      vertex 1.409457e-01 -5.225199e-01 -6.798757e-02
      vertex -1.265604e-01 -5.225199e-01 -6.798757e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.281159e-01 -8.490196e-01 -1.179876e-01
      vertex 1.426781e-01 -5.289422e-01 -1.179876e-01
      vertex 1.426781e-01 -8.490196e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.281159e-01 -8.490196e-01 -1.179876e-01
      vertex -1.281159e-01 -5.289422e-01 -1.179876e-01
      vertex 1.426781e-01 -5.289422e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.265604e-01 -8.387109e-01 -6.798757e-02
      vertex 1.409457e-01 -8.387109e-01 -6.798757e-02
      vertex 1.426781e-01 -8.490196e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.265604e-01 -8.387109e-01 -6.798757e-02
      vertex 1.426781e-01 -8.490196e-01 -1.179876e-01
      vertex -1.281159e-01 -8.490196e-01 -1.179876e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.409457e-01 -8.387109e-01 -6.798757e-02
      vertex 1.409457e-01 -5.225199e-01 -6.798757e-02
      vertex 1.426781e-01 -5.289422e-01 -1.179876e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.409457e-01 -8.387109e-01 -6.798757e-02
      vertex 1.426781e-01 -5.289422e-01 -1.179876e-01
      vertex 1.426781e-01 -8.490196e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex 1.409457e-01 -5.225199e-01 -6.798757e-02
      vertex -1.265604e-01 -5.225199e-01 -6.798757e-02
      vertex -1.281159e-01 -5.289422e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex 1.409457e-01 -5.225199e-01 -6.798757e-02
      vertex -1.281159e-01 -5.289422e-01 -1.179876e-01
      vertex 1.426781e-01 -5.289422e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.265604e-01 -5.225199e-01 -6.798757e-02
      vertex -1.265604e-01 -8.387109e-01 -6.798757e-02
      vertex -1.281159e-01 -8.490196e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.265604e-01 -5.225199e-01 -6.798757e-02
      vertex -1.281159e-01 -8.490196e-01 -1.179876e-01
      vertex -1.281159e-01 -5.289422e-01 -1.179876e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.228730e-01 -3.994641e-01 4.536296e-01
      vertex 1.228730e-01 1.357344e-02 4.536296e-01
      vertex -1.103322e-01 1.357344e-02 4.536296e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.228730e-01 -3.994641e-01 4.536296e-01
      vertex -1.103322e-01 1.357344e-02 4.536296e-01
      vertex -1.103322e-01 -3.994641e-01 4.536296e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.246054e-01 -4.050961e-01 4.036296e-01
      vertex -1.118878e-01 1.376481e-02 4.036296e-01
      vertex 1.246054e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.246054e-01 -4.050961e-01 4.036296e-01
      vertex -1.118878e-01 -4.050961e-01 4.036296e-01
      vertex -1.118878e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.228730e-01 -3.994641e-01 4.536296e-01
      vertex 1.228730e-01 1.357344e-02 4.536296e-01
      vertex 1.246054e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.228730e-01 -3.994641e-01 4.536296e-01
      vertex 1.246054e-01 1.376481e-02 4.036296e-01
      vertex 1.246054e-01 -4.050961e-01 4.036296e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex 1.228730e-01 1.357344e-02 4.536296e-01
      vertex -1.103322e-01 1.357344e-02 4.536296e-01
      vertex -1.118878e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex 1.228730e-01 1.357344e-02 4.536296e-01
      vertex -1.118878e-01 1.376481e-02 4.036296e-01
      vertex 1.246054e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal 9.995164e-01 -6.716618e-17 -3.109625e-02
    outer loop
      vertex -1.103322e-01 1.357344e-02 4.536296e-01
      vertex -1.103322e-01 -3.994641e-01 4.536296e-01
      vertex -1.118878e-01 -4.050961e-01 4.036296e-01
    endloop
  endfacet
  facet normal 9.995164e-01 -3.298683e-17 -3.109625e-02
    outer loop
      vertex -1.103322e-01 1.357344e-02 4.536296e-01
      vertex -1.118878e-01 -4.050961e-01 4.036296e-01
      vertex -1.118878e-01 1.376481e-02 4.036296e-01
    endloop
  endfacet
  facet normal 2.365398e-16 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.103322e-01 -3.994641e-01 4.536296e-01
      vertex 1.228730e-01 -3.994641e-01 4.536296e-01
      vertex 1.246054e-01 -4.050961e-01 4.036296e-01
    endloop
  endfacet
  facet normal 2.368958e-16 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.103322e-01 -3.994641e-01 4.536296e-01
      vertex 1.246054e-01 -4.050961e-01 4.036296e-01
      vertex -1.118878e-01 -4.050961e-01 4.036296e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.518628e-01 9.550411e-02 -3.830756e-01
      vertex 1.518628e-01 5.522502e-01 -3.830756e-01
      vertex -1.363632e-01 5.522502e-01 -3.830756e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.518628e-01 9.550411e-02 -3.830756e-01
      vertex -1.363632e-01 5.522502e-01 -3.830756e-01
      vertex -1.363632e-01 9.550411e-02 -3.830756e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.535951e-01 9.659357e-02 -4.330756e-01
      vertex -1.379187e-01 5.585500e-01 -4.330756e-01
      vertex 1.535951e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.535951e-01 9.659357e-02 -4.330756e-01
      vertex -1.379187e-01 9.659357e-02 -4.330756e-01
      vertex -1.379187e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.518628e-01 9.550411e-02 -3.830756e-01
      vertex 1.518628e-01 5.522502e-01 -3.830756e-01
      vertex 1.535951e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.518628e-01 9.550411e-02 -3.830756e-01
      vertex 1.535951e-01 5.585500e-01 -4.330756e-01
      vertex 1.535951e-01 9.659357e-02 -4.330756e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex 1.518628e-01 5.522502e-01 -3.830756e-01
      vertex -1.363632e-01 5.522502e-01 -3.830756e-01
      vertex -1.379187e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex 1.518628e-01 5.522502e-01 -3.830756e-01
      vertex -1.379187e-01 5.585500e-01 -4.330756e-01
      vertex 1.535951e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.363632e-01 5.522502e-01 -3.830756e-01
      vertex -1.363632e-01 9.550411e-02 -3.830756e-01
      vertex -1.379187e-01 9.659357e-02 -4.330756e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.363632e-01 5.522502e-01 -3.830756e-01
      vertex -1.379187e-01 9.659357e-02 -4.330756e-01
      vertex -1.379187e-01 5.585500e-01 -4.330756e-01
    endloop
  endfacet
  facet normal -2.888254e-16 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.363632e-01 9.550411e-02 -3.830756e-01
      vertex 1.518628e-01 9.550411e-02 -3.830756e-01
      vertex 1.535951e-01 9.659357e-02 -4.330756e-01
    endloop
  endfacet
  facet normal -3.332553e-16 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.363632e-01 9.550411e-02 -3.830756e-01
      vertex 1.535951e-01 9.659357e-02 -4.330756e-01
      vertex -1.379187e-01 9.659357e-02 -4.330756e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.265459e-01 4.938547e-01 3.476216e-01
      vertex 1.265459e-01 5.269047e-01 3.476216e-01
      vertex -1.136302e-01 5.269047e-01 3.476216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.265459e-01 4.938547e-01 3.476216e-01
      vertex -1.136302e-01 5.269047e-01 3.476216e-01
      vertex -1.136302e-01 4.938547e-01 3.476216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.282783e-01 5.006154e-01 2.976216e-01
      vertex -1.151858e-01 5.341179e-01 2.976216e-01
      vertex 1.282783e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.282783e-01 5.006154e-01 2.976216e-01
      vertex -1.151858e-01 5.006154e-01 2.976216e-01
      vertex -1.151858e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.265459e-01 4.938547e-01 3.476216e-01
      vertex 1.265459e-01 5.269047e-01 3.476216e-01
      vertex 1.282783e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.265459e-01 4.938547e-01 3.476216e-01
      vertex 1.282783e-01 5.341179e-01 2.976216e-01
      vertex 1.282783e-01 5.006154e-01 2.976216e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.897537e-01 -1.427853e-01
    outer loop
      vertex 1.265459e-01 5.269047e-01 3.476216e-01
      vertex -1.136302e-01 5.269047e-01 3.476216e-01
      vertex -1.151858e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.897537e-01 -1.427853e-01
    outer loop
      vertex 1.265459e-01 5.269047e-01 3.476216e-01
      vertex -1.151858e-01 5.341179e-01 2.976216e-01
      vertex 1.282783e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.136302e-01 5.269047e-01 3.476216e-01
      vertex -1.136302e-01 4.938547e-01 3.476216e-01
      vertex -1.151858e-01 5.006154e-01 2.976216e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.136302e-01 5.269047e-01 3.476216e-01
      vertex -1.151858e-01 5.006154e-01 2.976216e-01
      vertex -1.151858e-01 5.341179e-01 2.976216e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.909820e-01 1.339952e-01
    outer loop
      vertex -1.136302e-01 4.938547e-01 3.476216e-01
      vertex 1.265459e-01 4.938547e-01 3.476216e-01
      vertex 1.282783e-01 5.006154e-01 2.976216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.909820e-01 1.339952e-01
    outer loop
      vertex -1.136302e-01 4.938547e-01 3.476216e-01
      vertex 1.282783e-01 5.006154e-01 2.976216e-01
      vertex -1.151858e-01 5.006154e-01 2.976216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -3.551481e-01 -1.104697e+00 -1.643516e-01
      vertex -1.939877e-01 -1.383835e+00 -1.643516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -1.939877e-01 -1.383835e+00 -1.643516e-01
      vertex -1.634165e-01 -1.383835e+00 -1.643516e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -1.634165e-01 -1.383835e+00 -1.643516e-01
      vertex -1.634165e-01 -1.003001e+00 -1.643516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
      vertex -1.963168e-01 -1.400450e+00 -2.143516e-01
      vertex -3.594122e-01 -1.117960e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
      vertex -1.653786e-01 -1.400450e+00 -2.143516e-01
      vertex -1.963168e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
      vertex -1.653786e-01 -1.015043e+00 -2.143516e-01
      vertex -1.653786e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 8.645332e-01 -4.991385e-01 5.867883e-02
    outer loop
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -3.551481e-01 -1.104697e+00 -1.643516e-01
      vertex -3.594122e-01 -1.117960e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 8.645332e-01 -4.991385e-01 5.867883e-02
    outer loop
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -3.594122e-01 -1.117960e+00 -2.143516e-01
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 8.481320e-01 4.896692e-01 -2.022280e-01
    outer loop
      vertex -3.551481e-01 -1.104697e+00 -1.643516e-01
      vertex -1.939877e-01 -1.383835e+00 -1.643516e-01
      vertex -1.963168e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 8.481320e-01 4.896692e-01 -2.022280e-01
    outer loop
      vertex -3.551481e-01 -1.104697e+00 -1.643516e-01
      vertex -1.963168e-01 -1.400450e+00 -2.143516e-01
      vertex -3.594122e-01 -1.117960e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.489757e-01 -3.153493e-01
    outer loop
      vertex -1.939877e-01 -1.383835e+00 -1.643516e-01
      vertex -1.634165e-01 -1.383835e+00 -1.643516e-01
      vertex -1.653786e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.489757e-01 -3.153493e-01
    outer loop
      vertex -1.939877e-01 -1.383835e+00 -1.643516e-01
      vertex -1.653786e-01 -1.400450e+00 -2.143516e-01
      vertex -1.963168e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal -9.992309e-01 7.282500e-17 3.921158e-02
    outer loop
      vertex -1.634165e-01 -1.383835e+00 -1.643516e-01
      vertex -1.634165e-01 -1.003001e+00 -1.643516e-01
      vertex -1.653786e-01 -1.015043e+00 -2.143516e-01
    endloop
  endfacet
  facet normal -9.992309e-01 7.167989e-17 3.921158e-02
    outer loop
      vertex -1.634165e-01 -1.383835e+00 -1.643516e-01
      vertex -1.653786e-01 -1.015043e+00 -2.143516e-01
      vertex -1.653786e-01 -1.400450e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.721986e-01 2.341579e-01
    outer loop
      vertex -1.634165e-01 -1.003001e+00 -1.643516e-01
      vertex -2.964339e-01 -1.003001e+00 -1.643516e-01
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.721986e-01 2.341579e-01
    outer loop
      vertex -1.634165e-01 -1.003001e+00 -1.643516e-01
      vertex -2.999931e-01 -1.015043e+00 -2.143516e-01
      vertex -1.653786e-01 -1.015043e+00 -2.143516e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.634849e-01 -8.076035e-01 -2.951704e-01
      vertex -1.950164e-01 -8.076035e-01 -2.951704e-01
      vertex -3.006809e-01 -9.906198e-01 -2.951704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.634849e-01 -8.076035e-01 -2.951704e-01
      vertex -3.006809e-01 -9.906198e-01 -2.951704e-01
      vertex -1.634849e-01 -9.906198e-01 -2.951704e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.653880e-01 -8.170048e-01 -3.451704e-01
      vertex -3.041812e-01 -1.002152e+00 -3.451704e-01
      vertex -1.972866e-01 -8.170048e-01 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.653880e-01 -8.170048e-01 -3.451704e-01
      vertex -1.653880e-01 -1.002152e+00 -3.451704e-01
      vertex -3.041812e-01 -1.002152e+00 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827784e-01 1.847879e-01
    outer loop
      vertex -1.634849e-01 -8.076035e-01 -2.951704e-01
      vertex -1.950164e-01 -8.076035e-01 -2.951704e-01
      vertex -1.972866e-01 -8.170048e-01 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827784e-01 1.847879e-01
    outer loop
      vertex -1.634849e-01 -8.076035e-01 -2.951704e-01
      vertex -1.972866e-01 -8.170048e-01 -3.451704e-01
      vertex -1.653880e-01 -8.170048e-01 -3.451704e-01
    endloop
  endfacet
  facet normal 8.647331e-01 -4.992539e-01 5.461064e-02
    outer loop
      vertex -1.950164e-01 -8.076035e-01 -2.951704e-01
      vertex -3.006809e-01 -9.906198e-01 -2.951704e-01
      vertex -3.041812e-01 -1.002152e+00 -3.451704e-01
    endloop
  endfacet
  facet normal 8.647331e-01 -4.992539e-01 5.461064e-02
    outer loop
      vertex -1.950164e-01 -8.076035e-01 -2.951704e-01
      vertex -3.041812e-01 -1.002152e+00 -3.451704e-01
      vertex -1.972866e-01 -8.170048e-01 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.744197e-01 -2.247360e-01
    outer loop
      vertex -3.006809e-01 -9.906198e-01 -2.951704e-01
      vertex -1.634849e-01 -9.906198e-01 -2.951704e-01
      vertex -1.653880e-01 -1.002152e+00 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.744197e-01 -2.247360e-01
    outer loop
      vertex -3.006809e-01 -9.906198e-01 -2.951704e-01
      vertex -1.653880e-01 -1.002152e+00 -3.451704e-01
      vertex -3.041812e-01 -1.002152e+00 -3.451704e-01
    endloop
  endfacet
  facet normal -9.992764e-01 0.000000e+00 3.803495e-02
    outer loop
      vertex -1.634849e-01 -9.906198e-01 -2.951704e-01
      vertex -1.634849e-01 -8.076035e-01 -2.951704e-01
      vertex -1.653880e-01 -8.170048e-01 -3.451704e-01
    endloop
  endfacet
  facet normal -9.992764e-01 0.000000e+00 3.803495e-02
    outer loop
      vertex -1.634849e-01 -9.906198e-01 -2.951704e-01
      vertex -1.653880e-01 -8.170048e-01 -3.451704e-01
      vertex -1.653880e-01 -1.002152e+00 -3.451704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex -1.231807e-01 -1.440532e+00 -3.189870e-01
      vertex 1.794025e-01 -1.440532e+00 -3.189870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex 1.794025e-01 -1.440532e+00 -3.189870e-01
      vertex 2.523672e-01 -1.314153e+00 -3.189870e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex 2.523672e-01 -1.314153e+00 -3.189870e-01
      vertex 2.523672e-01 -1.045556e+00 -3.189870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
      vertex 1.814794e-01 -1.457209e+00 -3.689870e-01
      vertex -1.246067e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
      vertex 2.552888e-01 -1.329367e+00 -3.689870e-01
      vertex 1.814794e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
      vertex 2.552888e-01 -1.057661e+00 -3.689870e-01
      vertex 2.552888e-01 -1.329367e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex -1.231807e-01 -1.440532e+00 -3.189870e-01
      vertex -1.246067e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex -1.246067e-01 -1.457209e+00 -3.689870e-01
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.486260e-01 -3.163996e-01
    outer loop
      vertex -1.231807e-01 -1.440532e+00 -3.189870e-01
      vertex 1.794025e-01 -1.440532e+00 -3.189870e-01
      vertex 1.814794e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.486260e-01 -3.163996e-01
    outer loop
      vertex -1.231807e-01 -1.440532e+00 -3.189870e-01
      vertex 1.814794e-01 -1.457209e+00 -3.689870e-01
      vertex -1.246067e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal -8.487575e-01 4.900304e-01 -1.986979e-01
    outer loop
      vertex 1.794025e-01 -1.440532e+00 -3.189870e-01
      vertex 2.523672e-01 -1.314153e+00 -3.189870e-01
      vertex 2.552888e-01 -1.329367e+00 -3.689870e-01
    endloop
  endfacet
  facet normal -8.487575e-01 4.900304e-01 -1.986979e-01
    outer loop
      vertex 1.794025e-01 -1.440532e+00 -3.189870e-01
      vertex 2.552888e-01 -1.329367e+00 -3.689870e-01
      vertex 1.814794e-01 -1.457209e+00 -3.689870e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.523672e-01 -1.314153e+00 -3.189870e-01
      vertex 2.523672e-01 -1.045556e+00 -3.189870e-01
      vertex 2.552888e-01 -1.057661e+00 -3.689870e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.523672e-01 -1.314153e+00 -3.189870e-01
      vertex 2.552888e-01 -1.057661e+00 -3.689870e-01
      vertex 2.552888e-01 -1.329367e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.719258e-01 2.352874e-01
    outer loop
      vertex 2.523672e-01 -1.045556e+00 -3.189870e-01
      vertex -1.231807e-01 -1.045556e+00 -3.189870e-01
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.719258e-01 2.352874e-01
    outer loop
      vertex 2.523672e-01 -1.045556e+00 -3.189870e-01
      vertex -1.246067e-01 -1.057661e+00 -3.689870e-01
      vertex 2.552888e-01 -1.057661e+00 -3.689870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex 1.722737e-01 -7.808868e-01 -1.473664e-01
      vertex -1.182859e-01 -7.808868e-01 -1.473664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex -1.182859e-01 -7.808868e-01 -1.473664e-01
      vertex -1.182859e-01 -9.576052e-01 -1.473664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex -1.182859e-01 -9.576052e-01 -1.473664e-01
      vertex 2.423390e-01 -9.576052e-01 -1.473664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
      vertex -1.197120e-01 -7.903011e-01 -1.973664e-01
      vertex 1.743506e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
      vertex -1.197120e-01 -9.691500e-01 -1.973664e-01
      vertex -1.197120e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
      vertex 2.452606e-01 -9.691500e-01 -1.973664e-01
      vertex -1.197120e-01 -9.691500e-01 -1.973664e-01
    endloop
  endfacet
  facet normal -8.645639e-01 -4.991562e-01 5.807128e-02
    outer loop
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex 1.722737e-01 -7.808868e-01 -1.473664e-01
      vertex 1.743506e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal -8.645639e-01 -4.991562e-01 5.807128e-02
    outer loop
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex 1.743506e-01 -7.903011e-01 -1.973664e-01
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827322e-01 1.850337e-01
    outer loop
      vertex 1.722737e-01 -7.808868e-01 -1.473664e-01
      vertex -1.182859e-01 -7.808868e-01 -1.473664e-01
      vertex -1.197120e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827322e-01 1.850337e-01
    outer loop
      vertex 1.722737e-01 -7.808868e-01 -1.473664e-01
      vertex -1.197120e-01 -7.903011e-01 -1.973664e-01
      vertex 1.743506e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.182859e-01 -7.808868e-01 -1.473664e-01
      vertex -1.182859e-01 -9.576052e-01 -1.473664e-01
      vertex -1.197120e-01 -9.691500e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.182859e-01 -7.808868e-01 -1.473664e-01
      vertex -1.197120e-01 -9.691500e-01 -1.973664e-01
      vertex -1.197120e-01 -7.903011e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.743644e-01 -2.249756e-01
    outer loop
      vertex -1.182859e-01 -9.576052e-01 -1.473664e-01
      vertex 2.423390e-01 -9.576052e-01 -1.473664e-01
      vertex 2.452606e-01 -9.691500e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.743644e-01 -2.249756e-01
    outer loop
      vertex -1.182859e-01 -9.576052e-01 -1.473664e-01
      vertex 2.452606e-01 -9.691500e-01 -1.973664e-01
      vertex -1.197120e-01 -9.691500e-01 -1.973664e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.423390e-01 -9.576052e-01 -1.473664e-01
      vertex 2.423390e-01 -9.022435e-01 -1.473664e-01
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.423390e-01 -9.576052e-01 -1.473664e-01
      vertex 2.452606e-01 -9.131209e-01 -1.973664e-01
      vertex 2.452606e-01 -9.691500e-01 -1.973664e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 3.234759e-01 -9.670897e-01 3.095137e-01
      vertex 2.714428e-01 -8.769659e-01 3.095137e-01
      vertex 2.430009e-01 -8.769659e-01 3.095137e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 3.234759e-01 -9.670897e-01 3.095137e-01
      vertex 2.430009e-01 -8.769659e-01 3.095137e-01
      vertex 2.430009e-01 -1.106476e+00 3.095137e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.278584e-01 -9.801922e-01 2.595137e-01
      vertex 2.462931e-01 -8.888473e-01 2.595137e-01
      vertex 2.751204e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.278584e-01 -9.801922e-01 2.595137e-01
      vertex 2.462931e-01 -1.121467e+00 2.595137e-01
      vertex 2.462931e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal -8.647130e-01 -4.992423e-01 5.503294e-02
    outer loop
      vertex 3.234759e-01 -9.670897e-01 3.095137e-01
      vertex 2.714428e-01 -8.769659e-01 3.095137e-01
      vertex 2.751204e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal -8.647130e-01 -4.992423e-01 5.503294e-02
    outer loop
      vertex 3.234759e-01 -9.670897e-01 3.095137e-01
      vertex 2.751204e-01 -8.888473e-01 2.595137e-01
      vertex 3.278584e-01 -9.801922e-01 2.595137e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.729084e-01 2.311911e-01
    outer loop
      vertex 2.714428e-01 -8.769659e-01 3.095137e-01
      vertex 2.430009e-01 -8.769659e-01 3.095137e-01
      vertex 2.462931e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.729084e-01 2.311911e-01
    outer loop
      vertex 2.714428e-01 -8.769659e-01 3.095137e-01
      vertex 2.462931e-01 -8.888473e-01 2.595137e-01
      vertex 2.751204e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal 9.978392e-01 0.000000e+00 6.570294e-02
    outer loop
      vertex 2.430009e-01 -8.769659e-01 3.095137e-01
      vertex 2.430009e-01 -1.106476e+00 3.095137e-01
      vertex 2.462931e-01 -1.121467e+00 2.595137e-01
    endloop
  endfacet
  facet normal 9.978392e-01 0.000000e+00 6.570294e-02
    outer loop
      vertex 2.430009e-01 -8.769659e-01 3.095137e-01
      vertex 2.462931e-01 -1.121467e+00 2.595137e-01
      vertex 2.462931e-01 -8.888473e-01 2.595137e-01
    endloop
  endfacet
  facet normal -8.480583e-01 4.896267e-01 -2.026398e-01
    outer loop
      vertex 2.430009e-01 -1.106476e+00 3.095137e-01
      vertex 3.234759e-01 -9.670897e-01 3.095137e-01
      vertex 3.278584e-01 -9.801922e-01 2.595137e-01
    endloop
  endfacet
  facet normal -8.480583e-01 4.896267e-01 -2.026398e-01
    outer loop
      vertex 2.430009e-01 -1.106476e+00 3.095137e-01
      vertex 3.278584e-01 -9.801922e-01 2.595137e-01
      vertex 2.462931e-01 -1.121467e+00 2.595137e-01
    endloop
  endfacet
endsolid shards
```

<!-- optional proof anchor (uncomment to enable):
<p align="center"><sub>MPC signing architecture audited to 0 Critical/High · threshold-BLS air-gapped signing presented at NBC-2025, NTU Singapore</sub></p>
-->

---

<p align="center">
  <sub>📍 Bangalore · open to Singapore · ✉️ <a href="mailto:rana.iiitb@gmail.com">rana.iiitb@gmail.com</a> · ✍️ writeups soon</sub>
</p>
