from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.api.shared.event import KeywordQueryEvent

ENTRIES = [
    {
        "icon": "images/lock.png",
        "name": "Lock",
        "id": "lock"
    },
    {
        "icon": "images/logout.png",
        "name": "Logout",
        "id": "logout"
    },
    {
        "icon": "images/reboot.png",
        "name": "Reboot",
        "id": "reboot"
    },
    {
        "icon": "images/shutdown.png",
        "name": "Shutdown",
        "id": "shutdown"
    }
]

class Terminal_Runner(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()

        options = []
        for entry in ENTRIES:
            if not query or query.upper() in entry["name"].upper():
                options.append(ExtensionResultItem(icon=entry["icon"], name=entry["name"],
                    on_enter=RunScriptAction(extension.preferences[entry["id"]])))

        return RenderResultListAction(options)


if __name__ == '__main__':
    Terminal_Runner().run()
