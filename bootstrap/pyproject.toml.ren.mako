## Hey Emacs, this is -*- coding: utf-8 -*-
<%
  project_name = utils.kebab_case(config["project_name"])
%>\
[tool.poetry]
name = "${project_name}"
version = "0.1.0"
description = ""
authors = ["ramblehead <rh@gmail.com>"]
readme = "README.md"
packages = [{ include = "poetry_utils", from = "utils" }]

[tool.poetry.scripts]
lint = "poetry_utils.scripts:lint"
cdaq-link = "cdaq_link.start:start"

[tool.poetry.dependencies]
python = ">=3.11,<3.15"
conan = "^2.24.0"
numpy = "^2.4.1"

[tool.poetry.group.dev.dependencies]
black = "^25.12.0"
basedpyright = "^1.37.1"
ruff = "^0.14.11"
mypy = "^1.19.1"
ruff-lsp = "^0.0.62"

[tool.ruff]
select = ["ALL"]

ignore = [
  # No need
  "DJ",    # flake8-django
  "UP009", # UTF-8 encoding declaration is unnecessary
  # subprocess call with shell=True seems safe, but
  # may be changed in the future; consider rewriting without shell
  "S602",
  "S607", # Starting a process with a partial executable path

  # Should be enabled later when project is more mature
  "D", # pydocstyle

  # Should be enabled for releases
  "ERA001", # eradicate (e.g. comments)
  "T20",    # flake8-print
]

line-length = 110

extend-exclude = [
  "**/__pycache__",
  "**/.*",
]

[tool.black]
line-length = 79

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
