## Hey Emacs, this is -*- coding: utf-8 -*-

from string import Template
from typing import TYPE_CHECKING

from autocodegen.utils import kebab_case

if TYPE_CHECKING:
    from autocodegen import Context

template_str = """\
// Hey Emacs, this is -*- coding: utf-8 -*-

// NOLINTBEGIN(misc-include-cleaner)

#include "main.hpp"
#include <boost/test/tools/old/interface.hpp>

#define BOOST_TEST_MODULE ${project_name_kebab}
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_CASE(binary_gap) {
  // BOOST_REQUIRE_EQUAL(solution(42), 42);
  // BOOST_REQUIRE_NE(solution(42), 43);
}

// NOLINTEND(misc-include-cleaner)

// #include <cassert>
// #include <concepts/concepts.hpp>
// #include <iostream>

// auto main(int /*argc*/, char* /*argv*/[]) -> int {
//   assert(warp() == 42);

//   std::cout << "Tests passed!" << std::endl;

//   return EXIT_SUCCESS;
// }
"""


def generate(ctx: Context) -> str:
    project_name = ctx.template_config.project_name

    return Template(template_str).substitute(
        {
            "project_name_kebab": kebab_case(project_name),
        },
    )
