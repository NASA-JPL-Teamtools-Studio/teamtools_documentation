# About the Teamtools Studio

## Overview
The goal of TTS is to provide libraries that can solve the first 80% of any spacecraft operations issue while abstracting out
nit-picky issues of programming. We would like our customers to be able to import our libraries and immediately start working on
problems that truly require their expertise, rather than having to manage which data comes from where and how it gets to them.

The core TTS team all has significant experience in both spacecraft operations and software development, uniquely situating us
to develop solutions that are technically sound while still meeting the expectations of our other operations colleagues.

## We eat our own dog food.
Teamtools Studio is a collection of operator/developers defining what it means to do continuous development in spacecraft
operations. We are not ivory tower middle managers philosophizing on how to do mission operators, nor are we solely
software engineers who work only abstractly with requirements. Most of us are spacecraft operators and systems
engineers first, and software engineers after that.

That doesn't mean that we don't take software engineering seriously. But it does mean that we keep close to the actual
problems that operators are facing. We use these libraries on a day to day basis to do our jobs, so if they're painful
for you, they'll be painful for us, too. And we'll have an incentive to fix them.

## Atomization
TTS has a philosophy of atomizing our solutions as much as possible, both to facilitate reuse and to allow any
given project to select our libraries a la carte. We expect our primary customers (JPL missions) to already have significant
and complex Ground Data Systems (GDS) before they consider our work, but pick up our atoms to either fill the gaps between those
larger, less agile tools, or to use them to solve last mile problems that GDS tools do not solve well for various reasons. 

The most significant of these is the fact that GDS developers typically only have modest operations experience, and operators are
typically better at solving the very specific and deep problems. Historically, this has meant that the last mile layer has been
messy and hard to maintain. By delivering the first three quarters of that last mile, TTS hopes to enable operators.

While the primary use case of TTS is to take libraries one at a time a la carte, a significant set of functions needed to plan
spacecraft activities and keep a vehicle safe are implemented here. And for a mission on the order of magnitude of a cubesat or
a small explorer, TTS libraries could potentially form a large portion, or even the entire planning and analysis system.

## Portability
Another major philosophy of TTS is portability of our solutions across many systems. For this reason we have chosen to write
almost exclusively in Python, which has good cross-platform compatibility and has a very large and active community of developers
and educators. We have chosen to support Python versions as far back as 3.6 because many older missions still have technical
debt that keeps them attached to these old versions, and we want these tools to be available to them as well (although please,
if you have the power, use something more modern).

While we have not ruled out the possibility entirely, TTS is also generally unintersted in writing applications. Nothing you
see here is in itself stateful. It might connect to a database, or might write to a file system, but we make as few assumptions
about those technologies as possible, expecting our customers to bring their own solutions. We use a lot of HTML, but do not
currently support any web apps, and if we did they would similarly not be stateful.

## Interoperability
TTS has also put siginifant effort into interoperability. For this reason, you will see many Abstract Base Classes throughout
this code base. We use this mechanism to enforce enough standardization across projects that once the customer devloper writes
the correct ingestion classes, they have access to the rest of the ecosystem without needing to write glueware.

## Reference Formats
There is no way to avoid requiring some amount of standardization in certain inputs such as command sequences and command and
telemetry dictionaries. For these, we have chosen to use many JPL-native constructs like AMPCS XML dicitonaries, and SeqJSON,
RML, and .seq command sequence formats. While your interfaces are not strictly required to match these, if they do not, you 
may have more work to do in your adaptation layer. This topic is discussed further in the Reference Project section of this
documetnation, where we discuss the DemoSat project, which is a cartoon spacecraft we have developed to illustrate each of these
tools with a minimally realistic adaption layer (since many of these tools make little sense when only looking at the core layer).

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/about.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>