# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlNamespaceAutoclean(PerlPackage):
    """Keep imports out of your namespace"""

    homepage = "https://metacpan.org/pod/namespace::autoclean"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/namespace-autoclean-0.29.tar.gz"

    maintainers("EbiArnie")

    version("0.29", sha256="45ebd8e64a54a86f88d8e01ae55212967c8aa8fed57e814085def7608ac65804")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-b-hooks-endofscope@0.12:", type=("run"))
    depends_on("perl-namespace-clean@0.20:", type=("run"))
    depends_on("perl-sub-identify", type=("run"))
    depends_on("perl-test-needs", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
