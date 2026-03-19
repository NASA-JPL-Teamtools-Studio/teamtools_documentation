# Testing

Unit testing is one of the single most important ingredients in writing maintainable code.
Once you trust your tests, you will be set free to pull things apart, put them back together
again, and have confidence that you have minimized the risk of breaking your downstream 
customers with your next update.

For this reason, TTS strives to have 100% coverage on all of our libraries, and has included
test coverage reports in our unit test matrix (see https://github.com/NASA-JPL-Teamtools-Studio/tts_ci_cd/)

## TTS Testing Conventions

* Use pytest. The world won't end if you're contributing something using unittest, but 
in general, that is our style.
* Unless there is a compelling reason not to, try to match your test architecture one-to-one with
the architecture with your code architecture.
    * One test file per code file
    * One test per function/method
    * When using supporting files, structure your test file directory so it is 
    very easy to track which file belongs to which test
    * When using supportnig files, only share files between tests if they are extremely similar
* Tests written by GenAI are better than no tests at all.
	* GenAI is a powerful tool in writing tests, but shoulnd't be used naively
	* If you write a test with GenAI, you should mark it as unreviewed until you have clearly
	walked through and understand it (https://github.com/NASA-JPL-Teamtools-Studio/tts_ci_cd/issues/1)
	    * Note: we have not followed this convention to date, but will soon start. 
	    * To begin, all tests should be marked as unreviewed even though many were written by
	    humans
* Know how code coverage actually works
	* pytest-cov gives you credit for exerising a line of code
	* It has no way to understand that you have written a valid test
	* You could exercise every line and just assert True at the end and get 100% coverage
	* See https://github.com/NASA-JPL-Teamtools-Studio/tts_ci_cd/issues/2 for more information

## Test Matrix

Although it is impossible to test in every permutation of Python version and dependency version
that out customers may be using, TTS understands that teams using our code may be using different
configurations than we are. "It works on my machine" is not sufficient.

For this reason, we have developed a matrix testing strategy as follows:
* Run tests against every major version of Python. 
    * In general this is the most recent minor version of each major version
    * The exception is 3.6.8, which we use as our oldest supported version
    * 3.6.8 still comes as default on many systems
* Allow pip to resolve whichever lastest version of each library is available for each test
* Use a clean Docker container for testing each library. Clone it and install all of its dependencies
at run time.
    * These libraries are best used as a whole suite, but are designed to be used independently
    of each other, so we smoke out any implicit dependencies here so we can fix them
* Use unit testing as a time to run other housekeeping tools
    * Security flaws via pip-audit and bandit
    * Test coverage via pytest-cov
    * Documentation coverage via a home-grown script
    	* Check if every function, method, class, and arg/kwarg has a docstring

See https://https://nasa-jpl-teamtools-studio.github.io/tts_ci_cd/ for latest matrix test results

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools-documentation/blob/main/docs/collaboration/testing.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>