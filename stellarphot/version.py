version = "unknown.dev"
try:
    from importlib_metadata import version as _version, PackageNotFoundError

    version = _version("my-package")
except ImportError:
    from pkg_resources import get_distribution, DistributionNotFound

    try:
        version = get_distribution("my-package").version
    except DistributionNotFound:
        pass
except PackageNotFoundError:
    pass
