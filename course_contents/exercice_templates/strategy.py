import abc



# strategy pour "contrat d'utilisation"
# plusieurs strategies de langage de prog
    # argument: for loop
class TranslationStrategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def translate(cls) -> str:
        """blabla"""


class ToEnglishStrategy( TranslationStrategy ):
    @classmethod
    def translate(cls) -> str:
        return "My name is "


class ToFrenchStrategy( TranslationStrategy ):
    @classmethod
    def translate(cls) -> str:
        return "Je m'appelle "


class LanguageTranslator:
    def __init__(self, translation_strategy: TranslationStrategy) -> None:
        self._compiling_strategy = translation_strategy

    @property
    def translation_strategy(self) -> TranslationStrategy:
        return self._compiling_strategy

    def compile(self) -> str:
        return self.translation_strategy.translate()


def main() -> None:
    translation_strategy = ToEnglishStrategy
    # translation_strategy = ToFrenchStrategy

    compiler = LanguageTranslator(translation_strategy)
    compiled_code = compiler.compile()

    print(compiled_code)

if __name__ == '__main__':
    main()