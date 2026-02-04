import asyncio
import sys

def get_next_expression(expressions, first) -> str:
    """ Return the lowest index expression in expressions that's not in first,
        or an empty string if all expressions are in first.

    >>> get_next_expression(['1 + 1', '[1, 2] + [5, 6]'], {})
    '1 + 1'
    >>> get_next_expression(['1 + 1', '[1, 2] + [5, 6]'], {'1 + 1': 'John'})
    '[1, 2] + [5, 6]'
    >>>
    >>> get_next_expression(['1 + 1'], {'1 + 1': 'John'})
    ''
    """
    for expr in expressions:
        if expr not in first.keys():
            return expr
    else:
        return ''

async def run_challenges(name: str, get_result, expressions: list[str], first: dict[str, str]):
    expression = get_next_expression(expressions, first)
    while expression != '':
        result = await get_result(expression)

        correct_answer = str(eval(expression))
        if result.strip() == correct_answer:
            print(f"-- Good job {name}; you correctly evaluated '{expression}' --")
            if expression not in first.keys():
                first[expression] = name
        
        else:
            print(f"-- Not quite {name}. Try to evaluate '{expression}' again! --")

        if expression in first.keys():
            expression = get_next_expression(expressions, first)

async def get_input_from_user(expression):
    print('What does the following Python expression evaluate to', expression)
    return await asyncio.to_thread(sys.stdin.readline)

async def get_input_from_computer(expression: str):
    """Return the result of evaluating the expression, after 0.3 seconds."""
    await asyncio.sleep(2)
    return str(eval(expression))

async def run_challenge(player: str):
    """
    Return a dictionary mapping each expression to the player name that evaluated it first.
    One player reads from stdin using the get_input_from_user coroutine and has name player, and the other
    is named 'computer' and gets input using get_input_from_computer.
    """
    expressions = ['1 + 1', '[1, 2].append([5, 6])', '[1, 2] + [5, 6]']
    first = {}
    await asyncio.gather(run_challenges(player, get_input_from_user, expressions, first), run_challenges("computer", get_input_from_computer, expressions, first))
    print(first)
    return first

if __name__ == "__main__":
    """
    >>> python .\main.py
    What does the following Python expression evaluate to 1 + 1
    2
    -- Good job z0z0r4; you correctly evaluated '1 + 1' --
    What does the following Python expression evaluate to [1, 2].append([5, 6])
    -- Good job computer; you correctly evaluated '1 + 1' --
    -- Good job computer; you correctly evaluated '[1, 2].append([5, 6])' --
    -- Good job computer; you correctly evaluated '[1, 2] + [5, 6]' --
    [1,2,5,6]
    -- Not quite z0z0r4. Try to evaluate '[1, 2].append([5, 6])' again! --
    {'1 + 1': 'z0z0r4', '[1, 2].append([5, 6])': 'computer', '[1, 2] + [5, 6]': 'computer'}
    """
    asyncio.run(run_challenge("z0z0r4"))