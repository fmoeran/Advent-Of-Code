# Advent-Of-Code

This is collection of most of the AOC problems I've done so far. 
I don't make it my priority to have pretty code in AOC so sorry for the mess.

Also, yes most of this code only solves the part 2 for each day, 
I do most of them for speed so I just edit my part 1 solutions to get part 2 and I cba remake them later just for my github



## Positions
These are my ranks for each day so far.

They tend to vary quite a bit because I change whether I get up at 5am each day.

### 2024

```
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  4   00:19:57  4070      0   00:22:49  2199      0
  3   00:06:03  2065      0   00:07:36   579      0
  2   00:04:59   501      0   00:10:13   852      0
  1   00:02:53   716      0   00:03:52   399      0
 ```


### 2023

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   02:04:54   2510      0   02:05:28   2119      0
 24   00:15:24     82     19   13:57:57   4761      0
 23   00:14:55    356      0   01:10:42    614      0
 22   00:48:02    961      0   00:56:21    703      0
 21   00:05:52    216      0   13:33:16   5603      0
 20   00:43:07    681      0   04:45:39   3397      0
 19   00:22:37    948      0   00:45:49    563      0
 18   00:14:56    447      0   01:24:57   1758      0
 17   00:19:58    212      0   00:26:31    280      0
 16   00:25:20   1155      0   00:31:13   1027      0
 15   00:04:33    991      0   00:21:02   1013      0
 14   00:09:01    937      0   00:32:49    764      0
 13   00:09:26    124      0   00:13:01     77     24
 12   01:12:16   4914      0   01:18:18   1441      0
 11   00:21:26   2356      0   00:22:00   1190      0
 10   00:22:19    711      0   01:09:10    921      0
  9   06:11:32  25285      0   06:14:08  24195      0
  8   00:10:40   2553      0   18:47:47  42315      0
  7   00:29:24   2386      0   02:29:08  10005      0
  6   00:05:07    531      0   00:10:05   1167      0
  5   00:22:43   1772      0   06:46:04  13569      0
  4   00:05:15    820      0   00:08:45    215      0
  3   00:11:31    415      0   00:20:48    572      0
  2   00:10:07   1294      0   00:12:25    968      0
  1   00:02:21    347      0   00:10:41    420      0
```


### 2022
```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25       >24h  12880      0       >24h   8071      0
 24       >24h  10892      0       >24h  10671      0
 23   19:09:22  11102      0   19:13:21  10815      0
 22   17:56:36  12079      0       >24h  10821      0
 21   10:50:07  13714      0   11:14:55  10623      0
 20   11:50:14   9709      0   12:00:52   8815      0
 19   16:18:56   7279      0       >24h  11652      0
 18   06:40:14  10887      0   08:54:37   8975      0
 17   06:27:15   6509      0   09:51:41   4861      0
 16   18:21:24  12644      0   18:58:00   7982      0
 15   08:33:51  16635      0   10:07:34  12252      0
 14   14:21:36  24898      0   14:23:35  23428      0
 13   06:45:21  15415      0   06:56:08  14436      0
 12   00:33:13   2329      0   00:40:17   2304      0
 11   00:32:16   2036      0   00:35:07    913      0
 10   00:17:59   3411      0   00:24:46   1404      0
  9   00:16:40   1256      0   00:21:48    566      0
  8   00:17:55   2616      0   00:33:04   2606      0
  7   01:11:58   7327      0   01:18:21   6616      0
  6   00:03:45    999      0   00:04:14    718      0
  5   00:15:20   1516      0   00:22:43   2446      0
  4   00:04:51   1218      0   00:10:53   2874      0
  3   00:07:39   1610      0   00:12:01   1334      0
  2   00:07:03   1236      0   00:12:00   1377      0
  1   00:02:45    933      0   00:05:20   1471      0
```


## Times

Running ```2023/timer.py``` will create a ```times.txt``` file for the run times of each of the 2023 files.
Here are the run times on my machine:
```
day 1: 0.044s
day 2: 0.003s
day 3: 0.04s
day 4: 0.005s
day 5: 0.009s
day 6: 0.002s
day 7: 0.011s
day 8: 0.042s
day 9: 0.009s
day 10: 0.151s
day 11: 1.631s
day 12: 0.615s
day 13: 0.014s
day 14: 1.953s
day 15: 0.009s
day 16: 4.195s
day 17: 3.63s
day 18: 0.01s
day 19: 0.012s
day 20: 0.35s
day 21: 1.071s
day 22: 0.074s
day 23: 24.223s
day 24: 1.346s
day 25: 0.085s
```

## Optimisations

I also like to add optimisations sometimes to problems and might put them in <year>/optimisations/<day>.
They usually have things like vectorisation, bitmasks, parallelization, etc.