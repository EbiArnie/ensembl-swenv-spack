# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestWeaken(PerlPackage):
    """Test that freed memory objects were, indeed, freed"""

    homepage = "https://metacpan.org/pod/Test::Weaken"
    url = "https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Test-Weaken-3.022000.tar.gz"

    maintainers("EbiArnie")

    version("3.022000", sha256="2631a87121310262e0e96107a6fa0ed69487b7701520773bee5fa9accc295f5b")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
