class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n - " + ( "\n - ".join(dependencies) \
                if len(dependencies) > 0 \
                else "-" ) + "\n"

    def __str__(self):
        dep = self._stringify_dependencies(self.dependencies)
        dev = self._stringify_dependencies(self.dev_dependencies)
        aut = self._stringify_dependencies(self.authors)
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: {aut}"
            f"\nDependencies: {dep}"
            f"\nDevelopment dependencies: {dev}"
        )
