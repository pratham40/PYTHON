if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(1,n+1):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    namestud = input()
    avg_score=sum(student_marks[namestud])/len(student_marks[namestud])
    print(avg_score,f'.2f')
    
    