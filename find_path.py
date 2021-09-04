def solve_maze(start_cord: list[list[int]], current_cord: list[list[int]], end_cord: list[list[int]], explored_cord: list,  maze: dict) -> list:
    """this will find a path to solve the maze.

    Args:
        start_cord (list[list[int]]): the starting pos of the player
        current_cord (list[list[int]]): the current pos which is used for recursion 
        end_cord (list[list[int]]): the destination pos
        explored_cord (list): a list of cords which has been travelled by the code 
        maze (dict): a dict with all the info about the maze that

    Returns:
        list: contains a list of cords which is the path from the start to end
    """
    if current_cord == end_cord:  # check if we have reached the destination
        return [current_cord]
    elif current_cord in explored_cord:  # check if we have explored the cord
        return
    else:
        explored_cord.append(current_cord)

        # check if we can move to top of the current box
        if current_cord[1] >= 1:
            if not(maze["horizontal_wall"][current_cord[1]-1][current_cord[0]]):
                ans = solve_maze(start_cord, [current_cord[0], current_cord[1]-1],
                                 end_cord, explored_cord, maze)
                if ans and start_cord == current_cord:
                    ans.append(current_cord)
                    return ans[::-1]
                elif ans:
                    ans.append(current_cord)
                    return ans

        # check if we can move to bottom of the current box
        if current_cord[1] < 5:
            if not(maze["horizontal_wall"][current_cord[1]][current_cord[0]]):
                ans = solve_maze(start_cord, [current_cord[0], current_cord[1]+1],
                                 end_cord, explored_cord, maze)
                if ans and start_cord == current_cord:
                    ans.append(current_cord)
                    return ans[::-1]
                elif ans:
                    ans.append(current_cord)
                    return ans

        # check if we can move to left of the current box
        if current_cord[0] >= 1:
            if not(maze["vertical_wall"][current_cord[1]][current_cord[0]-1]):
                ans = solve_maze(start_cord, [current_cord[0]-1, current_cord[1]],
                                 end_cord, explored_cord, maze)
                if ans and start_cord == current_cord:
                    ans.append(current_cord)
                    return ans[::-1]
                elif ans:
                    ans.append(current_cord)
                    return ans

        # check if we can move to right of the current box
        if current_cord[0] < 5:
            if not(maze["vertical_wall"][current_cord[1]][current_cord[0]]):
                ans = solve_maze(start_cord, [current_cord[0]+1, current_cord[1]],
                                 end_cord, explored_cord, maze)
                if ans and start_cord == current_cord:
                    ans.append(current_cord)
                    return ans[::-1]
                elif ans:
                    ans.append(current_cord)
                    return ans
