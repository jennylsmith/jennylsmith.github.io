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

### Contributing

For new features or fixes, create an issue on github and create a new branch with the changes.

```
PR=18
ISSUE=4
# view the PR
gh pr view $PR

# ensure it passes checks and is mergeable
gh pr view $PR $--json mergeable
gh pr checks

# mark draft as ready and merge using squash method
gh pr ready $PR
gh pr comment 18 --body "Related to $ISSUE"
gh pr merge $PR --squash -t 'Added new feat: XYZ'
```

If this pull request closes the issue, it can be closed using the following:

```
gh issue close -c "done" 4
```



