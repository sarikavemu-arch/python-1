
marks = int(input("Enter aggregate marks: "))
subject = int(input("Enter minimum subject marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))

if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
    print("Scholarship Eligible")
else:
    print("Scholarship Not Eligible")

Algorithm
1. Start.
2. Enter aggregate marks.
3. Enter minimum subject marks.
4. Enter attendance percentage.
5. Enter family income.
6. Check all eligibility conditions.
7. If all conditions are satisfied, display “Scholarship Eligible”.
8. Otherwise, display “Scholarship Not Eligible”.
9. Stop.

    Sample Input and Output
Input
Enter aggregate marks: 85
Enter minimum subject marks: 45
Enter attendance percentage: 90
Enter family income: 150000

    Output
Scholarship Eligible

    
```mermaid
flowchart TD
    A([START]) --> B[/Enter units and previous bill/]
    B --> C{Units <= 100?}
    C -->|Yes| D[Bill = Units * 2]
    C -->|No| E{Units <= 200?}
    E -->|Yes| F[Bill = 200 + extra units * 3]
    E -->|No| G[Bill = 500 + extra units * 5]
    D --> H[Add fixed charge 50]
    F --> H
    G --> I[Add fixed charge 50 and surcharge 100]
    H --> J{Units <= 100?}
    J -->|Yes| K[Apply rebate 20]
    J -->|No| L[Keep bill]
    I --> M[/Display current bill/]
    K --> M
    L --> M
    M --> N{Bill > Previous bill * 1.5?}
    N -->|Yes| O[/Unusual Increase/]
    N -->|No| P[/Normal Bill/]
    O --> Q([STOP])
    P --> Q
```

    
