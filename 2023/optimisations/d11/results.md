# Results from optimising day 11

```
Basic: 4274.37 µs
Prefix Sum: 193.852 µs
No MaxMin: 127.23 µs
Bitset: 404.78 µs
RC Bitsets: 181.946 µs
Small types: 181.582 µs
```

Pretty interesting. I didn't add any parallel things this time,
sadly the binary stuff was a bit slower than the string logic probably because of 
the input size being too big for a U64 and too small for bitsets to be good.