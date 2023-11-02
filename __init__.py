# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class XyzPositionPlugin(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.SimpleApiPlugin):

    def on_after_startup(self):
        self._logger.info("XYZPosition plugin started!")

    def get_api_commands(self):
        return dict(
            get_position=[]
        )

    def on_api_command(self, command, data):
        import flask
        if command == "get_position":
            # Assuming the printer firmware supports M114
            self._printer.commands("M114")
            # We'll need to catch the position from the printer's response
            # This part requires further elaboration depending on the printer's firmware
            position = self._printer.get_current_position()
            return flask.jsonify(position)

__plugin_name__ = "XYZ Position"
__plugin_implementation__ = XyzPositionPlugin()
