from fixture import group
from model.group import Group
import random


def test_del_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new(Group(name="Temp_group"))
    old_groups = app.groups.get_group_list()
    index = random.choice(range(len(old_groups)))
    app.groups.del_group_by_index(index)
    new_groups = app.groups.get_group_list()
    old_groups.pop(index)
    assert sorted(old_groups, key=Group.name) == sorted(new_groups, key=Group.name)
