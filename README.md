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

<sub>A cloud of shards. Exactly one camera angle resolves it. Drag, or hit the viewer's auto-rotation and watch it pass through.</sub>

```stl
solid shards
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -4.026413e-01 4.731923e-01 -2.874477e-01
      vertex -1.581283e-01 4.731923e-01 -2.874477e-01
      vertex -1.581283e-01 5.827840e-01 -3.641846e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -4.026413e-01 4.731923e-01 -2.874477e-01
      vertex -1.581283e-01 5.827840e-01 -3.641846e-01
      vertex -4.026413e-01 5.827840e-01 -3.641846e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.087357e-01 4.456279e-01 -3.413934e-01
      vertex -1.605217e-01 5.568783e-01 -4.192918e-01
      vertex -1.605217e-01 4.456279e-01 -3.413934e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.087357e-01 4.456279e-01 -3.413934e-01
      vertex -4.087357e-01 5.568783e-01 -4.192918e-01
      vertex -1.605217e-01 5.568783e-01 -4.192918e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex -4.026413e-01 4.731923e-01 -2.874477e-01
      vertex -1.581283e-01 4.731923e-01 -2.874477e-01
      vertex -1.605217e-01 4.456279e-01 -3.413934e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex -4.026413e-01 4.731923e-01 -2.874477e-01
      vertex -1.605217e-01 4.456279e-01 -3.413934e-01
      vertex -4.087357e-01 4.456279e-01 -3.413934e-01
    endloop
  endfacet
  facet normal -9.992053e-01 2.286211e-02 3.265048e-02
    outer loop
      vertex -1.581283e-01 4.731923e-01 -2.874477e-01
      vertex -1.581283e-01 5.827840e-01 -3.641846e-01
      vertex -1.605217e-01 5.568783e-01 -4.192918e-01
    endloop
  endfacet
  facet normal -9.992053e-01 2.286211e-02 3.265048e-02
    outer loop
      vertex -1.581283e-01 4.731923e-01 -2.874477e-01
      vertex -1.605217e-01 5.568783e-01 -4.192918e-01
      vertex -1.605217e-01 4.456279e-01 -3.413934e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex -1.581283e-01 5.827840e-01 -3.641846e-01
      vertex -4.026413e-01 5.827840e-01 -3.641846e-01
      vertex -4.087357e-01 5.568783e-01 -4.192918e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex -1.581283e-01 5.827840e-01 -3.641846e-01
      vertex -4.087357e-01 5.568783e-01 -4.192918e-01
      vertex -1.605217e-01 5.568783e-01 -4.192918e-01
    endloop
  endfacet
  facet normal 9.948810e-01 -5.796176e-02 -8.277797e-02
    outer loop
      vertex -4.026413e-01 5.827840e-01 -3.641846e-01
      vertex -4.026413e-01 4.731923e-01 -2.874477e-01
      vertex -4.087357e-01 4.456279e-01 -3.413934e-01
    endloop
  endfacet
  facet normal 9.948810e-01 -5.796176e-02 -8.277797e-02
    outer loop
      vertex -4.026413e-01 5.827840e-01 -3.641846e-01
      vertex -4.087357e-01 4.456279e-01 -3.413934e-01
      vertex -4.087357e-01 5.568783e-01 -4.192918e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.363124e-01 3.004772e-01 -6.254640e-01
      vertex 2.586152e-01 3.004772e-01 -6.254640e-01
      vertex 2.586152e-01 4.204626e-01 -7.094787e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.363124e-01 3.004772e-01 -6.254640e-01
      vertex 2.586152e-01 4.204626e-01 -7.094787e-01
      vertex -1.363124e-01 4.204626e-01 -7.094787e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.381969e-01 2.729128e-01 -6.794097e-01
      vertex 2.621905e-01 3.945570e-01 -7.645859e-01
      vertex 2.621905e-01 2.729128e-01 -6.794097e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.381969e-01 2.729128e-01 -6.794097e-01
      vertex -1.381969e-01 3.945570e-01 -7.645859e-01
      vertex 2.621905e-01 3.945570e-01 -7.645859e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex -1.363124e-01 3.004772e-01 -6.254640e-01
      vertex 2.586152e-01 3.004772e-01 -6.254640e-01
      vertex 2.621905e-01 2.729128e-01 -6.794097e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex -1.363124e-01 3.004772e-01 -6.254640e-01
      vertex 2.621905e-01 2.729128e-01 -6.794097e-01
      vertex -1.381969e-01 2.729128e-01 -6.794097e-01
    endloop
  endfacet
  facet normal -9.982293e-01 -3.411816e-02 -4.872578e-02
    outer loop
      vertex 2.586152e-01 3.004772e-01 -6.254640e-01
      vertex 2.586152e-01 4.204626e-01 -7.094787e-01
      vertex 2.621905e-01 3.945570e-01 -7.645859e-01
    endloop
  endfacet
  facet normal -9.982293e-01 -3.411816e-02 -4.872578e-02
    outer loop
      vertex 2.586152e-01 3.004772e-01 -6.254640e-01
      vertex 2.621905e-01 3.945570e-01 -7.645859e-01
      vertex 2.621905e-01 2.729128e-01 -6.794097e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex 2.586152e-01 4.204626e-01 -7.094787e-01
      vertex -1.363124e-01 4.204626e-01 -7.094787e-01
      vertex -1.381969e-01 3.945570e-01 -7.645859e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex 2.586152e-01 4.204626e-01 -7.094787e-01
      vertex -1.381969e-01 3.945570e-01 -7.645859e-01
      vertex 2.621905e-01 3.945570e-01 -7.645859e-01
    endloop
  endfacet
  facet normal 9.995071e-01 -1.800622e-02 -2.571555e-02
    outer loop
      vertex -1.363124e-01 4.204626e-01 -7.094787e-01
      vertex -1.363124e-01 3.004772e-01 -6.254640e-01
      vertex -1.381969e-01 2.729128e-01 -6.794097e-01
    endloop
  endfacet
  facet normal 9.995071e-01 -1.800622e-02 -2.571555e-02
    outer loop
      vertex -1.363124e-01 4.204626e-01 -7.094787e-01
      vertex -1.381969e-01 2.729128e-01 -6.794097e-01
      vertex -1.381969e-01 3.945570e-01 -7.645859e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.681864e-01 4.460726e-01 -3.405231e-01
      vertex 4.143060e-01 4.460726e-01 -3.405231e-01
      vertex 4.143060e-01 5.572963e-01 -4.184027e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.681864e-01 4.460726e-01 -3.405231e-01
      vertex 4.143060e-01 5.572963e-01 -4.184027e-01
      vertex 2.681864e-01 5.572963e-01 -4.184027e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.721861e-01 4.185081e-01 -3.944687e-01
      vertex 4.204849e-01 5.313906e-01 -4.735099e-01
      vertex 4.204849e-01 4.185081e-01 -3.944687e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.721861e-01 4.185081e-01 -3.944687e-01
      vertex 2.721861e-01 5.313906e-01 -4.735099e-01
      vertex 4.204849e-01 5.313906e-01 -4.735099e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex 2.681864e-01 4.460726e-01 -3.405231e-01
      vertex 4.143060e-01 4.460726e-01 -3.405231e-01
      vertex 4.204849e-01 4.185081e-01 -3.944687e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.904868e-01 -4.550090e-01
    outer loop
      vertex 2.681864e-01 4.460726e-01 -3.405231e-01
      vertex 4.204849e-01 4.185081e-01 -3.944687e-01
      vertex 2.721861e-01 4.185081e-01 -3.944687e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.143060e-01 4.460726e-01 -3.405231e-01
      vertex 4.143060e-01 5.572963e-01 -4.184027e-01
      vertex 4.204849e-01 5.313906e-01 -4.735099e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.143060e-01 4.460726e-01 -3.405231e-01
      vertex 4.204849e-01 5.313906e-01 -4.735099e-01
      vertex 4.204849e-01 4.185081e-01 -3.944687e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex 4.143060e-01 5.572963e-01 -4.184027e-01
      vertex 2.681864e-01 5.572963e-01 -4.184027e-01
      vertex 2.721861e-01 5.313906e-01 -4.735099e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.049903e-01 4.254322e-01
    outer loop
      vertex 4.143060e-01 5.572963e-01 -4.184027e-01
      vertex 2.721861e-01 5.313906e-01 -4.735099e-01
      vertex 4.204849e-01 5.313906e-01 -4.735099e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.681864e-01 5.572963e-01 -4.184027e-01
      vertex 2.681864e-01 4.460726e-01 -3.405231e-01
      vertex 2.721861e-01 4.185081e-01 -3.944687e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.681864e-01 5.572963e-01 -4.184027e-01
      vertex 2.721861e-01 4.185081e-01 -3.944687e-01
      vertex 2.721861e-01 5.313906e-01 -4.735099e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -4.389613e-01 4.519697e-01 -6.999370e-01
      vertex -1.865855e-01 4.519697e-01 -6.999370e-01
      vertex -1.865855e-01 6.986353e-01 -8.726541e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -4.389613e-01 4.519697e-01 -6.999370e-01
      vertex -1.865855e-01 6.986353e-01 -8.726541e-01
      vertex -4.389613e-01 6.986353e-01 -8.726541e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.450663e-01 4.263468e-01 -7.552421e-01
      vertex -1.891805e-01 6.764429e-01 -9.303613e-01
      vertex -1.891805e-01 4.263468e-01 -7.552421e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.450663e-01 4.263468e-01 -7.552421e-01
      vertex -4.450663e-01 6.764429e-01 -9.303613e-01
      vertex -1.891805e-01 6.764429e-01 -9.303613e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex -4.389613e-01 4.519697e-01 -6.999370e-01
      vertex -1.865855e-01 4.519697e-01 -6.999370e-01
      vertex -1.891805e-01 4.263468e-01 -7.552421e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex -4.389613e-01 4.519697e-01 -6.999370e-01
      vertex -1.891805e-01 4.263468e-01 -7.552421e-01
      vertex -4.450663e-01 4.263468e-01 -7.552421e-01
    endloop
  endfacet
  facet normal -9.990660e-01 2.478401e-02 3.539524e-02
    outer loop
      vertex -1.865855e-01 4.519697e-01 -6.999370e-01
      vertex -1.865855e-01 6.986353e-01 -8.726541e-01
      vertex -1.891805e-01 6.764429e-01 -9.303613e-01
    endloop
  endfacet
  facet normal -9.990660e-01 2.478401e-02 3.539524e-02
    outer loop
      vertex -1.865855e-01 4.519697e-01 -6.999370e-01
      vertex -1.891805e-01 6.764429e-01 -9.303613e-01
      vertex -1.891805e-01 4.263468e-01 -7.552421e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex -1.865855e-01 6.986353e-01 -8.726541e-01
      vertex -4.389613e-01 6.986353e-01 -8.726541e-01
      vertex -4.450663e-01 6.764429e-01 -9.303613e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex -1.865855e-01 6.986353e-01 -8.726541e-01
      vertex -4.450663e-01 6.764429e-01 -9.303613e-01
      vertex -1.891805e-01 6.764429e-01 -9.303613e-01
    endloop
  endfacet
  facet normal 9.948633e-01 -5.806162e-02 -8.292058e-02
    outer loop
      vertex -4.389613e-01 6.986353e-01 -8.726541e-01
      vertex -4.389613e-01 4.519697e-01 -6.999370e-01
      vertex -4.450663e-01 4.263468e-01 -7.552421e-01
    endloop
  endfacet
  facet normal 9.948633e-01 -5.806162e-02 -8.292058e-02
    outer loop
      vertex -4.389613e-01 6.986353e-01 -8.726541e-01
      vertex -4.450663e-01 4.263468e-01 -7.552421e-01
      vertex -4.450663e-01 6.764429e-01 -9.303613e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.858638e-01 7.246084e-01 -8.704707e-01
      vertex -1.858638e-01 8.353220e-01 -9.479932e-01
      vertex -4.372635e-01 8.353220e-01 -9.479932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.858638e-01 7.246084e-01 -8.704707e-01
      vertex -4.372635e-01 8.353220e-01 -9.479932e-01
      vertex -4.372635e-01 7.246084e-01 -8.704707e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.884588e-01 7.026925e-01 -9.283716e-01
      vertex -4.433685e-01 8.149519e-01 -1.006976e+00
      vertex -1.884588e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.884588e-01 7.026925e-01 -9.283716e-01
      vertex -4.433685e-01 7.026925e-01 -9.283716e-01
      vertex -4.433685e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal -9.990660e-01 2.478401e-02 3.539524e-02
    outer loop
      vertex -1.858638e-01 7.246084e-01 -8.704707e-01
      vertex -1.858638e-01 8.353220e-01 -9.479932e-01
      vertex -1.884588e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal -9.990660e-01 2.478401e-02 3.539524e-02
    outer loop
      vertex -1.858638e-01 7.246084e-01 -8.704707e-01
      vertex -1.884588e-01 8.149519e-01 -1.006976e+00
      vertex -1.884588e-01 7.026925e-01 -9.283716e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex -1.858638e-01 8.353220e-01 -9.479932e-01
      vertex -4.372635e-01 8.353220e-01 -9.479932e-01
      vertex -4.433685e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex -1.858638e-01 8.353220e-01 -9.479932e-01
      vertex -4.433685e-01 8.149519e-01 -1.006976e+00
      vertex -1.884588e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal 9.948633e-01 -5.806162e-02 -8.292058e-02
    outer loop
      vertex -4.372635e-01 8.353220e-01 -9.479932e-01
      vertex -4.372635e-01 7.246084e-01 -8.704707e-01
      vertex -4.433685e-01 7.026925e-01 -9.283716e-01
    endloop
  endfacet
  facet normal 9.948633e-01 -5.806162e-02 -8.292058e-02
    outer loop
      vertex -4.372635e-01 8.353220e-01 -9.479932e-01
      vertex -4.433685e-01 7.026925e-01 -9.283716e-01
      vertex -4.433685e-01 8.149519e-01 -1.006976e+00
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex -4.372635e-01 7.246084e-01 -8.704707e-01
      vertex -1.858638e-01 7.246084e-01 -8.704707e-01
      vertex -1.884588e-01 7.026925e-01 -9.283716e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex -4.372635e-01 7.246084e-01 -8.704707e-01
      vertex -1.884588e-01 7.026925e-01 -9.283716e-01
      vertex -4.433685e-01 7.026925e-01 -9.283716e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.661816e-01 5.731366e-01 -4.384074e-01
      vertex 2.555744e-01 5.731366e-01 -4.384074e-01
      vertex 2.555744e-01 8.035794e-01 -5.997652e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.661816e-01 5.731366e-01 -4.384074e-01
      vertex 2.555744e-01 8.035794e-01 -5.997652e-01
      vertex 1.661816e-01 8.035794e-01 -5.997652e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.686556e-01 5.475137e-01 -4.937125e-01
      vertex 2.593791e-01 7.813871e-01 -6.574724e-01
      vertex 2.593791e-01 5.475137e-01 -4.937125e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.686556e-01 5.475137e-01 -4.937125e-01
      vertex 1.686556e-01 7.813871e-01 -6.574724e-01
      vertex 2.593791e-01 7.813871e-01 -6.574724e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex 1.661816e-01 5.731366e-01 -4.384074e-01
      vertex 2.555744e-01 5.731366e-01 -4.384074e-01
      vertex 2.593791e-01 5.475137e-01 -4.937125e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex 1.661816e-01 5.731366e-01 -4.384074e-01
      vertex 2.593791e-01 5.475137e-01 -4.937125e-01
      vertex 1.686556e-01 5.475137e-01 -4.937125e-01
    endloop
  endfacet
  facet normal -9.979955e-01 -3.629867e-02 -5.183987e-02
    outer loop
      vertex 2.555744e-01 5.731366e-01 -4.384074e-01
      vertex 2.555744e-01 8.035794e-01 -5.997652e-01
      vertex 2.593791e-01 7.813871e-01 -6.574724e-01
    endloop
  endfacet
  facet normal -9.979955e-01 -3.629867e-02 -5.183987e-02
    outer loop
      vertex 2.555744e-01 5.731366e-01 -4.384074e-01
      vertex 2.593791e-01 7.813871e-01 -6.574724e-01
      vertex 2.593791e-01 5.475137e-01 -4.937125e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex 2.555744e-01 8.035794e-01 -5.997652e-01
      vertex 1.661816e-01 8.035794e-01 -5.997652e-01
      vertex 1.686556e-01 7.813871e-01 -6.574724e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex 2.555744e-01 8.035794e-01 -5.997652e-01
      vertex 1.686556e-01 7.813871e-01 -6.574724e-01
      vertex 2.593791e-01 7.813871e-01 -6.574724e-01
    endloop
  endfacet
  facet normal 9.991510e-01 2.362974e-02 3.374677e-02
    outer loop
      vertex 1.661816e-01 8.035794e-01 -5.997652e-01
      vertex 1.661816e-01 5.731366e-01 -4.384074e-01
      vertex 1.686556e-01 5.475137e-01 -4.937125e-01
    endloop
  endfacet
  facet normal 9.991510e-01 2.362974e-02 3.374677e-02
    outer loop
      vertex 1.661816e-01 8.035794e-01 -5.997652e-01
      vertex 1.686556e-01 5.475137e-01 -4.937125e-01
      vertex 1.686556e-01 7.813871e-01 -6.574724e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.351642e-01 9.397166e-01 -3.021632e-01
      vertex 2.351642e-01 1.035258e+00 -3.690622e-01
      vertex 1.529104e-01 1.035258e+00 -3.690622e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.351642e-01 9.397166e-01 -3.021632e-01
      vertex 1.529104e-01 1.035258e+00 -3.690622e-01
      vertex 1.529104e-01 9.397166e-01 -3.021632e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.389689e-01 9.178007e-01 -3.600640e-01
      vertex 1.553843e-01 1.014888e+00 -4.280454e-01
      vertex 2.389689e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.389689e-01 9.178007e-01 -3.600640e-01
      vertex 1.553843e-01 9.178007e-01 -3.600640e-01
      vertex 1.553843e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal -9.979955e-01 -3.629867e-02 -5.183987e-02
    outer loop
      vertex 2.351642e-01 9.397166e-01 -3.021632e-01
      vertex 2.351642e-01 1.035258e+00 -3.690622e-01
      vertex 2.389689e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal -9.979955e-01 -3.629867e-02 -5.183987e-02
    outer loop
      vertex 2.351642e-01 9.397166e-01 -3.021632e-01
      vertex 2.389689e-01 1.014888e+00 -4.280454e-01
      vertex 2.389689e-01 9.178007e-01 -3.600640e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex 2.351642e-01 1.035258e+00 -3.690622e-01
      vertex 1.529104e-01 1.035258e+00 -3.690622e-01
      vertex 1.553843e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex 2.351642e-01 1.035258e+00 -3.690622e-01
      vertex 1.553843e-01 1.014888e+00 -4.280454e-01
      vertex 2.389689e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal 9.991510e-01 2.362974e-02 3.374677e-02
    outer loop
      vertex 1.529104e-01 1.035258e+00 -3.690622e-01
      vertex 1.529104e-01 9.397166e-01 -3.021632e-01
      vertex 1.553843e-01 9.178007e-01 -3.600640e-01
    endloop
  endfacet
  facet normal 9.991510e-01 2.362974e-02 3.374677e-02
    outer loop
      vertex 1.529104e-01 1.035258e+00 -3.690622e-01
      vertex 1.553843e-01 9.178007e-01 -3.600640e-01
      vertex 1.553843e-01 1.014888e+00 -4.280454e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex 1.529104e-01 9.397166e-01 -3.021632e-01
      vertex 2.351642e-01 9.397166e-01 -3.021632e-01
      vertex 2.389689e-01 9.178007e-01 -3.600640e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex 1.529104e-01 9.397166e-01 -3.021632e-01
      vertex 2.389689e-01 9.178007e-01 -3.600640e-01
      vertex 1.553843e-01 9.178007e-01 -3.600640e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.847102e-01 4.703999e-01 -6.601568e-01
      vertex 4.398327e-01 4.703999e-01 -6.601568e-01
      vertex 4.398327e-01 7.145979e-01 -8.311460e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.847102e-01 4.703999e-01 -6.601568e-01
      vertex 4.398327e-01 7.145979e-01 -8.311460e-01
      vertex 2.847102e-01 7.145979e-01 -8.311460e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.887099e-01 4.447770e-01 -7.154619e-01
      vertex 4.460117e-01 6.924056e-01 -8.888533e-01
      vertex 4.460117e-01 4.447770e-01 -7.154619e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.887099e-01 4.447770e-01 -7.154619e-01
      vertex 2.887099e-01 6.924056e-01 -8.888533e-01
      vertex 4.460117e-01 6.924056e-01 -8.888533e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex 2.847102e-01 4.703999e-01 -6.601568e-01
      vertex 4.398327e-01 4.703999e-01 -6.601568e-01
      vertex 4.460117e-01 4.447770e-01 -7.154619e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.073501e-01 -4.203759e-01
    outer loop
      vertex 2.847102e-01 4.703999e-01 -6.601568e-01
      vertex 4.460117e-01 4.447770e-01 -7.154619e-01
      vertex 2.887099e-01 4.447770e-01 -7.154619e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.398327e-01 4.703999e-01 -6.601568e-01
      vertex 4.398327e-01 7.145979e-01 -8.311460e-01
      vertex 4.460117e-01 6.924056e-01 -8.888533e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.398327e-01 4.703999e-01 -6.601568e-01
      vertex 4.460117e-01 6.924056e-01 -8.888533e-01
      vertex 4.460117e-01 4.447770e-01 -7.154619e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex 4.398327e-01 7.145979e-01 -8.311460e-01
      vertex 2.847102e-01 7.145979e-01 -8.311460e-01
      vertex 2.887099e-01 6.924056e-01 -8.888533e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.333606e-01 3.589400e-01
    outer loop
      vertex 4.398327e-01 7.145979e-01 -8.311460e-01
      vertex 2.887099e-01 6.924056e-01 -8.888533e-01
      vertex 4.460117e-01 6.924056e-01 -8.888533e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.847102e-01 7.145979e-01 -8.311460e-01
      vertex 2.847102e-01 4.703999e-01 -6.601568e-01
      vertex 2.887099e-01 4.447770e-01 -7.154619e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.847102e-01 7.145979e-01 -8.311460e-01
      vertex 2.887099e-01 4.447770e-01 -7.154619e-01
      vertex 2.887099e-01 6.924056e-01 -8.888533e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 4.316405e-01 7.633340e-01 -7.681592e-01
      vertex 4.316405e-01 8.713162e-01 -8.437692e-01
      vertex 2.794073e-01 8.713162e-01 -8.437692e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 4.316405e-01 7.633340e-01 -7.681592e-01
      vertex 2.794073e-01 8.713162e-01 -8.437692e-01
      vertex 2.794073e-01 7.633340e-01 -7.681592e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.378195e-01 7.414181e-01 -8.260601e-01
      vertex 2.834070e-01 8.509461e-01 -9.027524e-01
      vertex 4.378195e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.378195e-01 7.414181e-01 -8.260601e-01
      vertex 2.834070e-01 7.414181e-01 -8.260601e-01
      vertex 2.834070e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.316405e-01 7.633340e-01 -7.681592e-01
      vertex 4.316405e-01 8.713162e-01 -8.437692e-01
      vertex 4.378195e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal -9.947391e-01 -5.875742e-02 -8.391429e-02
    outer loop
      vertex 4.316405e-01 7.633340e-01 -7.681592e-01
      vertex 4.378195e-01 8.509461e-01 -9.027524e-01
      vertex 4.378195e-01 7.414181e-01 -8.260601e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex 4.316405e-01 8.713162e-01 -8.437692e-01
      vertex 2.794073e-01 8.713162e-01 -8.437692e-01
      vertex 2.834070e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.452195e-01 3.264355e-01
    outer loop
      vertex 4.316405e-01 8.713162e-01 -8.437692e-01
      vertex 2.834070e-01 8.509461e-01 -9.027524e-01
      vertex 4.378195e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.794073e-01 8.713162e-01 -8.437692e-01
      vertex 2.794073e-01 7.633340e-01 -7.681592e-01
      vertex 2.834070e-01 7.414181e-01 -8.260601e-01
    endloop
  endfacet
  facet normal 9.977855e-01 3.815102e-02 5.448531e-02
    outer loop
      vertex 2.794073e-01 8.713162e-01 -8.437692e-01
      vertex 2.834070e-01 7.414181e-01 -8.260601e-01
      vertex 2.834070e-01 8.509461e-01 -9.027524e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex 2.794073e-01 7.633340e-01 -7.681592e-01
      vertex 4.316405e-01 7.633340e-01 -7.681592e-01
      vertex 4.378195e-01 7.414181e-01 -8.260601e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.352465e-01 -3.539971e-01
    outer loop
      vertex 2.794073e-01 7.633340e-01 -7.681592e-01
      vertex 4.378195e-01 7.414181e-01 -8.260601e-01
      vertex 2.834070e-01 7.414181e-01 -8.260601e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.540382e-01 -5.833113e-01 5.695160e-01
      vertex -1.417277e-01 -5.833113e-01 5.695160e-01
      vertex -1.417277e-01 -3.255778e-01 3.890491e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.540382e-01 -5.833113e-01 5.695160e-01
      vertex -1.417277e-01 -3.255778e-01 3.890491e-01
      vertex -1.540382e-01 -3.255778e-01 3.890491e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.564276e-01 -6.279480e-01 5.275245e-01
      vertex -1.439261e-01 -3.662166e-01 3.442582e-01
      vertex -1.439261e-01 -6.279480e-01 5.275245e-01
    endloop
  endfacet
  facet normal -1.737151e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.564276e-01 -6.279480e-01 5.275245e-01
      vertex -1.564276e-01 -3.662166e-01 3.442582e-01
      vertex -1.439261e-01 -3.662166e-01 3.442582e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.851965e-01 -7.283583e-01
    outer loop
      vertex -1.540382e-01 -5.833113e-01 5.695160e-01
      vertex -1.417277e-01 -5.833113e-01 5.695160e-01
      vertex -1.439261e-01 -6.279480e-01 5.275245e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.851965e-01 -7.283583e-01
    outer loop
      vertex -1.540382e-01 -5.833113e-01 5.695160e-01
      vertex -1.439261e-01 -6.279480e-01 5.275245e-01
      vertex -1.564276e-01 -6.279480e-01 5.275245e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.417277e-01 -5.833113e-01 5.695160e-01
      vertex -1.417277e-01 -3.255778e-01 3.890491e-01
      vertex -1.439261e-01 -3.662166e-01 3.442582e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.417277e-01 -5.833113e-01 5.695160e-01
      vertex -1.439261e-01 -3.662166e-01 3.442582e-01
      vertex -1.439261e-01 -6.279480e-01 5.275245e-01
    endloop
  endfacet
  facet normal -6.369517e-15 -7.405997e-01 6.719464e-01
    outer loop
      vertex -1.417277e-01 -3.255778e-01 3.890491e-01
      vertex -1.540382e-01 -3.255778e-01 3.890491e-01
      vertex -1.564276e-01 -3.662166e-01 3.442582e-01
    endloop
  endfacet
  facet normal -9.464263e-15 -7.405997e-01 6.719464e-01
    outer loop
      vertex -1.417277e-01 -3.255778e-01 3.890491e-01
      vertex -1.564276e-01 -3.662166e-01 3.442582e-01
      vertex -1.439261e-01 -3.662166e-01 3.442582e-01
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.540382e-01 -3.255778e-01 3.890491e-01
      vertex -1.540382e-01 -5.833113e-01 5.695160e-01
      vertex -1.564276e-01 -6.279480e-01 5.275245e-01
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.540382e-01 -3.255778e-01 3.890491e-01
      vertex -1.564276e-01 -6.279480e-01 5.275245e-01
      vertex -1.564276e-01 -3.662166e-01 3.442582e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.323396e-01 -1.186321e-01 5.569317e-01
      vertex -1.323396e-01 2.419811e-01 3.044276e-01
      vertex -1.438347e-01 2.419811e-01 3.044276e-01
    endloop
  endfacet
  facet normal 5.539748e-15 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.323396e-01 -1.186321e-01 5.569317e-01
      vertex -1.438347e-01 2.419811e-01 3.044276e-01
      vertex -1.438347e-01 -1.186321e-01 5.569317e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.345381e-01 -1.587160e-01 5.117522e-01
      vertex -1.462241e-01 2.078878e-01 2.550535e-01
      vertex -1.345381e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal -2.724612e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.345381e-01 -1.587160e-01 5.117522e-01
      vertex -1.462241e-01 -1.587160e-01 5.117522e-01
      vertex -1.462241e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.323396e-01 -1.186321e-01 5.569317e-01
      vertex -1.323396e-01 2.419811e-01 3.044276e-01
      vertex -1.345381e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.323396e-01 -1.186321e-01 5.569317e-01
      vertex -1.345381e-01 2.078878e-01 2.550535e-01
      vertex -1.345381e-01 -1.587160e-01 5.117522e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.228833e-01 5.682103e-01
    outer loop
      vertex -1.323396e-01 2.419811e-01 3.044276e-01
      vertex -1.438347e-01 2.419811e-01 3.044276e-01
      vertex -1.462241e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.228833e-01 5.682103e-01
    outer loop
      vertex -1.323396e-01 2.419811e-01 3.044276e-01
      vertex -1.462241e-01 2.078878e-01 2.550535e-01
      vertex -1.345381e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.438347e-01 2.419811e-01 3.044276e-01
      vertex -1.438347e-01 -1.186321e-01 5.569317e-01
      vertex -1.462241e-01 -1.587160e-01 5.117522e-01
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.438347e-01 2.419811e-01 3.044276e-01
      vertex -1.462241e-01 -1.587160e-01 5.117522e-01
      vertex -1.462241e-01 2.078878e-01 2.550535e-01
    endloop
  endfacet
  facet normal 7.224672e-15 7.480307e-01 -6.636641e-01
    outer loop
      vertex -1.438347e-01 -1.186321e-01 5.569317e-01
      vertex -1.323396e-01 -1.186321e-01 5.569317e-01
      vertex -1.345381e-01 -1.587160e-01 5.117522e-01
    endloop
  endfacet
  facet normal 3.686662e-15 7.480307e-01 -6.636641e-01
    outer loop
      vertex -1.438347e-01 -1.186321e-01 5.569317e-01
      vertex -1.345381e-01 -1.587160e-01 5.117522e-01
      vertex -1.462241e-01 -1.587160e-01 5.117522e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.432030e-01 1.145868e-01 3.168894e-02
      vertex -1.432030e-01 4.637226e-01 -2.127786e-01
      vertex -1.556417e-01 4.637226e-01 -2.127786e-01
    endloop
  endfacet
  facet normal 2.730397e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.432030e-01 1.145868e-01 3.168894e-02
      vertex -1.556417e-01 4.637226e-01 -2.127786e-01
      vertex -1.556417e-01 1.145868e-01 3.168894e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.454014e-01 8.112405e-02 -1.812665e-02
      vertex -1.580311e-01 4.356197e-01 -2.663472e-01
      vertex -1.454014e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal 9.916128e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.454014e-01 8.112405e-02 -1.812665e-02
      vertex -1.580311e-01 8.112405e-02 -1.812665e-02
      vertex -1.580311e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.432030e-01 1.145868e-01 3.168894e-02
      vertex -1.432030e-01 4.637226e-01 -2.127786e-01
      vertex -1.454014e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal -9.993294e-01 2.100208e-02 2.999407e-02
    outer loop
      vertex -1.432030e-01 1.145868e-01 3.168894e-02
      vertex -1.454014e-01 4.356197e-01 -2.663472e-01
      vertex -1.454014e-01 8.112405e-02 -1.812665e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.855383e-01 4.645663e-01
    outer loop
      vertex -1.432030e-01 4.637226e-01 -2.127786e-01
      vertex -1.556417e-01 4.637226e-01 -2.127786e-01
      vertex -1.580311e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.855383e-01 4.645663e-01
    outer loop
      vertex -1.432030e-01 4.637226e-01 -2.127786e-01
      vertex -1.580311e-01 4.356197e-01 -2.663472e-01
      vertex -1.454014e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.556417e-01 4.637226e-01 -2.127786e-01
      vertex -1.556417e-01 1.145868e-01 3.168894e-02
      vertex -1.580311e-01 8.112405e-02 -1.812665e-02
    endloop
  endfacet
  facet normal 9.992080e-01 -2.282355e-02 -3.259541e-02
    outer loop
      vertex -1.556417e-01 4.637226e-01 -2.127786e-01
      vertex -1.580311e-01 8.112405e-02 -1.812665e-02
      vertex -1.580311e-01 4.356197e-01 -2.663472e-01
    endloop
  endfacet
  facet normal -8.356422e-15 8.301042e-01 -5.576083e-01
    outer loop
      vertex -1.556417e-01 1.145868e-01 3.168894e-02
      vertex -1.432030e-01 1.145868e-01 3.168894e-02
      vertex -1.454014e-01 8.112405e-02 -1.812665e-02
    endloop
  endfacet
  facet normal -1.001349e-14 8.301042e-01 -5.576083e-01
    outer loop
      vertex -1.556417e-01 1.145868e-01 3.168894e-02
      vertex -1.454014e-01 8.112405e-02 -1.812665e-02
      vertex -1.580311e-01 8.112405e-02 -1.812665e-02
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.322810e-01 -7.206451e-01 4.403205e-01
      vertex 1.466122e-01 -7.206451e-01 4.403205e-01
      vertex 1.466122e-01 -4.506113e-01 2.512408e-01
    endloop
  endfacet
  facet normal 7.547423e-17 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.322810e-01 -7.206451e-01 4.403205e-01
      vertex 1.466122e-01 -4.506113e-01 2.512408e-01
      vertex -1.322810e-01 -4.506113e-01 2.512408e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.342394e-01 -7.652818e-01 3.983290e-01
      vertex 1.487828e-01 -4.912501e-01 2.064499e-01
      vertex 1.487828e-01 -7.652818e-01 3.983290e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.342394e-01 -7.652818e-01 3.983290e-01
      vertex -1.342394e-01 -4.912501e-01 2.064499e-01
      vertex 1.487828e-01 -4.912501e-01 2.064499e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.851965e-01 -7.283583e-01
    outer loop
      vertex -1.322810e-01 -7.206451e-01 4.403205e-01
      vertex 1.466122e-01 -7.206451e-01 4.403205e-01
      vertex 1.487828e-01 -7.652818e-01 3.983290e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.851965e-01 -7.283583e-01
    outer loop
      vertex -1.322810e-01 -7.206451e-01 4.403205e-01
      vertex 1.487828e-01 -7.652818e-01 3.983290e-01
      vertex -1.342394e-01 -7.652818e-01 3.983290e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.466122e-01 -7.206451e-01 4.403205e-01
      vertex 1.466122e-01 -4.506113e-01 2.512408e-01
      vertex 1.487828e-01 -4.912501e-01 2.064499e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.466122e-01 -7.206451e-01 4.403205e-01
      vertex 1.487828e-01 -4.912501e-01 2.064499e-01
      vertex 1.487828e-01 -7.652818e-01 3.983290e-01
    endloop
  endfacet
  facet normal -4.285641e-16 -7.405997e-01 6.719464e-01
    outer loop
      vertex 1.466122e-01 -4.506113e-01 2.512408e-01
      vertex -1.322810e-01 -4.506113e-01 2.512408e-01
      vertex -1.342394e-01 -4.912501e-01 2.064499e-01
    endloop
  endfacet
  facet normal -4.180494e-16 -7.405997e-01 6.719464e-01
    outer loop
      vertex 1.466122e-01 -4.506113e-01 2.512408e-01
      vertex -1.342394e-01 -4.912501e-01 2.064499e-01
      vertex 1.487828e-01 -4.912501e-01 2.064499e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.322810e-01 -4.506113e-01 2.512408e-01
      vertex -1.322810e-01 -7.206451e-01 4.403205e-01
      vertex -1.342394e-01 -7.652818e-01 3.983290e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.322810e-01 -4.506113e-01 2.512408e-01
      vertex -1.342394e-01 -7.652818e-01 3.983290e-01
      vertex -1.342394e-01 -4.912501e-01 2.064499e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.298384e-01 -1.033755e-01 5.741277e-01
      vertex 1.298384e-01 2.549576e-01 3.232201e-01
      vertex -1.171469e-01 2.549576e-01 3.232201e-01
    endloop
  endfacet
  facet normal -1.103886e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.298384e-01 -1.033755e-01 5.741277e-01
      vertex -1.171469e-01 2.549576e-01 3.232201e-01
      vertex -1.171469e-01 -1.033755e-01 5.741277e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.320090e-01 -1.434594e-01 5.289482e-01
      vertex -1.191053e-01 2.208642e-01 2.738461e-01
      vertex 1.320090e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal 1.085735e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.320090e-01 -1.434594e-01 5.289482e-01
      vertex -1.191053e-01 -1.434594e-01 5.289482e-01
      vertex -1.191053e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.298384e-01 -1.033755e-01 5.741277e-01
      vertex 1.298384e-01 2.549576e-01 3.232201e-01
      vertex 1.320090e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.298384e-01 -1.033755e-01 5.741277e-01
      vertex 1.320090e-01 2.208642e-01 2.738461e-01
      vertex 1.320090e-01 -1.434594e-01 5.289482e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.228833e-01 5.682103e-01
    outer loop
      vertex 1.298384e-01 2.549576e-01 3.232201e-01
      vertex -1.171469e-01 2.549576e-01 3.232201e-01
      vertex -1.191053e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.228833e-01 5.682103e-01
    outer loop
      vertex 1.298384e-01 2.549576e-01 3.232201e-01
      vertex -1.191053e-01 2.208642e-01 2.738461e-01
      vertex 1.320090e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.171469e-01 2.549576e-01 3.232201e-01
      vertex -1.171469e-01 -1.033755e-01 5.741277e-01
      vertex -1.191053e-01 -1.434594e-01 5.289482e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.171469e-01 2.549576e-01 3.232201e-01
      vertex -1.191053e-01 -1.434594e-01 5.289482e-01
      vertex -1.191053e-01 2.208642e-01 2.738461e-01
    endloop
  endfacet
  facet normal 6.345705e-16 7.480307e-01 -6.636641e-01
    outer loop
      vertex -1.171469e-01 -1.033755e-01 5.741277e-01
      vertex 1.298384e-01 -1.033755e-01 5.741277e-01
      vertex 1.320090e-01 -1.434594e-01 5.289482e-01
    endloop
  endfacet
  facet normal 6.290714e-16 7.480307e-01 -6.636641e-01
    outer loop
      vertex -1.171469e-01 -1.033755e-01 5.741277e-01
      vertex 1.320090e-01 -1.434594e-01 5.289482e-01
      vertex -1.191053e-01 -1.434594e-01 5.289482e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.567445e-01 -1.221155e-01 -3.206868e-01
      vertex 1.567445e-01 2.649339e-01 -5.917018e-01
      vertex -1.414229e-01 2.649339e-01 -5.917018e-01
    endloop
  endfacet
  facet normal -3.436905e-17 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.567445e-01 -1.221155e-01 -3.206868e-01
      vertex -1.414229e-01 2.649339e-01 -5.917018e-01
      vertex -1.414229e-01 -1.221155e-01 -3.206868e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.589151e-01 -1.555783e-01 -3.705024e-01
      vertex -1.433814e-01 2.368311e-01 -6.452704e-01
      vertex 1.589151e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal 7.567933e-18 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.589151e-01 -1.555783e-01 -3.705024e-01
      vertex -1.433814e-01 -1.555783e-01 -3.705024e-01
      vertex -1.433814e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.567445e-01 -1.221155e-01 -3.206868e-01
      vertex 1.567445e-01 2.649339e-01 -5.917018e-01
      vertex 1.589151e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.567445e-01 -1.221155e-01 -3.206868e-01
      vertex 1.589151e-01 2.368311e-01 -6.452704e-01
      vertex 1.589151e-01 -1.555783e-01 -3.705024e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.855383e-01 4.645663e-01
    outer loop
      vertex 1.567445e-01 2.649339e-01 -5.917018e-01
      vertex -1.414229e-01 2.649339e-01 -5.917018e-01
      vertex -1.433814e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.855383e-01 4.645663e-01
    outer loop
      vertex 1.567445e-01 2.649339e-01 -5.917018e-01
      vertex -1.433814e-01 2.368311e-01 -6.452704e-01
      vertex 1.589151e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.414229e-01 2.649339e-01 -5.917018e-01
      vertex -1.414229e-01 -1.221155e-01 -3.206868e-01
      vertex -1.433814e-01 -1.555783e-01 -3.705024e-01
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.414229e-01 2.649339e-01 -5.917018e-01
      vertex -1.433814e-01 -1.555783e-01 -3.705024e-01
      vertex -1.433814e-01 2.368311e-01 -6.452704e-01
    endloop
  endfacet
  facet normal -3.742647e-16 8.301042e-01 -5.576083e-01
    outer loop
      vertex -1.414229e-01 -1.221155e-01 -3.206868e-01
      vertex 1.567445e-01 -1.221155e-01 -3.206868e-01
      vertex 1.589151e-01 -1.555783e-01 -3.705024e-01
    endloop
  endfacet
  facet normal -3.346822e-16 8.301042e-01 -5.576083e-01
    outer loop
      vertex -1.414229e-01 -1.221155e-01 -3.206868e-01
      vertex 1.589151e-01 -1.555783e-01 -3.705024e-01
      vertex -1.433814e-01 -1.555783e-01 -3.705024e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.332473e-01 5.890183e-01 -2.572448e-02
      vertex 1.332473e-01 6.175898e-01 -4.573048e-02
      vertex -1.202226e-01 6.175898e-01 -4.573048e-02
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.332473e-01 5.890183e-01 -2.572448e-02
      vertex -1.202226e-01 6.175898e-01 -4.573048e-02
      vertex -1.202226e-01 5.890183e-01 -2.572448e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.354180e-01 5.612391e-01 -7.951971e-02
      vertex -1.221810e-01 5.902760e-01 -9.985161e-02
      vertex 1.354180e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.354180e-01 5.612391e-01 -7.951971e-02
      vertex -1.221810e-01 5.612391e-01 -7.951971e-02
      vertex -1.221810e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.332473e-01 5.890183e-01 -2.572448e-02
      vertex 1.332473e-01 6.175898e-01 -4.573048e-02
      vertex 1.354180e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal -9.993463e-01 -2.073660e-02 -2.961494e-02
    outer loop
      vertex 1.332473e-01 5.890183e-01 -2.572448e-02
      vertex 1.354180e-01 5.902760e-01 -9.985161e-02
      vertex 1.354180e-01 5.612391e-01 -7.951971e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.927499e-01 4.505525e-01
    outer loop
      vertex 1.332473e-01 6.175898e-01 -4.573048e-02
      vertex -1.202226e-01 6.175898e-01 -4.573048e-02
      vertex -1.221810e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.927499e-01 4.505525e-01
    outer loop
      vertex 1.332473e-01 6.175898e-01 -4.573048e-02
      vertex -1.221810e-01 5.902760e-01 -9.985161e-02
      vertex 1.354180e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.202226e-01 6.175898e-01 -4.573048e-02
      vertex -1.202226e-01 5.890183e-01 -2.572448e-02
      vertex -1.221810e-01 5.612391e-01 -7.951971e-02
    endloop
  endfacet
  facet normal 9.994677e-01 -1.871190e-02 -2.672336e-02
    outer loop
      vertex -1.202226e-01 6.175898e-01 -4.573048e-02
      vertex -1.221810e-01 5.612391e-01 -7.951971e-02
      vertex -1.221810e-01 5.902760e-01 -9.985161e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.885266e-01 -4.588251e-01
    outer loop
      vertex -1.202226e-01 5.890183e-01 -2.572448e-02
      vertex 1.332473e-01 5.890183e-01 -2.572448e-02
      vertex 1.354180e-01 5.612391e-01 -7.951971e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.885266e-01 -4.588251e-01
    outer loop
      vertex -1.202226e-01 5.890183e-01 -2.572448e-02
      vertex 1.354180e-01 5.612391e-01 -7.951971e-02
      vertex -1.221810e-01 5.612391e-01 -7.951971e-02
    endloop
  endfacet
  facet normal -2.935958e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -3.585048e-01 -9.759018e-01 5.144853e-01
      vertex -1.909031e-01 -1.213697e+00 6.809914e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -1.909031e-01 -1.213697e+00 6.809914e-01
      vertex -1.591100e-01 -1.213697e+00 6.809914e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -1.591100e-01 -1.213697e+00 6.809914e-01
      vertex -1.591100e-01 -8.892679e-01 4.538236e-01
    endloop
  endfacet
  facet normal 7.607038e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
      vertex -1.936709e-01 -1.264559e+00 6.433585e-01
      vertex -3.637026e-01 -1.023315e+00 4.744382e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
      vertex -1.614169e-01 -1.264559e+00 6.433585e-01
      vertex -1.936709e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
      vertex -1.614169e-01 -9.354254e-01 4.128970e-01
      vertex -1.614169e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal 8.646113e-01 -3.761428e-01 3.331125e-01
    outer loop
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -3.585048e-01 -9.759018e-01 5.144853e-01
      vertex -3.637026e-01 -1.023315e+00 4.744382e-01
    endloop
  endfacet
  facet normal 8.646113e-01 -3.761428e-01 3.331125e-01
    outer loop
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -3.637026e-01 -1.023315e+00 4.744382e-01
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
    endloop
  endfacet
  facet normal 8.480023e-01 2.846438e-01 -4.470682e-01
    outer loop
      vertex -3.585048e-01 -9.759018e-01 5.144853e-01
      vertex -1.909031e-01 -1.213697e+00 6.809914e-01
      vertex -1.936709e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal 8.480023e-01 2.846438e-01 -4.470682e-01
    outer loop
      vertex -3.585048e-01 -9.759018e-01 5.144853e-01
      vertex -1.936709e-01 -1.264559e+00 6.433585e-01
      vertex -3.637026e-01 -1.023315e+00 4.744382e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.947978e-01 -8.038754e-01
    outer loop
      vertex -1.909031e-01 -1.213697e+00 6.809914e-01
      vertex -1.591100e-01 -1.213697e+00 6.809914e-01
      vertex -1.614169e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.947978e-01 -8.038754e-01
    outer loop
      vertex -1.909031e-01 -1.213697e+00 6.809914e-01
      vertex -1.614169e-01 -1.264559e+00 6.433585e-01
      vertex -1.936709e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal -9.992617e-01 2.203661e-02 3.147154e-02
    outer loop
      vertex -1.591100e-01 -1.213697e+00 6.809914e-01
      vertex -1.591100e-01 -8.892679e-01 4.538236e-01
      vertex -1.614169e-01 -9.354254e-01 4.128970e-01
    endloop
  endfacet
  facet normal -9.992617e-01 2.203661e-02 3.147154e-02
    outer loop
      vertex -1.591100e-01 -1.213697e+00 6.809914e-01
      vertex -1.614169e-01 -9.354254e-01 4.128970e-01
      vertex -1.614169e-01 -1.264559e+00 6.433585e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.634366e-01 7.482325e-01
    outer loop
      vertex -1.591100e-01 -8.892679e-01 4.538236e-01
      vertex -2.974439e-01 -8.892679e-01 4.538236e-01
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.634366e-01 7.482325e-01
    outer loop
      vertex -1.591100e-01 -8.892679e-01 4.538236e-01
      vertex -3.017565e-01 -9.354254e-01 4.128970e-01
      vertex -1.614169e-01 -9.354254e-01 4.128970e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.599971e-01 -7.978774e-01 2.478755e-01
      vertex -1.926835e-01 -7.978774e-01 2.478755e-01
      vertex -3.022181e-01 -9.532864e-01 3.566941e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.599971e-01 -7.978774e-01 2.478755e-01
      vertex -3.022181e-01 -9.532864e-01 3.566941e-01
      vertex -1.599971e-01 -9.532864e-01 3.566941e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.622535e-01 -8.414846e-01 2.051631e-01
      vertex -3.064801e-01 -9.990853e-01 3.155163e-01
      vertex -1.954008e-01 -8.414846e-01 2.051631e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.622535e-01 -8.414846e-01 2.051631e-01
      vertex -1.622535e-01 -9.990853e-01 3.155163e-01
      vertex -3.064801e-01 -9.990853e-01 3.155163e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.997392e-01 7.143984e-01
    outer loop
      vertex -1.599971e-01 -7.978774e-01 2.478755e-01
      vertex -1.926835e-01 -7.978774e-01 2.478755e-01
      vertex -1.954008e-01 -8.414846e-01 2.051631e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.997392e-01 7.143984e-01
    outer loop
      vertex -1.599971e-01 -7.978774e-01 2.478755e-01
      vertex -1.954008e-01 -8.414846e-01 2.051631e-01
      vertex -1.622535e-01 -8.414846e-01 2.051631e-01
    endloop
  endfacet
  facet normal 8.647516e-01 -3.778761e-01 3.307782e-01
    outer loop
      vertex -1.926835e-01 -7.978774e-01 2.478755e-01
      vertex -3.022181e-01 -9.532864e-01 3.566941e-01
      vertex -3.064801e-01 -9.990853e-01 3.155163e-01
    endloop
  endfacet
  facet normal 8.647516e-01 -3.778761e-01 3.307782e-01
    outer loop
      vertex -1.926835e-01 -7.978774e-01 2.478755e-01
      vertex -3.064801e-01 -9.990853e-01 3.155163e-01
      vertex -1.954008e-01 -8.414846e-01 2.051631e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.685954e-01 -7.436264e-01
    outer loop
      vertex -3.022181e-01 -9.532864e-01 3.566941e-01
      vertex -1.599971e-01 -9.532864e-01 3.566941e-01
      vertex -1.622535e-01 -9.990853e-01 3.155163e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.685954e-01 -7.436264e-01
    outer loop
      vertex -3.022181e-01 -9.532864e-01 3.566941e-01
      vertex -1.622535e-01 -9.990853e-01 3.155163e-01
      vertex -3.064801e-01 -9.990853e-01 3.155163e-01
    endloop
  endfacet
  facet normal -9.992937e-01 2.155452e-02 3.078304e-02
    outer loop
      vertex -1.599971e-01 -9.532864e-01 3.566941e-01
      vertex -1.599971e-01 -7.978774e-01 2.478755e-01
      vertex -1.622535e-01 -8.414846e-01 2.051631e-01
    endloop
  endfacet
  facet normal -9.992937e-01 2.155452e-02 3.078304e-02
    outer loop
      vertex -1.599971e-01 -9.532864e-01 3.566941e-01
      vertex -1.622535e-01 -8.414846e-01 2.051631e-01
      vertex -1.622535e-01 -9.990853e-01 3.155163e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex -1.316516e-01 -1.333292e+00 5.969324e-01
      vertex 1.818364e-01 -1.333292e+00 5.969324e-01
    endloop
  endfacet
  facet normal -2.892014e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex 1.818364e-01 -1.333292e+00 5.969324e-01
      vertex 2.574307e-01 -1.226037e+00 5.218323e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex 2.574307e-01 -1.226037e+00 5.218323e-01
      vertex 2.574307e-01 -9.980864e-01 3.622192e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
      vertex 1.843881e-01 -1.384196e+00 5.593297e-01
      vertex -1.334990e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal -3.750036e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
      vertex 2.610431e-01 -1.275437e+00 4.831757e-01
      vertex 1.843881e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
      vertex 2.610431e-01 -1.044287e+00 3.213228e-01
      vertex 2.610431e-01 -1.275437e+00 4.831757e-01
    endloop
  endfacet
  facet normal 9.995263e-01 -1.765215e-02 -2.520989e-02
    outer loop
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex -1.316516e-01 -1.333292e+00 5.969324e-01
      vertex -1.334990e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal 9.995263e-01 -1.765215e-02 -2.520989e-02
    outer loop
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex -1.334990e-01 -1.384196e+00 5.593297e-01
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.941628e-01 -8.043448e-01
    outer loop
      vertex -1.316516e-01 -1.333292e+00 5.969324e-01
      vertex 1.818364e-01 -1.333292e+00 5.969324e-01
      vertex 1.843881e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.941628e-01 -8.043448e-01
    outer loop
      vertex -1.316516e-01 -1.333292e+00 5.969324e-01
      vertex 1.843881e-01 -1.384196e+00 5.593297e-01
      vertex -1.334990e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal -8.484516e-01 2.863015e-01 -4.451531e-01
    outer loop
      vertex 1.818364e-01 -1.333292e+00 5.969324e-01
      vertex 2.574307e-01 -1.226037e+00 5.218323e-01
      vertex 2.610431e-01 -1.275437e+00 4.831757e-01
    endloop
  endfacet
  facet normal -8.484516e-01 2.863015e-01 -4.451531e-01
    outer loop
      vertex 1.818364e-01 -1.333292e+00 5.969324e-01
      vertex 2.610431e-01 -1.275437e+00 4.831757e-01
      vertex 1.843881e-01 -1.384196e+00 5.593297e-01
    endloop
  endfacet
  facet normal -9.981925e-01 -3.447084e-02 -4.922947e-02
    outer loop
      vertex 2.574307e-01 -1.226037e+00 5.218323e-01
      vertex 2.574307e-01 -9.980864e-01 3.622192e-01
      vertex 2.610431e-01 -1.044287e+00 3.213228e-01
    endloop
  endfacet
  facet normal -9.981925e-01 -3.447084e-02 -4.922947e-02
    outer loop
      vertex 2.574307e-01 -1.226037e+00 5.218323e-01
      vertex 2.610431e-01 -1.044287e+00 3.213228e-01
      vertex 2.610431e-01 -1.275437e+00 4.831757e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.628148e-01 7.487834e-01
    outer loop
      vertex 2.574307e-01 -9.980864e-01 3.622192e-01
      vertex -1.316516e-01 -9.980864e-01 3.622192e-01
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.628148e-01 7.487834e-01
    outer loop
      vertex 2.574307e-01 -9.980864e-01 3.622192e-01
      vertex -1.334990e-01 -1.044287e+00 3.213228e-01
      vertex 2.610431e-01 -1.044287e+00 3.213228e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex 1.753488e-01 -7.030161e-01 3.418400e-01
      vertex -1.269545e-01 -7.030161e-01 3.418400e-01
    endloop
  endfacet
  facet normal 3.143312e-17 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex -1.269545e-01 -7.030161e-01 3.418400e-01
      vertex -1.269545e-01 -8.536261e-01 4.472983e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex -1.269545e-01 -8.536261e-01 4.472983e-01
      vertex 2.482460e-01 -8.536261e-01 4.472983e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
      vertex -1.288019e-01 -7.466324e-01 2.991340e-01
      vertex 1.779005e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal -3.664548e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
      vertex -1.288019e-01 -8.994341e-01 4.061268e-01
      vertex -1.288019e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
      vertex 2.518584e-01 -8.994341e-01 4.061268e-01
      vertex -1.288019e-01 -8.994341e-01 4.061268e-01
    endloop
  endfacet
  facet normal -8.646327e-01 -3.764019e-01 3.327640e-01
    outer loop
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex 1.753488e-01 -7.030161e-01 3.418400e-01
      vertex 1.779005e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal -8.646327e-01 -3.764019e-01 3.327640e-01
    outer loop
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex 1.779005e-01 -7.466324e-01 2.991340e-01
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.996115e-01 7.145235e-01
    outer loop
      vertex 1.753488e-01 -7.030161e-01 3.418400e-01
      vertex -1.269545e-01 -7.030161e-01 3.418400e-01
      vertex -1.288019e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.996115e-01 7.145235e-01
    outer loop
      vertex 1.753488e-01 -7.030161e-01 3.418400e-01
      vertex -1.288019e-01 -7.466324e-01 2.991340e-01
      vertex 1.779005e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal 9.995263e-01 -1.765215e-02 -2.520989e-02
    outer loop
      vertex -1.269545e-01 -7.030161e-01 3.418400e-01
      vertex -1.269545e-01 -8.536261e-01 4.472983e-01
      vertex -1.288019e-01 -8.994341e-01 4.061268e-01
    endloop
  endfacet
  facet normal 9.995263e-01 -1.765215e-02 -2.520989e-02
    outer loop
      vertex -1.269545e-01 -7.030161e-01 3.418400e-01
      vertex -1.288019e-01 -8.994341e-01 4.061268e-01
      vertex -1.288019e-01 -7.466324e-01 2.991340e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.684648e-01 -7.437438e-01
    outer loop
      vertex -1.269545e-01 -8.536261e-01 4.472983e-01
      vertex 2.482460e-01 -8.536261e-01 4.472983e-01
      vertex 2.518584e-01 -8.994341e-01 4.061268e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.684648e-01 -7.437438e-01
    outer loop
      vertex -1.269545e-01 -8.536261e-01 4.472983e-01
      vertex 2.518584e-01 -8.994341e-01 4.061268e-01
      vertex -1.288019e-01 -8.994341e-01 4.061268e-01
    endloop
  endfacet
  facet normal -9.981925e-01 -3.447084e-02 -4.922947e-02
    outer loop
      vertex 2.482460e-01 -8.536261e-01 4.472983e-01
      vertex 2.482460e-01 -8.064436e-01 4.142607e-01
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
    endloop
  endfacet
  facet normal -9.981925e-01 -3.447084e-02 -4.922947e-02
    outer loop
      vertex 2.482460e-01 -8.536261e-01 4.472983e-01
      vertex 2.518584e-01 -8.515649e-01 3.726085e-01
      vertex 2.518584e-01 -8.994341e-01 4.061268e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.735764e-01 8.191520e-01
    outer loop
      vertex 3.283029e-01 -6.360327e-01 7.907134e-01
      vertex 2.734571e-01 -5.582168e-01 7.362261e-01
      vertex 2.434776e-01 -5.582168e-01 7.362261e-01
    endloop
  endfacet
  facet normal 3.381406e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex 3.283029e-01 -6.360327e-01 7.907134e-01
      vertex 2.434776e-01 -5.582168e-01 7.362261e-01
      vertex 2.434776e-01 -7.563840e-01 8.749842e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.336022e-01 -6.833332e-01 7.505870e-01
      vertex 2.474077e-01 -6.042611e-01 6.952202e-01
      vertex 2.778711e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal -8.187077e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.336022e-01 -6.833332e-01 7.505870e-01
      vertex 2.474077e-01 -8.056271e-01 8.362181e-01
      vertex 2.474077e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal -8.647374e-01 -3.776964e-01 3.310206e-01
    outer loop
      vertex 3.283029e-01 -6.360327e-01 7.907134e-01
      vertex 2.734571e-01 -5.582168e-01 7.362261e-01
      vertex 2.778711e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal -8.647374e-01 -3.776964e-01 3.310206e-01
    outer loop
      vertex 3.283029e-01 -6.360327e-01 7.907134e-01
      vertex 2.778711e-01 -6.042611e-01 6.952202e-01
      vertex 3.336022e-01 -6.833332e-01 7.505870e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.650665e-01 7.467842e-01
    outer loop
      vertex 2.734571e-01 -5.582168e-01 7.362261e-01
      vertex 2.434776e-01 -5.582168e-01 7.362261e-01
      vertex 2.474077e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.650665e-01 7.467842e-01
    outer loop
      vertex 2.734571e-01 -5.582168e-01 7.362261e-01
      vertex 2.474077e-01 -6.042611e-01 6.952202e-01
      vertex 2.778711e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal 9.978616e-01 3.749009e-02 5.354139e-02
    outer loop
      vertex 2.434776e-01 -5.582168e-01 7.362261e-01
      vertex 2.434776e-01 -7.563840e-01 8.749842e-01
      vertex 2.474077e-01 -8.056271e-01 8.362181e-01
    endloop
  endfacet
  facet normal 9.978616e-01 3.749009e-02 5.354139e-02
    outer loop
      vertex 2.434776e-01 -5.582168e-01 7.362261e-01
      vertex 2.474077e-01 -8.056271e-01 8.362181e-01
      vertex 2.474077e-01 -6.042611e-01 6.952202e-01
    endloop
  endfacet
  facet normal -8.479495e-01 2.844502e-01 -4.472915e-01
    outer loop
      vertex 2.434776e-01 -7.563840e-01 8.749842e-01
      vertex 3.283029e-01 -6.360327e-01 7.907134e-01
      vertex 3.336022e-01 -6.833332e-01 7.505870e-01
    endloop
  endfacet
  facet normal -8.479495e-01 2.844502e-01 -4.472915e-01
    outer loop
      vertex 2.434776e-01 -7.563840e-01 8.749842e-01
      vertex 3.336022e-01 -6.833332e-01 7.505870e-01
      vertex 2.474077e-01 -8.056271e-01 8.362181e-01
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
