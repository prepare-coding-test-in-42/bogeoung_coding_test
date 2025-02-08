answer = []


def dfs(cur_start_loc, cur_arrive_loc, cur_path, used_tickets, tickets):
    # print(cur_start_loc, cur_arrive_loc, cur_path, used_tickets)
    global answer
    if len(cur_path) == len(tickets):
        answer.append(cur_path + [cur_arrive_loc])
        return

    for idx, ticket in enumerate(tickets):
        if ticket[0] == cur_arrive_loc and used_tickets[idx] == 0:
            used_tickets[idx] = 1
            dfs(ticket[0], ticket[1], cur_path + [ticket[0]], used_tickets, tickets)
            used_tickets[idx] = 0


def solution(tickets):
    global answer

    used_tickets = [0 for _ in range(len(tickets))]
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            used_tickets[idx] = 1
            dfs(ticket[0], ticket[1], [ticket[0]], used_tickets, tickets)
            used_tickets[idx] = 0

    answer.sort()
    return answer[0]