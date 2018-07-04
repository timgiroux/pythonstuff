import re
text = """ Noah was mad because his __NOUN__ smelled like __SMELLY_NOUN__. __ADJECTIVE__ tears fell from his eyes as he threw his __NOUN__ across the room. He pooped his pants and the carpet was now ruined"""

def mad_libs(mls):
    """
    :param mls: String
    with parts the user should fill out surrounded by underscores.
    Underscores cant be in hint.
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}: ".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)


