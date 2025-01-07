def solution(todo_list, finished):
    answer = []
    for idx, todo in enumerate(todo_list):
        if not finished[idx]:
            answer.append(todo)
    return answer