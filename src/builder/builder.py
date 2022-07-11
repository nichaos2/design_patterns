# Builder is used to facilitate the complicated construction procedure of an object, like an html elementn chain
# First we need the algorithm to create the object like the HtmlElement
# Then the builder adds the elements side by side to create the final object
# A detail is that we can add a fluent creation
# Finally, the first object can implement a method to call the Builder itself, thus avoiding creating the build ourselves


from re import M


class HtmlElement:

    indent_size = 4

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    # method to return a nice html format
    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        # 0 is the indent
        return self.__str(0)

    @staticmethod
    def create(name):
        """
        creates a builder for the class
        """
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)

# TEST

def build_without_builder():
    # if you want to build a simple HTML paragraph using a list
    hello = "hello"
    parts = ["<p>", hello, "</p>"]
    print("".join(parts))

    # now I want an HTML list with 2 words in it
    words = ["hello", "world"]
    parts = ["<ul>"]
    for w in words:
        parts.append(f"  <li>{w}</li>")
    parts.append("</ul>")
    print("\n".join(parts))


def build_with_builder(builder):
    # ordinary non-fluent builder
    # builder = HtmlBuilder('ul')
    # builder = HtmlElement.create("ul")
    builder.add_child("li", "hello")
    builder.add_child("li", "world")
    print("Ordinary builder:")
    print(builder)

def build_with_builder_fluent(builder):
    # fluent builder
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print("Fluent builder:")
    print(builder)


if __name__ == "__main__":

    builder = HtmlBuilder("ul")
    # ==> or create a builder from the HtmlElement
    # builder = HtmlElement.create("ul")

    #
    build_without_builder()
    print("*" * 80)
    #
    build_with_builder(builder)
    print("*" * 80)
    #
    builder.clear() # builder has already children from the previous call
    build_with_builder_fluent(builder)
    print("*" * 80)
