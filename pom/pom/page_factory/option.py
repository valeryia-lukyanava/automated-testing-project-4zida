from pom.page_factory.component import Component


class Option(Component):
    @property
    def type_of(self) -> str:
        return 'option'
