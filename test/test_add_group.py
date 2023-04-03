from model.group import Group


def test_add_group(app, xlxs_groups):
    old_groups = app.groups.get_group_list()
    group = xlxs_groups
    app.groups.add_new(group)
    new_groups = app.groups.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.name) == sorted(new_groups, key=Group.name)