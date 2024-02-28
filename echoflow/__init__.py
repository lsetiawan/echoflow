from pkg_resources import DistributionNotFound, get_distribution

from . import echoflow_cli
from .models.datastore import StorageType
from .stages.echoflow import (echoflow_config_AWS,
                                       echoflow_config_AZ_cosmos,
                                       echoflow_create_prefect_profile,
                                       echoflow_start, get_active_profile,
                                       load_profile)
from .utils.config_utils import extract_fs, glob_url, load_block
from .utils.file_utils import get_ed_list, get_last_run_output, get_zarr_list
from .stages.docker_trigger import docker_trigger

try:
    VERSION = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    try:
        from .version import version as VERSION  # noqa
    except ImportError:  # pragma: no cover
        raise ImportError(
            "Failed to find (autogenerated) version.py. "
            "This might be because you are installing from GitHub's tarballs, "
            "use the PyPI ones."
        )
__version__ = VERSION

__all__ = [
    "echoflow_start",
    "echoflow_create_prefect_profile",
    "load_profile",
    "echoflow_config_AWS",
    "echoflow_config_AZ_cosmos",
    "get_active_profile",
    "StorageType",
    "load_block",
    "echoflow_cli",
    "extract_fs", 
    "glob_url",
    "get_last_run_output",
    "get_ed_list", 
    "get_zarr_list",
    "docker_trigger"
]
