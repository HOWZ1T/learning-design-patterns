from DI_IoC.exceptions import InjectionKeyError


def inject(module=None, attrib=None):
    '''
    inject: provides module injection at the function scope via function decoration.

    :param (string) module:
    :param (string) attrib:

    :raises InjectionKeyError:

    Examples:
        >>>@inject('time')
        >>>def test_module_import(module):
        >>>    if module is None:
        >>>        print("could not import check console for error :(")
        >>>    else:
        >>>        print("print module {} successfully imported".format(module))


        >>>@inject('time', 'sleep')
        >>>def sleep(function):
        >>>    if function is None:
        >>>        print("could not import function! check console for error :(")
        >>>    else:
        >>>        print("taking a quick nap...")
        >>>        function(1)  # sleep for 1 second
        >>>       print("what a nice nap :)")


        >>>@inject('time', 'altzone')
        >>>def print_module_variable(variable):
        >>>    if variable is None:
        >>>        print("could not import variable! check console for error :(")
        >>>    else:
        >>>        print("altzone: {}".format(variable))
    '''

    if module is None:
        raise InjectionKeyError("injection missing key: module!")

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            try:
                mod = __import__(module)
                if attrib is not None:
                    mod = getattr(mod, attrib)
            except ImportError as e:
                print("[ inject ] could not inject module: {} with attribute: {} as:\n{}".format(module, attrib, e))

            res = func(mod, *args, **kwargs)
            return res
        return inner_wrapper
    return wrapper
