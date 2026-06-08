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

#### Reconstruct the secret · drag to rotate

```stl
solid shards
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.971127e-01 5.553298e-01 3.689717e-02
      vertex -1.635228e-01 5.553298e-01 3.689717e-02
      vertex -1.635228e-01 6.831398e-01 3.689717e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.971127e-01 5.553298e-01 3.689717e-02
      vertex -1.635228e-01 6.831398e-01 3.689717e-02
      vertex -3.971127e-01 6.831398e-01 3.689717e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.021228e-01 5.623360e-01 -1.310283e-02
      vertex -1.655858e-01 6.917586e-01 -1.310283e-02
      vertex -1.655858e-01 5.623360e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.021228e-01 5.623360e-01 -1.310283e-02
      vertex -4.021228e-01 6.917586e-01 -1.310283e-02
      vertex -1.655858e-01 6.917586e-01 -1.310283e-02
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -3.971127e-01 5.553298e-01 3.689717e-02
      vertex -1.635228e-01 5.553298e-01 3.689717e-02
      vertex -1.655858e-01 5.623360e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -3.971127e-01 5.553298e-01 3.689717e-02
      vertex -1.655858e-01 5.623360e-01 -1.310283e-02
      vertex -4.021228e-01 5.623360e-01 -1.310283e-02
    endloop
  endfacet
  facet normal -9.991498e-01 0.000000e+00 4.122622e-02
    outer loop
      vertex -1.635228e-01 5.553298e-01 3.689717e-02
      vertex -1.635228e-01 6.831398e-01 3.689717e-02
      vertex -1.655858e-01 6.917586e-01 -1.310283e-02
    endloop
  endfacet
  facet normal -9.991498e-01 0.000000e+00 4.122622e-02
    outer loop
      vertex -1.635228e-01 5.553298e-01 3.689717e-02
      vertex -1.655858e-01 6.917586e-01 -1.310283e-02
      vertex -1.655858e-01 5.623360e-01 -1.310283e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex -1.635228e-01 6.831398e-01 3.689717e-02
      vertex -3.971127e-01 6.831398e-01 3.689717e-02
      vertex -4.021228e-01 6.917586e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex -1.635228e-01 6.831398e-01 3.689717e-02
      vertex -4.021228e-01 6.917586e-01 -1.310283e-02
      vertex -1.655858e-01 6.917586e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 9.950172e-01 0.000000e+00 -9.970318e-02
    outer loop
      vertex -3.971127e-01 6.831398e-01 3.689717e-02
      vertex -3.971127e-01 5.553298e-01 3.689717e-02
      vertex -4.021228e-01 5.623360e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 9.950172e-01 0.000000e+00 -9.970318e-02
    outer loop
      vertex -3.971127e-01 6.831398e-01 3.689717e-02
      vertex -4.021228e-01 5.623360e-01 -1.310283e-02
      vertex -4.021228e-01 6.917586e-01 -1.310283e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.385562e-01 6.606903e-01 -7.150069e-01
      vertex 2.714267e-01 6.606903e-01 -7.150069e-01
      vertex 2.714267e-01 8.127493e-01 -7.150069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.385562e-01 6.606903e-01 -7.150069e-01
      vertex 2.714267e-01 8.127493e-01 -7.150069e-01
      vertex -1.385562e-01 8.127493e-01 -7.150069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.400255e-01 6.676966e-01 -7.650069e-01
      vertex 2.743050e-01 8.213681e-01 -7.650069e-01
      vertex 2.743050e-01 6.676966e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.400255e-01 6.676966e-01 -7.650069e-01
      vertex -1.400255e-01 8.213681e-01 -7.650069e-01
      vertex 2.743050e-01 8.213681e-01 -7.650069e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -1.385562e-01 6.606903e-01 -7.150069e-01
      vertex 2.714267e-01 6.606903e-01 -7.150069e-01
      vertex 2.743050e-01 6.676966e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex -1.385562e-01 6.606903e-01 -7.150069e-01
      vertex 2.743050e-01 6.676966e-01 -7.650069e-01
      vertex -1.400255e-01 6.676966e-01 -7.650069e-01
    endloop
  endfacet
  facet normal -9.983472e-01 0.000000e+00 -5.747141e-02
    outer loop
      vertex 2.714267e-01 6.606903e-01 -7.150069e-01
      vertex 2.714267e-01 8.127493e-01 -7.150069e-01
      vertex 2.743050e-01 8.213681e-01 -7.650069e-01
    endloop
  endfacet
  facet normal -9.983472e-01 0.000000e+00 -5.747141e-02
    outer loop
      vertex 2.714267e-01 6.606903e-01 -7.150069e-01
      vertex 2.743050e-01 8.213681e-01 -7.650069e-01
      vertex 2.743050e-01 6.676966e-01 -7.650069e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 2.714267e-01 8.127493e-01 -7.150069e-01
      vertex -1.385562e-01 8.127493e-01 -7.150069e-01
      vertex -1.400255e-01 8.213681e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 2.714267e-01 8.127493e-01 -7.150069e-01
      vertex -1.400255e-01 8.213681e-01 -7.650069e-01
      vertex 2.743050e-01 8.213681e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 9.995685e-01 0.000000e+00 -2.937353e-02
    outer loop
      vertex -1.385562e-01 8.127493e-01 -7.150069e-01
      vertex -1.385562e-01 6.606903e-01 -7.150069e-01
      vertex -1.400255e-01 6.676966e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 9.995685e-01 0.000000e+00 -2.937353e-02
    outer loop
      vertex -1.385562e-01 8.127493e-01 -7.150069e-01
      vertex -1.400255e-01 6.676966e-01 -7.650069e-01
      vertex -1.400255e-01 8.213681e-01 -7.650069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.753523e-01 5.718735e-01 -8.116691e-02
      vertex 4.169936e-01 5.718735e-01 -8.116691e-02
      vertex 4.169936e-01 7.034911e-01 -8.116691e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.753523e-01 5.718735e-01 -8.116691e-02
      vertex 4.169936e-01 7.034911e-01 -8.116691e-02
      vertex 2.753523e-01 7.034911e-01 -8.116691e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.787258e-01 5.788798e-01 -1.311669e-01
      vertex 4.221023e-01 7.121099e-01 -1.311669e-01
      vertex 4.221023e-01 5.788798e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.787258e-01 5.788798e-01 -1.311669e-01
      vertex 2.787258e-01 7.121099e-01 -1.311669e-01
      vertex 4.221023e-01 7.121099e-01 -1.311669e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex 2.753523e-01 5.718735e-01 -8.116691e-02
      vertex 4.169936e-01 5.718735e-01 -8.116691e-02
      vertex 4.221023e-01 5.788798e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.903247e-01 1.387693e-01
    outer loop
      vertex 2.753523e-01 5.718735e-01 -8.116691e-02
      vertex 4.221023e-01 5.788798e-01 -1.311669e-01
      vertex 2.787258e-01 5.788798e-01 -1.311669e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.169936e-01 5.718735e-01 -8.116691e-02
      vertex 4.169936e-01 7.034911e-01 -8.116691e-02
      vertex 4.221023e-01 7.121099e-01 -1.311669e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.169936e-01 5.718735e-01 -8.116691e-02
      vertex 4.221023e-01 7.121099e-01 -1.311669e-01
      vertex 4.221023e-01 5.788798e-01 -1.311669e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 4.169936e-01 7.034911e-01 -8.116691e-02
      vertex 2.753523e-01 7.034911e-01 -8.116691e-02
      vertex 2.787258e-01 7.121099e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.854665e-01 -1.698698e-01
    outer loop
      vertex 4.169936e-01 7.034911e-01 -8.116691e-02
      vertex 2.787258e-01 7.121099e-01 -1.311669e-01
      vertex 4.221023e-01 7.121099e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.753523e-01 7.034911e-01 -8.116691e-02
      vertex 2.753523e-01 5.718735e-01 -8.116691e-02
      vertex 2.787258e-01 5.788798e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.753523e-01 7.034911e-01 -8.116691e-02
      vertex 2.787258e-01 5.788798e-01 -1.311669e-01
      vertex 2.787258e-01 7.121099e-01 -1.311669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -4.684216e-01 8.413815e-01 -6.632313e-01
      vertex -2.077470e-01 8.413815e-01 -6.632313e-01
      vertex -2.077470e-01 1.152406e+00 -6.632313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -4.684216e-01 8.413815e-01 -6.632313e-01
      vertex -2.077470e-01 1.152406e+00 -6.632313e-01
      vertex -4.684216e-01 1.152406e+00 -6.632313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.734441e-01 8.504029e-01 -7.132313e-01
      vertex -2.099745e-01 1.164763e+00 -7.132313e-01
      vertex -2.099745e-01 8.504029e-01 -7.132313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -4.734441e-01 8.504029e-01 -7.132313e-01
      vertex -4.734441e-01 1.164763e+00 -7.132313e-01
      vertex -2.099745e-01 1.164763e+00 -7.132313e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex -4.684216e-01 8.413815e-01 -6.632313e-01
      vertex -2.077470e-01 8.413815e-01 -6.632313e-01
      vertex -2.099745e-01 8.504029e-01 -7.132313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex -4.684216e-01 8.413815e-01 -6.632313e-01
      vertex -2.099745e-01 8.504029e-01 -7.132313e-01
      vertex -4.734441e-01 8.504029e-01 -7.132313e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -2.077470e-01 8.413815e-01 -6.632313e-01
      vertex -2.077470e-01 1.152406e+00 -6.632313e-01
      vertex -2.099745e-01 1.164763e+00 -7.132313e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -2.077470e-01 8.413815e-01 -6.632313e-01
      vertex -2.099745e-01 1.164763e+00 -7.132313e-01
      vertex -2.099745e-01 8.504029e-01 -7.132313e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex -2.077470e-01 1.152406e+00 -6.632313e-01
      vertex -4.684216e-01 1.152406e+00 -6.632313e-01
      vertex -4.734441e-01 1.164763e+00 -7.132313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex -2.077470e-01 1.152406e+00 -6.632313e-01
      vertex -4.734441e-01 1.164763e+00 -7.132313e-01
      vertex -2.099745e-01 1.164763e+00 -7.132313e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.684216e-01 1.152406e+00 -6.632313e-01
      vertex -4.684216e-01 8.413815e-01 -6.632313e-01
      vertex -4.734441e-01 8.504029e-01 -7.132313e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.684216e-01 1.152406e+00 -6.632313e-01
      vertex -4.734441e-01 8.504029e-01 -7.132313e-01
      vertex -4.734441e-01 1.164763e+00 -7.132313e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -2.062602e-01 1.180619e+00 -6.298592e-01
      vertex -2.062602e-01 1.319759e+00 -6.298592e-01
      vertex -4.650694e-01 1.319759e+00 -6.298592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -2.062602e-01 1.180619e+00 -6.298592e-01
      vertex -4.650694e-01 1.319759e+00 -6.298592e-01
      vertex -4.650694e-01 1.180619e+00 -6.298592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.084877e-01 1.193369e+00 -6.798592e-01
      vertex -4.700919e-01 1.334012e+00 -6.798592e-01
      vertex -2.084877e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.084877e-01 1.193369e+00 -6.798592e-01
      vertex -4.700919e-01 1.193369e+00 -6.798592e-01
      vertex -4.700919e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -2.062602e-01 1.180619e+00 -6.298592e-01
      vertex -2.062602e-01 1.319759e+00 -6.298592e-01
      vertex -2.084877e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal -9.990091e-01 0.000000e+00 4.450586e-02
    outer loop
      vertex -2.062602e-01 1.180619e+00 -6.298592e-01
      vertex -2.084877e-01 1.334012e+00 -6.798592e-01
      vertex -2.084877e-01 1.193369e+00 -6.798592e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex -2.062602e-01 1.319759e+00 -6.298592e-01
      vertex -4.650694e-01 1.319759e+00 -6.298592e-01
      vertex -4.700919e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex -2.062602e-01 1.319759e+00 -6.298592e-01
      vertex -4.700919e-01 1.334012e+00 -6.798592e-01
      vertex -2.084877e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.650694e-01 1.319759e+00 -6.298592e-01
      vertex -4.650694e-01 1.180619e+00 -6.298592e-01
      vertex -4.700919e-01 1.193369e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 9.949928e-01 0.000000e+00 -9.994702e-02
    outer loop
      vertex -4.650694e-01 1.319759e+00 -6.298592e-01
      vertex -4.700919e-01 1.193369e+00 -6.798592e-01
      vertex -4.700919e-01 1.334012e+00 -6.798592e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex -4.650694e-01 1.180619e+00 -6.298592e-01
      vertex -2.062602e-01 1.180619e+00 -6.298592e-01
      vertex -2.084877e-01 1.193369e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex -4.650694e-01 1.180619e+00 -6.298592e-01
      vertex -2.084877e-01 1.193369e+00 -6.798592e-01
      vertex -4.700919e-01 1.193369e+00 -6.798592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.708963e-01 7.389949e-01 -9.576930e-02
      vertex 2.577018e-01 7.389949e-01 -9.576930e-02
      vertex 2.577018e-01 1.012172e+00 -9.576930e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.708963e-01 7.389949e-01 -9.576930e-02
      vertex 2.577018e-01 1.012172e+00 -9.576930e-02
      vertex 1.708963e-01 1.012172e+00 -9.576930e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.729826e-01 7.480164e-01 -1.457693e-01
      vertex 2.608477e-01 1.024528e+00 -1.457693e-01
      vertex 2.608477e-01 7.480164e-01 -1.457693e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.729826e-01 7.480164e-01 -1.457693e-01
      vertex 1.729826e-01 1.024528e+00 -1.457693e-01
      vertex 2.608477e-01 1.024528e+00 -1.457693e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 1.708963e-01 7.389949e-01 -9.576930e-02
      vertex 2.577018e-01 7.389949e-01 -9.576930e-02
      vertex 2.608477e-01 7.480164e-01 -1.457693e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 1.708963e-01 7.389949e-01 -9.576930e-02
      vertex 2.608477e-01 7.480164e-01 -1.457693e-01
      vertex 1.729826e-01 7.480164e-01 -1.457693e-01
    endloop
  endfacet
  facet normal -9.980265e-01 -2.028050e-16 -6.279485e-02
    outer loop
      vertex 2.577018e-01 7.389949e-01 -9.576930e-02
      vertex 2.577018e-01 1.012172e+00 -9.576930e-02
      vertex 2.608477e-01 1.024528e+00 -1.457693e-01
    endloop
  endfacet
  facet normal -9.980265e-01 -2.015331e-16 -6.279485e-02
    outer loop
      vertex 2.577018e-01 7.389949e-01 -9.576930e-02
      vertex 2.608477e-01 1.024528e+00 -1.457693e-01
      vertex 2.608477e-01 7.480164e-01 -1.457693e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 2.577018e-01 1.012172e+00 -9.576930e-02
      vertex 1.708963e-01 1.012172e+00 -9.576930e-02
      vertex 1.729826e-01 1.024528e+00 -1.457693e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 2.577018e-01 1.012172e+00 -9.576930e-02
      vertex 1.729826e-01 1.024528e+00 -1.457693e-01
      vertex 2.608477e-01 1.024528e+00 -1.457693e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.708963e-01 1.012172e+00 -9.576930e-02
      vertex 1.708963e-01 7.389949e-01 -9.576930e-02
      vertex 1.729826e-01 7.480164e-01 -1.457693e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.708963e-01 1.012172e+00 -9.576930e-02
      vertex 1.729826e-01 7.480164e-01 -1.457693e-01
      vertex 1.729826e-01 1.024528e+00 -1.457693e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 2.171988e-01 8.802732e-01 5.479634e-01
      vertex 2.171988e-01 9.840163e-01 5.479634e-01
      vertex 1.440365e-01 9.840163e-01 5.479634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.171988e-01 8.802732e-01 5.479634e-01
      vertex 1.440365e-01 9.840163e-01 5.479634e-01
      vertex 1.440365e-01 8.802732e-01 5.479634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.203447e-01 8.930233e-01 4.979634e-01
      vertex 1.461228e-01 9.982690e-01 4.979634e-01
      vertex 2.203447e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.203447e-01 8.930233e-01 4.979634e-01
      vertex 1.461228e-01 8.930233e-01 4.979634e-01
      vertex 1.461228e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal -9.980265e-01 0.000000e+00 -6.279485e-02
    outer loop
      vertex 2.171988e-01 8.802732e-01 5.479634e-01
      vertex 2.171988e-01 9.840163e-01 5.479634e-01
      vertex 2.203447e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal -9.980265e-01 0.000000e+00 -6.279485e-02
    outer loop
      vertex 2.171988e-01 8.802732e-01 5.479634e-01
      vertex 2.203447e-01 9.982690e-01 4.979634e-01
      vertex 2.203447e-01 8.930233e-01 4.979634e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 2.171988e-01 9.840163e-01 5.479634e-01
      vertex 1.440365e-01 9.840163e-01 5.479634e-01
      vertex 1.461228e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 2.171988e-01 9.840163e-01 5.479634e-01
      vertex 1.461228e-01 9.982690e-01 4.979634e-01
      vertex 2.203447e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.440365e-01 9.840163e-01 5.479634e-01
      vertex 1.440365e-01 8.802732e-01 5.479634e-01
      vertex 1.461228e-01 8.930233e-01 4.979634e-01
    endloop
  endfacet
  facet normal 9.991306e-01 0.000000e+00 4.168881e-02
    outer loop
      vertex 1.440365e-01 9.840163e-01 5.479634e-01
      vertex 1.461228e-01 8.930233e-01 4.979634e-01
      vertex 1.461228e-01 9.982690e-01 4.979634e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 1.440365e-01 8.802732e-01 5.479634e-01
      vertex 2.171988e-01 8.802732e-01 5.479634e-01
      vertex 2.203447e-01 8.930233e-01 4.979634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 1.440365e-01 8.802732e-01 5.479634e-01
      vertex 2.203447e-01 8.930233e-01 4.979634e-01
      vertex 1.461228e-01 8.930233e-01 4.979634e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 3.088001e-01 8.258078e-01 -5.769169e-01
      vertex 4.676469e-01 8.258078e-01 -5.769169e-01
      vertex 4.676469e-01 1.131076e+00 -5.769169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 3.088001e-01 8.258078e-01 -5.769169e-01
      vertex 4.676469e-01 1.131076e+00 -5.769169e-01
      vertex 3.088001e-01 1.131076e+00 -5.769169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.121735e-01 8.348293e-01 -6.269169e-01
      vertex 4.727556e-01 1.143432e+00 -6.269169e-01
      vertex 4.727556e-01 8.348293e-01 -6.269169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.121735e-01 8.348293e-01 -6.269169e-01
      vertex 3.121735e-01 1.143432e+00 -6.269169e-01
      vertex 4.727556e-01 1.143432e+00 -6.269169e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 3.088001e-01 8.258078e-01 -5.769169e-01
      vertex 4.676469e-01 8.258078e-01 -5.769169e-01
      vertex 4.727556e-01 8.348293e-01 -6.269169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841097e-01 1.775618e-01
    outer loop
      vertex 3.088001e-01 8.258078e-01 -5.769169e-01
      vertex 4.727556e-01 8.348293e-01 -6.269169e-01
      vertex 3.121735e-01 8.348293e-01 -6.269169e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.676469e-01 8.258078e-01 -5.769169e-01
      vertex 4.676469e-01 1.131076e+00 -5.769169e-01
      vertex 4.727556e-01 1.143432e+00 -6.269169e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.676469e-01 8.258078e-01 -5.769169e-01
      vertex 4.727556e-01 1.143432e+00 -6.269169e-01
      vertex 4.727556e-01 8.348293e-01 -6.269169e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 4.676469e-01 1.131076e+00 -5.769169e-01
      vertex 3.088001e-01 1.131076e+00 -5.769169e-01
      vertex 3.121735e-01 1.143432e+00 -6.269169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.707954e-01 -2.399089e-01
    outer loop
      vertex 4.676469e-01 1.131076e+00 -5.769169e-01
      vertex 3.121735e-01 1.143432e+00 -6.269169e-01
      vertex 4.727556e-01 1.143432e+00 -6.269169e-01
    endloop
  endfacet
  facet normal 9.977317e-01 1.814316e-16 6.731598e-02
    outer loop
      vertex 3.088001e-01 1.131076e+00 -5.769169e-01
      vertex 3.088001e-01 8.258078e-01 -5.769169e-01
      vertex 3.121735e-01 8.348293e-01 -6.269169e-01
    endloop
  endfacet
  facet normal 9.977317e-01 1.805226e-16 6.731598e-02
    outer loop
      vertex 3.088001e-01 1.131076e+00 -5.769169e-01
      vertex 3.121735e-01 8.348293e-01 -6.269169e-01
      vertex 3.121735e-01 1.143432e+00 -6.269169e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 4.513909e-01 1.126548e+00 -4.178177e-01
      vertex 4.513909e-01 1.259316e+00 -4.178177e-01
      vertex 2.980658e-01 1.259316e+00 -4.178177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 4.513909e-01 1.126548e+00 -4.178177e-01
      vertex 2.980658e-01 1.259316e+00 -4.178177e-01
      vertex 2.980658e-01 1.126548e+00 -4.178177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 4.564997e-01 1.139299e+00 -4.678177e-01
      vertex 3.014393e-01 1.273569e+00 -4.678177e-01
      vertex 4.564997e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 4.564997e-01 1.139299e+00 -4.678177e-01
      vertex 3.014393e-01 1.139299e+00 -4.678177e-01
      vertex 3.014393e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.513909e-01 1.126548e+00 -4.178177e-01
      vertex 4.513909e-01 1.259316e+00 -4.178177e-01
      vertex 4.564997e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal -9.948206e-01 0.000000e+00 -1.016459e-01
    outer loop
      vertex 4.513909e-01 1.126548e+00 -4.178177e-01
      vertex 4.564997e-01 1.273569e+00 -4.678177e-01
      vertex 4.564997e-01 1.139299e+00 -4.678177e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 4.513909e-01 1.259316e+00 -4.178177e-01
      vertex 2.980658e-01 1.259316e+00 -4.178177e-01
      vertex 3.014393e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.616915e-01 -2.741339e-01
    outer loop
      vertex 4.513909e-01 1.259316e+00 -4.178177e-01
      vertex 3.014393e-01 1.273569e+00 -4.678177e-01
      vertex 4.564997e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.980658e-01 1.259316e+00 -4.178177e-01
      vertex 2.980658e-01 1.126548e+00 -4.178177e-01
      vertex 3.014393e-01 1.139299e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 9.977317e-01 0.000000e+00 6.731598e-02
    outer loop
      vertex 2.980658e-01 1.259316e+00 -4.178177e-01
      vertex 3.014393e-01 1.139299e+00 -4.678177e-01
      vertex 3.014393e-01 1.273569e+00 -4.678177e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 2.980658e-01 1.126548e+00 -4.178177e-01
      vertex 4.513909e-01 1.126548e+00 -4.178177e-01
      vertex 4.564997e-01 1.139299e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.689915e-01 2.470939e-01
    outer loop
      vertex 2.980658e-01 1.126548e+00 -4.178177e-01
      vertex 4.564997e-01 1.139299e+00 -4.678177e-01
      vertex 3.014393e-01 1.139299e+00 -4.678177e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.499108e-01 -7.775020e-01 2.288932e-01
      vertex -1.384422e-01 -7.775020e-01 2.288932e-01
      vertex -1.384422e-01 -4.843865e-01 2.288932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.499108e-01 -7.775020e-01 2.288932e-01
      vertex -1.384422e-01 -4.843865e-01 2.288932e-01
      vertex -1.499108e-01 -4.843865e-01 2.288932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.518984e-01 -7.878106e-01 1.788932e-01
      vertex -1.402778e-01 -4.908088e-01 1.788932e-01
      vertex -1.402778e-01 -7.878106e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.518984e-01 -7.878106e-01 1.788932e-01
      vertex -1.518984e-01 -4.908088e-01 1.788932e-01
      vertex -1.402778e-01 -4.908088e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.499108e-01 -7.775020e-01 2.288932e-01
      vertex -1.384422e-01 -7.775020e-01 2.288932e-01
      vertex -1.402778e-01 -7.878106e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.499108e-01 -7.775020e-01 2.288932e-01
      vertex -1.402778e-01 -7.878106e-01 1.788932e-01
      vertex -1.518984e-01 -7.878106e-01 1.788932e-01
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.384422e-01 -7.775020e-01 2.288932e-01
      vertex -1.384422e-01 -4.843865e-01 2.288932e-01
      vertex -1.402778e-01 -4.908088e-01 1.788932e-01
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.384422e-01 -7.775020e-01 2.288932e-01
      vertex -1.402778e-01 -4.908088e-01 1.788932e-01
      vertex -1.402778e-01 -7.878106e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex -1.384422e-01 -4.843865e-01 2.288932e-01
      vertex -1.499108e-01 -4.843865e-01 2.288932e-01
      vertex -1.518984e-01 -4.908088e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex -1.384422e-01 -4.843865e-01 2.288932e-01
      vertex -1.518984e-01 -4.908088e-01 1.788932e-01
      vertex -1.402778e-01 -4.908088e-01 1.788932e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.499108e-01 -4.843865e-01 2.288932e-01
      vertex -1.499108e-01 -7.775020e-01 2.288932e-01
      vertex -1.518984e-01 -7.878106e-01 1.788932e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.499108e-01 -4.843865e-01 2.288932e-01
      vertex -1.518984e-01 -7.878106e-01 1.788932e-01
      vertex -1.518984e-01 -4.908088e-01 1.788932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -1.196299e-01 -3.670569e-01 7.413343e-01
      vertex -1.196299e-01 1.247228e-02 7.413343e-01
      vertex -1.295400e-01 1.247228e-02 7.413343e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.196299e-01 -3.670569e-01 7.413343e-01
      vertex -1.295400e-01 1.247228e-02 7.413343e-01
      vertex -1.295400e-01 -3.670569e-01 7.413343e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.214654e-01 -3.726890e-01 6.913343e-01
      vertex -1.315276e-01 1.266365e-02 6.913343e-01
      vertex -1.214654e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.214654e-01 -3.726890e-01 6.913343e-01
      vertex -1.315276e-01 -3.726890e-01 6.913343e-01
      vertex -1.315276e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal -9.993268e-01 3.654118e-17 3.668659e-02
    outer loop
      vertex -1.196299e-01 -3.670569e-01 7.413343e-01
      vertex -1.196299e-01 1.247228e-02 7.413343e-01
      vertex -1.214654e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal -9.993268e-01 3.655130e-17 3.668659e-02
    outer loop
      vertex -1.196299e-01 -3.670569e-01 7.413343e-01
      vertex -1.214654e-01 1.266365e-02 6.913343e-01
      vertex -1.214654e-01 -3.726890e-01 6.913343e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex -1.196299e-01 1.247228e-02 7.413343e-01
      vertex -1.295400e-01 1.247228e-02 7.413343e-01
      vertex -1.315276e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex -1.196299e-01 1.247228e-02 7.413343e-01
      vertex -1.315276e-01 1.266365e-02 6.913343e-01
      vertex -1.214654e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.295400e-01 1.247228e-02 7.413343e-01
      vertex -1.295400e-01 -3.670569e-01 7.413343e-01
      vertex -1.315276e-01 -3.726890e-01 6.913343e-01
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.295400e-01 1.247228e-02 7.413343e-01
      vertex -1.315276e-01 -3.726890e-01 6.913343e-01
      vertex -1.315276e-01 1.266365e-02 6.913343e-01
    endloop
  endfacet
  facet normal 1.113250e-14 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.295400e-01 -3.670569e-01 7.413343e-01
      vertex -1.196299e-01 -3.670569e-01 7.413343e-01
      vertex -1.214654e-01 -3.726890e-01 6.913343e-01
    endloop
  endfacet
  facet normal 1.092144e-14 9.937158e-01 -1.119324e-01
    outer loop
      vertex -1.295400e-01 -3.670569e-01 7.413343e-01
      vertex -1.214654e-01 -3.726890e-01 6.913343e-01
      vertex -1.315276e-01 -3.726890e-01 6.913343e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex -1.413985e-01 8.392440e-02 1.483647e-01
      vertex -1.413985e-01 4.852908e-01 1.483647e-01
      vertex -1.531120e-01 4.852908e-01 1.483647e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.413985e-01 8.392440e-02 1.483647e-01
      vertex -1.531120e-01 4.852908e-01 1.483647e-01
      vertex -1.531120e-01 8.392440e-02 1.483647e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.432341e-01 8.501387e-02 9.836472e-02
      vertex -1.550996e-01 4.915907e-01 9.836472e-02
      vertex -1.432341e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.432341e-01 8.501387e-02 9.836472e-02
      vertex -1.550996e-01 8.501387e-02 9.836472e-02
      vertex -1.550996e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.413985e-01 8.392440e-02 1.483647e-01
      vertex -1.413985e-01 4.852908e-01 1.483647e-01
      vertex -1.432341e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal -9.993268e-01 0.000000e+00 3.668659e-02
    outer loop
      vertex -1.413985e-01 8.392440e-02 1.483647e-01
      vertex -1.432341e-01 4.915907e-01 9.836472e-02
      vertex -1.432341e-01 8.501387e-02 9.836472e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex -1.413985e-01 4.852908e-01 1.483647e-01
      vertex -1.531120e-01 4.852908e-01 1.483647e-01
      vertex -1.550996e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex -1.413985e-01 4.852908e-01 1.483647e-01
      vertex -1.550996e-01 4.915907e-01 9.836472e-02
      vertex -1.432341e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.531120e-01 4.852908e-01 1.483647e-01
      vertex -1.531120e-01 8.392440e-02 1.483647e-01
      vertex -1.550996e-01 8.501387e-02 9.836472e-02
    endloop
  endfacet
  facet normal 9.992108e-01 0.000000e+00 -3.972109e-02
    outer loop
      vertex -1.531120e-01 4.852908e-01 1.483647e-01
      vertex -1.550996e-01 8.501387e-02 9.836472e-02
      vertex -1.550996e-01 4.915907e-01 9.836472e-02
    endloop
  endfacet
  facet normal -5.922461e-15 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.531120e-01 8.392440e-02 1.483647e-01
      vertex -1.413985e-01 8.392440e-02 1.483647e-01
      vertex -1.432341e-01 8.501387e-02 9.836472e-02
    endloop
  endfacet
  facet normal -7.022728e-15 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.531120e-01 8.392440e-02 1.483647e-01
      vertex -1.432341e-01 8.501387e-02 9.836472e-02
      vertex -1.550996e-01 8.501387e-02 9.836472e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.288105e-01 -8.536221e-01 -1.403112e-01
      vertex 1.434516e-01 -8.536221e-01 -1.403112e-01
      vertex 1.434516e-01 -5.318096e-01 -1.403112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.288105e-01 -8.536221e-01 -1.403112e-01
      vertex 1.434516e-01 -5.318096e-01 -1.403112e-01
      vertex -1.288105e-01 -5.318096e-01 -1.403112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.303660e-01 -8.639308e-01 -1.903112e-01
      vertex 1.451840e-01 -5.382319e-01 -1.903112e-01
      vertex 1.451840e-01 -8.639308e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.303660e-01 -8.639308e-01 -1.903112e-01
      vertex -1.303660e-01 -5.382319e-01 -1.903112e-01
      vertex 1.451840e-01 -5.382319e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.288105e-01 -8.536221e-01 -1.403112e-01
      vertex 1.434516e-01 -8.536221e-01 -1.403112e-01
      vertex 1.451840e-01 -8.639308e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.794007e-01 -2.019264e-01
    outer loop
      vertex -1.288105e-01 -8.536221e-01 -1.403112e-01
      vertex 1.451840e-01 -8.639308e-01 -1.903112e-01
      vertex -1.303660e-01 -8.639308e-01 -1.903112e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.434516e-01 -8.536221e-01 -1.403112e-01
      vertex 1.434516e-01 -5.318096e-01 -1.403112e-01
      vertex 1.451840e-01 -5.382319e-01 -1.903112e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.434516e-01 -8.536221e-01 -1.403112e-01
      vertex 1.451840e-01 -5.382319e-01 -1.903112e-01
      vertex 1.451840e-01 -8.639308e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex 1.434516e-01 -5.318096e-01 -1.403112e-01
      vertex -1.288105e-01 -5.318096e-01 -1.403112e-01
      vertex -1.303660e-01 -5.382319e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.918514e-01 1.274001e-01
    outer loop
      vertex 1.434516e-01 -5.318096e-01 -1.403112e-01
      vertex -1.303660e-01 -5.382319e-01 -1.903112e-01
      vertex 1.451840e-01 -5.382319e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.288105e-01 -5.318096e-01 -1.403112e-01
      vertex -1.288105e-01 -8.536221e-01 -1.403112e-01
      vertex -1.303660e-01 -8.639308e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.288105e-01 -5.318096e-01 -1.403112e-01
      vertex -1.303660e-01 -8.639308e-01 -1.903112e-01
      vertex -1.303660e-01 -5.382319e-01 -1.903112e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.113223e-01 -3.619122e-01 7.870082e-01
      vertex 1.113223e-01 1.229746e-02 7.870082e-01
      vertex -9.996035e-02 1.229746e-02 7.870082e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.113223e-01 -3.619122e-01 7.870082e-01
      vertex -9.996035e-02 1.229746e-02 7.870082e-01
      vertex -9.996035e-02 -3.619122e-01 7.870082e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.130546e-01 -3.675442e-01 7.370082e-01
      vertex -1.015159e-01 1.248883e-02 7.370082e-01
      vertex 1.130546e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.130546e-01 -3.675442e-01 7.370082e-01
      vertex -1.015159e-01 -3.675442e-01 7.370082e-01
      vertex -1.015159e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.113223e-01 -3.619122e-01 7.870082e-01
      vertex 1.113223e-01 1.229746e-02 7.870082e-01
      vertex 1.130546e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.113223e-01 -3.619122e-01 7.870082e-01
      vertex 1.130546e-01 1.248883e-02 7.370082e-01
      vertex 1.130546e-01 -3.675442e-01 7.370082e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex 1.113223e-01 1.229746e-02 7.870082e-01
      vertex -9.996035e-02 1.229746e-02 7.870082e-01
      vertex -1.015159e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.999927e-01 -3.827390e-03
    outer loop
      vertex 1.113223e-01 1.229746e-02 7.870082e-01
      vertex -1.015159e-01 1.248883e-02 7.370082e-01
      vertex 1.130546e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal 9.995164e-01 -3.706766e-17 -3.109625e-02
    outer loop
      vertex -9.996035e-02 1.229746e-02 7.870082e-01
      vertex -9.996035e-02 -3.619122e-01 7.870082e-01
      vertex -1.015159e-01 -3.675442e-01 7.370082e-01
    endloop
  endfacet
  facet normal 9.995164e-01 -7.342704e-17 -3.109625e-02
    outer loop
      vertex -9.996035e-02 1.229746e-02 7.870082e-01
      vertex -1.015159e-01 -3.675442e-01 7.370082e-01
      vertex -1.015159e-01 1.248883e-02 7.370082e-01
    endloop
  endfacet
  facet normal 2.610831e-16 9.937158e-01 -1.119324e-01
    outer loop
      vertex -9.996035e-02 -3.619122e-01 7.870082e-01
      vertex 1.113223e-01 -3.619122e-01 7.870082e-01
      vertex 1.130546e-01 -3.675442e-01 7.370082e-01
    endloop
  endfacet
  facet normal 2.610993e-16 9.937158e-01 -1.119324e-01
    outer loop
      vertex -9.996035e-02 -3.619122e-01 7.870082e-01
      vertex 1.130546e-01 -3.675442e-01 7.370082e-01
      vertex -1.015159e-01 -3.675442e-01 7.370082e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.628596e-01 1.024199e-01 -7.004677e-01
      vertex 1.628596e-01 5.922404e-01 -7.004677e-01
      vertex -1.462377e-01 5.922404e-01 -7.004677e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.628596e-01 1.024199e-01 -7.004677e-01
      vertex -1.462377e-01 5.922404e-01 -7.004677e-01
      vertex -1.462377e-01 1.024199e-01 -7.004677e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.645920e-01 1.035093e-01 -7.504677e-01
      vertex -1.477932e-01 5.985402e-01 -7.504677e-01
      vertex 1.645920e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.645920e-01 1.035093e-01 -7.504677e-01
      vertex -1.477932e-01 1.035093e-01 -7.504677e-01
      vertex -1.477932e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.628596e-01 1.024199e-01 -7.004677e-01
      vertex 1.628596e-01 5.922404e-01 -7.004677e-01
      vertex 1.645920e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.628596e-01 1.024199e-01 -7.004677e-01
      vertex 1.645920e-01 5.985402e-01 -7.504677e-01
      vertex 1.645920e-01 1.035093e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex 1.628596e-01 5.922404e-01 -7.004677e-01
      vertex -1.462377e-01 5.922404e-01 -7.004677e-01
      vertex -1.477932e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.921558e-01 -1.250077e-01
    outer loop
      vertex 1.628596e-01 5.922404e-01 -7.004677e-01
      vertex -1.477932e-01 5.985402e-01 -7.504677e-01
      vertex 1.645920e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.462377e-01 5.922404e-01 -7.004677e-01
      vertex -1.462377e-01 1.024199e-01 -7.004677e-01
      vertex -1.477932e-01 1.035093e-01 -7.504677e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.462377e-01 5.922404e-01 -7.004677e-01
      vertex -1.477932e-01 1.035093e-01 -7.504677e-01
      vertex -1.477932e-01 5.985402e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -3.142100e-16 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.462377e-01 1.024199e-01 -7.004677e-01
      vertex 1.628596e-01 1.024199e-01 -7.004677e-01
      vertex 1.645920e-01 1.035093e-01 -7.504677e-01
    endloop
  endfacet
  facet normal -3.109896e-16 9.997627e-01 2.178412e-02
    outer loop
      vertex -1.462377e-01 1.024199e-01 -7.004677e-01
      vertex 1.645920e-01 1.035093e-01 -7.504677e-01
      vertex -1.477932e-01 1.035093e-01 -7.504677e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 1.000000e+00
    outer loop
      vertex 1.178519e-01 4.599256e-01 5.985495e-01
      vertex 1.178519e-01 4.907050e-01 5.985495e-01
      vertex -1.058235e-01 4.907050e-01 5.985495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 1.178519e-01 4.599256e-01 5.985495e-01
      vertex -1.058235e-01 4.907050e-01 5.985495e-01
      vertex -1.058235e-01 4.599256e-01 5.985495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.195843e-01 4.666863e-01 5.485495e-01
      vertex -1.073791e-01 4.979182e-01 5.485495e-01
      vertex 1.195843e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 1.195843e-01 4.666863e-01 5.485495e-01
      vertex -1.073791e-01 4.666863e-01 5.485495e-01
      vertex -1.073791e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.178519e-01 4.599256e-01 5.985495e-01
      vertex 1.178519e-01 4.907050e-01 5.985495e-01
      vertex 1.195843e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal -9.994003e-01 0.000000e+00 -3.462676e-02
    outer loop
      vertex 1.178519e-01 4.599256e-01 5.985495e-01
      vertex 1.195843e-01 4.979182e-01 5.485495e-01
      vertex 1.195843e-01 4.666863e-01 5.485495e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -9.897537e-01 -1.427853e-01
    outer loop
      vertex 1.178519e-01 4.907050e-01 5.985495e-01
      vertex -1.058235e-01 4.907050e-01 5.985495e-01
      vertex -1.073791e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.897537e-01 -1.427853e-01
    outer loop
      vertex 1.178519e-01 4.907050e-01 5.985495e-01
      vertex -1.073791e-01 4.979182e-01 5.485495e-01
      vertex 1.195843e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.058235e-01 4.907050e-01 5.985495e-01
      vertex -1.058235e-01 4.599256e-01 5.985495e-01
      vertex -1.073791e-01 4.666863e-01 5.485495e-01
    endloop
  endfacet
  facet normal 9.995164e-01 0.000000e+00 -3.109625e-02
    outer loop
      vertex -1.058235e-01 4.907050e-01 5.985495e-01
      vertex -1.073791e-01 4.666863e-01 5.485495e-01
      vertex -1.073791e-01 4.979182e-01 5.485495e-01
    endloop
  endfacet
  facet normal -0.000000e+00 9.909820e-01 1.339952e-01
    outer loop
      vertex -1.058235e-01 4.599256e-01 5.985495e-01
      vertex 1.178519e-01 4.599256e-01 5.985495e-01
      vertex 1.195843e-01 4.666863e-01 5.485495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.909820e-01 1.339952e-01
    outer loop
      vertex -1.058235e-01 4.599256e-01 5.985495e-01
      vertex 1.195843e-01 4.666863e-01 5.485495e-01
      vertex -1.073791e-01 4.666863e-01 5.485495e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -3.677080e-01 -1.143765e+00 -3.116251e-01
      vertex -2.008481e-01 -1.432774e+00 -3.116251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -2.008481e-01 -1.432774e+00 -3.116251e-01
      vertex -1.691958e-01 -1.432774e+00 -3.116251e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -1.691958e-01 -1.432774e+00 -3.116251e-01
      vertex -1.691958e-01 -1.038472e+00 -3.116251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
      vertex -2.031773e-01 -1.449390e+00 -3.616251e-01
      vertex -3.719722e-01 -1.157028e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
      vertex -1.711579e-01 -1.449390e+00 -3.616251e-01
      vertex -2.031773e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
      vertex -1.711579e-01 -1.050515e+00 -3.616251e-01
      vertex -1.711579e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 8.645332e-01 -4.991385e-01 5.867883e-02
    outer loop
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -3.677080e-01 -1.143765e+00 -3.116251e-01
      vertex -3.719722e-01 -1.157028e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 8.645332e-01 -4.991385e-01 5.867883e-02
    outer loop
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -3.719722e-01 -1.157028e+00 -3.616251e-01
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 8.481320e-01 4.896692e-01 -2.022280e-01
    outer loop
      vertex -3.677080e-01 -1.143765e+00 -3.116251e-01
      vertex -2.008481e-01 -1.432774e+00 -3.116251e-01
      vertex -2.031773e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 8.481320e-01 4.896692e-01 -2.022280e-01
    outer loop
      vertex -3.677080e-01 -1.143765e+00 -3.116251e-01
      vertex -2.031773e-01 -1.449390e+00 -3.616251e-01
      vertex -3.719722e-01 -1.157028e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.489757e-01 -3.153493e-01
    outer loop
      vertex -2.008481e-01 -1.432774e+00 -3.116251e-01
      vertex -1.691958e-01 -1.432774e+00 -3.116251e-01
      vertex -1.711579e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.489757e-01 -3.153493e-01
    outer loop
      vertex -2.008481e-01 -1.432774e+00 -3.116251e-01
      vertex -1.711579e-01 -1.449390e+00 -3.616251e-01
      vertex -2.031773e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal -9.992309e-01 1.406750e-16 3.921158e-02
    outer loop
      vertex -1.691958e-01 -1.432774e+00 -3.116251e-01
      vertex -1.691958e-01 -1.038472e+00 -3.116251e-01
      vertex -1.711579e-01 -1.050515e+00 -3.616251e-01
    endloop
  endfacet
  facet normal -9.992309e-01 6.925957e-17 3.921158e-02
    outer loop
      vertex -1.691958e-01 -1.432774e+00 -3.116251e-01
      vertex -1.711579e-01 -1.050515e+00 -3.616251e-01
      vertex -1.711579e-01 -1.449390e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.721986e-01 2.341579e-01
    outer loop
      vertex -1.691958e-01 -1.038472e+00 -3.116251e-01
      vertex -3.069174e-01 -1.038472e+00 -3.116251e-01
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.721986e-01 2.341579e-01
    outer loop
      vertex -1.691958e-01 -1.038472e+00 -3.116251e-01
      vertex -3.104766e-01 -1.050515e+00 -3.616251e-01
      vertex -1.711579e-01 -1.050515e+00 -3.616251e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.729633e-01 -8.544260e-01 -5.441919e-01
      vertex -2.063229e-01 -8.544260e-01 -5.441919e-01
      vertex -3.181136e-01 -1.048053e+00 -5.441919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.729633e-01 -8.544260e-01 -5.441919e-01
      vertex -3.181136e-01 -1.048053e+00 -5.441919e-01
      vertex -1.729633e-01 -1.048053e+00 -5.441919e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.748664e-01 -8.638273e-01 -5.941919e-01
      vertex -3.216138e-01 -1.059585e+00 -5.941919e-01
      vertex -2.085931e-01 -8.638273e-01 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.748664e-01 -8.638273e-01 -5.941919e-01
      vertex -1.748664e-01 -1.059585e+00 -5.941919e-01
      vertex -3.216138e-01 -1.059585e+00 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827784e-01 1.847879e-01
    outer loop
      vertex -1.729633e-01 -8.544260e-01 -5.441919e-01
      vertex -2.063229e-01 -8.544260e-01 -5.441919e-01
      vertex -2.085931e-01 -8.638273e-01 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827784e-01 1.847879e-01
    outer loop
      vertex -1.729633e-01 -8.544260e-01 -5.441919e-01
      vertex -2.085931e-01 -8.638273e-01 -5.941919e-01
      vertex -1.748664e-01 -8.638273e-01 -5.941919e-01
    endloop
  endfacet
  facet normal 8.647331e-01 -4.992539e-01 5.461064e-02
    outer loop
      vertex -2.063229e-01 -8.544260e-01 -5.441919e-01
      vertex -3.181136e-01 -1.048053e+00 -5.441919e-01
      vertex -3.216138e-01 -1.059585e+00 -5.941919e-01
    endloop
  endfacet
  facet normal 8.647331e-01 -4.992539e-01 5.461064e-02
    outer loop
      vertex -2.063229e-01 -8.544260e-01 -5.441919e-01
      vertex -3.216138e-01 -1.059585e+00 -5.941919e-01
      vertex -2.085931e-01 -8.638273e-01 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.744197e-01 -2.247360e-01
    outer loop
      vertex -3.181136e-01 -1.048053e+00 -5.441919e-01
      vertex -1.729633e-01 -1.048053e+00 -5.441919e-01
      vertex -1.748664e-01 -1.059585e+00 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.744197e-01 -2.247360e-01
    outer loop
      vertex -3.181136e-01 -1.048053e+00 -5.441919e-01
      vertex -1.748664e-01 -1.059585e+00 -5.941919e-01
      vertex -3.216138e-01 -1.059585e+00 -5.941919e-01
    endloop
  endfacet
  facet normal -9.992764e-01 0.000000e+00 3.803495e-02
    outer loop
      vertex -1.729633e-01 -1.048053e+00 -5.441919e-01
      vertex -1.729633e-01 -8.544260e-01 -5.441919e-01
      vertex -1.748664e-01 -8.638273e-01 -5.941919e-01
    endloop
  endfacet
  facet normal -9.992764e-01 0.000000e+00 3.803495e-02
    outer loop
      vertex -1.729633e-01 -1.048053e+00 -5.441919e-01
      vertex -1.748664e-01 -8.638273e-01 -5.941919e-01
      vertex -1.748664e-01 -1.059585e+00 -5.941919e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex -1.308113e-01 -1.529767e+00 -5.865324e-01
      vertex 1.905158e-01 -1.529767e+00 -5.865324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex 1.905158e-01 -1.529767e+00 -5.865324e-01
      vertex 2.680004e-01 -1.395560e+00 -5.865324e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex 2.680004e-01 -1.395560e+00 -5.865324e-01
      vertex 2.680004e-01 -1.110325e+00 -5.865324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
      vertex 1.925927e-01 -1.546444e+00 -6.365324e-01
      vertex -1.322373e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
      vertex 2.709220e-01 -1.410774e+00 -6.365324e-01
      vertex 1.925927e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
      vertex 2.709220e-01 -1.122429e+00 -6.365324e-01
      vertex 2.709220e-01 -1.410774e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex -1.308113e-01 -1.529767e+00 -5.865324e-01
      vertex -1.322373e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex -1.322373e-01 -1.546444e+00 -6.365324e-01
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.486260e-01 -3.163996e-01
    outer loop
      vertex -1.308113e-01 -1.529767e+00 -5.865324e-01
      vertex 1.905158e-01 -1.529767e+00 -5.865324e-01
      vertex 1.925927e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.486260e-01 -3.163996e-01
    outer loop
      vertex -1.308113e-01 -1.529767e+00 -5.865324e-01
      vertex 1.925927e-01 -1.546444e+00 -6.365324e-01
      vertex -1.322373e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal -8.487575e-01 4.900304e-01 -1.986979e-01
    outer loop
      vertex 1.905158e-01 -1.529767e+00 -5.865324e-01
      vertex 2.680004e-01 -1.395560e+00 -5.865324e-01
      vertex 2.709220e-01 -1.410774e+00 -6.365324e-01
    endloop
  endfacet
  facet normal -8.487575e-01 4.900304e-01 -1.986979e-01
    outer loop
      vertex 1.905158e-01 -1.529767e+00 -5.865324e-01
      vertex 2.709220e-01 -1.410774e+00 -6.365324e-01
      vertex 1.925927e-01 -1.546444e+00 -6.365324e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.680004e-01 -1.395560e+00 -5.865324e-01
      vertex 2.680004e-01 -1.110325e+00 -5.865324e-01
      vertex 2.709220e-01 -1.122429e+00 -6.365324e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.680004e-01 -1.395560e+00 -5.865324e-01
      vertex 2.709220e-01 -1.122429e+00 -6.365324e-01
      vertex 2.709220e-01 -1.410774e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.719258e-01 2.352874e-01
    outer loop
      vertex 2.680004e-01 -1.110325e+00 -5.865324e-01
      vertex -1.308113e-01 -1.110325e+00 -5.865324e-01
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.719258e-01 2.352874e-01
    outer loop
      vertex 2.680004e-01 -1.110325e+00 -5.865324e-01
      vertex -1.322373e-01 -1.122429e+00 -6.365324e-01
      vertex 2.709220e-01 -1.122429e+00 -6.365324e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex 1.778424e-01 -8.061288e-01 -2.814291e-01
      vertex -1.221095e-01 -8.061288e-01 -2.814291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex -1.221095e-01 -8.061288e-01 -2.814291e-01
      vertex -1.221095e-01 -9.885596e-01 -2.814291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex -1.221095e-01 -9.885596e-01 -2.814291e-01
      vertex 2.501726e-01 -9.885596e-01 -2.814291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
      vertex -1.235355e-01 -8.155431e-01 -3.314291e-01
      vertex 1.799193e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
      vertex -1.235355e-01 -1.000104e+00 -3.314291e-01
      vertex -1.235355e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -0.000000e+00 -1.000000e+00
    outer loop
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
      vertex 2.530942e-01 -1.000104e+00 -3.314291e-01
      vertex -1.235355e-01 -1.000104e+00 -3.314291e-01
    endloop
  endfacet
  facet normal -8.645639e-01 -4.991562e-01 5.807128e-02
    outer loop
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex 1.778424e-01 -8.061288e-01 -2.814291e-01
      vertex 1.799193e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal -8.645639e-01 -4.991562e-01 5.807128e-02
    outer loop
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex 1.799193e-01 -8.155431e-01 -3.314291e-01
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827322e-01 1.850337e-01
    outer loop
      vertex 1.778424e-01 -8.061288e-01 -2.814291e-01
      vertex -1.221095e-01 -8.061288e-01 -2.814291e-01
      vertex -1.235355e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.827322e-01 1.850337e-01
    outer loop
      vertex 1.778424e-01 -8.061288e-01 -2.814291e-01
      vertex -1.235355e-01 -8.155431e-01 -3.314291e-01
      vertex 1.799193e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.221095e-01 -8.061288e-01 -2.814291e-01
      vertex -1.221095e-01 -9.885596e-01 -2.814291e-01
      vertex -1.235355e-01 -1.000104e+00 -3.314291e-01
    endloop
  endfacet
  facet normal 9.995935e-01 0.000000e+00 -2.850914e-02
    outer loop
      vertex -1.221095e-01 -8.061288e-01 -2.814291e-01
      vertex -1.235355e-01 -1.000104e+00 -3.314291e-01
      vertex -1.235355e-01 -8.155431e-01 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.743644e-01 -2.249756e-01
    outer loop
      vertex -1.221095e-01 -9.885596e-01 -2.814291e-01
      vertex 2.501726e-01 -9.885596e-01 -2.814291e-01
      vertex 2.530942e-01 -1.000104e+00 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.743644e-01 -2.249756e-01
    outer loop
      vertex -1.221095e-01 -9.885596e-01 -2.814291e-01
      vertex 2.530942e-01 -1.000104e+00 -3.314291e-01
      vertex -1.235355e-01 -1.000104e+00 -3.314291e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.501726e-01 -9.885596e-01 -2.814291e-01
      vertex 2.501726e-01 -9.314084e-01 -2.814291e-01
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
    endloop
  endfacet
  facet normal -9.982972e-01 0.000000e+00 -5.833253e-02
    outer loop
      vertex 2.501726e-01 -9.885596e-01 -2.814291e-01
      vertex 2.530942e-01 -9.422857e-01 -3.314291e-01
      vertex 2.530942e-01 -1.000104e+00 -3.314291e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 3.040796e-01 -9.091012e-01 5.308022e-01
      vertex 2.551666e-01 -8.243814e-01 5.308022e-01
      vertex 2.284301e-01 -8.243814e-01 5.308022e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex 3.040796e-01 -9.091012e-01 5.308022e-01
      vertex 2.284301e-01 -8.243814e-01 5.308022e-01
      vertex 2.284301e-01 -1.040130e+00 5.308022e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.084622e-01 -9.222037e-01 4.808022e-01
      vertex 2.317223e-01 -8.362628e-01 4.808022e-01
      vertex 2.588442e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal -0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex 3.084622e-01 -9.222037e-01 4.808022e-01
      vertex 2.317223e-01 -1.055121e+00 4.808022e-01
      vertex 2.317223e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal -8.647130e-01 -4.992423e-01 5.503294e-02
    outer loop
      vertex 3.040796e-01 -9.091012e-01 5.308022e-01
      vertex 2.551666e-01 -8.243814e-01 5.308022e-01
      vertex 2.588442e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal -8.647130e-01 -4.992423e-01 5.503294e-02
    outer loop
      vertex 3.040796e-01 -9.091012e-01 5.308022e-01
      vertex 2.588442e-01 -8.362628e-01 4.808022e-01
      vertex 3.084622e-01 -9.222037e-01 4.808022e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.729084e-01 2.311911e-01
    outer loop
      vertex 2.551666e-01 -8.243814e-01 5.308022e-01
      vertex 2.284301e-01 -8.243814e-01 5.308022e-01
      vertex 2.317223e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.729084e-01 2.311911e-01
    outer loop
      vertex 2.551666e-01 -8.243814e-01 5.308022e-01
      vertex 2.317223e-01 -8.362628e-01 4.808022e-01
      vertex 2.588442e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal 9.978392e-01 0.000000e+00 6.570294e-02
    outer loop
      vertex 2.284301e-01 -8.243814e-01 5.308022e-01
      vertex 2.284301e-01 -1.040130e+00 5.308022e-01
      vertex 2.317223e-01 -1.055121e+00 4.808022e-01
    endloop
  endfacet
  facet normal 9.978392e-01 0.000000e+00 6.570294e-02
    outer loop
      vertex 2.284301e-01 -8.243814e-01 5.308022e-01
      vertex 2.317223e-01 -1.055121e+00 4.808022e-01
      vertex 2.317223e-01 -8.362628e-01 4.808022e-01
    endloop
  endfacet
  facet normal -8.480583e-01 4.896267e-01 -2.026398e-01
    outer loop
      vertex 2.284301e-01 -1.040130e+00 5.308022e-01
      vertex 3.040796e-01 -9.091012e-01 5.308022e-01
      vertex 3.084622e-01 -9.222037e-01 4.808022e-01
    endloop
  endfacet
  facet normal -8.480583e-01 4.896267e-01 -2.026398e-01
    outer loop
      vertex 2.284301e-01 -1.040130e+00 5.308022e-01
      vertex 3.084622e-01 -9.222037e-01 4.808022e-01
      vertex 2.317223e-01 -1.055121e+00 4.808022e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex 9.500000e-01 -1.490000e+00 0.000000e+00
      vertex 7.685661e-01 -1.490000e+00 5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex 7.685661e-01 -1.520000e+00 5.583960e-01
      vertex 9.500000e-01 -1.520000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 9.510565e-01 0.000000e+00 3.090170e-01
    outer loop
      vertex 9.500000e-01 -1.490000e+00 0.000000e+00
      vertex 7.685661e-01 -1.490000e+00 5.583960e-01
      vertex 7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal 9.510565e-01 0.000000e+00 3.090170e-01
    outer loop
      vertex 9.500000e-01 -1.490000e+00 0.000000e+00
      vertex 7.685661e-01 -1.520000e+00 5.583960e-01
      vertex 9.500000e-01 -1.520000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex 7.685661e-01 -1.490000e+00 5.583960e-01
      vertex 2.935661e-01 -1.490000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex 2.935661e-01 -1.520000e+00 9.035037e-01
      vertex 7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal 5.877853e-01 0.000000e+00 8.090170e-01
    outer loop
      vertex 7.685661e-01 -1.490000e+00 5.583960e-01
      vertex 2.935661e-01 -1.490000e+00 9.035037e-01
      vertex 2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 5.877853e-01 0.000000e+00 8.090170e-01
    outer loop
      vertex 7.685661e-01 -1.490000e+00 5.583960e-01
      vertex 2.935661e-01 -1.520000e+00 9.035037e-01
      vertex 7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex 2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -2.935661e-01 -1.490000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 -0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex -2.935661e-01 -1.520000e+00 9.035037e-01
      vertex 2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 1.890925e-16 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 1.890925e-16 0.000000e+00 1.000000e+00
    outer loop
      vertex 2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -2.935661e-01 -1.520000e+00 9.035037e-01
      vertex 2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex -2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -7.685661e-01 -1.490000e+00 5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex -7.685661e-01 -1.520000e+00 5.583960e-01
      vertex -2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal -5.877853e-01 0.000000e+00 8.090170e-01
    outer loop
      vertex -2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -7.685661e-01 -1.490000e+00 5.583960e-01
      vertex -7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal -5.877853e-01 0.000000e+00 8.090170e-01
    outer loop
      vertex -2.935661e-01 -1.490000e+00 9.035037e-01
      vertex -7.685661e-01 -1.520000e+00 5.583960e-01
      vertex -2.935661e-01 -1.520000e+00 9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex -7.685661e-01 -1.490000e+00 5.583960e-01
      vertex -9.500000e-01 -1.490000e+00 1.163414e-16
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex -9.500000e-01 -1.520000e+00 1.163414e-16
      vertex -7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal -9.510565e-01 0.000000e+00 3.090170e-01
    outer loop
      vertex -7.685661e-01 -1.490000e+00 5.583960e-01
      vertex -9.500000e-01 -1.490000e+00 1.163414e-16
      vertex -9.500000e-01 -1.520000e+00 1.163414e-16
    endloop
  endfacet
  facet normal -9.510565e-01 0.000000e+00 3.090170e-01
    outer loop
      vertex -7.685661e-01 -1.490000e+00 5.583960e-01
      vertex -9.500000e-01 -1.520000e+00 1.163414e-16
      vertex -7.685661e-01 -1.520000e+00 5.583960e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex -9.500000e-01 -1.490000e+00 1.163414e-16
      vertex -7.685661e-01 -1.490000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex -7.685661e-01 -1.520000e+00 -5.583960e-01
      vertex -9.500000e-01 -1.520000e+00 1.163414e-16
    endloop
  endfacet
  facet normal -9.510565e-01 0.000000e+00 -3.090170e-01
    outer loop
      vertex -9.500000e-01 -1.490000e+00 1.163414e-16
      vertex -7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex -7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal -9.510565e-01 -0.000000e+00 -3.090170e-01
    outer loop
      vertex -9.500000e-01 -1.490000e+00 1.163414e-16
      vertex -7.685661e-01 -1.520000e+00 -5.583960e-01
      vertex -9.500000e-01 -1.520000e+00 1.163414e-16
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex -7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex -2.935661e-01 -1.490000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex -2.935661e-01 -1.520000e+00 -9.035037e-01
      vertex -7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal -5.877853e-01 0.000000e+00 -8.090170e-01
    outer loop
      vertex -7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex -2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex -2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal -5.877853e-01 -0.000000e+00 -8.090170e-01
    outer loop
      vertex -7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex -2.935661e-01 -1.520000e+00 -9.035037e-01
      vertex -7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 -0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex -2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 2.935661e-01 -1.490000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex 2.935661e-01 -1.520000e+00 -9.035037e-01
      vertex -2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal -1.890925e-16 0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal -1.890925e-16 -0.000000e+00 -1.000000e+00
    outer loop
      vertex -2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 2.935661e-01 -1.520000e+00 -9.035037e-01
      vertex -2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex 2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 7.685661e-01 -1.490000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex 7.685661e-01 -1.520000e+00 -5.583960e-01
      vertex 2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal 5.877853e-01 0.000000e+00 -8.090170e-01
    outer loop
      vertex 2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex 7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 5.877853e-01 0.000000e+00 -8.090170e-01
    outer loop
      vertex 2.935661e-01 -1.490000e+00 -9.035037e-01
      vertex 7.685661e-01 -1.520000e+00 -5.583960e-01
      vertex 2.935661e-01 -1.520000e+00 -9.035037e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.490000e+00 0.000000e+00
      vertex 7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex 9.500000e-01 -1.490000e+00 0.000000e+00
    endloop
  endfacet
  facet normal -0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex 0.000000e+00 -1.520000e+00 0.000000e+00
      vertex 9.500000e-01 -1.520000e+00 0.000000e+00
      vertex 7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 9.510565e-01 0.000000e+00 -3.090170e-01
    outer loop
      vertex 7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex 9.500000e-01 -1.490000e+00 0.000000e+00
      vertex 9.500000e-01 -1.520000e+00 0.000000e+00
    endloop
  endfacet
  facet normal 9.510565e-01 0.000000e+00 -3.090170e-01
    outer loop
      vertex 7.685661e-01 -1.490000e+00 -5.583960e-01
      vertex 9.500000e-01 -1.520000e+00 0.000000e+00
      vertex 7.685661e-01 -1.520000e+00 -5.583960e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -5.000000e-02 -1.520000e+00 -5.000000e-02
      vertex 5.000000e-02 -1.520000e+00 -5.000000e-02
      vertex 5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -5.000000e-02 -1.520000e+00 -5.000000e-02
      vertex 5.000000e-02 -1.500000e+00 -5.000000e-02
      vertex -5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -5.000000e-02 -1.500000e+00 4.500000e-01
      vertex 5.000000e-02 -1.500000e+00 4.500000e-01
      vertex 5.000000e-02 -1.520000e+00 4.500000e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00
    outer loop
      vertex -5.000000e-02 -1.500000e+00 4.500000e-01
      vertex 5.000000e-02 -1.520000e+00 4.500000e-01
      vertex -5.000000e-02 -1.520000e+00 4.500000e-01
    endloop
  endfacet
  facet normal -0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex -5.000000e-02 -1.520000e+00 4.500000e-01
      vertex 5.000000e-02 -1.520000e+00 4.500000e-01
      vertex 5.000000e-02 -1.520000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex -5.000000e-02 -1.520000e+00 4.500000e-01
      vertex 5.000000e-02 -1.520000e+00 -5.000000e-02
      vertex -5.000000e-02 -1.520000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex 5.000000e-02 -1.500000e+00 4.500000e-01
      vertex -5.000000e-02 -1.500000e+00 4.500000e-01
      vertex -5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 -0.000000e+00
    outer loop
      vertex 5.000000e-02 -1.500000e+00 4.500000e-01
      vertex -5.000000e-02 -1.500000e+00 -5.000000e-02
      vertex 5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal -1.000000e+00 0.000000e+00 0.000000e+00
    outer loop
      vertex 5.000000e-02 -1.520000e+00 4.500000e-01
      vertex 5.000000e-02 -1.500000e+00 4.500000e-01
      vertex 5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal -1.000000e+00 0.000000e+00 0.000000e+00
    outer loop
      vertex 5.000000e-02 -1.520000e+00 4.500000e-01
      vertex 5.000000e-02 -1.500000e+00 -5.000000e-02
      vertex 5.000000e-02 -1.520000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 1.000000e+00 0.000000e+00 0.000000e+00
    outer loop
      vertex -5.000000e-02 -1.500000e+00 4.500000e-01
      vertex -5.000000e-02 -1.520000e+00 4.500000e-01
      vertex -5.000000e-02 -1.520000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 1.000000e+00 0.000000e+00 0.000000e+00
    outer loop
      vertex -5.000000e-02 -1.500000e+00 4.500000e-01
      vertex -5.000000e-02 -1.520000e+00 -5.000000e-02
      vertex -5.000000e-02 -1.500000e+00 -5.000000e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -1.000000e+00 0.000000e+00
    outer loop
      vertex -1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 0.000000e+00 -1.520000e+00 6.200000e-01
    endloop
  endfacet
  facet normal 0.000000e+00 1.000000e+00 0.000000e+00
    outer loop
      vertex -1.400000e-01 -1.500000e+00 4.500000e-01
      vertex 0.000000e+00 -1.500000e+00 6.200000e-01
      vertex 1.400000e-01 -1.500000e+00 4.500000e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 1.400000e-01 -1.500000e+00 4.500000e-01
    endloop
  endfacet
  facet normal 0.000000e+00 0.000000e+00 1.000000e+00
    outer loop
      vertex -1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 1.400000e-01 -1.500000e+00 4.500000e-01
      vertex -1.400000e-01 -1.500000e+00 4.500000e-01
    endloop
  endfacet
  facet normal -7.719302e-01 0.000000e+00 -6.357073e-01
    outer loop
      vertex 1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 0.000000e+00 -1.520000e+00 6.200000e-01
      vertex 0.000000e+00 -1.500000e+00 6.200000e-01
    endloop
  endfacet
  facet normal -7.719302e-01 0.000000e+00 -6.357073e-01
    outer loop
      vertex 1.400000e-01 -1.520000e+00 4.500000e-01
      vertex 0.000000e+00 -1.500000e+00 6.200000e-01
      vertex 1.400000e-01 -1.500000e+00 4.500000e-01
    endloop
  endfacet
  facet normal 7.719302e-01 0.000000e+00 -6.357073e-01
    outer loop
      vertex 0.000000e+00 -1.520000e+00 6.200000e-01
      vertex -1.400000e-01 -1.520000e+00 4.500000e-01
      vertex -1.400000e-01 -1.500000e+00 4.500000e-01
    endloop
  endfacet
  facet normal 7.719302e-01 0.000000e+00 -6.357073e-01
    outer loop
      vertex 0.000000e+00 -1.520000e+00 6.200000e-01
      vertex -1.400000e-01 -1.500000e+00 4.500000e-01
      vertex 0.000000e+00 -1.500000e+00 6.200000e-01
    endloop
  endfacet
endsolid shards
```

<!-- optional proof anchor (uncomment to enable): -->
<p align="center"><sub>MPC signing architecture audited to 0 Critical/High · threshold-BLS air-gapped signing paper presented at NBC-2025, NTU Singapore</sub></p>


---

<p align="center">
  <sub>📍 Bangalore · ✉️ <a href="mailto:rana.iiitb@gmail.com">rana.iiitb@gmail.com</a> · ✍️ writeups soon</sub>
</p>
