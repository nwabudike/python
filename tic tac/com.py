import filecmp

f1 = "tic_tac_toe.py"
f2 = "tictactoe.py"

# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
