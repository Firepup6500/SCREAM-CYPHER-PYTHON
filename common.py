# pylint: disable=missing-module-docstring,missing-function-docstring
chars = [
    "A",
    "Ȧ",
    "A̧",
    "A̱",
    "Á",
    "A̮",
    "A̋",
    "A̰",
    "Ả",
    "A̓",
    "Ạ",
    "Ă",
    "Ǎ",
    "Â",
    "Å",
    "A̯",
    "A̤",
    "Ȃ",
    "Ã",
    "Ā",
    "Ä",
    "À",
    "Ȁ",
    "Aͯ",
    "A̦",
    "Ⱥ",
    "Ḁ",
    "Ḁ̇",
    "Ḁ̧",
    "A̱̥",
    "Ḁ́",
    "A̮̥",
    "Ḁ̋",
    "A̰̥",
    "Ḁ̉",
    "Ḁ̓",
    "Ạ̥",
    "Ḁ̆",
    "Ḁ̌",
    "Ḁ̂",
    "Ḁ̊",
    "A̯̥",
    "A̤̥",
    "Ḁ̑",
    "Ḁ̃",
    "Ḁ̄",
    "Ḁ̈",
    "Ḁ̀",
    "Ḁ̏",
    "Ḁͯ",
    "A̦̥",
    "Ⱥ̥",
]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
lower = "̥"
validSymbols = "̧̱̮̰̣̯̤̥̦̇́̋̉̓̆̌̂̊̑̃̄̈̀̏ͯ"
thingsThatCountAsAnA = "AȺ"
bad = "ȦÁẢẠĂǍÂÅȂĀÃÄÀȀḀ"
badFix = ["Ȧ", "Á", "Ả", "Ạ", "Ă", "Ǎ", "Â", "Å", "Ȃ", "Ā", "Ã", "Ä", "À", "Ȁ", "Ḁ"]


def fixup(string: str) -> str:
    fixed = string
    for i, char in enumerate(bad):
        fixed = fixed.replace(char, badFix[i])
    return fixed
