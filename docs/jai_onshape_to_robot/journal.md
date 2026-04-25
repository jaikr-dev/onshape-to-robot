# onshape-to-robot Journal

## 2026-04-25

### Moving the repo out of Onshape2Robot

The `onshape-to-robot` repo was previously cloned inside `/home/jai/GitHub/Onshape2Robot/onshape-to-robot`. This was a standalone git repo nested inside a non-git folder. Moved it to `/home/jai/GitHub/onshape-to-robot` so it sits at the same level as every other repo.

Moving the folder broke the Python install because it was installed in editable mode (`pip install -e`). Editable mode works differently from a normal pip install:

- **Normal install** -- pip downloads the package from PyPI (pypi.org) and copies the code into a central location called `site-packages` (`/home/jai/miniconda3/lib/python3.13/site-packages/`). After that, the original source folder doesn't matter -- you could delete it and the package still works.
- **Editable install** -- pip doesn't copy anything. Instead it creates a pointer in `site-packages` that says "when someone imports this package, go read the code from this specific folder." So when you edit the source code, the changes take effect immediately without reinstalling. The source folder must stay where it is.

The pointer was still pointing to the old path (`/home/jai/GitHub/Onshape2Robot/onshape-to-robot`), which no longer existed after the move. Running `onshape-to-robot` would have failed because Python would look for code in a folder that's not there anymore.

Fix was to reinstall in editable mode from the new location:

```bash
pip install -e /home/jai/GitHub/onshape-to-robot
```

This updated the pointer to the new path. It also picked up v1.8.2 (from the upstream merge) -- was on v1.7.9 before.

The editable install is the right choice here because this is a fork with active changes (camera support, actuator naming, R2 XML matching). Installing normally from PyPI would give the upstream version without any of those customizations.
