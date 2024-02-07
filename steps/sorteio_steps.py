from behave import given, when, then
from time import sleep
from random import randint
from nose.tools import assert_equal


@given(u'que acesso o programa')
def step_impl(context):
    pass


@when(u'sorteio um número {num1} à {num2}')
def step_impl(context, num1, num2):
    context.num = randint(int(num1), int(num2))


@then(u'verifico se o resultado é igual {res}')
def step_impl(context, res):
    assert_equal(context.num, int(res))
