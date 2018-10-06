Jisho-alfred-workflow
====================

Yet another alfred workflow for [jisho.org](http://jisho.org).

Feature (a.k.a shortcomings)
--------------------

- Use Python 3.
- Work for Mac OS 10.12.6.
- As a result, the path to python 3 binary is hard-coded to the brew-installed python3.
- Need user to install the runtime before use it if not using the pre-compiled version.
- Display the defnition of the word in *VERY HUGE FONT* via `enter`.
- Go to the corresponding website via `ctrl + enter`.

Installation
--------------------

This code is dependent on local-installed [requests](https://github.com/requests/requests), so just type this in the workflow folder:
```
pip install --target=. requests
```

Credits
--------------------

The icon is from [jisho.org](http://jisho.org) itself.
