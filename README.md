# etude-ChArUco

<!-- Badges -->
[![Last Commit](https://img.shields.io/github/last-commit/shin-sforzando/etude-ChArUco)](https://github.com/shin-sforzando/etude-ChArUco/graphs/commit-activity)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<!-- Screenshots -->
| ![Screenshot 1](https://placehold.jp/32/3d4070/ffffff/720x480.png?text=Screenshot%201) | ![Screenshot 2](https://placehold.jp/32/703d40/ffffff/720x480.png?text=Screenshot%202) |
|:--------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
|                                      Screenshot 1                                      |                                      Screenshot 2                                      |

<!-- Synopsis -->
Etude for ChArUco calibration.

<!-- TOC -->
- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [First time preparation](#first-time-preparation)
    - [Init](#init)
    - [Setup Git Hooks (Lefthook)](#setup-git-hooks-lefthook)
  - [Develop](#develop)
    - [Start](#start)
    - [Format](#format)
    - [Lint](#lint)
  - [Document](#document)
    - [API Document](#api-document)
    - [CHANGELOG](#changelog)
  - [Clean](#clean)
- [Misc](#misc)
- [Notes](#notes)
  - [LICENSE](#license)
  - [Contributors](#contributors)

## Prerequisites

- [Python](https://www.python.org) (Version 3.10 or higher)
  - Production Dependencies
    - (T. B. D.)
  - Development Dependencies
    - [black](https://github.com/psf/black) as *Python Formatter*
    - [flake8](https://pypi.org/project/flake8/) as *Python Code Linter*
    - [Sphinx](https://www.sphinx-doc.org/) as *Python Document Generator*
    - [loguru](https://github.com/Delgan/loguru) as *Application Logger*
- [Lefthook](https://github.com/evilmartians/lefthook) as *Git Hooks Manager*
- [git-secret](https://git-secret.io/) as *Secret File Manager*
- [direnv](https://direnv.net) as *`.env` Loader*

## How to

```shell
$ make help
default              常用
init                 初期
install              導入
start                起動
open                 閲覧
format               整形
lint                 検証
doc                  文書
sphinx               文書
clean                掃除
help                 助言
```

### First time preparation

#### Init

To install some development commands, run below.

```shell
make init
```

After that, all actions must be taken in a venv environment.

```shell
source venv/bin/activate
```

Install dependencies,

```shell
pip install --upgrade pip && pip install -r requirements.txt
```

#### Setup Git Hooks (Lefthook)

To install [Lefthook](https://github.com/evilmartians/lefthook) via [Homebrew](https://brew.sh), `brew install lefthook`.

```shell
lefthook install
```

Thereafter, each commit will validate by `make format` and `make lint`, and each push will validate by `make test` and [secretlint](https://github.com/secretlint/secretlint).

### Develop

Commands that are often used during development should be prepared in `default`.

```shell
make
```

#### Start

If it succeeds, [http.server](https://docs.python.org/3/library/http.server.html) will start waiting on `http://0.0.0.0:8000/`.
To check this address, run below.

```shell
make open
```

#### Format

To format Python source codes using [Black](https://github.com/psf/black) manually, run below.

```shell
make format
```

#### Lint

To lint Python source codes using [flake8](https://pypi.org/project/flake8/) manually, run below.

```shell
make lint
```

### Document

#### API Document

When the main branch is updated, `pages.yml` will update the [API Document](https://shin-sforzando.github.io/etude-ChArUco/).

To generate API Documents using [Sphinx](https://www.sphinx-doc.org/) manually, run below.

```shell
make doc
```

#### CHANGELOG

To install [git-cliff](https://github.com/orhun/git-cliff) via [Homebrew](https://brew.sh) manually, `brew install git-cliff`.

To update `CHANGELOG.md` manually, run [git-cliff](https://github.com/orhun/git-cliff) like below.

```shell
git cliff --output CHANGELOG.md
```

### Clean

To clean up miscellaneous files, run below.

```shell
make clean
```

## Misc

## Notes

This repository is [Commitizen](https://commitizen.github.io/cz-cli/) friendly, following [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow).
See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

### LICENSE

See [LICENSE](LICENSE).

### Contributors

- [sforzando LLC. and Inc.](https://sforzando.co.jp/)
  - [Shin'ichiro Suzuki](https://github.com/shin-sforzando)
