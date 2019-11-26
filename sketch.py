if 0 <= rr < N and 0 <= cc < N and [rr, cc] not in pathh:
    if arr[rr][cc] < arr[r][c]:
        DFS(rr, cc, pathh, k)
    elif k:
        for kk in range(1, K + 1):
            if arr[rr][cc] - kk == arr[r][c] - 1:
                arr[rr][cc] -= kk
                DFS(rr, cc, pathh, False)
                arr[rr][cc] += kk
            else:
                Max = max(Max, len(pathh))
    else:
        Max = max(Max, len(pathh))