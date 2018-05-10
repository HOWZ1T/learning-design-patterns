from DI_IoC.injector import inject


@inject('time')
def test_module_import(module):
    if module is None:
        print("could not import check console for error :(")
    else:
        print("print module {} successfully imported".format(module))


@inject('time', 'sleep')
def sleep(function):
    if function is None:
        print("could not import function! check console for error :(")
    else:
        print("taking a quick nap...")
        function(1)  # sleep for 1 second
        print("what a nice nap :)")


@inject('time', 'altzone')
def print_module_variable(variable):
    if variable is None:
        print("could not import variable! check console for error :(")
    else:
        print("altzone: {}".format(variable))


test_module_import()
sleep()
print_module_variable()