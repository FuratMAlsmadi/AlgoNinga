"""
Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
    for val in data:
        val *= factor
Explain why or why not.
Because val is an alias to each element in data so when assign it to another value we just break
the alias 
"""
