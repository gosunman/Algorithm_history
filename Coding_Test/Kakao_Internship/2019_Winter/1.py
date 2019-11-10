def solution(board, moves):
    stack = []
    answer = 0
    size_board = len(board)
    new_board = [[] for _ in range(size_board)]
    for j in range(size_board):
        for i in range(size_board):
            if board[i][j]:
                new_board[j].append(board[i][j])
    for move in moves:
        move -= 1
        if new_board[move]:
            if stack and new_board[move][0] == stack[-1]:
                del new_board[move][0]
                del stack[-1]
                answer += 2
            else:
                stack.append(new_board[move].pop(0))
    return answer