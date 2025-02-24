# Personal Website

A quarto website to describe professional and personal accomplishments.

Website can be found at [jennylsmith.github.io](https://jennylsmith.github.io/)

### Author
Jenny Leopoldina Smith

### Usage

Clone the repository and build a preview of the website in the `main` or `dev` branches
using the following command in a terminal:

```
quarto preview --render all --no-watch-inputs --no-browse
```

For new features or fixes, create an issue on github in a new branch.

Then open a pull request using `gh` commandline utility to merge changes into the `dev` branch, like the example below for issue #4.

```
gh pr create -B dev -H [BRANCH TO MERGE] --title "collapsible bullet points for pipelines" --body "Closes #4" --draft [--dry-run]
```

```
gh issue close -c "done" 4
```

