# jnj_nebula Dev Container
Welcome to the Nebula Dev Container!

## Initial Setup
To begin developing in this container, you'll first need to solve these three riddles:
1. Install Docker Desktop, or [Rancher Desktop](https://rancherdesktop.io/) (and make sure it's running).
2. Install the "Remote Development" extension pack by microsoft in VSCode.
3. Copy your username & password into the placeholders in [.devcontainer/pip.conf](pip.conf).
    > Alternatively, you can get an encrypted version of your password and indeed the entire URL from [JFrog](https://artifactrepo.jnj.com/ui/packages)
    - "Set Me Up"
    - Package Type: `PyPI`
    - Repository: `tadj-pypi-snapshot`
    - Type your password
    - Click the lock
    - "Resolve"
    - Copy URL. Make sure you use `extra-index-url` instead of the supplied `index-url`

> **_NOTE:_**  DO NOT COMMIT THE CONTENTS OF pip.conf! Don't commit your password (encrypted or not) to the repository! If you do, your coworkers will know it was you because your username will be right there next to it, and you'll never be able to escape from the shame.

## Running the Container
Running the container is easy, just click on the green box in the bottom left of VS Code and click "Reopen in Container". Boom, bam, you're ready to go.

## Bash Aliasing
Two command-line methods are included in this container for executing unit tests:
- `run_unit_tests` runs all the unit tests, stopping at the first failure, or if a path is provided, only the unit tests in the given file/directory will be executed.
- `debug_unit_tests` works the same way as its `run_` variant, but with the custom `--hold` flag supplied to pytest.

For ruther customization, this Dev Container copies [.devcontainer/.bash_aliases](.bash_aliases) to the user's home directory, executing its contents for each new bash shell started in this container. Feel free to add anything you want here, but maybe discuss with the rest of the team before comitting changes to the repository.

## Future Improvements
- [ ] Full git integration (including ssh keys username etc) would be a nice addition so that git can be used directly from inside the dev container
- [ ] Automatically prompt or obtain artifactory credentials for pip.conf so the developer doesn't need to manually supply these
- [ ] Cache & Stash™ the dev container image in a completely-built or nearly-built state to expediate spin-up