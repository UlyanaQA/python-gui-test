from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.group_cache = []
            self.open_group_editor()
            tree = self.group_editor.window(auto_id="uxAddressTreeView")
            root = tree.tree_root()
            for node in root.children():
                name = node.text()
                self.group_cache.append(Group(name=name))
            self.close_group_editor()
        return list(self.group_cache)

    def add_new(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys("\n")
        self.close_group_editor()
        self.group_cache = None

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def del_group_by_index(self, index):
        self.open_group_editor()
        self.select_group_by_index(index)
        self.open_group_deletion()
        self.group_deletion.window(auto_id="uxDeleteAllRadioButton").click()
        self.group_deletion.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()
        self.group_cache = None

    def select_group_by_index(self, index):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.children()[index].select()

    def open_group_deletion(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_deletion = self.app.application.window(title="Delete group")