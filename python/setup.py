import sys

import setuptools

__version__ = '0.0.0'
__title__ = 'gh-secrets-action'
__author__ = 'Tomasz Trębski'
__author_email__ = 'kornicameister@gmail.com'
__maintainer__ = __author__
__url__ = 'https://github.com/kornicameister/gh-secrets-action'
__min_python__ = (3, 8)

if sys.version_info < __min_python__:
    raise RuntimeError(
        f'{__title__}:{__version__} requires Python 3.8 or newer',
    )

setuptools.setup(
    setup_requires='setupmeta',
    python_requires=f'>={".".join(map(str, __min_python__))}',
    versioning='post',
    zip_safe=False,
)
