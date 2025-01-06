if __name__ == '__main__':
    value_N = int(input())
    
    # Read input into a list of tuples (name, score)
    students = []
    for _ in range(value_N):
        name = input()
        score = float(input())
        students.append((name, score))
    
    # Extract unique scores and sort them
    scores = sorted(set(score for _, score in students))
    
    if len(scores) < 2:
        print()
    else:
        # Find the second lowest score
        second_lowest_score = scores[1]
        
        # Find all students with the second lowest score and sort them alphabetically
        second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])
        
        # Print names of students with the second lowest score
        for student in second_lowest_students:
            print(student)
