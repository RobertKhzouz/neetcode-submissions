class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows:  dict[int, set[int]] = {} # number maps to what rows it is in
        cols:  dict[int, set[int]] = {} # number maps to what cols it is in
        boxes: dict[int, set[int]] = {} # number maps to what boxes it is in

        for i, row in enumerate(board):

            for j, val in enumerate(row):

                if val == ".":
                    continue

                b = self.determineBox(i, j)

                if val in rows:
                    if i in rows[val]:
                        return False
                    rows[val].add(i)
                else:
                    rows[val] = {i}

                if val in cols:
                    if j in cols[val]:
                        return False
                    cols[val].add(j)
                else:
                    cols[val] = {j}

                if val in boxes:
                    if b in boxes[val]:
                        return False
                    boxes[val].add(b)
                else:
                    boxes[val] = {b}
        return True

    def determineBox(self, i, j) -> int:
        if i < 3:
            if j < 3:
                return 0
            elif j < 6:
                return 1
            else:
                return 2
        elif i < 6:
            if j < 3:
                return 4
            elif j < 6:
                return 5
            else:
                return 6
        else:
            if j < 3:
                return 7
            elif j < 6:
                return 8
            else:
                return 9





