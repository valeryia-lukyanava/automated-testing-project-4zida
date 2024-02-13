from pom.page_factory.component import Component


class Select(Component):
    @property
    def type_of(self) -> str:
        return 'select'
