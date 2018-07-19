from __future__ import print_function
import os
import sys
import shutil
import tarfile
import urllib.parse as urlparse
from contextlib import contextmanager
from pathlib import Path
from subprocess import check_call
from tempfile import TemporaryDirectory as tempdir
from conda.exports import download, hashsum_file
import yaml 

config = {}
versions = ["9.2"]
for v in versions:
    config[v] = {"linux": {}, "windows": {}, "osx": {}}


cu_92 = config["9.2"]
cu_92["base_url"] = "https://developer.nvidia.com/compute/cuda/9.2/Prod2/"
cu_92["installers_url_ext"] = "local_installers/"
cu_92["patch_url_ext"] = ""
cu_92["md5_url"] = "http://developer.download.nvidia.com/compute/cuda/9.2/Prod2/docs/sidebar/md5sum.txt"

cu_92['libdevice_versions'] = ['10']

cu_92['linux'] = {'blob': 'cuda_9.2.148_396.37_linux',
                 'patches': [],
                 # need globs to handle symlinks
                 'cuda_lib_fmt': 'lib{0}.so*',
                 'nvtoolsext_fmt': 'lib{0}.so*',
                 'nvvm_lib_fmt': 'lib{0}.so*',
                 'libdevice_lib_fmt': 'libdevice.{0}.bc'
                 }

cu_92['windows'] = {'blob': 'cuda_9.2.148_windows',
                   'patches': [],
                   'cuda_lib_fmt': '{0}64_91.dll',
                   'nvtoolsext_fmt': '{0}64_1.dll',
                   'nvvm_lib_fmt': '{0}64_32_0.dll',
                   'libdevice_lib_fmt': 'libdevice.{0}.bc',
                   'NvToolsExtPath' :
                       os.path.join('c:' + os.sep, 'Program Files',
                                    'NVIDIA Corporation', 'NVToolsExt', 'bin')
                   }

cu_92['osx'] = {'blob': 'cuda_9.2.148_mac',
               'patches': [],
               'cuda_lib_fmt': 'lib{0}.9.1.dylib',
               'nvtoolsext_fmt': 'lib{0}.1.dylib',
               'nvvm_lib_fmt': 'lib{0}.3.2.0.dylib',
               'libdevice_lib_fmt': 'libdevice.{0}.bc'
               }

