# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestBase(PerlPackage):
    """A Data Driven Testing Framework"""

    homepage = "https://metacpan.org/pod/Test::Base"
    url = "https://cpan.metacpan.org/authors/id/I/IN/INGY/Test-Base-0.89.tar.gz"

    maintainers("EbiArnie")

    version("0.89", sha256="2794a1aaaeb1d3a287dd2c7286258663796562f7db9ccc6b424bc4f1de8ad014")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))
    depends_on("perl-algorithm-diff@1.15:", type=("test"))
    depends_on("perl-spiffy@0.40:", type=("run"))
    depends_on("perl-text-diff@0.35:", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
