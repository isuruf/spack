import subprocess
from spack.architecture import Platform, Target
from spack.operating_systems.mac_os import MacOs


class Darwin(Platform):
    priority    = 89
    front_end   = 'x86_64'
    back_end    = 'x86_64'
    default     = 'x86_64'

    def __init__(self):
        super(Darwin, self).__init__('darwin')
        self.add_target(self.default, Target(self.default))
        mac_os = MacOs()

        self.default_os = str(mac_os)
        self.front_os   = str(mac_os)
        self.back_os    = str(mac_os)

        self.add_operating_system(str(mac_os), mac_os)

    @classmethod
    def detect(self):
        platform = subprocess.Popen(['uname', '-a'], stdout=subprocess.PIPE)
        platform, _ = platform.communicate()
        return 'darwin' in platform.strip().lower()
