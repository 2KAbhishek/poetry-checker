<div align = "center">

<h1><a href="https://2kabhishek.github.io/poetry-checker">Poetry Checker</a></h1>

<a href="https://github.com/2KAbhishek/poetry-checker/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/poetry-checker?style=flat&color=eee&label="> </a>

<a href="https://github.com/2KAbhishek/poetry-checker/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/2kabhishek/poetry-checker?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/2KAbhishek/poetry-checker/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/poetry-checker?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/2KAbhishek/poetry-checker/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/poetry-checker?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/poetry-checker/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/2kabhishek/poetry-checker?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/2KAbhishek/poetry-checker/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/2kabhishek/poetry-checker?style=flat&color=e06c75&label="> </a>

<h3>Analyze your poetry ✍🏻📃</h3>

<figure>
  <img src= "images/screenshot.jpg" alt="poetry-checker Demo">
  <br/>
  <figcaption>poetry-checker screenshot</figcaption>
</figure>

</div>

## What is this

A poetry checking tool that analyzes poems and tells you information about them.
Can tell you different types of poetry based on dictionary and rhyming.

## Inspiration

Always enjoyed poetry, read about dictionaries and rhyming, implemented this.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of `python`

## Getting poetry-checker

To install poetry-checker, follow these steps:

```bash
git clone https://github.com/2kabhishek/poetry-checker
cd poetry-checker
```

## Using poetry-checker

To run poetry-checker, follow these steps: `python src/poetry_program.py`

By default it looks at the [sample_poems](./data/sample_poems/) directory, add your poem to the directory and run the program.
Enter the file name when prompted.

## Tests

Every module has it's own doctest, which can be run by running `python -m doctest -v <module>`.
Unit tests can be ran using `python -m unittest`.

Custom linter is present in the `util` directory.

## How it was built

poetry-checker was built using `python`

## Challenges faced

Setting up tests was tricky, due to module path issues.

## What I learned

- Learned about `doctest` and found it very useful for documentation.
- Pronunciation and they are used in rhyming.
- Different types of poetry.

## What's next

Add CLI flags to pass in poems.txt file.

Hit the ⭐ button if you found this useful.

## More Info

<div align="center">

<a href="https://github.com/2KAbhishek/poetry-checker">Source</a> | <a href="https://2kabhishek.github.io/poetry-checker">Website</a>

</div>
