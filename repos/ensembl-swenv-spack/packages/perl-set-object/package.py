# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSetObject(PerlPackage):
    """Unordered collections (sets) of Perl Objects"""

    homepage = "https://metacpan.org/pod/Set::Object"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Set-Object-1.42.tar.gz"

    maintainers("EbiArnie")

    version("1.42", sha256="d18c5a8a233eabbd0206cf3da5b00fcdd7b37febf12a93dcc3d1c026e6fdec45")


    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
