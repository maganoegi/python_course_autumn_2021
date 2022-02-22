
import abc

class InstallationStrategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def execute(cls):
        """ abstract method definingthe rules for the installation bla bvla """


class DmgInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls):
        """ abstract method definingthe rules for the installation bla bvla """
        print("opening up the dmg")

class PkgInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls):
        """ abstract method definingthe rules for the installation bla bvla """
        print("opening up the pkg")


class TarInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls):
        """ abstract method definingthe rules for the installation bla bvla """
        print("opening up the tar")


class BzipInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls):
        """ abstract method definingthe rules for the installation bla bvla """
        print("opening up the bzip")


NAME_STRATEGY_MAPPING = {
    ".dmg" : DmgInstallationStrategy,
    ".pkg" : PkgInstallationStrategy,
    ".tar" : TarInstallationStrategy,
    ".bzip" : BzipInstallationStrategy,
}


def install_download_app(soft_path: str, strategy: InstallationStrategy):
    strategy.execute()


if __name__ == '__main__':
    # on cherche a isoler notre extension bla bla 
    extension = ".pkg"
    strategy = NAME_STRATEGY_MAPPING[extension]

    install_download_app("blabla/blibli", strategy)

