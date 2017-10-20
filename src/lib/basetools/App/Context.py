class ContextFileNameError(Exception):
    """Context File Name error."""

    pass

class Context(object):
    """
    Abc about the current context of the application.
    """

    @classmethod
    def fileName(cls):
        """
        Return a string about current file path of the opened file.

        In case the file is not saved, then raise the exception ContextFileNameError.
        """
        raise NotImplementedError

    @classmethod
    def isEmpty(cls):
        """
        Return a boolean telling if the scene has never been saved.
        """
        raise NotImplementedError

    @classmethod
    def hasModification(cls):
        """
        Return a boolean telling if the scene has modifications.

        This is used to decide if the scene needs to be saved.
        """
        raise NotImplementedError

    @classmethod
    def hasGUI(cls):
        """
        Return a boolean telling if application is running with through GUI.
        """
        raise NotImplementedError