class Extractor(object):
    """Extractor base class, platform specific extractors should inherit
    from this class.
    """
    libdir = {'linux': 'lib',
              'osx': 'lib',
              'windows': 'DLLs', }

    def __init__(self, version, ver_config, platform_config):
        """Initialise an instance:
        Arguments:
          version - CUDA version string
          ver_config - the configuration for this CUDA version
          platform_config - the configuration for this platform
        """

        self.cu_version = version
        self.md5_url = ver_config["md5_url"]
        self.base_url = ver_config["base_url"]
        self.patch_url_text = ver_config["patch_url_ext"]
        self.installers_url_ext = ver_config["installers_url_ext"]
        self.cu_blob = platform_config['blob']
        self.config = {"version": version, **ver_config}
        self.conda_prefix = os.environ.get('CONDA_PREFIX')
        self.prefix = os.environ["PREFIX"]
        self.src_dir = Path(self.conda_prefix) / 'pkgs' / 'cudatoolkit-dev'
        self.extractdir = self.src_dir / 'extracted'
        try:
            os.makedirs(self.extractdir)

        except FileExistsError:
            pass

        self.output_dir = os.path.join(self.prefix, self.libdir[getplatform()])
        self.symlinks = getplatform() == "linux"
        self.debug_install_path = os.environ.get('DEBUG_INSTALLER_PATH')

    def download_blobs(self):
        """Downloads the binary blobs to the $SRC_DIR
        """
        dl_url = urlparse.urljoin(self.base_url, self.installers_url_ext)
        dl_url = urlparse.urljoin(dl_url, self.cu_blob)
        dl_path = os.path.join(self.src_dir, self.cu_blob)
        if not self.debug_install_path:
            print("downloading %s to %s" % (dl_url, dl_path))
            download(dl_url, dl_path)

        else:
            existing_file = os.path.join(self.debug_install_path, self.cu_blob)
            print("DEBUG: copying %s to %s" % (existing_file, dl_path))
            shutil.copy(existing_file, dl_path)

    def check_md5(self):
        """Checks the md5sums of the downloaded binaries
        """
        md5file = self.md5_url.split("/")[-1]
        path = os.path.join(self.src_dir, md5file)
        download(self.md5_url, path)

        # compute hash of blob
        blob_path = os.path.join(self.src_dir, self.cu_blob)
        md5sum = hashsum_file(blob_path, 'md5')

        # get checksums
        with open(path, 'r') as f:
            checksums = [x.strip().split() for x in f.read().splitlines() if x]

        # check md5 and filename match up
        check_dict = {x[0]: x[1] for x in checksums}
        assert check_dict[md5sum].startswith(self.cu_blob[:-7])
      
    def copy(self, *args):
        """The method to copy extracted files into the conda package platform
        specific directory. Platform specific extractors must implement.
        """
        raise RuntimeError("Must implement")

    def extract(self, *args):
        """The method to extract files from the cuda binary blobs.
        Platform specific extractors must implement.
        """
        raise RuntimeError("Must implement")

    def get_paths(self):
        print("Getting paths..............")

    def copy_files(self):
        print("Copying files............")

    def dump_config(self):

        """Dumps the config dictionary into the output directory
        """

        dumpfile = os.path.join(self.conda_prefix, 'cudatoolkit-dev_config.yaml')
        with open(dumpfile, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)


class WindowsExtractor(Extractor):
    """The windows extractor
    """

    def copy(self, *args):
        print("This is Windows Extractor Copy function...............")

    def extract(self):
        print("Extracting on Windows.....")
        runfile = os.path.join(self.src_dir, self.cu_blob)
        print("HELLLLLLLLLO", os.listdir(self.src_dir),
              os.listdir(self.extractdir))
        cmd = ['7za', 'x', '-o%s' %
               str(self.extractdir), runfile]
        check_call(cmd)
        self.copy()


class LinuxExtractor(Extractor):
    """The Linux Extractor
    """

    def copy(self, *args):
        print("This is Linux Extractor Copy function ..............")

    def extract(self):
        print("Extracting on Linux")
        runfile = os.path.join(self.src_dir, self.cu_blob)
        print("HELLLLLLLLLO", os.listdir(self.src_dir),
              os.listdir(self.extractdir))
        os.chmod(runfile, 0o777)
        cmd = ["bash", runfile,
               '--toolkitpath', str(self.extractdir), '--toolkit',
               '--silent', '--override']
        check_call(cmd)
        self.copy()


class OsxExtractor(Extractor):
    """The Osx Extractor
    """

    pass


def getplatform():
    plt = sys.platform
    if plt.startswith("linux"):
        return "linux"
    elif plt.startswith("win"):
        return "windows"
    elif plt.startswith("darwin"):
        return "osx"
    else:
        raise RuntimeError("Unknown platform")


dispatcher = {
    "linux": LinuxExtractor,
    "windows": WindowsExtractor,
    "osx": OsxExtractor, }


def _main():
    print("Running Post installation")

    # package version decl must match cuda release version 
    cu_version = "9.2"

    # get an extractor 
    plat = getplatform()
    extractor_impl = dispatcher[plat]
    version_cfg = config[cu_version]
    extractor = extractor_impl(cu_version, version_cfg, version_cfg[plat])

    # download binaries 
    extractor.download_blobs()

    # check md5sum 
    extractor.check_md5()

    # Extract 
    extractor.extract()

    # Dump config 
    extractor.dump_config()


if __name__ == "__main__":
    _main()
