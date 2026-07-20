# Simple small inefficient but custom algorithms
# made to parse a text into tokens

from collections import defaultdict

def tokenn2(text: str):
    token_count: dict[str, int] = defaultdict(int)
    SPAN_END: int = 8
    EXCLUDE: set[str] = {"", " ", "\n", "\r"}

    # first determiniate which tokens occure most often.
    # then value the tokens with more letters higher.
    for i, char in enumerate(text):
        # add all elements form current index to the end of the text.
        # If the span between index and end of the text is higher than SPAN_END,
        # only use the next SPAN_END elements, not the next n - i

        for num in range(i, i + SPAN_END if i + SPAN_END <= len(text) else len(text)):

            # add range form i to num+1
            if (
                append := ("".join([text[j] for j in range(i, num+1)]))
            ) not in EXCLUDE:
                token_count[append] += 1
