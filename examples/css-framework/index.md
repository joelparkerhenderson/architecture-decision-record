# CSS framework

Contents:

* [Summary](#summary)
  * [Issue](#issue)
  * [Decision](#decision)
  * [Status](#status)
* [Details](#details)
  * [Assumptions](#assumptions)
  * [Constraints](#constraints)
  * [Positions](#positions)
  * [Argument](#argument)
  * [Implications](#implications)
* [Related](#related)
  * [Related decisions](#related-decisions)
  * [Related requirements](#related-requirements)
  * [Related artifacts](#related-artifacts)
  * [Related principles](#related-principles)
* [Notes](#notes)


## Summary


### Issue

We want to use a CSS framework to create our web applications:

  * We want user experience to be fast and reliable, on all popular browsers and screen sizes.

  * We want rapid iteration on design, layout, UI/UX, etc.

  * We want responsive applications, especially for smaller screens such as on mobile devices, larger screens such as on 4K widescreens, and dynamic screens such as rotatable displays.  


### Decision

Decided on Bulma.


### Status

Decided on Bulma. Open to new CSS framework choices as they arrive.


## Details


### Assumptions

We want to create web apps that are modern, fast, reliable, responsive, etc.

Typical modern web apps are reducing/eliminating the use of jQuery because of multiple reasons: 

  * Modern JavaScript in phasing in many capabilities that jQuery has provided, so jQuery is less needed, and there are better/faster/smaller modules that provide specific implementations

  * jQuery's broad approach is to do direct DOM manipulation, which is an anti-pattern for modern JavaScript frameworks (e.g. React, Vue, Svelte)

  * jQuery interferes with itself if it's loaded twice, etc.


### Constraints

If we choose a CSS framework that uses jQuery, then we're stuck importing jQuery. For example, Semantic UI uses jQuery, and Tachyons does not.

If we choose a CSS framework that is minimal, then we forego framework components that we may want now or soon. For example, Semantic UI provides an image carousel, and Tachyons does not.


### Positions

We considered using no framework. This still seems viable, especially because CSS grid provides much of what we need for our project..

We considered many CSS frameworks using a quick shortlist triage: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, etc. Our two selections for deeper review are Semantic UI (because it has the most-semantic approach) and Bulma (because it has the lightest-weight approach that provides the components we want now).

We considered Semantic UI. This provides many components, including ones we want for our project: tabs, grids, buttons, etc. We did a pilot with Semantic UI two ways: using typical CDN files, and using NPM repos. We achieved success with Semantic UI in a static HTML page, but did not achieve success within our timebox to build a JavaScript SPA (primarly because of jQuery load issues). We discovered that other coders have been asking the Semantic UI developers to create a jQuery-free version, for the same reasons we have. Other coders have been requesting a jQuery-free version for many years, yet the developers have said no, and stated that any jQuery-free version would be too hard to write e.g. ~"the Semantic UI project has more than 22,000 touchpoints that use jQuery".

Example with Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

We considered Bulma. Bulma has many similar capabilties as Semantic UI, although not as many sophisticated components. Bulma is built with modern techniques, such as no jQuery. Bulma has some third-party components, some of which we may want to use.


Example with Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

As above.

Specifically, Semantic UI seems to have a caution flag both in terms of technology (i.e. so many jQuery touchpoints) and also in terms of leadership (i.e. jQuery-free was a hard no, rather than attemping a roadmap, or continous improvement, or donation fundraising, etc.).


### Implications

If we find a good non-jQuery CSS framework, this is generally helpful and good overall.


## Related


### Related decisions

The CSS framework we choose may affect testability.


### Related requirements

We want to ship a purely-modern app fast. 

We do not want to spend time working on older frameworks (esp. Semantic UI) using older dependencies (esp. jQuery).


### Related artifacts

Affects all the typical HTML that will use the CSS.


### Related principles

Easily reversible.

Need for speed.


## Notes

Any notes here.
