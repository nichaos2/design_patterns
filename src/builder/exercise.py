class CodeBuilder:
    """create str with class name and init method"""
    __elements = []
    __indent = 4
    def __init__(self, root_name):
        self.root_name = root_name

    def add_field(self, type, name):
        indent = " " * (self.__indent*2)
        self.__elements.append(f"{indent}self.{type} = {name}")
        return self

    def __str__(self):
        class_str = f"class {self.root_name}:"
        init_str = "def __init__(self):"
        all_str = class_str + "\n"+ \
                  " " * self.__indent + init_str + "\n" +\
                  "\n".join(self.__elements)
        return all_str

# but we need actually to create a class that can create a Class and Field
class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('    %s' % f)
        return '\n'.join(lines)

class CodeBuilderSolution:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
print(cb)


cbs = CodeBuilderSolution("Person").add_field("name", '""').add_field("age", "0")
print(cbs)