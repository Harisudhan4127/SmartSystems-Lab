letters = ['B','C','D','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y']
digits = ['2','3','4','6','7','8','9']
all_chars = letters + digits  # 23 characters

with open('qc_combinations.txt', 'w') as f:
    for c1 in all_chars:
        for c2 in all_chars:
            for c3 in all_chars:
                f.write(f"QC{c1}{c2}{c3}\n")