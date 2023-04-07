## Github

Tutorial for setting up git SSH.
So you can access remote repositories on GitHub trough SSH.

1. `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
3. Enter passphrase (empty for no passphrase): [Type a passphrase]
4. Enter same passphrase again: [Type passphrase again]
5. `eval "$(ssh-agent -s)"`
6. `ssh-add ~/.ssh/id_ed25519`
7. Go to Github.com -> Settings -> SSH and GPG keys
8. Click on `New SSH key` and create a title, then past your key id.pub file from .ssh folder. 