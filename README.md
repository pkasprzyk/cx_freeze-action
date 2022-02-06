# cx_freeze-action

This is a simple example that uses GitHub actions and [`cx_freeze`](https://pypi.org/project/cx-Freeze/) to build a [`pygame`](https://pypi.org/project/pygame/) executable for both Windows and Linux.

Executables are stored as artifacts named `windows-latest` and `ubuntu-lastes` (accessible via [https://github.com/pkasprzyk/cx_freeze-action/actions/](https://github.com/pkasprzyk/cx_freeze-action/actions/)), with access dependent on repo config (default: accessible for all logged-in GitHub users for public repo).

Feel free to take and reuse any part of this setup, as the whole repo is released in public domain.
