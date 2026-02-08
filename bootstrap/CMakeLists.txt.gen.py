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

cmake_minimum_required(VERSION 3.15)
project("%{project_name_kebab}" LANGUAGES C CXX)

enable_testing()

find_package(range-v3 REQUIRED)
find_package(Boost COMPONENTS unit_test_framework REQUIRED)

message("== Building with CMake version: ${CMAKE_VERSION}")

add_executable(${PROJECT_NAME} src/main.cpp)

add_executable(${PROJECT_NAME}.test src/main.test.cpp)
target_link_libraries(${PROJECT_NAME}.test PRIVATE Boost::unit_test_framework)
add_test(NAME ${PROJECT_NAME}.test COMMAND ${PROJECT_NAME}.test)

add_executable(${PROJECT_NAME}.perf src/main.perf.cpp)
target_link_libraries(${PROJECT_NAME}.perf range-v3::range-v3)
"""


def generate(ctx: Context) -> str:
    project_name = ctx.template_config.project_name

    return PercentTemplate(template_str).substitute(
        {
            "project_name_kebab": kebab_case(project_name),
        },
    )
