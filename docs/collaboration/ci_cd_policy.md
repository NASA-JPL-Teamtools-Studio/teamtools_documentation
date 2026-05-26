# CI/CD Policies

TTS uses GitHub actions to automate a test suite each time code is pushed to any branch. This suite includes basic unit tests, but also includes checks for test coverage, documentation coverage, and security screening. Due to the great nuance involved in each of these checks (Do I need to close out every vulnerability, or am I OK with some risks? What should I think about unit tests written with AI?), this page documents some of the risk postures that the studio has identified.

In general, this pattern follows those that will be recognizable to spacecraft operators. Provide verbose evidence of anything that _might_ be an issue with a particular build, but give the operators the ability to override those results based on the particular risk postures of the project. Different teams will have different needs, and trying to provide a one-size-fits-all risk strategy is not suitable.

However, because all TTS Core repositories are managed by the same team, we can make some basic assumptions here. Project adapting TTS can choose to take these same conventions or to tailor them to their own needs.

## Releases

In a perfect world, all of the CI/CD tests described below will roll up to one big ✅ by the time the code is released. But as we live in the real world, we expect that there will be some ⚠️'s in most releasesm and even potentially some ❌. The rules below are meant to set a baseline expectation for release standards for TTS, but the reality is that human beings are in the loop and should be trusted to deliver code that is capable, stable, and safe. All of the status emojis described below are meant to be tools for human operators.

A roll up table will be reported on every PR (and updated each time a new commit is added), and a Tower report will be created with more verbose results. Tower also provides an interface for human developers to record their rationale for releasing the code in the state in which it was released. Any FLAGGED or VIOLATING tests (which correspond to ⚠️ and ❌) need to be dispositioned by a human at each release. This workflow is enforced in order to keep humans honest about understanding the risks they are taking when releasing any less than perfect code.

## Unit Testing

Unit testing is further described in (tesing.md), this page only covers how conventions are handled in this CI/CD automation.

### Tests

In general all tests in a TTS repository should be working prior to release. There will be some cases where tests need to be masked using the xfail or skip features in pytest. This is not completely precluded, but should be avoided where possible. When it is truly impossible to avoid, a GH issue should be written against the masked test.

Unit test suites with failing tests will be marked as ❌, those with xfails or skips as ⚠️, and those with all tests passing will show ✅.

### Test Coverage

TTS strives for as full of test coverage as possible. The minimum allowable test coverage is 50%, and anything lower than that will be marked as ❌. Unit test suites with >50% but <80% will be marked as ⚠️, and >80% gets ✅. These values may be reconsidered as coverage improves

### Tests Written by AI

It is the policy of Teamtools Studio that any working unit tests are better than no tests at all, so we welcome the use of AI in expanding test coverage.

However, while there is little risk to accepting a unit test produce by AI to the code itself, it may lull developers into a false sense of security. For this reason any tests written with AI should use pytest markers to mark them `unreviewed_ai` until a human is able to account for every line of the test. 

This way, AI-developed test coverage can be covered separately from those that have been reviewed by a person. Humans do not need to write every line of TTS software, but the human who commits it to the repository takes 100% responsibility for its contents. The `unreviewed_ai` flag keeps situational awareness of which unit tests need more scrutiny.

## Security Screening

### Pip Audit

Pip Audit reports on any publicly known vulnerabilities in the library or anywhere in its dependency tree. Pip audit vulnerabilities come in different severities, which flow into the urgency with which TTS requires they be mitigated.

For MODERN python versions, all open vulnerabilities should be inspected and dispositioned. Any libraries that show known vulnerabilities but are no longer getting security updates should be removed from the depedency stack.

For versions of python that themselves are no longer getting security updates (before 3.10, see https://devguide.python.org/versions/), vulnerabilities need to be taken on a case by case basis. Projects using older versions of Python are free to make their own cybersecurity decisions, but the should do so with a full understanding of the risks they are taking.

### Bandit

Bandit and Pip audit go hand in hand. Whereas Pip Audit autids on the library level, Bandit goes line for line through the code to determine whether it has been used improperly anywhere (XML bombs come up a lot with the core Python XML implementation).

## Documentation

TTS strives to have 100% docstring completion, but this is a never-ending process. Docstring coverage >50% but <80% will be marked as ⚠️, and >80% gets ✅.

This percentage includes a docstring for every method, function and class, with functions and classes getting documentation for every arg and kwarg. Classes get their primary documentation on the \_\_init\_\_ method, which should also have every arg and kwarg documented.