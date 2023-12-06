class Pair:
    def __init__(self, left, right, parent=None, val=None):
        self.left = left
        self.right = right
        self.parent = parent
        if self.parent is None:
            self.parent = self
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        out = "[" + str(self.left) + "," + str(self.right) + "]"
        return out

    def mag(self):
        if self.val is not None:
            return self.val
        return 3*self.left.mag() + 2 * self.right.mag()

    def depth(self):
        if self.val is not None:
            return 0
        return max(self.left.depth(), self.right.depth()) + 1

    def explode(self, d=0):
        if self.val is not None:
            if d <= 4:
                return False
            # explode


            #left increase
            runner = self
            while runner.parent.left == runner:
                runner = runner.parent
                if runner.parent == runner:
                    break
            else:
                runner = runner.parent.left
                while runner.val is None:
                    runner = runner.right
                runner.val += self.val


            #right increase
            runner = self.parent.right
            while runner.parent.right == runner:
                runner = runner.parent
                if runner.parent == runner:
                    break
            else:
                runner = runner.parent.right
                while runner.val is None:
                    runner = runner.left
                runner.val += self.parent.right.val

            self.parent.val = 0
            return True

        if self.left.explode(d+1):
            return True
        if self.right.explode(d+1):
            return True
        return False

    def split(self):
        if self.val is not None:
            if self.val < 10:
                return False

            #split
            self.left = Pair(0, 0, self, self.val//2)
            self.right = Pair(0, 0, self, (self.val+1)//2)
            self.val = None
            return True

        if self.left.split():
            return True
        if self.right.split():
            return True
        return False

    def copy(self):
        if self.val is not None:
            return Pair(0, 0, val=self.val)
        out = Pair(self.left.copy(), self.right.copy())
        out.left.parent = out
        out.right.parent = out
        return out



def create_pair(s):
    root = Pair(0, 0)
    runner = root
    for c in s:
        if c == " ":
            continue
        if c == "[":
            runner.left = Pair(0, 0, runner)
            runner = runner.left
        elif c == "]":
            runner = runner.parent
        elif c == ",":
            runner.parent.right = Pair(0, 0, runner.parent)

            runner = runner.parent.right
        else:
            runner.val = int(c)
    return root



def add(p1, p2):
    out = Pair(p1, p2)
    p1.parent = out
    p2.parent = out
    changed = True
    while changed:
        changed = False
        #explode
        if out.explode():
            changed = True
            continue

        if out.split():
            changed = True
            continue



        # split


    return out


pairs = []
with open("18.txt", "r") as f:
    for l in f:
        pairs.append(create_pair(l.strip()))


mx = 0

for p1 in pairs:
    for p2 in pairs:
        if p1 == p2:
            continue

        mx = max(mx, add(p1.copy(), p2.copy()).mag())




print(mx)










