# Hey Emacs, this is -*- coding: utf-8 -*-

from string import Template
from typing import TYPE_CHECKING, ClassVar

from autocodegen.utils import kebab_case

if TYPE_CHECKING:
    from autocodegen import Context


class PercentTemplate(Template):  # noqa: D101
    delimiter: ClassVar[str] = "%"


template_str = """\
# Hey Emacs, this is -*- coding: utf-8 -*-

# shellcheck disable=2034

readonly PROJECT_NAME="%{project_name_kebab}"

readonly COMPILER=clang
readonly COMPILER_VERSION=20
readonly COMPILER_VERSION_SUFFIX=
readonly CLANG_CHECK_VERSION_SUFFIX=
readonly CLANG_TIDY_VERSION_SUFFIX=
# readonly COMPILER_VERSION_SUFFIX=-16
# readonly CLANG_CHECK_VERSION_SUFFIX=-17
# readonly CLANG_TIDY_VERSION_SUFFIX=-17

PRJ_ROOT_PATH="${SDPATH}/.."
PRJ_ROOT_PATH="$(cd "${PRJ_ROOT_PATH}" && pwd)"
readonly PRJ_ROOT_PATH

readonly BLD_DIR_NAME="build"
readonly BLD_PATH="${PRJ_ROOT_PATH}/${BLD_DIR_NAME}"
"""


def generate(ctx: Context) -> str:
    project_name = ctx.template_config.project_name

    return PercentTemplate(template_str).substitute(
        {
            "project_name_kebab": kebab_case(project_name),
        },
    )
