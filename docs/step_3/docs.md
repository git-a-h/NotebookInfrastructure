\+ := Pros \
\- := Cons

- Jupyter Notebooks: \
    \+ able to combine text, code and images \
    \+ able to run code and visualize data (via graphs) \
    \+ browser based IDE \
    \+ great for interactivity as code can be run \
    \-------------------------------- \
    \- Variables can sometimes be overwritten \
    \- Functions can not be imported elsewhere 
    
    Conclusions: \
    Jupyter Notebooks are suitable for interactivity (also in the context of testing), as it allows for code to be rewritten, (re-) run and visualized.
    
- Mathjax (used in Firedrake): \
    \+ rendering of equations \
    \+ native to the browser (Javascript Display Engine) \
    \+ able to combine text with equations \
    \+ supports Latex, MathML or AsciiMath input \
    \+ output types: HTML, SVG or MathML equations \
    \+ can handle Dynamic Content (for example via input) \
    \------------------------------------- \
    \- Can not run or execute code (ill-suited)

    Conclusions:
    Suited for documentation and somewhat able to render (with possible fallback) user input. However it is unable to run code, which makes it ill-suited for interactive testing but good for documentation.