from behave import given, when, then, model


@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])


@when(u'we count the number of people in each department')
def step_impl(context):
    pass


@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    pass


@then(u'we will find one person in "Beer Cans"')
def step_impl(context):
    pass
