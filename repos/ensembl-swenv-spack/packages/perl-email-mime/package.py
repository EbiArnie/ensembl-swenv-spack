# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlEmailMime(PerlPackage):
    """Easy MIME message handling"""

    homepage = "https://metacpan.org/pod/Email::MIME"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MIME-1.953.tar.gz"

    maintainers("EbiArnie")

    version("1.953", sha256="98fb067850699a224babc348f1cefe30d744c60da8902e7a5ce9d8b7e73df735")

    depends_on("perl@5.12.0:", type=("build", "link", "run", "test"))
    depends_on("perl-email-address-xs", type=("run"))
    depends_on("perl-email-messageid", type=("run"))
    depends_on("perl-email-mime-contenttype@1.023:", type=("run"))
    depends_on("perl-email-mime-encodings@1.314:", type=("run"))
    depends_on("perl-email-simple@2.212:", type=("run"))
    depends_on("perl-mime-types@1.13:", type=("run"))
    depends_on("perl-module-runtime", type=("run"))
