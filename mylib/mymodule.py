"""My module for documentation tests

This module does things that are described here.

"""


def about_me(your_name):
    """Return the most important thing about a person.

    Args:
        your_name: A string indicating the name of the person.
    Returns:
        The return value. True for success, False otherwise.

    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """Blah blah blah.

        Args:
            name: A string to assign to the `name` instance attribute.

        """
        self.name = name

    def about_self(self):
        """Return information about an instance created from ExampleClass."""
        return "I am a very smart {} object.".format(self.name)
