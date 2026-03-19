# Styles, Norms, and Best Practices

We use PEP8, we keep in sync with Python Black, blah blah blah

## Leave \_\_init\_\_.py alone!
It is the posture of this project that init files should be blank unless there is some reason to alias for continuous 
integration reasons like continuing to support a previous naming convention during a transition prior to deprecation. 
While aliasing in the \_\_init\_\_.py is preferred by many Python developers, this project considers it to usually be 
only an extra and unncessary layer of abstraction that makes it all the more difficult for new developers to trace 
through what the code is doing. This can be resolved through clear and clean practices, but there is too much room 
for drift. It does make for longer import lines as we use fully qualified paths, but the directory path of the file 
you're referncing is always apparent this way. And they don't charge you for extra characters.

## They don't charge you for extra characters
Sometimes you need to abbreviate for readability, we get it. But in general, we think you should be more verbose in 
comments, variable names, and logic statements. When you are unsure, err on the side of human readability over 
compactness. This also has the added benefit of keeping fewer pieces of information in human brains and creating
less room for error. PWR should be POWER. CMD should be COMMAND. It is not followed dogmatically in the codebase,
but it should be considered as you write code.

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/collaboration/styles_et_al.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>
