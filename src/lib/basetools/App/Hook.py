from .Context import Context

class HookNotRegisteredError(Exception):
    """Hook not registered error."""

    pass

class Hook(object):
    """
    Abc to hook application events.

    When implementing in derived classes, make sure the derived classes are
    still calling the methods from base class. This is going to be used
    to collect statistics, for instance how long a scene is taking
    to get loaded or saved...
    """

    __registeredHooks = {}
    __singletonHooks = {}

    def __init__(self, context):
        """
        Create a hook object (Please use "to" to get the hook instance).
        """
        self.__setContext(context)
        self.startup()

    def startup(self):
        """
        Perform startup routines.
        """
        pass

    def shutdown(self):
        """
        Perform shutdown routines.
        """
        pass

    def beforeOpenFile(self):
        """
        Perform routines before opening a file.
        """
        pass

    def afterOpenFile(self):
        """
        Perform routines after the file has been opened.
        """
        pass

    def beforeFileSave(self):
        """
        Perform routines before the file gets saved.
        """
        pass

    def afterFileSave(self):
        """
        Perform routines after a file has been saved.
        """
        pass

    def context(self):
        """
        Return the context that should be used by the hook.
        """
        return self.__context

    @staticmethod
    def to(name):
        """
        Return a singleton instance of a registered hook name.

        In case the hook name is not registered than the exception:
        "HookNotRegisteredError" is raised.
        """
        # factorying a hook when needed
        if name not in Hook.__singletonHooks and name in Hook.__registeredHooks:
            hookClass, contextClass = Hook.__registeredHooks[name]
            Hook.__singletonHooks[name] = hookClass(contextClass)

        # returning hook singleton instance
        if name in Hook.__singletonHooks:
            return Hook.__singletonHooks[name]
        else:
            raise HookNotRegisteredError(
                "hook is not registered: {0}".format(name)
            )

    @staticmethod
    def registeredNames():
        """
        Return a list of registered hook names.
        """
        return Hook.__registeredHooks.keys()

    @staticmethod
    def register(name, hookClass, contextClass):
        """
        Register a hook.
        """
        assert(issubclass(hookClass, Hook))
        assert(issubclass(contextClass, Context))

        Hook.__registeredHooks[name] = (hookClass, contextClass)

        # in case of overriding a hook
        if name in Hook.__singletonHooks:
            del Hook.__singletonHooks[name]

    def __setContext(self, contextClass):
        """
        Set the context that should be used by the hook.
        """
        assert(issubclass(contextClass, Context))

        self.__context = contextClass
