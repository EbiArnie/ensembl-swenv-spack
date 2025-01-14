# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSafeIsa(PerlPackage):
    """Call isa, can, does and DOES safely on things that may not be objects"""

    homepage = "https://metacpan.org/pod/Safe::Isa"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Safe-Isa-1.000010.tar.gz"

    maintainers("EbiArnie")

    version("1.000010", sha256="87f4148aa0ff1d5e652723322eab7dafa3801c967d6f91ac9147a3c467b8a66a")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
