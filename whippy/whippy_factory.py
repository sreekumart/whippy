from whippy.whippy_command import WhippyCommand


class WhippyFactory:

    _factory_objects = dict()

    @staticmethod
    def get_command(group_name: str, command_config=None) -> WhippyCommand:
        if WhippyFactory._factory_objects.get(group_name):
            return WhippyFactory._factory_objects[group_name]
        else:
            WhippyFactory._factory_objects[group_name] = WhippyCommand(command_config)

        return WhippyFactory._factory_objects[group_name]

    @staticmethod
    def create_decorator(whippy_command, method):
        return whippy_command.execute(method)






