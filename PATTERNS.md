# DSA Patterns — quick-reference notes

Ishan's living notes on the templates that keep tripping him up. Add as you encounter them. Re-read before each DSA block.

---

## Binary Search — the template

The form that works for 90% of "find largest m where condition holds" / "find smallest m where condition holds" problems:

```python
l, r = LOW, HIGH                # both INCLUSIVE bounds
while l <= r:                   # <= NOT <  (so single-element search still runs once)
    m = (l + r) // 2
    if condition_at_m_is_OK:    # m could be the answer, but maybe a better one exists higher
        l = m + 1               # advance — don't reuse m, that's how infinite loops happen
    else:
        r = m - 1               # m too high, exclude it
# After loop: l > r
# Return r if asking "largest m where condition holds"
# Return l if asking "smallest m where condition holds"
```

### Why `<=` not `<`

`while l < r` exits when `l == r` — but that single value never gets tested. For `x=1` you'd skip checking m=1 and miss the answer. With `<=`, you check that last single element too. **Always use `<=`.**

### Why `l = m+1` / `r = m-1` (not `l = m` / `r = m`)

If `l = m` and `m == l` (which happens because `(l+r)//2` floors), the pointer doesn't move and you loop forever. **Always shift past m**: if m is OK go above (`l = m+1`), if m is too high go below (`r = m-1`).

### Why return `r` for `mySqrt`

For "largest m where m*m ≤ x":
- Each time `m*m ≤ x` passes, we set `l = m+1` (moving past the known-good m).
- When the loop exits, `r` is sitting on the last m we KNOW passed (the prior iteration excluded its successor).
- So `r` = floor(sqrt(x)).

If the question were "smallest m where m*m > x" (= ceiling something), return `l` instead.

### The mental model

Think of it as **two pointers shrinking an inclusive range until the answer is squeezed out**. Whichever side passed the test last is the answer.

### Common mistakes

1. **Using a list of all candidates first** — defeats the point of binary search (now O(x) memory). Just compute the bound directly: `l, r = 0, x`.
2. **`l = m`, `r = m` (no ±1)** — infinite loop on overlap.
3. **`l, r = 0, x-1`** — wrong for x=1; you want `l, r = 0, x` so the answer x itself is in range.
4. **Returning `m` from inside the loop** — only correct if the problem has an exact target. For floor/ceiling problems, the exit-state of `l` or `r` is the answer.

### Reference problems
- LC 69 mySqrt (floor sqrt) → return r
- LC 35 search-insert-position → return l (first index where target could go)
- LC 704 binary-search → return m on exact match, else -1

---

## Group Anagrams (`anagram-groups` / LC 49) — `defaultdict` + sorted-key

This problem flagged two Python concepts I didn't know on Apr 30 cold review.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))   # 'eat' → 'aet'
            groups[key].append(s)
        return list(groups.values())
```

### `defaultdict(list)` — what it is

A `dict` that auto-creates a default value (here, an empty list) when you access a missing key. So `groups['aet'].append('eat')` doesn't error on first 'aet' — it creates `[]` automatically, then appends.

The plain-dict alternative is more verbose:

```python
groups = {}
for s in strs:
    key = ''.join(sorted(s))
    if key not in groups:
        groups[key] = []
    groups[key].append(s)
```

`defaultdict` removes the if-check. **Whenever you're grouping items by a key, reach for `defaultdict(list)` (or `defaultdict(int)` for counts, `defaultdict(set)` for unique).**

### `sorted(s)` — sorting a string

`sorted()` works on any iterable (strings included). Returns a **list of characters**, not a string. So:

```python
sorted('eat')         # → ['a', 'e', 't']
''.join(sorted('eat')) # → 'aet'
```

`''.join(...)` is the idiom to recombine the sorted chars into a string.

### Alternative key — char-frequency tuple

If `sorted` feels expensive (it's O(k log k) per string for length-k strings), use a frequency tuple:

```python
key = tuple(s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')
```

That's O(26·k) per string but generates the same key for anagrams. For LC 49 either approach is acceptable; sorted-key is simpler to read.

### Pattern recognition cue

When the problem says "group / bucket / partition X by some property," the template is:
1. `defaultdict(list)`
2. Compute the bucket key per item
3. Return `list(groups.values())`
