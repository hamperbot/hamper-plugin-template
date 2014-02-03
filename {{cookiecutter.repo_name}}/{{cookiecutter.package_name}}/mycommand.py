from hamper.interfaces import ChatCommandPlugin, Command


class MyPlugin(ChatCommandPlugin):
    name = 'myplugin'

    class TestCommand(Command):
        regex = 'test (.*)'

        def command(self, bot, comm, groups):
            they_said = groups[0]
            bot.reply(comm, 'You said "{0}"!'.format(they_said))


myplugin = MyPlugin()
