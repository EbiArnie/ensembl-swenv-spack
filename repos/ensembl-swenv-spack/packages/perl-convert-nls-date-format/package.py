# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlConvertNlsDateFormat(PerlPackage):
    """Convert Oracle NLS_DATE_FORMAT <-> strftime Format Strings"""

    homepage = "https://metacpan.org/pod/Convert::NLS_DATE_FORMAT"
    url = "https://cpan.metacpan.org/authors/id/K/KO/KOLIBRIE/Convert-NLS_DATE_FORMAT-0.06.tar.gz"

    maintainers("EbiArnie")

    version("0.06", sha256="20ab8070c56377bd302c9ec5a16873714026d03e56a31cf70ab65632c1ed5bc7")

    depends_on("perl@5.6.1:", type=("build", "link", "run", "test"))
    depends_on("perl-module-build-tiny@0.035:", type=("build"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
