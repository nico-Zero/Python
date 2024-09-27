robots_position_1 = [[1,0,0,1],[0,1,1,0]]
robots_position_2 = [[1,0,0,0,1],[1,0,1,0,0]]

def search_robots(robots_positions):
    for index_1,positions in enumerate( robots_positions[:-1] ):
        len_pos = len(positions) -1
        for index_2,robot in enumerate( positions ):
            if index_2 == 0 and robot:
                if 1 not in robots_positions[index_1+1][:2]:
                    return False
            elif index_2 == len_pos and robot:
                if 1 not in robots_positions[index_1+1][index_2-1:]:
                    return False
            else:
                if 1 not in robots_positions[index_1+1][index_2-1:index_2+1]:
                    return False
    return True

print(search_robots(robots_position_2))
