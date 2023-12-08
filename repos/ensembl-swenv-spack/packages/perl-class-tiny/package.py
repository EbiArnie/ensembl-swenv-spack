# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClassTiny(PerlPackage):
    """Minimalist class construction"""

    homepage = "https://metacpan.org/pod/Class::Tiny"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-1.008.tar.gz"

    maintainers("EbiArnie")

    version("1.008", sha256="ee058a63912fa1fcb9a72498f56ca421a2056dc7f9f4b67837446d6421815615")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args