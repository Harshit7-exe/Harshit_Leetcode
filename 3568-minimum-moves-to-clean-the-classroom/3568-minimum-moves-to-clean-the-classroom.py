from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])

        
        start_r = start_c = -1
        litter_positions = []

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))

        L = len(litter_positions)

        litter_id = {
            pos: i for i, pos in enumerate(litter_positions)
        }

        target_mask = (1 << L) - 1

        
        best_energy = [
            [
                [-1] * (1 << L)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        queue = deque()

        queue.append((start_r, start_c, energy, 0, 0))
        best_energy[start_r][start_c][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, rem_energy, mask, moves = queue.popleft()

            
            if mask == target_mask:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                
                next_energy = rem_energy - 1

                if next_energy < 0:
                    continue

                next_mask = mask
                cell = classroom[nr][nc]

                
                if cell == 'R':
                    next_energy = energy

                
                elif cell == 'L':
                    idx = litter_id[(nr, nc)]
                    next_mask |= (1 << idx)

                if (
                    next_energy == 0
                    and cell != 'R'
                    and next_mask != target_mask
                ):
                    continue

                
                if next_energy <= best_energy[nr][nc][next_mask]:
                    continue

                best_energy[nr][nc][next_mask] = next_energy

                queue.append(
                    (
                        nr,
                        nc,
                        next_energy,
                        next_mask,
                        moves + 1
                    )
                )

        return -1