# gh-secrets-action

Github Action that let's you update your repositories secrets.

## Rationale

Imagine a case where you are in a desparete need of having some `secrets` deployed to your repositories?
On top of that, imagine that those secrets change over time and you have to **manually** redeploy them each time?
If that's not enough, imagine that you have 30 secrets like that spreaded through 10 repositories?

You with me?

Now image that you can deal with that declaratively using Github Action ;-).

## Usage

```yml
- name: Deploy dynamic secrets
  uses: kornicameister/gh-secrets-action@master
  with:
    repository: kornicameister/gh-secrets-action
    token: ${{ secrets.GH_PA_TOKEN }}
    secrets: |
      verySecretPassword: secret
      soSecretAccessKey: accessKey
```

And that's it. All configuration keys are required apart from `repository` that defaults to repository currently using action.

## Need of a PAT ?

`PUT`-ing secrets to Github API requires a `repo` access which is not supplied in already available token.
Do you recall using `${{ github.token }}`? Well, that's the one that can not `PUT` tokens into a repository.

## Will this action delete unusued secrets?

No. There are no plans to remove actions using declarative manners.
If someone wants that...just create an issue ;-)

## Imporant note

  THIS REPOSITORY DOES NOT ANYTHING THAT IT SHOULD NOT DO.
  IT WILL CREATE OR UPDATE SECRETS IN DESIGNATED REPISOTORY AND STOP AT IT.
  
If, however, someone notices that something is going on that is not exactly correct, I strongly suggest
**create an issue**. I would like to avoid harming anyone through this action.
