# Contributing to DisBOT

We really, really appreciate your interest in contributing to this project. We are super excited to have you on board!

We welcome you to fix bugs, build improvements, update documentation, and even add new features.

If you see an open issue on the GitHub tracker, you are welcome to jump right in.

---

## How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout <branch-name>`)
    - Please note that in the branch name, you should include a keyword. For example: "bugFix", "newFeature", "documentation", "improvement" or other. It should be clear what the branch is for.
    - An example branch name might be: "bugFix-hello-display"
3. Make your changes
    - Follow the example.py file in the commands folder for the structure and expectation of how to, in general, structure the new command
4. Commit with a clear message, that identifies WHY things were changed
5. Push your branch
6. Open a Pull Request
7. Go through the Code Review Process

---

## Contribution Guidelines

- Follow PEP8 style guidelines (PEP8 is the primary, official Python style guide. That is why we use it.)
- Keep code modular, with each new command or set of commands linked to a primary command in its own file
    - Please use the example.py file for reference and general expected structure of each new command file
- Document new features
- Don't break existing functionality (so, please test extensively)
- Write clear commit messages

---

## Reporting Bugs

When opening an issue, include:

- Python version
- discord.py version
- Reproduction steps
- What we expect the behavior to do
- What behavior actually happens.

Please copy this and fill out each section when reporting a bug:

```bash
# Issue tittle:

### Python Version:
### discord.py Version:

## Reproduction Steps:

## Expected Behavior:

## Current Behavior:

### (Optional) Screenshot (or link):
```

---

## Suggesting Features

Open an issue labeled `Feature-Suggestion` and describe:

- What feature you want to add.
- Why you want to add it and the benefit (may be as simple as wanting to provide another command to the public for their use).
- How you will go about adding it.
- Possible alternatives.

Please copy this and fill out each section when suggesting a new feature:

```bash
# Feature tittle:

## What?
## Why?
## How?
## Possible Alternatives:

```


---

## Code Review Process / Code Expectations

When under code review, maintainers will check for:
- PEP8 formatting
- Overall code quality
- General maintainability (will it need to be maintained with versioning changes? How difficult would it be to update?)
- Structure (does it follow our required architecture? IE: a new python file for each command or command set)
Maintainers will review pull requests for:
- Scope alignment (is it within scope of the project?)
- COMMENTS! Please comment your code, describing briefly what things do. Please also add what specific imports do. If unsure how to structure comments, please see the approved code files and the example.py file. 
- Did you add ALL new requirements to the requirements.txt file?

We openly welcome feedback! If you disagree with a reviewer, you are more than welcome to give your reasoning; however, it must be done in a respectful manner. If the reviewer disagrees even after reasoning is provided, you may request a different reviewer. If that reviewer also denies the request and asks for the same changes, then please make the changes requested. We can assure no malicious intent, as we want to foster a positive community. Please see CODE_OF_CONDUCT.md for more information.

## New? Check out Beginner-Friendly Issues!

The project has a specific Issue tag, that being "good first issue". If you are new to the community and unsure where to start, feel free and head to the issue tracker and look for this tag!

This issues are built to get people familiar with the community and introduce new contributors to the project.

## Discussion

Have a question of just want to have a discussion with the community? Feel free and use our GitHub Issue tracker! Just be sure to name and lable the issue accourdingly (by adding something such as discussion, or question). Do note that we have two different question tags: "questions" and "[questions]" the former is for project related questions and the second is for off-topic (or potentially off-topic) questions.
