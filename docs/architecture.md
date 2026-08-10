# Architecture

This page shows a high-level heirarchy of the interdependencies of all TTS libraries, including the DemoSat adaptation layer.
It is not meant to strictly match the pip resolution of all packages. For example, TTS Utilities is required by every TTS library
(it's where our shared logger lives) but it is only illustrated as flowing to its direct children. Any node in this diagram
may depend on any of those in the flow of the heirarchy above it. Some depenencies are not illustrated because the diagram gets too
messy as more and more are added. Illustrating the general inheritance strategy is more important here than creating an image that
is exhaustively correct.

```mermaid
graph TD;
    %% Main Logic
    A[TTS Utilities] --> C[HTML Utilities];
    A --> D[TTS Dictionary Interface];
    D --> B[TTS Seq];
    A --> E[FRESH];
    C --> F[Papertrail];
    F --> G[Data Utils];
    G --> H[Dexter]
    G --> I[Dante]
    E --> J[DemoSat FRESH];
    F --> K[Tower];
    H --> L[DemoSat Dexter];
    I --> M[DemoSat Dante];
    K --> N[DemoSat Tower]; 
    D --> O[DemoSat Dictionary Interface];
    G --> P[DemoSat Data Utils];
    B --> Q[DemoSat Seq];
    A --> R[TTS Spice];
    R --> S[TTS Plan];
    S --> T[DemoSat Plan];
    M --> L;
    R --> B;
    P --> L;
    P --> M;
    O --> Q;
    B --> E;
    Q --> J;
    J --> N;
    
    %% Utility Nodes (Clean & Professional)
    classDef utility fill:#f8f9fb,stroke:#2980b9,stroke-width:1px,color:#333;
    class A,B,C,D,E,F,G,H,I,K,R,S utility;

    %% NASA Blue for DemoSat Nodes (The "Bottom Line")
    classDef demosat fill:#0032A0,stroke:#001d5e,stroke-width:2px,color:#fff,font-weight:bold;
    class J,L,M,N,O,P,Q,T demosat;
```


---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/architecture.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>