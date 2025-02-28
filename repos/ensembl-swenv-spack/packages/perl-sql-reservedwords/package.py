# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSqlReservedwords(PerlPackage):
    """Reserved SQL words by ANSI/ISO"""

    homepage = "https://metacpan.org/pod/SQL::ReservedWords"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/SQL-ReservedWords-0.8.tar.gz"

    maintainers("EbiArnie")

    version("0.8", sha256="09f4aecf1bd8efdd3f9b39f16a240c4e9ceb61eb295b88145c96eb9d58504a2a")

    depends_on("perl-sub-exporter", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
